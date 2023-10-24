from odoo import api, fields, models

class CleaningInspection(models.Model):
    _inherit = 'fsm.order'

    toilet_cubicle = fields.Boolean(string=" Toilet Cubicle", default=False)
    floors = fields.Boolean(string=" Floors", default=False)
    urinals = fields.Boolean(string=" Urinals", default=False)
    walls = fields.Boolean(string=" Walls", default=False)
    basins = fields.Boolean(string=" Basins", default=False)
    toilet_paper = fields.Integer(string='Toilet Paper (If restocked kindly indicate qty)')
    mirrors = fields.Boolean(string=" Mirrors", default=False)
    bins = fields.Boolean(string=" Bins", default=False)
    seatsan = fields.Boolean(string=" SeatSan", default=False)
    handsoaps = fields.Boolean(string=" Hand Soaps", default=False)
    handtowels = fields.Boolean(string=" Hand Towels", default=False)

    cleaner_signature = fields.Binary(string="Cleaner Signature", widget ="signature")
    client_signature = fields.Binary(string="Client Signature", widget ="signature")
    manager_signature = fields.Binary(string="Manager Signature", widget = "signature")
    
