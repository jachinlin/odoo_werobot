# -*- coding: utf-8 -*-

from odoo.http import request
from odoo.models import MissingError
import re
from . import robot

"""
    根据用户输入的 reply_id 自动回复
"""


@robot.filter(re.compile('^\d+$'))
def questions(message, session):
    reply = request.env['reply'].sudo().search([('id','=', int(message.content))], limit=1)
    if not reply:
        return u"该问题神奇般的消失了"
    result = reply.werobot_reply_format()

    return result




