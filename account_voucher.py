from openerp import fields, models, api

class account_voucher(models.Model):
    _inherit = 'account.voucher'

    balance = fields.Float(compute = 'compute_balance')
    balance_after = fields.Float(compute = 'compute_balance')
    plots = fields.Char(compute = 'compute_balance')

    @api.one
    def print_receipt(self):
        receipt = self.env['account.voucher'].search([('id','=',self.id)])
        return self.env['report'].get_action(receipt, 'madiba.customer_receipt')

    @api.one
    @api.depends('line_cr_ids')
    def compute_balance(self):
        self.balance = sum(line.amount_unreconciled for line in self.line_cr_ids)
        self.balance_after = sum(line.amount_unreconciled for line in self.line_cr_ids) - self.amount
        receipt_for = ''
        for line in self.line_cr_ids:
            if line.amount > 0:
                for item in line.move_line_id.invoice.invoice_line:
                    if item.name:
                        receipt_for += " " + item.name+","
                    else:
                        receipt_for += ""
        self.plots = receipt_for
