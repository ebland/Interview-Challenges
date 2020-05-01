import csv
import sys

class CSVDictReader(object):
    """Class that will convert rows/values into a {key : value} list"""

    def __init__(self, filename):
        """Name of file"""
        self.filename = filename

        # for file in filenames:
        #     if file.endswith('.csv'):
        #         csv_list.append(file)

    def get_contents(self):
        csv_list = []
        try :
            csv_Reader = csv.DictReader(open(self.filename, 'r'))
        except IOError:
            print("file upload error")
            sys.exit()
      # use built in method "itertools" to parse data
        for item in csv_Reader.__iter__():
            csv_list.append(item)
       # Debug
        if len(csv_list) == 0 :
            raise IOError('No Data')

        return csv_list