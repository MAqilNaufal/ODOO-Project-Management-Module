{
    'name': 'Project Management Module',
    'version': '1.0',
    'summary': 'A custom project management module for Odoo',
    'description': 'Manage projects, tasks, and teams with this custom module.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Project',
    'depends': ['base', 'project'],  # Add other dependencies as needed
    'data': [
        'security/ir.model.access.csv',  # Add the security file
        'views/project_management_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
