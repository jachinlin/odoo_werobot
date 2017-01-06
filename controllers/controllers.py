# -*- coding: utf-8 -*-
from odoo import http

# class Wechat(http.Controller):
#     @http.route('/wechat/wechat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wechat/wechat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wechat.listing', {
#             'root': '/wechat/wechat',
#             'objects': http.request.env['wechat.wechat'].search([]),
#         })

#     @http.route('/wechat/wechat/objects/<model("wechat.wechat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wechat.object', {
#             'object': obj
#         })