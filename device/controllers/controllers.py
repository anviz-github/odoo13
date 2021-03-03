# -*- coding: utf-8 -*-
# from odoo import http


# class Device(http.Controller):
#     @http.route('/device/device/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/device/device/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('device.listing', {
#             'root': '/device/device',
#             'objects': http.request.env['device.device'].search([]),
#         })

#     @http.route('/device/device/objects/<model("device.device"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('device.object', {
#             'object': obj
#         })
