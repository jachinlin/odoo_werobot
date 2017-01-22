# -*- coding: utf-8 -*-

from odoo import api, fields, models


class UserGroup(models.Model):
    _name = "user.group"

    name = fields.Char(string='Name', requried=True)
    user_ids = fields.One2many('res.users', 'user_group_id', string='Users')
    channel_id = fields.Many2one("mail.channel", string=u'讨论频道')
    comment = fields.Text('Additional Information')
    active = fields.Boolean('Active', default=True)

    @api.model
    def create(self, vals):
        """创建用户组时，创建相应的频道"""
        group = super(UserGroup, self).create(vals)
        channel = self.env['mail.channel'].create({'name': group.name})
        channel.channel_partner_ids |= self.env.user.partner_id
        group.channel_id = channel
        return group


class ResUsers(models.Model):
    _inherit = 'res.users'

    wechat_openid = fields.Char(string=u'Wechat OpenID', help=u'Wechat OpenID')
    user_group_id = fields.Many2one('user.group', string='User Group')

    @api.model
    def create(self, vals):
        """重写"""
        # 检查用户名字重复性
        user_name = vals.get('name')
        exist_names = self.env['res.users'].search([]).mapped('name')
        if user_name and (user_name in exist_names):
            raise models.ValidationError('You can not have two users with the same name')
        # 检查用户手机重复性
        user_mobile = vals.get('mobile')
        exist_mobiles = self.env['res.users'].search([]).mapped('mobile')
        if user_mobile and (user_mobile in exist_mobiles):
            raise models.ValidationError('You can not have two users with the same mobile')

        return super(ResUsers, self).create(vals)

    @api.multi
    def write(self, vals):
        """重写"""
        # 检查用户名字重复性
        user_name = vals.get('name')
        exist_names = self.env['res.users'].search([]).mapped('name')
        if user_name and (user_name in exist_names):
            raise models.ValidationError('You can not have two users with the same name')
        # 检查用户手机重复性
        user_mobile = vals.get('mobile')
        exist_mobiles = self.env['res.users'].search([]).mapped('mobile')
        if user_mobile and (user_mobile in exist_mobiles):
            raise models.ValidationError('You can not have two users with the same mobile')

        return super(ResUsers, self).write(vals)



