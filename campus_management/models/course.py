from odoo import api, fields, models, _


class CampusCourse(models.Model):
    _name = "campus.course"
    _inherit = 'mail.thread'
    _description = "Course Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    ict_faculty = fields.Boolean(string="ICT Faculty", tracking=True)
    humanities_faculty = fields.Boolean(string="Humanities Faculty", tracking=True)

    ref = fields.Char(string="Course ID", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, value_lists):
        for values in value_lists:
            values['ref'] = self.env['ir.sequence'].next_by_code('campus.course')
        return super(CampusCourse, self).create(value_lists)
