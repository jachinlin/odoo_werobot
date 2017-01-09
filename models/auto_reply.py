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

    @api.multi
    def werobot_reply_format(self):
        self.ensure_one()
        if self.state == 'text':
            result = self.text_reply_id.name + '\n' + self.text_reply_id.answer
        elif self.state == 'image':
            result = {}
        elif self.state == 'articles':
            article_ids = self.articles_reply_id.article_ids
            result = [[article.name, article.description, article.image_url, article.article_url]
                      for article in article_ids]
        elif self.state == 'voice':
            result = {}
        elif self.state == 'music':
            result = {}
        elif self.state == 'video':
            result = {}
        elif self.state == 'success':
            result = {}
        else:
            result = 'success'

        return result


class TextReply(models.Model):
    """文本信息回复"""
    _name = 'text.reply'

    name = fields.Char(string=u'标题', required=True)
    answer = fields.Text(string=u'回复', required=True)


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

    name = fields.Char(string=u'标题')
    article_ids = fields.Many2many('article', string=u'文章列表', required=True)

    @api.model
    def create(self, vals):
        """重写 检查文章数量"""
        article_ids = vals.get('article_ids')
        if len(article_ids[0][2]) > 8:
            raise models.UserError(u'图文回复文章数量最多为8篇！')

        return super(ArticlesReply, self).create(vals)

    @api.multi
    def write(self, vals):
        """重写 检查文章数量"""
        article_ids = vals.get('article_ids')
        if len(article_ids[0][2]) > 8:
            raise models.UserError(u'图文回复文章数量最多为8篇！')

        return super(ArticlesReply, self).write(vals)


class MusicReply(models.Model):
    """音乐信息回复"""
    _name = 'music.reply'

    name = fields.Char()


class SuccessReply(models.Model):
    """给微信服务器回复`success`"""
    _name = 'success.reply'

    name = fields.Char()


class Article(models.Model):
    """文章"""
    _name = 'article'

    name = fields.Char(u'标题', required=True)
    description = fields.Char(u'描述')
    image_url = fields.Char(string=u'图片')
    article_url = fields.Char(string=u'文章')




