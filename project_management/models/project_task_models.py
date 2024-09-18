from odoo import models, fields


class ProjectTask(models.Model):
    _name = 'project.task'
    _description = 'Project Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    project_id = fields.Many2one(
        'project.management', string='Project', required=True)
    assigned_user_id = fields.Many2one('res.users', string='Assigned To')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    state = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='State', default='todo')

    # Sub-task relationship
    parent_task_id = fields.Many2one('project.task', string='Parent Task')
    sub_task_ids = fields.One2many(
        'project.task', 'parent_task_id', string='Sub Tasks')


class ProjectMilestone(models.Model):
    _name = 'project.milestone'
    _description = 'Project Milestone'

    name = fields.Char(string='Milestone Name', required=True)
    project_id = fields.Many2one(
        'project.management', string='Project', required=True)
    due_date = fields.Date(string='Due Date')
    state = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('achieved', 'Achieved')
    ], string='State', default='upcoming')
