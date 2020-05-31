import folium
import pandas


volcanoesData = pandas.read_csv('Volcanoes.txt')


elevations = list(volcanoesData['ELEV'])
latitudes = list(volcanoesData['LAT'])
longitudes = list(volcanoesData['LON'])



map = folium.Map(location=[38.5, -63.09], zoom_start=6, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name='My Map')

for lat, lon, elv in zip(latitudes, longitudes, elevations):
    if elv < 1800:
        color = 'green'
    elif elv >= 1800 and elv <= 2100:
        color = 'orange'
    else:
        color = 'red'
    fg.add_child(folium.Marker(location=[lat, lon], popup='%sm' % elv, icon=folium.Icon(color=color)))

map.add_child(fg)
map.save('Map1.html')