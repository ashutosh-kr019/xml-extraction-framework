from lxml import etree

def load_xml(file_path):
    tree = etree.parse(file_path)
    return tree.getroot()