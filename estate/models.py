from odoo import fields, models

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"
    _order = "secuence"


    name = fields.Char(string="Name", required=True)  
    description = fields.Text(string="Description")