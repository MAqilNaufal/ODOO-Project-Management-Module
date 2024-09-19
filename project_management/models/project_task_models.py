from odoo import models, fields, api
from odoo.exceptions import ValidationError


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

    # Task Dependency
    depends_on = fields.Many2one('project.task', string='Depends on Task')

    # Link to Milestone (missing field added here)
    milestone_id = fields.Many2one('project.milestone', string='Milestone')

    # Ensure no circular dependencies
    @api.constrains('depends_on')
    def _check_task_dependency(self):
        for task in self:
            if task.depends_on and task.depends_on.id == task.id:
                raise ValidationError("A task cannot depend on itself.")

    # Method to check if the task can start based on the dependency
    def check_task_start(self):
        if self.depends_on and self.depends_on.state != 'done':
            raise ValidationError(f"Task {self.name} cannot start until {
                                  self.depends_on.name} is completed.")


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

    task_ids = fields.One2many('project.task', 'milestone_id', string='Tasks')
    progress = fields.Float(
        string='Progress', compute='_compute_progress', store=True)

    @api.depends('task_ids.state')
    def _compute_progress(self):
        for milestone in self:
            total_tasks = len(milestone.task_ids)
            completed_tasks = len(milestone.task_ids.filtered(
                lambda task: task.state == 'done'))
            milestone.progress = (
                completed_tasks / total_tasks * 100) if total_tasks else 0
