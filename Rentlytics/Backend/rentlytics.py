import json

with open('guest-cards.json') as json_data:
    d = json.load(json_data)


ym_set = set()
source_set = set()

for js in d:
    ym = ''
    if js['lease_signed'] is not None:
        ym = str(js['lease_signed'])[:7]
    else:
        ym = str(js['first_seen'])[:7]

    ym_set.add(ym)
    s = str(js['marketing_source'])
    source_set.add(s)

d = {}
for m in ym_set:
    data[m] = {}
    for s in source_set: 
        data[m][s] = {'signed_leases':0, 'total_leads':0,
                      'total_cost':0, 'avg_cost_per_lead':0}


for js in d:
    if js['lease_signed'] is not None:
        m = str(js['lease_signed'])[:7]
        s = str(js['marketing_source'])
        data[m][s]['signed_leases'] += 1 
        data[m][s]['total_leads'] += 1 
    else:
        m = str(js['first_seen'])[:7]
        s = str(js['marketing_source'])
        data[m][s]['total_leads'] += 1 
        

for key,val in data.items():
    for v in val:
        # check source type
        if v == 'Apartment Guide':
            data[key][v]['total_cost'] = 495
        elif v == 'Apartments.com':
            data[key][v]['total_cost'] = 295*data[key][v]['signed_leases']
        elif v == 'Rent.com':
            data[key][v]['total_cost'] = max(595,295*data[key][v]['signed_leases'])
        elif v == 'For Rent':
            data[key][v]['total_cost'] = 195+25*data[key][v]['Total_Leads']
        elif v == 'Craigslist.com':
            data[key][v]['Total_Cost'] = 0
        elif v == 'Resident Referral':
            data[key][v]['Total_Cost'] = 500*data[key][v]['signed_leases']
        else:
            pass
       
def get_quarter(key):
    ym = str(key).split('-')
    year = ym[0]
    month = ym[1]
    if month <= '03':
        q = 'Fiscal First Quarter'
    elif month <= '06':
        q = 'Fiscal Second Quarter'
    elif month <= '09':
        q = 'Fiscal Third Quarter'
    else:
        q = 'Fiscal Fourth Quarter'
    return (q + ' ' + year)

out = {}
for key, val in data.items():
    q = get_quarter(key)
    out[q] = {}
    for v in val:
        out[q][v] = {'quarter':q, 'source':v, 'total_leads':0, 
                     'signed_leases':0, 'total_cost':0, 'avg_cost_per_lead':0} 

for key, val in data.items():
    q = get_quarter(key)
    for v in val:
        if q == out[q][v]['quarter']:
            out[q][v]['total_cost'] += data[key][v]['total_cost']
            out[q][v]['total_leads'] += data[key][v]['total_leads']
            out[q][v]['signed_leases'] += data[key][v]['signed_leases']

print "########################## REPORT COST PER LEAD ###############################################"
print "########################## REPORT COST PER LEAD ###############################################"
print
for key, val in out.items():
    print key,':'
    print
    for v in val:
        print ("%s - total leads: %s, signed leases: %s, total cost: $%s, avg cost per lead: $%s") %(out[key][v]['source'], out[key][v]['total_leads'], out[q][v]['signed_leases'], out[q][v]['total_cost'], out[q][v]['total_cost']/max(1,out[key][v]['total_leads'])) 
    print
    print


    
