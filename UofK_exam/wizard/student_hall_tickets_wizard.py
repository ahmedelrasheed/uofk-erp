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


class StudentHallTicket(models.TransientModel):
    """ Student Hall Ticket Wizard """
    _name = "student.hall.ticket"
    _description = "Student Hall Ticket"

    exam_session_id = fields.Many2one(
        'op.exam.session', 'Exam Session', required=True,
        domain=[('state', 'not in', ['draft', 'cancel', 'done'])])

    def print_report(self):
        data = self.read(['exam_session_id'])[0]
        return self.env.ref(
            'uofk_exam.action_student_hall_ticket_report') \
            .report_action(self, data=data)
