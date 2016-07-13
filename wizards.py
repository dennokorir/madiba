from openerp import models, fields, api
from openerp.exceptions import ValidationError

class customer_dues(models.TransientModel):
    _name = 'customer.dues.wizard'

    as_at = fields.Date(String = "Due as At", default = fields.Date.today)

    @api.multi
    def print_customer_dues(self):
        res = []
        customer_dues = self.env['account.invoice'].search([('state','=','open'),('type','=','out_invoice')])
        for customer in customer_dues:
            if customer.amount_due > 0:
                res.append(customer.id)
        customer_final_dues = self.env['account.invoice'].search([('id','in',res)])
        return self.env['report'].get_action(customer_final_dues,'madiba.customer_dues')
