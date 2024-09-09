from odoo import fields, models

class estate_property_type(models.Model):
    _name = "estate.property.tipe"
    _description = "Estate Property Tipe"

    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many("estate.property", "property_tipe_id", string="Properties")
    property_count = fields.Integer(string="Property Count", compute="_compute_property_count")

    def _compute_property_count(self):
        for record in self:
            record.property_count = len(record.property_ids)