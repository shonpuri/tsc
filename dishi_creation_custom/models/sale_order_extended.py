import openerp
from openerp import models, fields, api


class SalesLinesExtend(models.Model):
    _inherit = 'sale.order'

    total_commission_amount = fields.Float(string='Total Commission Amount', compute='_compute_total_commission_amount', store=True, digits=(16, 4))

    @api.depends('order_line.commission_amount')
    def _compute_total_commission_amount(self):
        for order in self:
            order_lines = order.order_line.filtered(lambda line: line.commission_amount is not None)
            order.total_commission_amount = sum(order_lines.mapped('commission_amount'))
