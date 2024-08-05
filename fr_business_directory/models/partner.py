from odoo import api, fields, models, _
from odoo.tools import config

class ResPartner(models.Model):
    _inherit = 'res.partner'
    social_reason = fields.Char(string='Social Reason', tracking=True)

    def siret_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Search For Companies'),  # Translatable string wrapped with _
            'res_model': 'siret.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'active_id': self.id,
            },
        }