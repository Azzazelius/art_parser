import vk_api
from parser_main.security_values import access_token  # for security, my token is only accessible from local machine
import datetime

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

    def decode_id(self):  # получаем id и название объекта
        owner_type = self.owner_type()
        if owner_type == 'group':
            if isinstance(self.screen_id, int):
                object_id = abs(self.screen_id)  # если это группа и в адресе число, то берётся его значение по модулю

            else:  # если в адресе название, то id получаем через resolveScreenName
                group_info = vk.utils.resolveScreenName(screen_name=self.screen_id)
                object_id = abs(group_info['object_id'])  # тут надо указывать полученный id
            group_id = vk.groups.getById(group_id=object_id)
            id_name_result = [group_id[0]['id'] * -1, group_id[0]['name']]  # * -1 - coz group id must be negative
            # print('decoded. Group_id = ', id_name_result[0], 'Group_name = ', id_name_result[1], '\n')
            return id_name_result
        else:
            if isinstance(self.screen_id, int):  # если это пользоваатель и в адресе число
                object_id = abs(self.screen_id)
            else:
                screen_name = vk.utils.resolveScreenName(screen_name=self.screen_id)
                object_id = screen_name['object_id']
            user_first_name = vk.users.get(user_id=self.screen_id)[0]["first_name"]
            user_last_name = vk.users.get(user_id=self.screen_id)[0]["last_name"]
            id_name_result = list([object_id, f"{user_first_name} {user_last_name}"])
            # print('decoded. User_id = ', id_name_result[0], 'User_name = ', id_name_result[1], '\n')
        return id_name_result

    def grabbing_parameters(self):
        obj_id = self.decode_id()[0]

        if self.images_count > 0:
            response = vk.photos.get(owner_id=obj_id, album_id=self.album_id, count=self.images_count)
        else:
            response = vk.photos.get(owner_id=obj_id, album_id=self.album_id)
        # print('Response: ', response)
        return response

    def get_album_name(self):
        obj_id = self.decode_id()[0]   #--- !!!! добавить кэширование !!! --- это значение повторяется в разных методах
        album_info = vk.photos.getAlbums(owner_id=obj_id, album_ids=self.album_id)
        name = album_info['items'][0]['title']
        # print('album_name: ', name)
        return name

    def get_images_data(self):
        images_list = self.grabbing_parameters()['items']
        object_id = self.decode_id()[0]
        object_name = self.decode_id()[1]
        object_type = self.owner_type()
        album_name = self.get_album_name()
        result = []
        for image in images_list:
            date = datetime.datetime.fromtimestamp(image['date']) # UNIX-time (POSIX)
            creation_date = date.strftime('%Y-%m-%d')
            result.append(
                    [
                        image['id'],  # picture id
                        object_id,  # owner id
                        object_type,  # owner_type
                        object_name,  # owner name
                        image['album_id'],
                        album_name,  # album name
                        creation_date,
                        image['sizes'][-1]['url'],  # url to the biggest size is the last one in the dictionary
                        image['sizes'][5]['url'],  # url for thumbnail. In [5] the smallest size
                    ]
                )
        # description:
        # image_id, owner_id, owner_type, owner_name, album_id, album_name, creation_date, big_picture, thumbnail

        # print('get. Images_data: ', result)
        # print('get. Images data count : ', len(result))
        return result

    def __str__(self):
        return f"input data: Screen_name = {self.screen_id}, album_id =" \
               f"  {self.album_id}, images_count = {self.images_count}"








# ============================== Testing


images_count = 0
# тест на моей группе
owner_id = -39043966
album_id = 157130717

# тест на Ване
# owner_id = 7689860
# owner_id = "i_shokhin"
# album_id = 225552311

grabbed_images = VkImageGrabber(screen_id=owner_id, album_id=album_id, images_count=images_count)

# print(grabbed_images)
print(grabbed_images.get_images_data())
# grabbed_images.get_album_name()

# info = grabbed_images.decode_id()
# print(info)




