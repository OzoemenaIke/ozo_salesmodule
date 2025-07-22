from odoo import models, fields

class SalesOrder(models.Model):
    _inherit = 'sale.order'
    ordersource_id = fields.Many2one('sale.ordersource', string='OrderSource', ondelete="set null")
