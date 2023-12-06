# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright 2017  Kinsolve Solutions
# Copyright 2017 Kingsley Okonkwo (kingsley@kinsolve.com, +2348030412562)
# License: see https://www.gnu.org/licenses/lgpl-3.0.en.html

from openerp import api, fields, models, _



class OperatingUnitExtend(models.Model):

    _inherit = 'operating.unit'

    header_logo = fields.Binary(string='Header Logo')
    footer_banner = fields.Binary(string='Footer Banner')
    footer_data = fields.Html(string='Footer Data')
    header_data = fields.Html(string='Header Data',
                              help="e.g. Addresses of head Office and Tel No should be added here ")
    # logo_text = fields.Text(string='Logo Below Text', help="The text below the logo")
    po_note = fields.Text(string='Purchase Order Note', help="e.g. Terms and Conditions")
    inv_note = fields.Text(string='Invoice Note', help="e.g. Terms and Conditions")
    html_after_header = fields.Html('Html after Header')
    logo = fields.Binary('Logo',related='company_id.logo')



class ResCompanyReport(models.Model):
    _inherit = "res.company"

    header_logo = fields.Binary(string='Header Logo')
    footer_banner = fields.Binary(string='Footer Banner')
    footer_data = fields.Html(string='Footer Data')
    header_data = fields.Html(string='Header Data', help="e.g. Addresses of head Office and Tel No should be added here ")
    # logo_text = fields.Text(string='Logo Below Text', help="The text below the logo")
    po_note = fields.Text(string='Purchase Order Note', help="e.g. Terms and Conditions")
    inv_note = fields.Text(string='Invoice Note', help="e.g. Terms and Conditions")
    html_after_header = fields.Html('Html after Header')
    is_show_uom = fields.Boolean(string="Show Unit of Measure on Reports")










