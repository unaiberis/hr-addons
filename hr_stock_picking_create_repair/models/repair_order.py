# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class RepairOrder(models.Model):
    _inherit = "repair.order"

    employee_id = fields.Many2one(
        string="Employee", comodel_name="hr.employee", copy=False
    )
