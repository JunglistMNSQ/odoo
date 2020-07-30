from odoo import fields, models
from datetime import datetime


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    auto_re_order_ok = fields.Boolean('Auto re-Order', default=False)
    auto_re_order_condition = fields.Integer(
        'When The Product quantity is lower this value, re-order will do',
        default=0
    )

    def auto_re_order(self):
        if self.auto_re_order_ok and self.product_variant_id.qty_available < self.auto_re_order_condition:
            diff = self.auto_re_order_condition - self.product_variant_id.qty_available
            for vendor in self.seller_ids:
                now = datetime.now()
                order = self.env['purchase.order'].create({'partner_id': vendor.name.id})
                self.env['purchase.order.line'].create(
                    {'product_id': self.product_variant_id.id,
                     'partner_id': vendor.name.id,
                     'name': self.name,
                     'product_qty': diff,
                     'date_planned': now,
                     'product_uom': self.uom_po_id.id,
                     'price_unit': vendor.price,
                     'order_id': order.id}
                )
        return True
