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

from odoo import models, fields


class OpExamType(models.Model):
    _name = "op.exam.type"
    _description = "Exam Type"

    name = fields.Char('Name', size=256, required=True)
    code = fields.Char('Code', size=16, required=True)

    _sql_constraints = [
        ('unique_exam_type_code',
         'unique(code)', 'Code should be unique per exam type!')]
