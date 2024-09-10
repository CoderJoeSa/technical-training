from odoo import fields, models

class estate_property_offer (models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    property_id = fields.Many2one("estate.property", string="Property", required=True)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    price = fields.Float(string="Price", required=True)
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused'), ('pending', 'Pending')],
        default='pending',
    )
   