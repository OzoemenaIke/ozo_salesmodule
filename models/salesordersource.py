from odoo import models, fields

class SalesOrderSource (models.Model):
    _name = 'sale.ordersource'
    name = fields.Char(string='OrderSource', required=False)
    _description = 'Sales Order Source'


