import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim


df = pd.read_csv('Foreign-Born Population.csv')
df_texas = df[df['Place'].str.contains('TX') & (df['Year'] == 2023)]
geolocator = Nominatim(user_agent="myGeocoder")

def get_lat_lon(city):
    try:
        location = geolocator.geocode(city, timeout=10) 
        if location:
            print(f"Geocoded {city}: {location.latitude}, {location.longitude}")
            return location.latitude, location.longitude
    except Exception as e:
        print(f"Error geocoding {city}: {e}")
    return None, None

df_texas['Latitude'], df_texas['Longitude'] = zip(*df_texas['Place'].map(get_lat_lon))
df_texas = df_texas.dropna(subset=['Latitude', 'Longitude'])

fig = px.scatter_mapbox(
    df_texas,
    lat="Latitude", 
    lon="Longitude", 
    hover_name="Place", 
    size="Population", 
    color="Foreign-Born Citizens", 
    color_continuous_scale="Viridis", 
    size_max=15,                     
    zoom=6,                           
    center={"lat": 31.0, "lon": -100.0},
    mapbox_style="carto-positron",
    title="Foreign-Born Population in texas (2023)", 
    subtitle="Cities in texas by Foreign-Born Citizens", 
    opacity=0.7,          
)

fig.write_html("texas_population_map.html")
print("Map saved as 'texas_population_map.html'")