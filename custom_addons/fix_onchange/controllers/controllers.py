# -*- coding: utf-8 -*-
from odoo import http

# class FixOnchange(http.Controller):
#     @http.route('/fix_onchange/fix_onchange/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fix_onchange/fix_onchange/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fix_onchange.listing', {
#             'root': '/fix_onchange/fix_onchange',
#             'objects': http.request.env['fix_onchange.fix_onchange'].search([]),
#         })

#     @http.route('/fix_onchange/fix_onchange/objects/<model("fix_onchange.fix_onchange"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fix_onchange.object', {
#             'object': obj
#         })