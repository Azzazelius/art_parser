
import vk_api

from parser_main.security_values import access_token  # for security, my token is only accessible from local machine

# authentication info
vk_session = vk_api.VkApi(token=access_token)  # enter my token
vk = vk_session.get_api()  # get access to the API


class VkImageGrabber:

    def __init__(self, screen_id=-39043966, album_id=157131299, images_count=2):
        # if group id starts with positive number, this is a user. If with negative - it is a group
        self.screen_id = screen_id
        self.album_id = album_id
        self.images_count = images_count

    def owner_type(self):
        if isinstance (self.screen_id, int):  # Если в url прописаны цифры, то тип овнера определяем по + / - значению
            if self.screen_id < 0:
                owner_type = 'group'
            else:
                owner_type = 'user'
        else:                    # если значение не числовое, то находим тип методом АПИ
            screen_name = vk.utils.resolveScreenName(screen_name=self.screen_id)
            owner_type = screen_name['type']
        # print(owner_type)
        return owner_type


    def decode_id(self):
        owner_type = self.owner_type()
        if owner_type == 'group':
            if isinstance(self.screen_id, int):
                object_id = abs(self.screen_id)  # если это группа и в адресе число, то берётся его значение по модулю

            else:  # если в адресе название, то id получаем через resolveScreenName
                group_info = vk.utils.resolveScreenName(screen_name=self.screen_id)
                object_id = abs(group_info['object_id'])  # тут надо указывать полученный id
            group_id = vk.groups.getById(group_id=object_id)
            id_name_result = [group_id[0]['id'], group_id[0]['name']]
            # print('Group_id = ', id_name_result[0], 'Group_name = ', id_name_result[1], '\n')
            return id_name_result
        else:
            if isinstance(self.screen_id, int):  # если это пользоваатель и в адресе число
                object_id = abs(self.screen_id)
            else:
                screen_name = vk.utils.resolveScreenName(screen_name=self.screen_id)
                object_id = screen_name['object_id']
            user_first_name = vk.users.get(user_id=self.screen_id)[0]["first_name"]
            user_last_name = vk.users.get(user_id=self.screen_id)[0]["last_name"]
            id_name_result = list([object_id, (f"{user_first_name}_{user_last_name}")])
            # print('User_id = ', id_name_result[0], 'User_name = ', id_name_result[1], '\n')
        return id_name_result

    def grabbing_parameters(self):
        response = vk.photos.get(owner_id=self.screen_id, album_id=self.album_id, count=self.images_count)
        # print('Response: ', response)
        return response

    def get_images_data(self):
        images_list = self.grabbing_parameters()['items']
        result = []
        for image in images_list:
            result.append(
                    [
                        image['id'],  # picture id
                        image['owner_id'],  # user / group id
                        # owner name
                        image['album_id'],
                        # album name
                        image['date'],  # дата в виде UNIX-времени (POSIX-времени)
                        image['sizes'][-1]['url'],  # url to the biggest size is the last one in the dictionary
                        image['sizes'][5]['url'],  # url for thumbnail. In [5] the smallest size
                    ]
                )
        print('Images_data: ', result)
        print('Images data count : ', len(result))
        return result

    def __str__(self):
        return f"group_id = {self.screen_id}, album_id =  {self.album_id}, images_count = {self.images_count}"





# def album_name(album):  # <====================== Тут получаем название выбранного альбома
#     album_data = vk.photos.getAlbums(owner_id=album[0], album_ids=owner_album[1])
#     print('album_data: ', album_data)
#     name = album_data['items'][0]['title']
#     print('album_name: ', name)
#     return name

# owner_album = (-39043966, 157131299)
# album_name(owner_album)






# ============================== Testing


images_count = 2
# owner_id = "lentach"
owner_id = -39043966
# owner_id = "durov"
# owner_id = 52373470
album_id = 157130717
grabbed_images = VkImageGrabber(screen_id=owner_id, album_id=album_id, images_count=images_count)

info = grabbed_images.decode_id()
# info = grabbed_images.decode_test()
# info = grabbed_images.owner_type()

print(info)

# result = vk.utils.resolveScreenName(screen_name=owner_id)
# print(result)
#


# images_count = 2
# owner_id = '52373470'
# album_id = '123720889'
# grabbed_images = VkImageGrabber(owner_id=owner_id, album_id=album_id, images_count=images_count)
#
# print(grabbed_images.get_images_data())






# ======================
# ids = vk.utils.resolveScreenName(screen_name="durov")['object_id']
# res = vk.users.get(user_id=ids)
#
# # print(res)
# # print('User_id = ', id_name_result[0], 'User_name = ', id_name_result[1], '\n')
# print(ids, (res[0]["first_name"] + " " + res[0]["last_name"]))




