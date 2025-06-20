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


class ReportLibraryCardBarcode(models.AbstractModel):
    _name = "report.uofk_library.report_library_card_barcode"
    _description = "Library Card Barcode Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['op.library.card'].browse(docids)
        docargs = {
            'doc_model': 'op.library.card',
            'docs': docs,
            'time': time,
        }
        return docargs
