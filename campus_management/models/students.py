from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CampusStudent(models.Model):
    _name = "campus.student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
    priority = fields.Selection([('0', 'Low'), ('1','Normarl'), ('2', 'High'), ('3', 'Very High')], string ="Priority")
    state = fields.Selection([('draft', 'Draft'), ('in_progress','In Progress'), ('done', 'Done')],default='draft', string = "Status", required=True)
    dob = fields.Date( string = 'Date Of Birth')
    image = fields.Image(string ="Student Image")
    color = fields.Char(string = "Color") 
    active = fields.Boolean(string = "Active", default=True)
    registration_id = fields.Many2one('campus.student', string ="Registration")
    reason = fields.Text(string ="Reason")


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


    def action_button(self):
        print("Button Clicked")
        return {
            'effect':{
                
                    'fadeout' : 'slow',
                    'message': 'Click Successfull',
                    'type':'rainbow_man',

            }

        }

    @api.depends('dob')
    def _compute_age (self):
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1

        


