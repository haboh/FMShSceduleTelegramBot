# -*- coding: utf-8 -*-
import config
import time
import telebot
from ListWithNamesOfAlreadyPostedImages import ListWithNamesOfAlreadyPostedImages
from GetImage import get_list_of_names_of_not_posted_images


def main():
    bot = telebot.TeleBot(config.BotToken)
    list_with_names_of_already_posted_images = ListWithNamesOfAlreadyPostedImages(config.ListOfNamesOfImages)
    while True:
        names_of_images_for_post = get_list_of_names_of_not_posted_images(list_with_names_of_already_posted_images)
        for image_name in names_of_images_for_post:
            bot.send_chat_action(config.ChanelId, 'upload_photo')
            path_to_image = config.DirectoryWithImages + '\\' + image_name
            image_for_post = open(path_to_image, 'rb')
            bot.send_photo(config.ChanelId, image_for_post)
            image_for_post.close()
            list_with_names_of_already_posted_images.add_name_of_file(path_to_image)
        time.sleep(2)


if __name__ == '__main__':
    main()
