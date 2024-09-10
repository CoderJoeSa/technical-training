from odoo import fields, models, api

class estate_property(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    country_id = fields.Many2one("res.country", string="Country")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Availability" , default=fields.Date.today)
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
    user_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    tags_id = fields.Many2many("estate.property.tag", string="Property Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id",string="Offers")
    total_area = fields.Char(compute="_compute_total_area", store=True)
    best_price = fields.Float(string="Best Price", compute="_compute_best_price", store=True , inverse="_inverse_best_price")

    @api.depends('living_area', 'garden_area')

    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    def _compute_best_price(self):
        for rec in self:
            rec.best_price = rec.expected_price - 10000

            
