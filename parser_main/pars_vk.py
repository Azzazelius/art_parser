import os
import vk_api
import requests  # method for downloading photos
from PIL import Image  # method to show pictures
from io import BytesIO
from parser_main.security_values import access_token  # for security, my token is only accessible from local machine

# authentication info
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()


"""
here is forming urls for photos. "items" is a list consists of several dictionaries.
As VK saves photos in different sizes, each photo size has its own url (key = "URL")
the biggest photo always is the last in the list. 
That's why to form a result list we take key "sizes", in that list take the last object [-1] and save "url" value
"""


class VkImageGrabber:

    def __init__(self, group_id=-39043966, album_id=157131299, images_count=0):
        self.group_id = group_id
        self.album_id = album_id
        self.images_count = images_count

    def grabbing_parameters(self):

        # if we need to get all images from the album we use first code. else - define desired quantity
        if self.images_count == 0:
            response = vk.photos.get(owner_id=self.group_id, album_id=self.album_id)
        else:
            response = vk.photos.get(owner_id=self.group_id, album_id=self.album_id, count=self.images_count)
        # print(response)
        requested_images_list = response['items']  # "items" is a key from the 'response' dictionary with a necessary data.
        return requested_images_list

    def form_id_url_pair(self):
        requested_images_list = self.grabbing_parameters()
        image_pairs_list = []
        for image in requested_images_list:
            im_id = image['id']
            im_url = image['sizes'][-1]['url']
            im_tuple = (im_id, im_url)
            image_pairs_list.append(im_tuple)
        print(image_pairs_list)
        return image_pairs_list

    # for thumbnails which will be added to the db
    def form_thumbnails_list(self):
        requested_images_list = self.grabbing_parameters()
        thumbnails_list = []
        for image in requested_images_list:
            im_id = image['id']
            im_url = image['sizes'][5]['url']  # [5] is the smallest size
            im_tuple = (im_id, im_url)
            thumbnails_list.append(im_tuple)
        print(thumbnails_list)
        return thumbnails_list

    def download_images(self):
        image_pairs = self.form_id_url_pair()
        # path to save images
        save_images_to = "../../../Pictures/Photos/"
        os.makedirs(save_images_to, exist_ok=True)
        for pair in image_pairs:
            result = requests.get(pair[1])
            with open(f'{save_images_to}/vk_{pair[0]}.jpg', 'wb') as file:
                file.write(result.content)
                print('Image saved.')

    def show_image(self):  # for test purpose only
        image_pairs = self.form_id_url_pair()
        result = requests.get(image_pairs[0][1])
        image = Image.open(BytesIO(result.content))
        image.show()


images_count = 3

# VkImageGrabber(image_count=image_count).download_images()
# VkImageGrabber(image_count=image_count).show_image()
VkImageGrabber(images_count=images_count).form_thumbnails_list()






