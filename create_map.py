import folium
from geopy.geocoders import Nominatim
import http.server
import socketserver
import os

# Step 1: Define addresses with additional information
locations = [
    {
        "address": "1916 Estabrook Way, Superior, CO 80027",
        "info": "Owner Phong Thi Nguyen"
    },
    {
        "address": "1214 W Pine Ct, Louisville, CO 80027",
        "info": "Owner John Bowen Soot & Ash"
    },
    {
        "address": "1675 Rockview Circle, Superior, CO 80027",
        "info": "Owner Thomas Schadt Soot & Ash"
    },
    {
        "address": "220 Summit Blvd, Broomfiled, CO 80021",
        "info": "Owner Eugene Christiansen"
    },
    {
        "address": "500 Superior Drive, Superior, CO 80027",
        "info": "Owner Guy Harrigan"
    },
    {
        "address": "535 Apollo Drive, Boulder, CO 80303",
        "info": "Owner Henry Ruben Lopez Soot & Ash"
    },
    {
        "address": "791 W Mulberry Street, Louisville CO, 80027",
        "info": "Owner John E. Valdez Soot & Ash"
    },
    {
        "address": "643 Augusta Drive, Louisville, CO 80027",
        "info": "Owner John Reilly Soot & Ash"
    },
    {
        "address": "527 W Hackberry St. Louisville, CO 80027",
        "info": "Owner Lindsay Ross Soot & Ash"
    },
    {
        "address": "953 Eldorado Lane, Louisville, CO 80027",
        "info": "Owner Marc Hughes Total Loss"
    },
    {
        "address": "105 Cherrywood Lane, Louisville, CO 80027",
        "info": "Owner Maria McClure Total Loss"
    },
    {
        "address": "5912 S. Vale Rd., Boulder CO, 80303",
        "info": "Owner Peter Linsley"
    },
    {
        "address": "2855 Rock Creek Circle, Superior, CO 80027",
        "info": "Owner Roberta S. Gold Soot & Ash"
    },
    {
        "address": "985 Arapahoe Circle, Louisville, CO 80027",
        "info": "Owner Steve Leslie Buffer Property Damage"
    }
]

# Initialize the geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Step 2: Geocode the first address to center the map
first_location = geolocator.geocode(locations[0]["address"])
map_center = [first_location.latitude, first_location.longitude]

# Create the map
my_map = folium.Map(location=map_center, zoom_start=12)

# Step 3: Add a marker for each location with a popup that includes additional info
for loc in locations:
    location = geolocator.geocode(loc["address"])
    if location:
        # Create a popup with additional information
        popup_text = f"{loc['info']}<br>Address: {loc['address']}"
        folium.Marker(
            [location.latitude, location.longitude],
            popup=popup_text,
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(my_map)
    else:
        print(f"Could not geocode address: {loc['address']}")

# Save the map to an HTML file
map_file = "my_map.html"
my_map.save(map_file)
print(f"Map has been saved as {map_file}")

# Step 4: Serve the HTML map file on a local HTTP server
PORT = 8000
output_dir = os.path.dirname(os.path.abspath(map_file))
os.chdir(output_dir)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}/{map_file}")
    print(f"Or on the local network at http://<YOUR_IP_ADDRESS>:{PORT}/{map_file}")
    httpd.serve_forever()
