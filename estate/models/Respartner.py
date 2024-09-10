from odoo import fields, models

class res_partner(models.Model):
    _inherit = "res.partner"

    property_ids = fields.One2many("estate.property", "buyer_id", string="Properties")
    offer_ids = fields.One2many("estate.property.offer", "partner_id", string="Offers")
    offer_count = fields.Integer(string="Offer Count", compute="_compute_offer_count")

    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)