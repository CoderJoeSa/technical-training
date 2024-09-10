from odoo import fields, models, api

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
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline", store=True)

   
    @api.depends('validity')
    def _compute_date_deadline(self):
            for rec in self:
                if rec.create_date:
                    create_date = fields.Datetime.from_string(rec.create_date)
                    rec.date_deadline = create_date 

    def _inverse_date_deadline(self):
        for rec in self:
            rec.create_date = fields.Datetime.to_string(rec.date_deadline)
            