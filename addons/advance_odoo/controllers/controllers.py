# -*- coding: utf-8 -*-
# from odoo import http


# class AdvanceOdoo(http.Controller):
#     @http.route('/advance_odoo/advance_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advance_odoo/advance_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('advance_odoo.listing', {
#             'root': '/advance_odoo/advance_odoo',
#             'objects': http.request.env['advance_odoo.advance_odoo'].search([]),
#         })

#     @http.route('/advance_odoo/advance_odoo/objects/<model("advance_odoo.advance_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advance_odoo.object', {
#             'object': obj
#         })
