from odoo import api, fields, models


class PersonalInformation(models.Model):
    _inherit = 'bursary.personal_information'

    middle_name = fields.Char(string='First Name')
    country_of_citizenship = fields.Char(string='Country of Citizenship')
    home_phone = fields.Char(string='Home Phone')
    alternative_contact_first_name = fields.Char(string='Alternative Contact First Name')
    alternative_contact_Surname = fields.Char(string='Alternative Contact Surname')
    alternative_contact_marital_status = fields.Selection([('single', 'Single'), ('married', 'Married'),
                                                           ('divorced', 'Divorced'), ('widow', 'Widow')],
                                                          string="Marital Status")
    alternative_contact_id_passport = fields.Char(string='Alternative Contact ID/Passport')
    alternative_contact_phone_number = fields.Char(string='Alternative Contact Phone Number')
    alternative_contact_email = fields.Char(string='Alternative Contact Email')

    alternative_contact_street_name = fields.Char(string='Alternative Contact Street Name')
    alternative_contact_suburb = fields.Char(string='Alternative Contact Suburb')
    alternative_contact_city = fields.Char(string='Alternative Contact City')
    alternative_contact_province = fields.Char(string='Alternative Contact Province')
    alternative_contact_country = fields.Char(string='Alternative Contact Country')
    alternative_contact_postal_code = fields.Integer(string='Alternative Contact Postal Code')

    name_of_activity = fields.Char(string='Name of Activity')
    institution = fields.Char(string='Institution')
    position = fields.Char(string='Position')
    duration_of_involvement = fields.Char(string='Duration of Involvement')
    level = fields.Char(string='Level')
    reference = fields.Char(string='Reference')
#
# name_of_institution = fields.Char(string='Name of Institution')
# faculty_trade = fields.Char(string='Faculty / Trade')
# name_of_qualification = fields.Char(string='Name of Qualification')
# duration = fields.Char(string='Duration')
# name_of_institution = fields.Char(string='Name of Institution')
# faculty_trade = fields.Char(string='Faculty / Trade')
#
# name_of_qualification = fields.Char(string='Name of Qualification')
# duration = fields.Char(string='Duration')
# name_of_institution = fields.Char(string='Name of Institution')
# faculty_trade = fields.Char(string='Faculty / Trade')
# name_of_qualification = fields.Char(string='Name of Qualification')
# duration = fields.Char(string='Alternative Contact Postal Code')
# name_of_institution = fields.Char(string='Name of Institution')
# faculty_trade = fields.Char(string='Faculty / Trade')
# name_of_qualification = fields.Char(string='Name of Qualification')
# duration = fields.Char(string='Duration')
