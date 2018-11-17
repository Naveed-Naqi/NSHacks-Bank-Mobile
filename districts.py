import matplotlib as plt
import pandas as pd
import numpy as py
import folium
import os
#import osmnx as ox

capOneLocFile = "Capital_One_Locations.csv"
commDistFile = "nycd.csv"
cOneLocations = pd.read_csv(capOneLocFile)
commDist = pd.read_csv(commDistFile)

districtNY = 'nyccomdist.geojson'

commDist2 = pd.DataFrame(commDist['BoroCD'].value_counts().astype(float))
commDist2.to_json('commDists.json')
commDist2 = commDist2.reset_index()
commDist2.columns = ['District', 'Number']

distMap = folium.Map(location = [40.76831, -73.964915], tiles="Cartodb Positron", zoom_start=10)
distMap.choropleth(geo_data = districtNY, name = 'choropleth', data = commDist2 , columns = ['District', 'Number'], key_on = 'feature.properties.DISTRICT', fill_color = 'YlOrRd', fill_opacity = 0.7, line_opacity = 0.2, legend_name = 'Community District')

folium.LayerControl().add_to(distMap)

distMap.save(outfile = 'districtMap.html')