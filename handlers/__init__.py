# -*- coding: utf-8 -*-


from ..models import WechatRobot

# 实例化微信机器人
robot = WechatRobot(enable_session=True)

# 添加 handler
from . import authentication
from . import reply_category
from . import reply

