{
    'name': 'Project Management Module',
    'version': '1.0',
    'summary': 'A custom project management module for Odoo with task dependencies, milestones, and Gantt chart.',
    'description': """
        Manage projects, tasks, subtasks, and milestones with this custom module. 
        Includes task dependencies, milestone tracking, and Gantt chart visualization.
    """,
    'author': 'MAqil Naufal',
    'website': 'https://yourwebsite.com',
    'category': 'Project',
    # Adding 'project' for Gantt and task management features
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',  # Security access control
        # XML for project, task, and milestone views
        'views/project_management_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
