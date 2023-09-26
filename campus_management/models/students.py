from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CampusStudent(models.Model):
    _name = "campus.student"
    _inherit = 'mail.thread'
    _description = "Student Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    ict_registered = fields.Boolean(string="ICT Registered", tracking=True)
    under_eighteen = fields.Boolean(string="Under Eighteen", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender",
                              tracking=True)
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
    ref = fields.Char(string="Student Number", default=lambda self: _('New'))
    lecture_id = fields.Many2one('campus.lecture', string='Lecture')
    tag_ids = fields.Many2many('res.partner.category','campus_student_tag_rel','student_number','tag_id', string="Tags")

    @api.model_create_multi
    def create(self, vals_lists):
        for vals in vals_lists:
            vals['ref'] = self.env['ir.sequence'].next_by_code('campus.student')
        return super(CampusStudent, self).create(vals_lists)

    @api.constrains('under_eighteen', 'age')
    def _check_student_age(self):
        for rec in self:
            if rec.under_eighteen and rec.age == 0:
                raise ValidationError(_("Age has to be recorded!"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = self.name.upper()
            else:
                rec.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 17:
            self.under_eighteen = True
        else:
            self.under_eighteen = False


