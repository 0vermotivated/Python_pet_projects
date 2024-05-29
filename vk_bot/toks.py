import vk_api
import time
import random
from vk_api.longpoll import VkLongPoll, VkEventType



main_token = ""
#токен сообщества вк



vk_session = vk_api.VkApi(token=main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
coms = []
com = open("com.txt", encoding='utf-8')
for i in range(62):
    coms.append(str(com.readline())[0:-1])
def sender(id, text):
    vk_session.method("messages.send", {"user_id" : id, "message" : text, "random_id" : 0})
while True:
    if int(time.time()) % 14400 == 0:
        sender(519227997, coms[random.randint(0, 61)])
