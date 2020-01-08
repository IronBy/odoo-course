# Dietfacts application
from odoo import models, fields

# Extend product.template model with calories
class Dietfacts_product_template(models.Model):
  _name = 'product.template'
  _inherit = 'product.template'

  calories = fields.Integer("Calories")
  servingsize = fields.Float("Serving Size")
  lastupdated = fields.Date("Last Updated")
  dietitem = fields.Boolean("Diet Item")

