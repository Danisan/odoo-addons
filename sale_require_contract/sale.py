#-*- coding:utf-8 -*-
from openerp import models, _
from openerp.exceptions import Warning


class sale_order(models.Model):
    _inherit = "sale.order"

    def action_wait(self, cr, uid, ids, context=None):
        for o in self.browse(cr, uid, ids):
            if not o.project_id:
                raise Warning(_(
                    'You cannot confirm a sales order without a contract'))
        return super(sale_order, self).action_wait(cr, uid, ids, context)
