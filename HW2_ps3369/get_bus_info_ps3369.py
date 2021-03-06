from __future__ import print_function
import json
import urllib as ulr 
import os
import csv
import sys
import pylab as pl

url ="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

loc = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

f = open(sys.argv[3], 'w')
writer = csv.writer(f, delimiter=',')
writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])

for i in range(len(loc)):
    
    lat= loc[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    lon= loc[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    if (loc[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}):
        stop_same = 'N/A'
        stop_status = 'N/A'
        
    else:

        stop_name= loc[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stop_status= loc[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    writer.writerow((lat,lon,stop_name,stop_status))
        
