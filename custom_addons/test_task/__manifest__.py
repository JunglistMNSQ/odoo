# -*- coding: utf-8 -*-
{
    'name': "test_task",

    'summary': """
        this module is implementating auto reorder product, when a balance of
        product has been lower entered value. 
        
        """,

    'description': """
        Soon
    """,

    'author': "Vladimir",
    'email': "nuts.tech@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'purchase', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}