import matplotlib as plt
import pandas as pd
import numpy as py
import folium
import os
import json

capOneLocFile = "Capital_One_Locations.csv"
cOneLocations = pd.read_csv(capOneLocFile)
mapBanksLocations = folium.Map(location = [40.76831, -73.964915], tiles="Cartodb Positron", zoom_start=10)
for index,row in cOneLocations.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    address = row["Address"]
    bankNo = row["Bank Num"]
    newMarker = folium.CircleMarker([lat, lon], popup = address)
    newMarker.add_to(mapBanksLocations)

mapBanksLocations.save(outfile = 'bankRings.html')