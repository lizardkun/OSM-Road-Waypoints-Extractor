import osmapi as osm
import xml.etree.ElementTree as ET


#all nodes start at gajendra circle

class Get_osm():
    def __init__(self):
        # self.road=road
        self.api=osm.OsmApi()
        self.coords=[]
        self.get_road()


    def get_road(self):
        n=int(input("Enter a road network :\n 0 -- delhi avenue\n 1 -- alumni avenue \n 2 -- hostel avenue\n"))
        if(n==0):
            self.tree = ET.parse('osm_nodes/roads/delhiavenue.xml')
            self.root = self.tree.getroot()
        elif(n==1):
            self.tree = ET.parse('osm_nodes/roads/alumniavenue.xml')
            self.root = self.tree.getroot()
        elif(n==2):
            self.tree = ET.parse('osm_nodes/roads/hostelavenue.xml')
            self.root = self.tree.getroot()
        else:
            print("unrecognized")
        self.get_coord()

    def get_coord(self):
        for child in self.root:
            for grandchild in child:
                if('ref' in grandchild.attrib):
                    ref_id=grandchild.attrib['ref']
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
 
        # write the tree into an XML file
        tree.write("osm_nodes/gps_nodes/delhiavenue.xml", encoding ='utf-8', xml_declaration = True)
        print("Done and dusted")

        


road=Get_osm()