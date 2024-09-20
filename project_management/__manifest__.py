{
    'name': 'Project Management Module',
    'version': '1.0.0',
    'summary': 'A custom project management module for Odoo with task dependencies, milestones, and Gantt chart.',
    'description': """
        Manage projects, tasks, subtasks, and milestones with this custom module. 
        Includes task dependencies, milestone tracking, and Gantt chart visualization.
    """,
    'author': 'MAqil Naufal',
    'website': 'https://github.com/MAqilNaufal/ODOO-Project-Management-Module',
    'category': 'Project',
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_management_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
