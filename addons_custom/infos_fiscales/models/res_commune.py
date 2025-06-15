from odoo import fields, models


class ResCommune(models.Model):
    _name = 'res.commune'
    _description = 'Communes'
    _order = 'name,id'

    name = fields.Char(string='Commune', size=64, required=True)
    code = fields.Char(string='Code Commune', size=4, help='Le code de la commune sur 4 positions', required=True)
    state_id = fields.Many2one('res.country.state', string='Wilaya', required=True)
    country_id = fields.Many2one('res.country', 'Pays', ondelete='cascade')
