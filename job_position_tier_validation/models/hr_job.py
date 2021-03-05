# Copyright 2019 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class Job(models.Model):
    _name = "hr.job"
    _inherit = ["hr.job", "tier.validation"]
    _state_from = ["open"]
    _state_to = ["recruit"]
    state = fields.Selection([
        ('recruit', 'Recruitment in Progress'),
        ('open', 'Not Recruiting')
    ], string='Status', readonly=True, required=True, tracking=True, copy=False, default='open',
        help="Set whether the recruitment process is open or closed for this job position.")
    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id, department_id)',
         'The name of the job position must be unique per department in company!'),
    ]
    expect_date = fields.Date("Expect Availability", help="The expect date at which the employee will be available to start working")
