# -*- coding: utf-8 -*-
from odoo.tests import common

@common.tagged('post_install', 'auto_reorder')
class TestSaleOrder(common.SingleTransactionCase):
    def setUp(self):
        super(TestSaleOrder, self).setUp()
        self.vendor_1 = self.env['res.partner'].create(
            {'name': 'vendor_1',
             'supplier': True,
             'is_company': False}
        )
        self.vendor_2 = self.env['res.partner'].create(
            {'name': 'vendor_1',
             'supplier': True,
             'is_company': True}
        )
        self.product_1 = self.env['product.product'].create(
            {'name': 'Test_product_1',
             'type': 'product',
             'purchase_ok': True,
             'sale_ok': True,
             'auto_re_order_ok': True,
             'auto_re_order_condition': 10,
             'uom_id': 1,
             'uom_po_id': 1
             }
        )
        self.product_2 = self.env['product.product'].create(
            {'name': 'Test_product_2',
             'type': 'product',
             'purchase_ok': True,
             'sale_ok': True,
             'auto_re_order_ok': False,
             'uom_id': 1,
             'uom_po_id': 1
             }
        )
        self.env['product.supplierinfo'].create(
            [{'name': self.vendor_1.id,
              'product_tmpl_id': self.product_1.product_tmpl_id.id,
              'price': 100},
             {'name': self.vendor_2.id,
              'product_tmpl_id': self.product_1.product_tmpl_id.id,
              'price': 100}
             ])
        self.customer = self.env['res.partner'].create(
            {'name': 'test',
             'customer': True,
             'is_company': False}
        )

    def test_confirm_so(self):
        self.sale_order = self.env['sale.order'].create(
            {'partner_id': self.customer.id,
             })
        self.line_1 = self.env['sale.order.line'].create(
            {'product_id': self.product_1.id,
             'price_unit': 200,
             'product_uom_qty': 5,
             'order_id': self.sale_order.id}
        )
        self.line_2 = self.env['sale.order.line'].create(
            {'product_id': self.product_2.id,
             'price_unit': 500,
             'product_uom_qty': 1,
             'order_id': self.sale_order.id}
        )
        self.sale_order.action_confirm()
        order = self.env['purchase.order'].search(
            [('partner_id', 'in', [self.vendor_1.id, self.vendor_2.id])],
        )
        # for vendor in self.product_1.seller_ids:
        #     print(vendor.name)
        # print(self.vendor_1, self.vendor_2)
        # print(self.env['product.supplierinfo'].search([('product_tmpl_id', '=', self.product_1.id)]).id)
        print(order)
        self.assertEqual(len(order), 2)


