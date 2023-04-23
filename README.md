# OSM Road Node Extractor
To obtain the latitude and longitude values of all the nodes that make up a particular road in OpenStreetMap (OSM), you can enter the way-id of the road. The script will then extract this information from OSM and return it to you.
This can be helpful in a variety of applications, such as autonomous vehicle navigation, mapping and geospatial analysis.

In OSM all roads and routes have a way ID, you can find the way id by selecting the route, here it is highlighted number below _Way:Delhi Avenue_

![image](https://user-images.githubusercontent.com/94188928/233842612-79de6e05-20df-4fff-9456-824879531b04.png)

To obtain the GPS coordinates for a particular road, you can use Python scripts available in this repository. 

If you know the way-id of the road, you can run the **getfrom_way_id.py** file, enter the way-id, and the script will create an XML file in the **gps_nodes** folder, which contains the latitude and longitude values for all the nodes that make up the road. These coordinates can be used to help a self-driving car navigate the road.

If you don't know the way-id, you can run the **getfrom_way_name.py** file. This script creates a query request to the Overpass API to find the road based on its name. However, the query may not be accurate if the road name is not specific enough.

If you are a student at IIT Madras, you can use the **get_iitm_roads.py** file to select a road from a list of available roads at IIT Madras. The script will then obtain the GPS coordinates for the selected road using its way-id.
