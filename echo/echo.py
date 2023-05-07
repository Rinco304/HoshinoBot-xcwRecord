import random
import os
import requests

from nonebot import MessageSegment
import hoshino
from hoshino import R, Service, priv, util
from nonebot import NoticeSession

help_text='''
这是一个桃按钮，收集了部分某holocn成员的b动静
[@bot+我爱你]   taffy爱你哟
[来点塔菲|来点taffy|来点cfm]   随机taffy能量
[@bot+晚安]     来自cfm的晚安
[想听生日歌]    送上cfm限定生日歌一首
[爽死了]    爽死了
[对呀对呀]      对呀对呀
'''.strip()

sv = Service('来点taffy', enable_on_default=True, help_=help_text)


# @sv.on_fullmatch(('我好了', 'whl'))
# async def wohaole(bot, event):
#     voice = R.get('record/echo/', 'whl.mp3')
#     rec = MessageSegment.record(f'file:///{os.path.abspath(voice.path)}')
#     await bot.send(event, rec)


@sv.on_fullmatch('hso', '好涩噢', '好涩哦', '好色噢', '好色哦')
async def hso(bot, event):
    if random.random() <= 0.2:
        voice = R.get('record/echo/', 'hso.mp3')
    elif random.random() > 0.2 and random.random() <= 0.5:
        voice = R.get('record/echo/', 'cheche.mp3')
    elif random.random() > 0.5 and random.random() <= 0.6:
        voice = R.get('record/echo/', 'echohso.mp3')
    else:
        voice = R.get('record/echo/', 'hso.mp3')
    rec = MessageSegment.record(f'file:///{os.path.abspath(voice.path)}')
    await bot.send(event, rec)


@sv.on_fullmatch('对呀对呀')
async def duiya(bot, event):
    voice = R.get('record/echo/', 'duiya.mp3')
    rec = MessageSegment.record(f'file:///{os.path.abspath(voice.path)}')
    await bot.send(event, rec)


@sv.on_fullmatch('爽死了')
async def ywwuyidie(bot, event):
    voice = R.get('record/echo/', 'ywwuyidie.mp3')
    rec = MessageSegment.record(f'file:///{os.path.abspath(voice.path)}')
    await bot.send(event, rec)


@sv.on_fullmatch('想听生日歌', '今天我生日', '祝我生日快乐', '祝自己生日快乐', '生日快乐')
async def shengrige(bot, event):
    voice = R.get('record/echo/', 'shengri.mp3')
    rec = MessageSegment.record(f'file:///{os.path.abspath(voice.path)}')
    await bot.send(event, rec)


@sv.on_fullmatch('我爱你', only_to_me=True)
async def woaini(bot, event):
    if random.random() <= 0.3:
        voice = R.get('record/echo/', 'jiehun.mp3')
    elif random.random() > 0.3 and random.random() <= 0.6:
        voice = R.get('record/echo/', 'aini.mp3')
    elif random.random() > 0.6 and random.random() <= 0.8:
        voice = R.get('record/echo/', 'woaini.m4a')
    else:
        voice = R.get('record/echo/', 'jiehun2.mp3')
    rec = MessageSegment.record(f'file:///{os.path.abspath(voice.path)}')
    await bot.send(event, rec)


@sv.on_fullmatch(('晚安', '睡了', '睡觉了', '眠了'), only_to_me=True)
async def sleep(bot, event):
    if random.random() <= 0.3:
        voice = R.get('record/echo/', '晚安.mp3')
    elif random.random() > 0.3 and random.random() <= 0.6:
        voice = R.get('record/echo/', '不想睡觉.mp3')
    elif random.random() > 0.6 and random.random() <= 0.8:
        voice = R.get('record/echo/', '不行不行.mp3')
    else:
        voice = R.get('record/echo/', '不想睡觉-n.mp3')
    rec = MessageSegment.record(f'file:///{os.path.abspath(voice.path)}')
    await bot.send(event, rec)


@sv.on_fullmatch(('来点塔菲', '来点taffy', '来点cfm'))
async def random_echo(bot, event):
    echo_folder = R.get('record/echo/').path
    files = os.listdir(echo_folder)
    filename = random.choice(files)
    file = R.get('record/echo/', filename)
    rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
    await bot.send(event, rec)
