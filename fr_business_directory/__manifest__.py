# -*- coding: utf-8 -*-
{
    'name': "French Business Directory",

    'summary': """Quick Search for Business Directory""",

    'description': """
        This module implements a quick searchbar for Business Directory with an identical appearance to the native one.
    """,

    'author': "Doodex",
    'website': "https://www.doodex.net/",
    'license': 'LGPL-3',

    'category': 'Extra Tools',
    'version': '16.0.1.0.7',
    'application': False,

    'depends': ['base' , 'l10n_fr'],

    "data": [
        'security/ir.model.access.csv',
        "views/menu_item.xml",
        "views/partner.xml",
        "views/siret_wizard_views.xml",
    ],
    'images': [
        'static/description/icon.png',
    ],

    'assets': {
    }
}

