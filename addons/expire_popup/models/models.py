
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _check_expired_products(self):
        from datetime import timedelta

        print("11111111111111111111")
        today = fields.Date.today()
        #expired_products = self.search([('create_date', '=', today)])
        expired_products = self.search([('create_date', '>=', today), ('create_date', '<', today + timedelta(days=1))])
        print("2222222222222222",expired_products,today)
        for product in expired_products:
            self.env['expire_popup.expired_product_alert'].create({
                'product_name': product.name,
                'alert_date': fields.Datetime.now(),
            })
            
            print("333333333333333")
            # Show pop-up using the view
            # ~ self.env['ir.ui.view'].sudo().load("expire_popup.view_expire_alert").render({
                # ~ 'product_name': product.name,
            # ~ })

        return True





class ExpiredProductAlert(models.Model):
    _name = 'expire_popup.expired_product_alert'
    _description = 'Expired Product Alert'

    name = fields.Char()
    product_name = fields.Char(string='Product Name', required=True)
    alert_date = fields.Datetime(string='Alert Date', required=True)

