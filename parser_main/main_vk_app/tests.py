# Create your tests here.

from django.db.models import Max
from parser_main.art_parser_app.models import *
# from parser_main.art_parser_app.models import Owners
from models import Owners


# ============================= создать
#
# OWNER

        # id = models.IntegerField(primary_key=True)
        # owner_name = models.CharField(max_length=255)

owner1 = Owners.objects.create(id=1, owner_name='vasiliy')

# альбом


# фотографии