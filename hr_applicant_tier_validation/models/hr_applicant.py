# Copyright 2019 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class Applicant(models.Model):
    _name = "hr.applicant"
    _inherit = ["hr.applicant", "tier.validation"]
    _state_from = ["processing"]
    _state_to = ["proposal"]
    state = fields.Selection([
        ('processing', 'In Progress'),
        ('proposal', 'Proposal')
    ], string='Status', required=True, tracking=True, copy=False, default='processing',
        help="Set whether the recruitment process is open or closed for this job position.")

    @api.onchange('stage_id')
    def onchange_stage_id(self):
        #vals = self._onchange_stage_id_internal(self.stage_id.id)
        print('stage_id-------', self.stage_id)
        print('vals ###', self.stage_id.id)
        print('state ####', self.state)
        if self.stage_id.id == 4:
            print("if state &&&&&:", self.state)
            self.state = 'proposal'
        else:
            self.state = 'processing'
            print('processing ......')
