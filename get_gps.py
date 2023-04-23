import xml.etree.ElementTree as ET
import osmapi as osm
import sys

class Get_osm():
    def __init__(self,way_id):
        # self.road=road
        self.api=osm.OsmApi()
        self.coords=[]
        self.way_id=way_id
        self.get_road()


    def get_road(self):
        self.tree = ET.parse(f'roads/way_{self.way_id}_nodes.xml')
        self.root = self.tree.getroot()
        self.get_coord()

    def get_coord(self):
        for child in self.root:
            if('ref' in child.attrib):
                ref_id=child.attrib['ref']
                node = self.api.NodeGet(ref_id)
                print(node['lat'],node['lon'])
                coordinates=[node['lat'],node['lon']]
                self.coords.append(coordinates)
        self.write2file()

    def write2file(self):

        OSM_coordinates = ET.Element("OSM_coordinates")
 
        # create sub element
        OSM_coordinates = ET.SubElement(OSM_coordinates, "OSM_coordinates")
 
        # insert list element into sub elements
        for points in range(len( self.coords)):
            lat_long = ET.SubElement(OSM_coordinates, "node")
            lat_long.text = str(self.coords[points])
 
        tree = ET.ElementTree(OSM_coordinates)
        print(self.coords)
        # write the tree into an XML file
        tree.write(f"gps_nodes/way_{self.way_id}_nodes.xml", encoding ='utf-8', xml_declaration = True)
        print("Done and dusted")
