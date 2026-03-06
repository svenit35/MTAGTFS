#Turning stops.txt csv file into useful dictionary for converting stop_id to stop name

import pandas as pd

df = pd.read_csv('gtfs_subway/stops.txt')

#creates dictionary with stop_id keys and stop_name values
stop_dict = df.set_index('stop_id')['stop_name'].to_dict()

#retrieves name of stop when given the stop_ID.
def stop_name(stop_id):
    return stop_dict.get(stop_id)

#NEEDS WORK: needs to return possible stop id's based on user inputted stop name... of which there are multiple id's
def stop_id(stop_name):
    return stop_dict.key(stop_name)

print(stop_name("107N"))