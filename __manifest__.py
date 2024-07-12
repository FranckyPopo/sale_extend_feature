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
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'car_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/car_management_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
}

