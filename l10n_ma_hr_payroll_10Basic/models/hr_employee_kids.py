# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)

class HrEmployeeKids(models.Model):
    _name = 'hr.employee.kids'
    _rec_name = 'name'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    name = fields.Char(
        string='Nom',
    )

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Père',
    )

    requested_client_limit = fields.date(
        string='Date de naissance',
    )

    # ------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------

#    @api.model
#    def create(self, values):
#        seq = self.env['ir.sequence'].next_by_code('partner_credit_limit')
#        values.update({
#            'ref': seq
#        })
#        return super(ResPartnerCredit, self).create(values)
