# -*- coding: utf-8 -*-
import os
import config


def get_list_of_names_of_not_posted_images(list_with_names_of_already_posted_images):
    list_of_all_images_in_directory = os.listdir(config.DirectoryWithImages)
    list_of_already_posted_images = list_with_names_of_already_posted_images.get_list()
    list_of_images_for_post = []
    for image_name in list_of_all_images_in_directory:
        if config.DirectoryWithImages + '\\' + image_name not in list_of_already_posted_images:
            list_of_images_for_post.append(image_name)
    return list_of_images_for_post
