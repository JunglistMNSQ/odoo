# -*- coding: utf-8 -*-
# from odoo import http


# class RfmAutomaton(http.Controller):
#     @http.route('/rfm_automaton/rfm_automaton/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rfm_automaton/rfm_automaton/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rfm_automaton.listing', {
#             'root': '/rfm_automaton/rfm_automaton',
#             'objects': http.request.env['rfm_automaton.rfm_automaton'].search([]),
#         })

#     @http.route('/rfm_automaton/rfm_automaton/objects/<model("rfm_automaton.rfm_automaton"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rfm_automaton.object', {
#             'object': obj
#         })
