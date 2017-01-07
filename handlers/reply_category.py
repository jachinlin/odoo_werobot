# -*- coding: utf-8 -*-

from odoo.http import request
import re
from . import robot

"""
        如果用户输入消息与自动回复类别名字匹配，
        则返回该类别下的所有问题的列表
"""


@robot.filter(re.compile('^#.*$'))
def questions(message, session):
    domain = [('name', 'ilike', message.content[1:])]
    reply_category_id = request.env['reply.category'].sudo().search(domain)
    if not reply_category_id:
        return u"没有该类别的问题"
    result = ''
    for category_id in reply_category_id:
        if category_id.reply_ids:
            result += '#' + category_id.name + '\n'
            for reply in category_id.reply_ids:
                result += str(reply.id) + '. ' + reply.name + '\n'
            result += '\n'
    if result:
        result += u'回复问题前面的序号获取答案'
    return result




