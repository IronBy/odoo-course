# Dietfacts application
from odoo import models, fields, api

# Extend product.template model with calories
class Dietfacts_product_template(models.Model):
  _name = 'product.template'
  _inherit = 'product.template'

  calories = fields.Integer("Calories")
  servingsize = fields.Float("Serving Size")
  lastupdated = fields.Date("Last Updated")
  nutrient_ids = fields.One2many('product.template.nutrient', 'product_id')

class Dietfacts_res_users_meal(models.Model):
  _name = 'res.users.meal'
  _description = 'Expiriments with Meal Menu model'
  name = fields.Char("Meal Name")
  meal_date = fields.Datetime("Meal Date")
  item_ids = fields.One2many('res.users.mealitem', 'meal_id')
  user_id = fields.Many2one("res.users", "Meal User")
  notes = fields.Text("Meal Notes")
  totalcalories = fields.Integer(string='Total Meal Calories', store=True, compute='_calccalories')
  largemeal = feilds.Boolean('Large Meal')

  @api.depends('item_ids', 'item_ids.servings', 'item_ids.calories')
  def _calccalories(self):
    calories = 0
    for item in self.item_ids:
      calories += item.calories * item.servings
    self.totalcalories = calories

  @api.onchange('totalcalories')
  def check_totalcalories(self):
    self.largemeal = self.totalcalories > 500

class Dietfacts_res_users_mealitem(models.Model):
  _name = 'res.users.mealitem'
  _description = 'Meal item'
  meal_id = fields.Many2one('res.users.meal', "Meal")
  item_id = fields.Many2one('product.template')
  servings = fields.Float('Servings')
  notes = fields.Text('Meal item notes')
  calories = fields.Integer(related='item_id.calories', string='Calories per serving', store=True, readonly=True)

# Nutrients

class Dietfacts_product_nutrient(models.Model):
  _name = 'product.nutrient'
  _description = 'Nutrient'
  name = fields.Char('Nutrient Name')
  uom_id = fields.Many2one('uom.uom', 'Unit of measure')
  description = fields.Text('Description')

class Dietfacts_product_template_nutrient(models.Model):
  _name = 'product.template.nutrient'
  _description = 'Product nutrient'
  nutrient_id = fields.Many2one('product.nutrient', string='Product Nutrient')
  product_id = fields.Many2one('product.template')
  value = fields.Float('Nutrient Value')
  dailypercent = fields.Float('Daily Recommended Value')
  uom = fields.Char(related='nutrient_id.uom_id.name', string='Unit of Measure', store=False, readonly=True)
