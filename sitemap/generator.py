import xml.dom.minidom

from xml.etree import ElementTree

class Xml(object):
    """docstring for ."""
    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg

def xml_header():
    return '''<?xml version="1.0" encoding="utf-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n'''

def xml_footer():
    return '</urlset>'

def create_xml_text(*args, **kwargs):
    config = {};
    if args:
        config["host"] = args[0]
        config["url"] = args[1]
        config["lastmod"] = args[2]
        config["freq"] = args[3]
        config["priority"] = args[4]
        # print(config)
    else:
        config = kwargs

    xml_body = ''
    xml_body += xml_header()
    data = []
    
    for index, item in enumerate(config["url"]):
        url = config["host"] + item
        xml_body += '<url><loc>%s</loc>\n' % url
        xml_body += '<lastmod>%s</lastmod>\n' % config["lastmod"]
        xml_body += '<changefreq>%s</changefreq>\n' % config["freq"]
        xml_body += '<priority>%s</priority></url>\n' % config["priority"]

    xml_body += xml_footer()

    data.append(xml_body)

    prety_xml = prettyfy_xml(data)

    return prety_xml

def prettyfy_xml(xml_text):
    xml_file = ''
    for text in xml_text:
        xml_file = xml.dom.minidom.parseString(text)
        xml_file = xml_file.toprettyxml()

    return xml_file
