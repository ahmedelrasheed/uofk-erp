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

import time
from odoo import models, api


class ReportMediaBarcode(models.AbstractModel):
    _name = "report.uofk_library.report_media_barcode"
    _description = "Media Barcode Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['op.media'].browse(docids)
        docargs = {
            'doc_model': 'op.media',
            'docs': docs,
            'time': time,
        }
        return docargs
