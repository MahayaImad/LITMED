# __manifest__.py
{
    'name': 'Infos Fiscales Dz',
    'version': '1.1',
    'category': 'Localization',
    'summary': 'Ajoute des informations fiscales pour les clients et fournisseurs',
    'description': 'Ajoute des champs NIF, NIS, RC et AI dans les informations des partenaires (clients et fournisseurs)',
    'author': 'MAHAYA IMAD',
    'depends': ['base','mail','contacts','account'],
    'data': [
        'security/ir.model.access.csv',

        'data/activity_code_data.xml',
        'data/res_forme_juridique.xml',
        'data/wilayas_data.xml',
        'data/commune_data.xml',

        'views/partner_views.xml',
        'views/forme_juridique_views.xml',
        'views/commune_views.xml',
        'views/country_state_views.xml',
        'views/activity_code.xml',
        'views/res_company.xml',

        #'reports/infos_fiscales_report.xml',
    ],
    'icon': 'static/src/img/logo_if.png',
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
