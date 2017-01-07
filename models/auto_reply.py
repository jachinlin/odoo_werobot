# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReplyCategory(models.Model):
    """自动回复问题分类"""
    _name = 'reply.category'

    name = fields.Char(string=u'问题类别', required=True)
    reply_ids = fields.One2many('reply', 'category_id', string=u'热门问题')


class Reply(models.Model):
    """自动回复问题分类"""
    _name = 'reply'

    name = fields.Char(string=u'问题', required=True)

    state = fields.Selection([    # 为了使用`states`属性，将此字段命名为`state`，最好命名为`reply_type`
        ('text', u'文本信息'),
        ('image', u'图片信息'),
        ('articles', u'图文信息'),
        ('voice', u'语音信息'),
        ('music', u'音乐信息'),
        ('video', u'视频信息'),
        ('success', u'不回复信息')], string=u'回复类型', required=True, default='text')

    category_id = fields.Many2one('reply.category', string=u'问题类别')
    user_group_ids = fields.Many2many('user.group', string=u'用户组',
                                      help='Only users in these groups will receive the reply')

    text_reply_id = fields.Many2one('text.reply', string=u'回复内容',
                                    states={'image': [('invisible', True)],
                                            'articles': [('invisible', True)],
                                            'voice': [('invisible', True)],
                                            'video': [('invisible', True)],
                                            'music': [('invisible', True)],
                                            'success': [('invisible', True)]}
                                    )
    image_reply_id = fields.Many2one('image.reply', string=u'回复内容',
                                     states={'text': [('invisible', True)],
                                             'articles': [('invisible', True)],
                                             'voice': [('invisible', True)],
                                             'video': [('invisible', True)],
                                             'music': [('invisible', True)],
                                             'success': [('invisible', True)]}
                                     )
    articles_reply_id = fields.Many2one('articles.reply', string=u'回复内容',
                                        states={'text': [('invisible', True)],
                                                'image': [('invisible', True)],
                                                'voice': [('invisible', True)],
                                                'video': [('invisible', True)],
                                                'music': [('invisible', True)],
                                                'success': [('invisible', True)]}
                                        )
    voice_reply_id = fields.Many2one('voice.reply', string=u'回复内容',
                                     states={'text': [('invisible', True)],
                                             'image': [('invisible', True)],
                                             'articles': [('invisible', True)],
                                             'video': [('invisible', True)],
                                             'music': [('invisible', True)],
                                             'success': [('invisible', True)]}
                                     )
    video_reply_id = fields.Many2one('video.reply', string=u'回复内容',
                                     states={'text': [('invisible', True)],
                                             'image': [('invisible', True)],
                                             'articles': [('invisible', True)],
                                             'voice': [('invisible', True)],
                                             'music': [('invisible', True)],
                                             'success': [('invisible', True)]}
                                     )
    music_reply_id = fields.Many2one('music.reply', string=u'回复内容',
                                     states={'text': [('invisible', True)],
                                             'image': [('invisible', True)],
                                             'articles': [('invisible', True)],
                                             'voice': [('invisible', True)],
                                             'video': [('invisible', True)],
                                             'success': [('invisible', True)]}
                                     )
    success_reply_id = fields.Many2one('success.reply', string=u'回复内容',
                                       states={'text': [('invisible', True)],
                                               'image': [('invisible', True)],
                                               'articles': [('invisible', True)],
                                               'voice': [('invisible', True)],
                                               'video': [('invisible', True)],
                                               'music': [('invisible', True)]})


class TextReply(models.Model):
    """文本信息回复"""
    _name = 'text.reply'

    name = fields.Char()


class ImageReply(models.Model):
    """图片信息回复"""
    _name = 'image.reply'

    name = fields.Char()


class VoiceReply(models.Model):
    """语音信息回复"""
    _name = 'voice.reply'

    name = fields.Char()


class VideoReply(models.Model):
    """视频信息回复"""
    _name = 'video.reply'

    name = fields.Char()


class ArticlesReply(models.Model):
    """图文信息回复"""
    _name = 'articles.reply'

    name = fields.Char()


class MusicReply(models.Model):
    """音乐信息回复"""
    _name = 'music.reply'

    name = fields.Char()


class SuccessReply(models.Model):
    """给微信服务器回复`success`"""
    _name = 'success.reply'

    name = fields.Char()

