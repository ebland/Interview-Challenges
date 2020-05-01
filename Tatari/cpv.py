from datetime import datetime
from csvDictReader import CSVDictReader 
from pprint import pprint

class CostPerView (object):
    """This class  consumes two separate .csv's, spots.csv and rotations.csv 
     that will show total cost by each creative and by each rotation by day """


    def __init__(self, rotations_filename, spots_filename):
        # filename = self.filename
        self.spots = CSVDictReader('spots.csv').get_contents()
        self.rotation = CSVDictReader('rotations.csv').get_contents()


    def cpvByDate(self, date, rotation):
        """returns a dictionary of the cpv for particular date for a specific rotation"""

        totalViews = 0
        totalSpend = 0

        # Loop through all the spots converting all the time values into datetime objects
        for spots in self.spots:
            strptime_string = '%I:%M %p'
            spotDate = spot.get('Date')
            spotTime = datetime.strptime(spot.get('Time'), strptime_string)
            rotationStartTime = datetime.strptime(rotation.get('Start'), strptime_string)
            rotationEndTime = datetime.strptime(rotation.get('End'), strptime_string)

            # see if the time spot the ad aired is in between the time for that rotatation
            if date == spotDate:
                if  rotationStartTime < spotTime < rotationEndTime:
                    totalViews += int(spot.get('Views'))
                    totalSpend += float(spot.get('Spend'))                

        # account for instances of no ads shown during the specified time spot
        cpv = 0
        if totalViews != 0 and totalSpend != 0 :
            cpv = self.calculate (totalSpend, totalViews)

        return {date: cpv}

    def calculate(self, totalSpend, totalViews):

        return totalSpend / totalViews

    def costByAd(self):
        """This will return the cost per view by Ads/Creatives shown"""

        creatives = [spot.get('Creative') for spot in self.spots]
        # store data found for each ad shown in all time spots
        data_output = {}

       # Get total for each ad
        for creative in creatives :
            total_viewed = 0
            total_spent = 0
            for spot in self.spots :
                if spot.get('Creative') == creative :
                    totalViews += int(spots.get('Views'))
                    totalSpend += float(spots.get('Spend'))

            # Divide Views by spend to get cpv (costperview)
            cpv = self.calculate (totalSpend, totalViews)
            # store new data to data output list 
            data_output[ad] = cpv
        return data_output


        
    def costPerViewByRotationByDay(self):
        """Gives the revenue for the ads that aired each day broken down to show the total cpv 
        for each of the rotations on the given dates"""

        data_output = {}
        dates = set(spots.get('Date') for spot in self.spots)
        # doing the same as we did before but instead of looping over each ad to get number
        # of spots...we are looping over dates the ad was aired to get the total number of views during
        # each of the 3 time frames
        for rotation in self.rotations:
            rotationName = rotation.get('Name')
            for view in date:
                # As we build the result dictionary if the result_dict has a specific rotation already,
                    # continue to use but update that value.
                if data_output.get(rotationName) :
                    data_output[rotationName].update(self.cpvByDate(date, rotation))
                # Else have that new rotation added to the result_dict
                else :
                    data_output[rotation_name] = self.cpvByDate(date, rotation)

        return data_output


        morningRotation = {}
        afternoonRotation = {}
        primeRotation = {}
        # compare rotation value and time
        if( rotationName ==  "Morning" ):
          #print( " Morning match  " )
            if rotationStartTime <  spotTime and spotTime <  rotationEndTime:
            #print( " rotationStartTimeConverted is less than spotTimeConverted  " )
                morningRotation[j] = spotDataRow

        # compare rotation value and time
        if( rotationName ==  "Afternoon" ):
          #print( " Evening match  " )
            if rotationStartTime <  spotTime and spotTime<  rotationEndTime:
            #print( " rotationStartTimeConverted is less than spotTimeConverted  " )
                afternoonRotation[j] = spotDataRow

        # compare rotation value and time
        if( rotationName ==  "Prime" ):
          #print( " Prime match  " )
            if rotationStartTime <  spotTime and spotTime <  rotationEndTime:
            #print( " rotationStartTimeConverted is less than spotTimeConverted  " )
                primeRotation[j] = spotDataRow

        #rotationName = [(spotTime-rotationStartTimeConverted) % 24 < (rotationEndTime-rotationStartTime) % 24 for spotTime in range(24)]

#Print Dictionaries
        print( "morningRotation" )
        print( morningRotation )
        print( "afternoonRotation" )
        print( afternoonRotation )
        print( primeRotation )

        
if __name__ == '__main__':

    cpv = CostPerView('spots.csv','rotations.csv')
    print("CPV By Creative")
    print('***********************************************************')
    pprint(CostPerView.costByAd('spots.csv'))
    print("\nCPV By Rotation By Day")
    print('***********************************************************')    
    pprint(CostPerView.costPerViewByRotationByDay())