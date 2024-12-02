# -*- coding: utf-8 -*-
# from odoo import http


# class TravelManagement(http.Controller):
#     @http.route('/travel_management/travel_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/travel_management/travel_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('travel_management.listing', {
#             'root': '/travel_management/travel_management',
#             'objects': http.request.env['travel_management.travel_management'].search([]),
#         })

#     @http.route('/travel_management/travel_management/objects/<model("travel_management.travel_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('travel_management.object', {
#             'object': obj
#         })
