import matplotlib as plt
import pandas as pd
import numpy as py
import folium
import os
import json
#import osmnx as ox

capOneLocFile = "Capital_One_Locations.csv"
commDistFile = "nycd.csv"
cOneLocations = pd.read_csv(capOneLocFile)
commDist = pd.read_csv(commDistFile)

districtNY = 'nycommdistrict.geojson'

commDist2 = pd.DataFrame(cOneLocations)
commDist2.to_json('cap.json')
commDist2 = commDist2.reset_index()
#commDist2.columns = ['District', 'Number']
'''
bankLocDen = pd.DataFrame(cOneLocations['Bank District'].value_counts().astype(float))
bankLocDen.to_json('bankLocs.json')
bankLocDen = bankLocDen.reset_index()
bankLocDen.columns = ['District', 'Number of Banks']


with open('bankLocs.json') as json_data:
    bank2 = json.load(json_data)
    #print(bank2)
    bank3 = bank2['Bank District']
    #print(bank3)
    bank3 = {int(float(k)):int(v) for k,v in bank3.items()}
    bank2['Bank District'] = bank3
    print(bank2)
    
    #print(bank3)
    #bank3.to_json('bank3.json')
#bank3 = bank3.reset_index()
#bank4 = {"Bank District"}
#print(bank2)

'''
#distMap = folium.Map(location = [40.76831, -73.964915], tiles="Cartodb Positron", zoom_start=10)
#distMap.choropleth(geo_data = districtNY, name = 'choropleth', data = commDist2 , columns = ['District', 'Number'], key_on = 'feature.properties.DISTRICT', fill_color = 'PuBuGn', fill_opacity = 0.7, line_opacity = 1.0, legend_name = 'Community District')

#folium.LayerControl().add_to(distMap)
'''

#bankLocDen = "bankLocs.json"
densityMap = folium.Map(location = [40.76831, -73.964915], tiles="Cartodb Positron", zoom_start=10)
densityMap.choropleth(geo_data = districtNY, name = 'choropleth', data = bank2, columns = ['District', 'Number of Banks'], key_on = 'feature.properties.DISTRICT', fill_color = 'PuBuGn', fill_opacity = 0.7, line_opacity = 1.0, legend_name = 'Number of Banks')

folium.LayerControl().add_to(densityMap)
'''
#distMap.save(outfile = 'districtMap.html')
#densityMap.save(outfile = 'densityMap.html')