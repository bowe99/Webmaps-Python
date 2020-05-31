import folium
import pandas

#Project Done


volcanoesData = pandas.read_csv('Volcanoes.txt')


elevations = list(volcanoesData['ELEV'])
latitudes = list(volcanoesData['LAT'])
longitudes = list(volcanoesData['LON'])


map = folium.Map(location=[38.5, -63.09], zoom_start=6, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name='Volcanoes')
fg2 = folium.FeatureGroup(name='Population')

for lat, lon, elv in zip(latitudes, longitudes, elevations):
    if elv < 1800:
        color = 'green'
    elif elv >= 1800 and elv <= 2100:
        color = 'orange'
    else:
        color = 'red'
    fg.add_child(folium.CircleMarker(location=[
                 lat, lon], popup='%sm' % elv, radius=6, fill_color=color, color='grey', fill_opacity=0.7,))

fg2.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 30000000
                                                      else 'orange' if 30000000 <= x['properties']['POP2005'] < 50000000
                                                      else 'red'}))


map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())

map.save('Map1.html')
