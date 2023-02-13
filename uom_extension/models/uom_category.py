from odoo import models, fields


class UoMCategory(models.Model):
    _inherit = 'uom.category'

    digits_special_variant = fields.Boolean(default=False, compute='_compute_digits_special_variant')

    def _compute_digits_special_variant(self):
        for rec in self:
            rec.digits_special_variant = any(name in rec.uom_ids.mapped('name') for name in ['Units', 'Dozens'])
