from odoo import api, fields, models


class PersonalInformation(models.Model):
    _name = 'bursary.personal_information'
    _description = 'Personal Information'

    first_name = fields.Char(string='First Name')
    surname = fields.Char(string='Surname')
    dob = fields.Char(string='Date Of Birth')
    race = fields.Char(string='Race')
    home_language = fields.Char(string='Home language')
    identity_document_type = fields.Selection([('id', 'ID'), ('passport', 'Passport')],
                                              string='Identity Document Type ID/Passport')
    id_passport_no = fields.Char(string='ID/Passport Number')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    email = fields.Char(string='Email')
    house_number = fields.Integer(string='House Number')
    street_name = fields.Char(string='Street Name')
    Suburb = fields.Char(string='Suburb')
    city = fields.Char(string='Province')
    country = fields.Char(string='Country')
    postal_code = fields.Integer(string='Postal Code')
