import os
import vk_api
import requests  # method for downloading photos
from PIL import Image  # method to show pictures
from io import BytesIO
from parser_main.security_values import access_token  # for security, my token is only accessible from local machine

# authentication info
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()



class VkImageGrabber:

    def __init__(self, group_id=-39043966, album_id=157131299, images_count=0):
        # if group id starts with positive number, this is a user. If with negative - it is a group
        self.group_id = group_id
        self.album_id = album_id
        self.images_count = images_count

    def grabbing_parameters(self):
        response = vk.photos.get(owner_id=self.group_id, album_id=self.album_id, count=self.images_count)
        # print('Response: ', response)
        return response

    def get_images_data(self):
        images_list = self.grabbing_parameters()['items']
        result = []
        # print('result', result, '\n')
        for image in images_list:
            result.append(
                    [
                        image['id'],  # picture id
                        image['owner_id'],  # user/ group id
                        image['album_id'],
                        image['date'],  # дата в виде UNIX-времени (POSIX-времени)
                        image['sizes'][-1]['url'],  # url to the biggest size is the last one in the dictionary
                        image['sizes'][5]['url'],  # url for thumbnail. In [5] the smallest size
                    ]
                )
        # print('Images_data: ', result)
        # print('Images data count : ', len(result))
        return result

    # =========================== methods for testing
    def show_image(self):
        images_data = self.get_images_data()
        image_to_show = 0
        print(images_data)
        result = requests.get(images_data[image_to_show][4])
        print(result)
        image = Image.open(BytesIO(result.content))
        image.show()

    def download_images(self):
        images_data = self.get_images_data()
        # path to save images
        save_images_to = "../../../Pictures/Photos/"
        os.makedirs(save_images_to, exist_ok=True)
        for ind in images_data:
            result = requests.get(ind[4])
            with open(f'{save_images_to}/vk_{ind[0]}.jpg', 'wb') as file:
                file.write(result.content)
                print('Image saved.')
        print(f"Saved {len(images_data)}" ' images')
    # =====================================


images_count = 10
# grabbed_images = VkImageGrabber(images_count=images_count)
grabbed_images = VkImageGrabber(images_count=images_count)

data_list = grabbed_images.get_images_data()

print(data_list)



# print(grabbed_images.show_image())
# print(grabbed_images.download_images())


#
# Надо добавить вывод названия гуппы и альбома



