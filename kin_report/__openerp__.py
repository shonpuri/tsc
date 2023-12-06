# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright 2017  Kinsolve Solutions
# Copyright 2017 Kingsley Okonkwo (kingsley@kinsolve.com, +2348030412562)
# License: see https://www.gnu.org/licenses/lgpl-3.0.en.html

{
    'name': 'Common Reports Modifications',
    'version': '0.1',
    'category': 'report',
    'description': """
Report Modifications
=======================================================================================
""",
    'author': 'Kingsley Okonkwo (kingsley@kinsolve.com, +2348030412562)',
    'website': 'http://kinsolve.com',
    'depends': ['base','sale','kin_sales','purchase','kin_purchase','account','kin_account','stock','kin_stock','report_xlsx','operating_unit','account_payment_group','kin_account_payment_group', 'kay_custom'],
    'data': [
        'data/account_data.xml',
        'wizard/stock_level_wizard_view.xml',
        'wizard/financial_statement_report_wizard_view.xml',
        'wizard/sales_report_wizard_view.xml',
        'wizard/purchase_report_wizard_view.xml',
        'report/custom_report_layouts.xml',
        'report/custom_rfq.xml',
        'report/custom_purchase_order.xml',
        'report/custom_sales_quotation.xml',
        'report/custom_sales_order.xml',
        'report/custom_waybill.xml',
        'report/custom_invoice.xml',
        'report/custom_receipt.xml',
        'kin_report.xml',
    ],
    'test':[],
    'installable': True,
    'images': [],
}
