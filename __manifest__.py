# -*- coding: utf-8 -*-
{
    'name': "tatausaha",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/dapodik_views.xml',
        'views/humas_views.xml',
        'views/kepegawaian_views.xml',
        'views/persuratan_views.xml',
        'views/kesiswaaan_views.xml',
        'views/keuangan_views.xml',
        'views/kurikulum_views.xml',
        'views/sarpras_views.xml',
        'views/menu_views.xml',
        'views/penugasan_report.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
