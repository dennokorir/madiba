# -*- coding: utf-8 -*-
from openerp import http

# class Madiba(http.Controller):
#     @http.route('/madiba/madiba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/madiba/madiba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('madiba.listing', {
#             'root': '/madiba/madiba',
#             'objects': http.request.env['madiba.madiba'].search([]),
#         })

#     @http.route('/madiba/madiba/objects/<model("madiba.madiba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('madiba.object', {
#             'object': obj
#         })