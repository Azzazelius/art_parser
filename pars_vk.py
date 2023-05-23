import os
import vk_api
import requests  # method for downloading photos
from PIL import Image, ImageStat  # method to show pictures
from io import BytesIO
from vk_api_token import access_token  # for security, my token is only accessible from local machine


vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

group_id = -39043966  # "-" is used to indicate that this is a group id, but positive numbers are used for user id
album_id = 157131299
print(album_id)
images_count = 0
# Find a way to download particular photos based on my filer parameters.

save_images_to = "../../../Pictures/Photos/"


"""
here is forming urls for photos. "items" is a list consists of several dictionaries.
VK saves photos in different sizes. Each size has its own url (key = "URL")
the biggest photo always is the last in the list. 
That's why to form a result list we take key "sizes", in that list take the last object [-1] and save "url" value
"""
def form_id_url_pair(input_list):
    pair_list = []
    for image in input_list:
        im_id = image['id']
        im_url = image['sizes'][-1]['url']
        im_tuple = (im_id, im_url)
        pair_list.append(im_tuple)
    print(pair_list)
    return pair_list


def download_images(input_pairs):
    os.makedirs(save_images_to, exist_ok=True)
    for pair in input_pairs:
        result = requests.get(pair[1])
        with open(f'{save_images_to}/vk_{pair[0]}.jpg', 'wb') as file:
            file.write(result.content)
            print('Image saved.')


def show_image(image_pairs):  # for test purpose only
    result = requests.get(image_pairs[0][1])
    image = Image.open(BytesIO(result.content))
    image.show()


# if we need to get all images from the album we use first code. else - define desired quantity
if images_count == 0:
    response = vk.photos.get(owner_id=group_id, album_id=album_id)
else:
    response = vk.photos.get(owner_id=group_id, album_id=album_id, count=images_count)
images_list = response['items']  # "items" is a key from the 'response' dictionary with a necessary data.

image_pairs = form_id_url_pair(images_list)
download_images(image_pairs)
# show_image(image_pairs)  # for testing






