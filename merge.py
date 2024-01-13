from pykml import parser
from math import radians, degrees

def merge_coordinates(kml_file):
    # Parse the KML file
    with open(kml_file, 'r') as f:
        doc = parser.parse(f)

    # Get all coordinates from the KML file
    coordinates = []
    for placemark in doc.getroot().Document.Placemark:
        if hasattr(placemark, 'LineString'):
            coords = str(placemark.LineString.coordinates).split()
            for coord in coords:
                longitude, latitude, _ = coord.split(',')
                coordinates.append((float(latitude), float(longitude)))

    # Calculate the average latitude and longitude
    total_latitude = 0
    total_longitude = 0
    for lat, lon in coordinates:
        total_latitude += lat
        total_longitude += lon

    avg_latitude = total_latitude / len(coordinates)
    avg_longitude = total_longitude / len(coordinates)

    return avg_latitude, avg_longitude

# Usage
kml_file = r"C:\Users\athar\Downloads\Satara_Farm-2.kml"
latitude, longitude = merge_coordinates(kml_file)
print(f"Merged coordinates: ({latitude}, {longitude})")