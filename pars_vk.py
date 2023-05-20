from io import BytesIO
import requests
import urllib.request
from PIL import Image, ImageStat
from io import BytesIO


# Переменные
TOKEN_USER = "vk1.a.hMhNmNJtZvWAiq5s0pikGGkxxSzTUVa-9y5VESGeXJQeX4RZNiljAmoeDualDaqIcGRRagoRzv5Ucj4a4ildMCl9E31ingrMqBN4wyQu58RO1nipThf-eWG7Xke2wFSAH5g1GA6Igq2Qfw3l3TRaC2oWwWssAWE2a4_Phzofyr_LaE0LLsczM0QZ1_LScHiI6xoqedOLdxqlawR8F2N_Hg"
VERSION = 5.131
DOMAIN = 'club39043966'

# Получаем список альбомов пользователя или группы

method_url = "https://api.vk.com/method/photos.get"
method_params = {
    'access_token': TOKEN_USER,
    'v': VERSION,
    "owner_id": "-39043966",
    "album_id": "157131299"
}

response = requests.get(method_url, params=method_params)
album_dict = response.json()
print("album_dict", album_dict)




# ================= показать картинку по ссылке =============

'''
url = 'https://sun9-62.userapi.com/impf/c303809/v303809470/a30/kXm4iXJbC_s.jpg?size=97x130&quality=96&sign=69146e34b8bb898e7dfc2d9a58edf4c7&c_uniq_tag=SQRSHlldxz67JOeO_sKDz5kBrnkMm-2uDlwLPO033OU&type=album'  # Замените на ваш URL изображения
response = requests.get(url)
image = Image.open(BytesIO(response.content))
image.show()
'''


def extract_attribute(data, name):
    """
    Функция для извлечения словаря с ключём "name" из
    "dictionary", который является многоуровневым словарём.
    """
    def find_attribute(dictionary):
        # print('Recursion start')
        if isinstance(dictionary, dict):
            if name in dictionary:
                # print('__AT LAST, desired has been found!__')
                return {name: dictionary[name]}
            else:
                # print('desired NOT found')
                for value in dictionary.values():
                    mid_result = find_attribute(value)
                    # print('size not found')
                    if mid_result is not None:
                        return mid_result
        elif isinstance(dictionary, list):
            # print("we're not in a dictionary anymore. This is the LIST!")
            for item in dictionary:
                result = find_attribute(item)
                if result is not None:
                    return result
        # print("The end?")
        return None

    # print("run find_attribute")
    result_of_recursion = find_attribute(data)
    return result_of_recursion

attribute_name = 'sizes'
attribute_value = extract_attribute(album_dict, attribute_name)
attribute_value = attribute_value[attribute_name]  # only list with ulr remains


def photos_url(dict):
    photo_list = []
    for p in dict:
        list_id = 0
        photo = dict[list_id]["url"]
        photo_list.append(photo)
        print(photo)
        list_id += 1

    return photo_list

# result_photo = photos_url(attribute_value)
#
# print(result_photo)
