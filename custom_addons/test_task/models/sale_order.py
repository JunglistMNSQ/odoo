from odoo import models


class SaleOrderRe(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrderRe, self).action_confirm()
        self.call_to_reorder()
        return res

    def call_to_reorder(self):
        for line in self.order_line:
            line.product_id.product_tmpl_id.auto_re_order()
