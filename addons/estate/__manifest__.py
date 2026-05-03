{
    'name': "Real Estate",
    'summary': "Real Estate",
    'description': "Real Estate",
    'author': "Saya",
    'website': "https://www.example.com",
    'category': "Real Estate",
    'version': "1.0",
    'depends': ["base"],
    'data': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',

        'views/estate_property_tag_views.xml',  
        'views/estate_property_type_views.xml',
        'views/estate_property_offer_views.xml',
    ]
}