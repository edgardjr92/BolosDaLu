# -*- coding: utf-8 -*-
__author__ = 'edgard.barbosa'

from PIL import Image, ImageDraw
import os.path
from BolosDaLu import settings


class Util(object):
    PATH_IMG_MIN = "images/uploads/galeria/img_min/"
    EXTENSION = ".jpg"
    SYMBOL_MIN = "_min"

    @staticmethod
    def create_small_image(image, width, height):
        name_img = str(image.name.encode('utf-8'))
        name_img_min = Util.PATH_IMG_MIN + name_img[0:len(name_img) - 4] + Util.SYMBOL_MIN
        path_img_min = name_img_min + Util.EXTENSION
        path_complete = unicode(os.path.join(settings.MEDIA_ROOT) + path_img_min, 'utf-8')

        img = Image.open(image)

        img_min = img.resize((width, height), Image.NEAREST)

        img_min.save(path_complete)

        return path_img_min