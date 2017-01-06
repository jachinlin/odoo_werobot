# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from ..models import robot
from ..contrib import make_view


class WeChat(http.Controller):

    def __init__(self):
        """initiate wechat robot"""
        param = request.env['ir.config_parameter']
        robot.config.update(
            TOKEN=param.get_param('token'),
            APP_ID=param.get_param('app_id'),
            APP_SECRET=param.get_param('app_secret')
        )

    @http.route('/wechat', type='http', auth="none", methods=['GET', 'POST'], csrf=False)
    def wechat(self, *args, **kwargs):
        """WeRoBot 挂载地址"""
        return make_view(robot)()



