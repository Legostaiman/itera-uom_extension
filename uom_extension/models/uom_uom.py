from odoo import models, fields


class UoMCategory(models.Model):
    _inherit = 'uom.uom'

    # The "translation" parameter must be changed to True, otherwise the
    # field cannot be found when using a language other than English.
    name = fields.Char(translate=False)
    digits_preview = fields.Float('Digits Preview',
                                  help="To change the settings for this field, contact your administrator.")
