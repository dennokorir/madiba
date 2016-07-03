# -*- coding: utf-8 -*-
{
    'name': "madiba",

    'summary': """
        Contains Extensions Specific to Madiba Properties
        """,

    'description': """
        =================================================
        Contains Extensions Specific to Madiba Properties
        =================================================
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Madiba',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'reports/reports.xml',
        'views/account_voucher.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
