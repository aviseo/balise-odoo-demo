from odoo import api, fields, models, _


class CampusExtension(models.Model):
    _inherit = 'campus.student'

    parent_name = fields.Char(string='Parent Name')
    parent_mobile = fields.Char(string='Parent Mobile')

