from odoo import fields, models

class FormeJuridique(models.Model):

    _name = 'forme.juridique'
    _description = 'Formes juridiques'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Acronyme', required=True)
    full_name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Description')

