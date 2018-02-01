# -*- coding: utf-8 -*-
from odoo import http

# class MyfirstModel(http.Controller):
#     @http.route('/myfirst_model/myfirst_model/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myfirst_model/myfirst_model/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myfirst_model.listing', {
#             'root': '/myfirst_model/myfirst_model',
#             'objects': http.request.env['myfirst_model.myfirst_model'].search([]),
#         })

#     @http.route('/myfirst_model/myfirst_model/objects/<model("myfirst_model.myfirst_model"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myfirst_model.object', {
#             'object': obj
#         })