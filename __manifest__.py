# -*- coding: utf-8 -*-
{
    'name': "Wechat",

    'summary': """
        Wechat
    """,

    'description': """
        Wechat Module:
            - user login
            - message push
            - blabla
    """,

    'author': "Jachin",
    'website': "https://github.com/jachinlin",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_users_view.xml',
        'views/user_group_view.xml',
        'views/article_view.xml',
        'views/reply_view.xml',
        'views/auto_reply_view.xml',
        'views/setting_wizard_view.xml',
        'views/wechat_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
