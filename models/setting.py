# -*- coding: utf-8 -*-

import werobot.utils
from odoo import models, fields, api


class Setting(models.TransientModel):
    _name = 'wechat.settings'
    _inherit = 'res.config.settings'

    app_id = fields.Char('AppId', )
    app_secret = fields.Char('AppSecret', )
    token = fields.Char('Token')
    access_token = fields.Char('Access Token')
    url = fields.Char('URL', readonly=True)

    @api.multi
    def set_appid(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('app_id', config.app_id)
        param.set_param('app_secret', config.app_secret)
        param.set_param('token', config.token)
        param.set_param('url', config.url)

    @api.multi
    def set_app_id(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('app_id', config.app_id)

    @api.multi
    def set_app_secret(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('app_secret', config.app_secret)

    @api.multi
    def set_token(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('token', config.token)

    @api.multi
    def set_url(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('url', config.url)

    @api.model
    def get_default_app_id(self, fields):
        """get config information from database"""
        param = self.env["ir.config_parameter"]
        return {
            'app_id': param.get_param('app_id'),
            'app_secret': param.get_param('app_secret'),
            'token': param.get_param('token', default=werobot.utils.generate_token()),
            'url': param.get_param('url', default='/wechat'),
        }
