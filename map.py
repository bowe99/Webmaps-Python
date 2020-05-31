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
    fg.add_child(folium.CircleMarker(location=[
                 lat, lon], popup='%sm' % elv, radius=6, fill_color=color, color='grey', fill_opacity=0.7,))

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))
map.add_child(fg)
map.save('Map1.html')

