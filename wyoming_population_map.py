import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim


df = pd.read_csv('Foreign-Born Population.csv')
df_wyoming = df[df['Place'].str.contains('WY') & (df['Year'] == 2023)]
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

df_wyoming['Latitude'], df_wyoming['Longitude'] = zip(*df_wyoming['Place'].map(get_lat_lon))
df_wyoming = df_wyoming.dropna(subset=['Latitude', 'Longitude'])

fig = px.scatter_mapbox(
    df_wyoming,
    lat="Latitude", 
    lon="Longitude", 
    hover_name="Place", 
    size="Population", 
    color="Foreign-Born Citizens", 
    color_continuous_scale="Viridis", 
    size_max=15,                     
    zoom=6,                           
    center={"lat": 42.0, "lon": -106.0},
    mapbox_style="carto-positron",
    title="Foreign-Born Population in Wyoming (2023)", 
    subtitle="Cities in Wyoming by Foreign-Born Citizens", 
    opacity=0.7,          
)

fig.write_html("wyoming_population_map.html")
print("Map saved as 'wyoming_population_map.html'")