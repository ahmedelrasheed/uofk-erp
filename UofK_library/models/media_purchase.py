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


class OpMediaPurchase(models.Model):
    _name = "op.media.purchase"
    _inherit = "mail.thread"
    _description = "Media Purchase Request"

    name = fields.Char('Title', size=128, required=True)
    author = fields.Char(
        'Author(s)', size=256, required=True, tracking=True)
    edition = fields.Char('Edition')
    publisher = fields.Char('Publisher(s)', size=256)
    course_ids = fields.Many2one(
        'op.course', 'Course', required=True, tracking=True)
    subject_ids = fields.Many2one(
        'op.subject', 'Subject', required=True, tracking=True)
    requested_id = fields.Many2one(
        'res.partner', 'Requested By',
        default=lambda self: self.env.user.partner_id.id)
    state = fields.Selection(
        [('draft', 'Draft'), ('request', 'Requested'),
         ('reject', 'Rejected'), ('accept', 'Accepted')],
        'State', readonly=True, default='draft', tracking=True)
    media_type_id = fields.Many2one('op.media.type', 'Media Type')
    active = fields.Boolean(default=True)

    def act_requested(self):
        self.state = 'request'

    def act_accept(self):
        self.state = 'accept'

    def act_reject(self):
        self.state = 'reject'

    @api.model_create_multi
    def create(self, vals):
        if self.env.user.child_ids:
            raise ValidationError(_('Invalid Action!\n Parent can not create \
            Media Purchase Requests!'))
        return super(OpMediaPurchase, self).create(vals)

    def write(self, vals):
        if self.env.user.child_ids:
            raise ValidationError(_('Invalid Action!\n Parent can not edit \
            Media Purchase Requests!'))
        return super(OpMediaPurchase, self).write(vals)
