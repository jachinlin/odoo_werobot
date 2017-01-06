# -*- coding: utf-8 -*-

from werobot import WeRoBot


class WechatRobot(WeRoBot):
    pass


robot = WechatRobot()

@robot.text
def echo(message):
    return message.content + ' & i love u'




