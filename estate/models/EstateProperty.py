from odoo import fields, models

class estate_property(models.Model):
    _name = "estate_property"
    _description = "Estate Property"

    name = fields.Char()