# -*- coding: utf-8 -*-

{
    'name': 'UOM extension',
    'version': '15.0.0.0.0',
    'category': 'UOM/UOM',
    'summary': 'Expansion and change of the UOM model and just units of measurement.',
    'description': """
        Expansion and change of the UOM model and just units of measurement.
    """,
    'depends': [
        'uom',
        'base',
    ],
    'data': [
        'views/test_account_view_move_form.xml',
        'views/uom_uom_views.xml',
        'views/product_template_tree_view.xml',
        'views/product_template_kanban_view.xml',
        'views/purchase_order_form.xml',
        'views/product_product_view.xml',
        'views/mrp_production_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'uom_extension/static/src/js/uom_widget.js',
            'uom_extension/static/src/js/fields/field_utils.js'
        ],
    },
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
