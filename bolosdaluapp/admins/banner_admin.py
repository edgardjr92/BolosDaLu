from image_cropping import ImageCroppingMixin

__author__ = 'Edgard JR'

from django.contrib import admin


class BannerAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass