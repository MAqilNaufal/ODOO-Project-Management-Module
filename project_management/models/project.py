from odoo import models, fields


class Project(models.Model):
    _name = 'project.management'
    _description = 'Project Management'

    partner_id = fields.Many2one(
        'res.partner', ondelete='cascade', required=True, string='Customer')
    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
