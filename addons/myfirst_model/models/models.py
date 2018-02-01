# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Customer(models.Model):
    _name = 'customer'
    name = fields.Char()
    lastName = fields.Char()
    age=fields.Integer()
