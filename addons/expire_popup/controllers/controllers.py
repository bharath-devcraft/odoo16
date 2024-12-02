# -*- coding: utf-8 -*-
# from odoo import http


# class ExpirePopup(http.Controller):
#     @http.route('/expire_popup/expire_popup', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/expire_popup/expire_popup/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('expire_popup.listing', {
#             'root': '/expire_popup/expire_popup',
#             'objects': http.request.env['expire_popup.expire_popup'].search([]),
#         })

#     @http.route('/expire_popup/expire_popup/objects/<model("expire_popup.expire_popup"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('expire_popup.object', {
#             'object': obj
#         })
