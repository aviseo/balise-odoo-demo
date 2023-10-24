from odoo import api, fields, models, _


class CampusExtension(models.Model):
    _inherit = 'campus.student'

    parent_name = fields.Char(string='Parent Name')
    parent_mobile = fields.Char(string='Parent Mobile')



    def action_registration(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state ='in_progress'
       

    
        