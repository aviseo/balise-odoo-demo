from odoo import api, fields, models, _


class CampusLecture(models.Model):
    _name = "campus.lecture"
    _inherit = 'mail.thread'
    _description = "Lectures Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender",
                              tracking=True)
    ict_registered_lecture = fields.Boolean(string="ICT Registered Lecture", tracking=True)

    ref = fields.Char(string="Stuff Number", default=lambda self: _('New'))
    active = fields.Boolean(default=True)

    @api.model_create_multi
    def create(self, value_lists):
        for values in value_lists:
            values['ref'] = self.env['ir.sequence'].next_by_code('campus.lecture')
        return super(CampusLecture, self).create(value_lists)

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = self.name.upper()
            else:
                rec.capitalized_name = ''

    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id, name))
        return res
