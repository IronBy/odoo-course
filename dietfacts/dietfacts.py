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
  _description = 'Expiriments with Meal Menu model'
  name = fields.Char("Meal Name")
  meal_date = fields.Datetime("Meal Date")
  item_ids = fields.One2many('res.users.mealitem', 'meal_id')
  user_id = fields.Many2one("res.users", "Meal User")
  notes = fields.Text("Meal Notes")

class Dietfacts_res_users_mealitem(models.Model):
  _name = 'res.users.mealitem'
  _description = 'Meal item'
  meal_id = fields.Many2one('res.users.meal', "Meal")
  item_id = fields.Many2one('product.template')
  servings = fields.Float('Servings')
  notes = fields.Text('Meal item notes')
  caloris = fields.Integer(related='item_id.calories', string='Calories per serving', store=True, readonly=True)
