# -*- coding: utf-8 -*-
import json


class ListWithNamesOfAlreadyPostedImages:
    def __init__(self, filename):
        self.fileName = filename
        open(filename, 'a').close()
        with open(filename, 'r') as curFile:
            empty = (curFile.read() == '')
        if empty:
            with open(filename, 'a') as curFile:
                curFile.write('[]')

    def get_list(self):
        with open(self.fileName, 'r') as curFile:
            list_of_names_of_image = json.loads(curFile.read())
            return list_of_names_of_image

    def in_list(self, name_of_image):
        list_of_names_of_images = self.get_list()
        return name_of_image in list_of_names_of_images

    def add_name_of_file(self, name_of_file):
        list_of_names_of_images = self.get_list()
        if name_of_file not in list_of_names_of_images:
            list_of_names_of_images.append(name_of_file)
        json_list_of_names_of_images = json.dumps(list_of_names_of_images)
        with open(self.fileName, 'w') as curFile:
            curFile.write(json_list_of_names_of_images)

    def remove_name_of_file(self, name_of_file):
        list_of_names_of_images = self.get_list()
        if name_of_file in list_of_names_of_images:
            list_of_names_of_images.remove(name_of_file)
        json_list_of_names_of_images = json.dumps(list_of_names_of_images)
        with open(self.fileName, 'w') as curFile:
            curFile.write(json_list_of_names_of_images)
