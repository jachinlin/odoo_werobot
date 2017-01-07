# -*- coding: utf-8 -*-

from werobot import WeRoBot
from odoo.http import request


class WechatRobot(WeRoBot):
    pass


robot = WechatRobot(enable_session=True)


@robot.text
def authentication(message, session):
    """binding wechat users"""
    if session.get('is_wechat_authenticated'):
        session['is_wechat_authenticated'] = False
        name = message.content
        domain = ['|', '|', ('name', '=', name), ('login', '=', name), ('mobile', '=', name)]
        user = request.env['res.users'].sudo().search(domain, limit=1)
        if not user:
            return u"输入信息错误或者该账号不存在"
        if user.wechat_openid:
            return u"输入信息错误或者该账号不存在"
        user.wechat_openid = message.source
        return u"已绑定用户:" + user.name
    if message.content == u"微信用户认证":
        session['is_wechat_authenticated'] = True
        return u"请回复用户账号/名字/手机号"

    return 'hi & i love u '




