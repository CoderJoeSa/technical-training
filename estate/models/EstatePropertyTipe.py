from odoo import fields, models

class estate_property_type(models.Model):
    _name = "estate.property.tipe"
    _description = "Estate Property Tipe"

    name = fields.Char(string="Name", required=True)
    