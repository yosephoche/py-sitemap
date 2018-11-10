import os
import time
import xml.dom.minidom
import pprint

import generator
# import glob
# from xml.dom import minidom
# from xml.etree import ElementTree
# from bs4 import BeautifulSoup
pp = pprint.PrettyPrinter(indent=4)

class Sitemap(object):

    def __init__(self, *args, **kwargs):
        # define sitemap file name
        self.file_name="sitemap"

        # define url
        self.url_list = []
        self.url_map =[]

        #define sitemap option
        self.changefreq = "daily"
        self.lastmod = time.strftime("%Y-%m-%d")
        self.priority = 0.9

        # define sitemap max item per file
        self.maximum_sitemap_item = 50000

        # define path to store sitemap file
        self.path = '/xml/'

        self.sitemap_index = False
        self.hostname = 'http://example.com/'

    def add_url(self, url):
        self.url_list.append(url)

    def set_hostname(self, hostname):
        self.hostname = hostname

    def set_filename(self, file_name):
        self.file_name = file_name

    def set_max_item(self, item_max):
        self.maximum_sitemap_item = item_max

    def create(self):
        item_length = len(self.url_list)
        if item_length > self.maximum_sitemap_item:
            self.sitemap_index = True
            self.create_chunk(self.url_list, 3)

        self.write_xml()

    def create_directory(self):
        try:
            # define the access rights
            access_rights = 0o755
            root_path = os.path.abspath("")
            os.makedirs(root_path + self.path, access_rights)
        except OSError as e:
            print ("Creation of the directory %s failed" % self.path)
            raise Exception(e)
            # return False
        else:
            print ("Successfully created the directory %s " % self.path)
            # return True

    def write_xml(self):
        xml_data = []

        path = os.path.abspath("") + self.path
        # check if directory exist or not
        if not os.path.exists(path):
            self.create_directory()

        if self.url_map:
            for index, url_index in enumerate(self.url_map):
                with open(path + self.file_name + "-"+str(index)+".xml", "w+") as file:
                    file.write(generator.create_xml_text(
                        host=self.hostname,
                        url=url_index,
                        lastmod=self.lastmod,
                        freq=self.changefreq,
                        priority=self.priority
                    ))
        else:
            with open(path + self.file_name + ".xml", "w+") as file:
                file.write(generator.create_xml_text(
                    host=self.hostname,
                    url=self.url_list,
                    lastmod=self.lastmod,
                    freq=self.changefreq,
                    priority=self.priority
                ))

    def create_chunk(self, list, n):
        for url in range(0, len(list), n):
            self.url_map.append(list[url:url+n])



# from sitemapg import sitemap

sitemap = Sitemap()

# set file name of sitemap
sitemap.set_filename("sitemap")

# set max item per sitemap
sitemap.set_max_item(2)

# add url to sitemap
sitemap.add_url("home.php")
sitemap.add_url("about.php")
sitemap.add_url("contact.php")
# for url in [1, 2, 3, 4, 5]:
#     sitemap.add_url("http://eproc.id/%s" % url)

# generate sitemap
sitemap.create()
