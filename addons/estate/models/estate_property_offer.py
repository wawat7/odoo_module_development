from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

from odoo.tools import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float(string="Price", required=True)
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
        ],  
        string="Status",
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline and record.create_date:
                delta = record.date_deadline - record.create_date.date()
                record.validity = delta.days
            else:
                record.validity = (record.date_deadline - fields.Date.today()).days
    
    def action_accept(self):
        for record in self:
            if record.property_id.selling_price > record.price:
                raise UserError(_("Cannot accept an offer that is lower than the expected price."))
            if record.property_id.state == "sold" or record.property_id.state == "cancelled":
                raise UserError(_("Cannot accept an offer that is sold or cancelled."))
            if record.status == "accepted":
                raise UserError(_("Cannot accept an offer that is already accepted."))
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id

        return True
    
    def action_refuse(self):
        for record in self:

            if record.property_id.state == "sold":
                raise UserError(_("Cannot refuse an offer that is sold."))
            if record.status == "accepted":
                raise UserError(_("Cannot refuse an offer that is accepted."))

            record.status = "rejected"

        return True