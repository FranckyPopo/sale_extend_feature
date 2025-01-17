# -*- coding: utf-8 -*-
{
    'name': "Sale Extend Feature",

    'summary': "Application qui ajoute des fonctionnalités au module de vente",

    'description': """
        Application qui ajoute des fonctionnalités au module de vente
    """,

    'author': "Afri Kreto Franck",
    'website': "https://www.akfa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "auto_install": False,
    "application": True,
    'assets': {
    'web.assets_backend': [
            'sale_extend_feature/static/src/js/related_fields.js',
        ]
    }

}
