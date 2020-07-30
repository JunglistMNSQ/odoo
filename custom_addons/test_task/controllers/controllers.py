# -*- coding: utf-8 -*-
from odoo import http

# class TestTask(http.Controller):
#     @http.route('/test_task/test_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_task/test_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_task.listing', {
#             'root': '/test_task/test_task',
#             'objects': http.request.env['test_task.test_task'].search([]),
#         })

#     @http.route('/test_task/test_task/objects/<model("test_task.test_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_task.object', {
#             'object': obj
#         })