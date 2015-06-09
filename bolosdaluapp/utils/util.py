__author__ = 'edgard.barbosa'

from PIL import Image
import os.path
from BolosDaLu import settings


class Util(object):
    PATH_IMG_MIN = "images/uploads/galeria/img_min/"
    EXTENSION = ".jpg"
    SYMBOL_MIN = "_min"

    @staticmethod
    def create_small_image(image, width, height):
        name_img = str(image.name)
        name_img_min = Util.PATH_IMG_MIN + name_img[0:len(name_img) - 4] + Util.SYMBOL_MIN
        path_img_min = name_img_min + Util.EXTENSION

        img = Image.open(image)

        img_min = img.resize((width, height), Image.NEAREST)

        img_min.save(os.path.join(settings.MEDIA_ROOT) + name_img_min + Util.EXTENSION)

        return path_img_min