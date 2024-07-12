from odoo import models, fields, api


class InheritedCar(models.Model):
    _inherit = "car_management.car"
    test_field = fields.Char(string='Ceci est un champs ajouté par un autres module')


