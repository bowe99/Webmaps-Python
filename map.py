import folium

map = folium.Map(location=[38.5, -63.09], zoom_start=6, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[38.5, -64], popup='Hi I am a marker', icon=folium.Icon(color='green')))

map.add_child(fg)
map.save('Map1.html')