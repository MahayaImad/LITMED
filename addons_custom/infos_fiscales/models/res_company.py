from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re  # To use regular expressions for pattern matching


class ResPartnerFiscal(models.Model):
    _inherit = 'res.company'

    fax_number = fields.Char(string="Fax")

    rc = fields.Char(string="Numéro RC")
    nif = fields.Char(string="NIF")
    nis = fields.Char(string="NIS")
    ai = fields.Char(string="Article d'imposition")
    share_capital = fields.Char(string="Capital Social")

    nin = fields.Char(string="Numéro d'identification National")

    commune_id = fields.Many2one('res.commune', string='Commune')
    activity_code_ids = fields.Many2many('activity.code', string="Code d'activité")
    forme_juridique_id = fields.Many2one('forme.juridique', string="Formes juridiques")


    @api.onchange('commune_id')
    def commune_id_change(self):
        for company in self:
            company.state_id = company.commune_id.state_id.id
            company.city = company.commune_id.name
            company.country_id = company.commune_id.state_id.country_id.id

    _sql_constraints = [
        (
            'unique_nif',
            'unique(nif)',
            "Ce Numéro d'Identification Fiscale existe déjà."
        ),
        (
            'unique_nis',
            'unique(nis)',
            "Ce Numéro d'Identification Statistique existe déjà."
        ),
        (
            'unique_rc',
            'unique(rc)',
            "Ce Numéro de Registre de Commerce existe déjà."
        ),
        (
            'unique_ai',
            'unique(ai)',
            "Ce Numéro d'Article d'imposition existe déjà."
        ),
        (
            'unique_nin',
            'unique(nin)',
            "Ce Numéro d'Identification Fiscale existe déjà."
        ),
    ]

    @api.constrains('nif')
    def _check_nif(self):
        """
        Validates the NIF (Numéro d'Identification Fiscale) field.
        - Must be exactly 15 digits long.
        - Must contain only numeric characters.
        """
        for record in self:
            if record.nif:  # Check if the NIF field is not empty
                if not re.fullmatch(r'\d{15}', record.nif):
                    raise ValidationError(
                        "Le NIF doit contenir exactement 15 chiffres. "
                        "Veuillez vérifier le numéro saisi : %s" % record.nif
                    )

    @api.constrains('nis')
    def _check_nis(self):
        """
        Valide le NIS (Numéro d'Identification Statistique).
        - Vide = valide.
        - Si renseigné, doit être exactement 16 chiffres.
        """
        for record in self:
            if record.nis:  # Valider uniquement si le NIS est renseigné
                if not re.fullmatch(r'\d{16}', record.nis):
                    raise ValidationError(
                        "Le NIS doit contenir exactement 16 chiffres. "
                        "Veuillez vérifier le numéro saisi : %s" % record.nis
                    )
    @api.constrains('nin')
    def _check_nin(self):
        """
        Validates the NIN (Numéro d'Identification National) field.
        - Must be exactly 18 digits long.
        - Must contain only numeric characters.
        """
        for record in self:
            if record.nin:  # Check if the NIF field is not empty
                if not re.fullmatch(r'\d{18}', record.nin):
                    raise ValidationError(
                        "Le NIN doit contenir exactement 18 chiffres. "
                        "Veuillez vérifier le numéro saisi : %s" % record.nin
                    )
