# -*- coding: utf-8 -*-
__author__ = 'edgard.barbosa'

from PIL import Image, ImageDraw
import os.path

from BolosDaLu import settings


class Util(object):
    PATH_IMG_MIN = "images/uploads/galeria/img_min/"
    PATH_IMG = "images/uploads/galeria/"
    EXTENSION = ".jpg"
    SYMBOL_MIN = "_min"

    @staticmethod
    def create_small_image(image, width, height):
        name_img = str(image.name.encode('utf-8'))
        name_img_min = Util.PATH_IMG_MIN + name_img[0:len(name_img) - 4] + Util.SYMBOL_MIN
        path_img_min = name_img_min + Util.EXTENSION
        path_complete = unicode(os.path.join(settings.MEDIA_ROOT) + path_img_min, 'utf-8')

        img = Image.open(image)

        wpercent = (width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img_min = img.resize((width, hsize), Image.ANTIALIAS)

        box = (0, 0, width, height)
        img_crop = img_min.crop(box)

        img_crop.save(path_complete)

        return path_img_min

    @staticmethod
    def is_new_image(image):
        new_image = False
        if not Util.PATH_IMG in str(
                image.name.encode('utf-8')):
            new_image = True

        return new_image