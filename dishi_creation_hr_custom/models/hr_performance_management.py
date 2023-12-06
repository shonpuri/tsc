# -*- coding: utf-8 -*-
import openerp

from openerp import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime


class EmployeeEvaluation(models.Model):
    _name = 'employee.evaluation'
    _description = 'Employee Evaluation Form'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, domain=[('active', '=', True)])
    employee_name = fields.Char(string="Employee’s Name", related='employee_id.name', store=True,
                                compute="_onchange_employee_id")
    department = fields.Char(string="Department", store=True, compute="_onchange_employee_id")
    job_title = fields.Char(string="Job Title", store=True, compute="_onchange_employee_id")
    length_of_time_in_company = fields.Char(string="Length of Time in Company", store=True,
                                            compute="_onchange_employee_id")
    employment_date = fields.Date(string="Employment Date", store=True, compute="_onchange_employee_id")
    length_of_time_in_role = fields.Char(string="Length of Time in Role", store=True)
    review_period_start = fields.Date(string="Review Period Start", store=True)
    review_period_end = fields.Date(string="Review Period End", store=True)

    supervisor_name = fields.Char(string="Supervisor’s Name", store=True, compute="_onchange_employee_id")
    manager_job_title = fields.Char(string="Supervisor’s Job Title", store=True, compute="_onchange_employee_id")

    # Section I: Evaluation Goals
    evaluation_goals = fields.One2many(
        'employee.evaluation.goal',
        'evaluation_id',
        string='Evaluation Goals',
    )

    # Section II: Competencies
    competencies = fields.One2many(
        'employee.evaluation.competency',
        'evaluation_id',
        string='Competencies',
    )

    # Section III: Supervisor/Appraiser’s Comments
    key_strengths = fields.Text(string='Key Strengths of Employee', help='To be filled by supervisor')
    recommended_trainings = fields.One2many(
        'employee.evaluation.training',
        'evaluation_id',
        string='Recommended Trainings for Employee',
        help='To be filled by supervisor',
    )
    name = fields.Char(string="Sequence", default=lambda self: self._generate_sequence(), readonly=True)
    # for overall comments
    overall_comments = fields.Text(string="Supervisor's Overall Comments")

    supervisor_signature = fields.Char(string="Supervisor's Signature")
    date = fields.Date(string='Date')

    @api.model
    def _generate_sequence(self):
        sequence = self.env['ir.sequence'].next_by_code('employee.evaluation.sequence') or '/'
        return sequence

    @api.depends('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            self.department = self.employee_id.department_id.name
            self.job_title = self.employee_id.job_id.name
            self.employment_date = self.employee_id.employment_date
            self.supervisor_name = self.employee_id.parent_id.name
            self.manager_job_title = self.employee_id.parent_id.job_id.name
            if self.employment_date:
                today = datetime.now().date()
                employment_date = fields.Date.from_string(self.employment_date)
                delta = relativedelta(today, employment_date)
                years_months_days = "{0} years, {1} months, {2} days".format(delta.years, delta.months, delta.days)
                self.length_of_time_in_company = years_months_days
            else:
                self.length_of_time_in_company = False
        else:
            self.department = False
            self.job_title = False
            self.employment_date = False
            self.supervisor_name = False

    # Section IV: Future Goals for the Employee
    future_goals = fields.One2many(
        'employee.evaluation.future_goal',
        'evaluation_id',
        string='Future Goals for the Employee',
        help='To be completed after the appraisals. Employee and Supervisor are to agree on the KRAs and KPIs',
    )

    # Section V: Reward/Consequent Recommendation
    reward_recommendation = fields.Selection([
        ('promote', 'Promote Employee'),
        ('salary_increment', 'Recommend Salary Increment'),
        ('demote', 'Demote Employee'),
        ('probation', 'Place Employee on Probation'),
        ('terminate', 'Terminate Employment'),
    ], string='Reward/Consequent Recommendation', help='To be completed by review team')


class EmployeeEvaluationFutureGoal(models.Model):
    _name = 'employee.evaluation.future_goal'
    _description = 'Employee Evaluation Future Goal'

    objectives = fields.Text(string='Objectives for Year 2023')
    kra = fields.Char(string='Key Result Areas (KRA)')
    kpi = fields.Char(string='Key Performance Indicators (KPI)')

    evaluation_id = fields.Many2one(
        'employee.evaluation',
        string='Employee Evaluation',
    )
