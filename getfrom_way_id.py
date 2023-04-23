import requests
import xml.etree.ElementTree as ET
import osmapi as osm
import subprocess

# Request the way id from the user
way_id = input("Enter the way id: ")

# Define the Overpass API query
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
for node_id in node_ref_ids:
    nd_elem = ET.Element("nd")
    nd_elem.set("ref", node_id)
    way_elem.append(nd_elem)

xml_tree = ET.ElementTree(way_elem)
xml_tree.write(f"roads/way_{way_id}_nodes.xml", encoding="utf-8", xml_declaration=True)


# Print the node ref ids and the filename of the saved XML file
print(f"Node ref ids: {node_ref_ids}")
print(f"XML file saved: roads/way_{way_id}_nodes.xml")


from get_gps import Get_osm
Get_osm(way_id)
# subprocess.run(["python3", "get_gps.py", way_id])

