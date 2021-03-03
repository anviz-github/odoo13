# -*- coding: utf-8 -*-
{
    'name': "device",

    'summary': """
        客户端来建一笔记录，传device id上来，odoo返回记录id； odoo根据新建记录的，如果quota>0,odoo发device id向服务器申请key，客户端再来查询key""",

    'description': """
        Device key request
    """,

    'author': "Awahuang",
    'website': "http://www.anviz.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customize',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/device_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/device_menu.xml',
        'views/server_view.xml',
        'views/device_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
