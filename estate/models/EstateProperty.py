from odoo import fields, models

class estate_property(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    country_id = fields.Many2one("res.country", string="Country")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Availability" , default=fields.Date.today, nowrap=True)
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(string="Selling Price" , readonly=True)
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
    )
    state = fields.Selection(
        string="Status",
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold')],
        default='new',
    )
    active = fields.Boolean(string="Active", default=True)
    last_seen = fields.Datetime(string="Last Seen", readonly=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")