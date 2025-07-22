from odoo import models, fields

class SalesOrderSource (models.Model):
    _name = 'sale.ordersource'
    _description = 'Sales Order Source'

    name = fields.Char(string='OrderSource', required=False)



