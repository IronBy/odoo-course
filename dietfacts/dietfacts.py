# Dietfacts application
from odoo import models, fields

# Extend product.template model with calories
class Dietfacts_product_template(models.Model):
  _name = 'product.template'
  _inherit = 'product.template'

  calories = fields.Integer("Calories")
  servingsize = fields.Float("Serving Size")
  lastupdated = fields.Date("Last Updated")

class Dietfacts_res_users_meal(models.Model):
  _name = 'res.users.meal'
  name = fields.Char("Meal Name")
  meal_date = fields.Datetime("Meal Date")
  # item_ids = fields.One2many()
  user_id = felds.Many2one("res.users", "Meal User")
  notes = fields.Text("Meal Notes")
