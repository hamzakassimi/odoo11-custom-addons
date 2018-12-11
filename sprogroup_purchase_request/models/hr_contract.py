# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing det


from odoo import fields, models,api
from odoo.addons import decimal_precision as dp
from odoo.tools.translate import _
from odoo.exceptions import UserError

class hr_contract(models.Model):
    _inherit = 'hr.contract'
    etat_contrat =  fields.Selection([('non_legalise', 'Non légalisé'),
	('legalise', 'Légalisé'),
	('integration', 'INTEGRATION'),
	('inactif', 'Inactif')])
