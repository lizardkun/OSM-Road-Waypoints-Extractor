import requests
import xml.etree.ElementTree as ET

# Request the way name from the user
way_name = input("Enter the way name: ")

# Define the Overpass API query to search for the closest way to the given name
query = f"""
[out:xml];
way["name"~"{way_name}"];
out center;"""

# Send the query to the Overpass API and parse the response as XML
response = requests.get(f"https://overpass-api.de/api/interpreter?data={query}")
root = ET.fromstring(response.content)

# Extract the way id and center coordinates from the response
way_elem = root.find("way")
way_id = way_elem.attrib["id"]
lat = way_elem.attrib["lat"]
lon = way_elem.attrib["lon"]

# Define the Overpass API query to get all the nodes in the way
query = f"""
[out:xml];
way({way_id});
(._;>;);
out;"""

# Send the query to the Overpass API and parse the response as XML
response = requests.get(f"https://overpass-api.de/api/interpreter?data={query}")
root = ET.fromstring(response.content)

# Extract the node ref ids from the response
node_ref_ids = []
for child in root.iter("nd"):
    node_ref_ids.append(child.attrib["ref"])

# Create the XML file with the node ids
way_elem = ET.Element("way")
way_elem.set("id", way_id)
way_elem.set("lat", lat)
way_elem.set("lon", lon)
way_elem.set("name", way_name)
for node_id in node_ref_ids:
    nd_elem = ET.Element("nd")
    nd_elem.set("ref", node_id)
    way_elem.append(nd_elem)

xml_tree = ET.ElementTree(way_elem)
xml_tree.write(f"{way_name}_nodes.xml", encoding="utf-8", xml_declaration=True)

# Print the node ref ids, way id, center coordinates, and filename of the saved XML file
print(f"Node ref ids: {node_ref_ids}")
print(f"Way id: {way_id}")
print(f"Center coordinates: ({lat}, {lon})")
print(f"XML file saved: {way_name}_nodes.xml")
