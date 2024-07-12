# -*- coding: utf-8 -*-
# from odoo import http


# class SaleExtendFeature(http.Controller):
#     @http.route('/sale_extend_feature/sale_extend_feature', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_extend_feature/sale_extend_feature/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_extend_feature.listing', {
#             'root': '/sale_extend_feature/sale_extend_feature',
#             'objects': http.request.env['sale_extend_feature.sale_extend_feature'].search([]),
#         })

#     @http.route('/sale_extend_feature/sale_extend_feature/objects/<model("sale_extend_feature.sale_extend_feature"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_extend_feature.object', {
#             'object': obj
#         })

