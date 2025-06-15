from odoo import fields, models

class ResCountryState(models.Model):

    _inherit = 'res.country.state'
    _description = 'Wilayas'

    code = fields.Char(string='Code Wilaya', size=2, help='Le code de la Wilaya sur deux positions', required=True)
    country_id = fields.Many2one('res.country', string='Pays', required=True)
    name = fields.Char(string='Wilaya', size=64, required=True)
    commune_ids = fields.One2many('res.commune', 'state_id', 'Communes', readonly=False)
