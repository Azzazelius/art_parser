from django.forms import ModelForm
# import models
from models import (Owners, Albums, VkImages)


class Owners_form(ModelForm):
    class Meta:
        model = Owners
        fields = '__all__'


class VkImages_form(ModelForm):
    class Meta:
        model = VkImages
        fields = '__all__'
