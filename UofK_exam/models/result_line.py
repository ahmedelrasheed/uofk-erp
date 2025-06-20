# -*- coding: utf-8 -*-
###############################################################################
#
#    UofK Inc
#    Copyright (C) 2009-TODAY UofK Inc(<https://www.uofk.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OpResultLine(models.Model):
    _name = "op.result.line"
    _rec_name = "marks"
    _description = "Result Line"

    marksheet_line_id = fields.Many2one(
        'op.marksheet.line', 'Marksheet Line', ondelete='cascade')
    exam_id = fields.Many2one('op.exam', 'Exam', required=True)
    evaluation_type = fields.Selection(
        related='exam_id.session_id.evaluation_type', store=True)
    marks = fields.Integer('Marks', required=True)
    grade = fields.Char('Grade', readonly=True, compute='_compute_grade')
    student_id = fields.Many2one('op.student', 'Student', required=True)
    status = fields.Selection([('pass', 'Pass'), ('fail', 'Fail')], 'Status',
                              compute='_compute_status', store=True)

    @api.constrains('marks', 'marks')
    def _check_marks(self):
        for record in self:
            if record.marks < 0.0:
                raise ValidationError(_("Enter proper Marks or Percentage!"))

    @api.depends('marks')
    def _compute_grade(self):
        for record in self:
            if record.evaluation_type == 'grade':
                grades = record.marksheet_line_id.marksheet_reg_id. \
                    result_template_id.grade_ids
                if grades:
                    for grade in grades:
                        if grade.min_per <= record.marks and \
                                grade.max_per >= record.marks:
                            record.grade = grade.result
                else:
                    record.grade = None
            else:
                record.grade = None

    @api.depends('marks')
    def _compute_status(self):
        for record in self:
            record.status = 'pass'
            if record.marks < record.exam_id.min_marks:
                record.status = 'fail'
            else:
                record.status = 'pass'

    def unlink(self):
        for res in self:
            super(OpResultLine, res).unlink()
        return self
