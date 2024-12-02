# -*- coding: utf-8 -*-

from odoo import models, fields, api


class advance_odoo(models.Model):
    _name = 'advance_odoo.advance_odoo'
    _description = 'advance_odoo.advance_odoo'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
	for record in self:
	    record.value2 = float(record.value) / 100
