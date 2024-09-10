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
    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(string="Deadline")
    currency_id = fields.Many2one("res.currency", string="Currency", required=True, default=lambda self: self.env.company.currency_id)
    notes = fields.Text(string="Notes")