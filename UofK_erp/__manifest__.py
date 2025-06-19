# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################

{
    'name': 'UofK',
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Students, Faculties and Education Institute',
    'complexity': "easy",
    'author': 'UofK Inc',
    'website': 'https://www.uofk.org',
    'depends': [
        'uofk_admission',
        'uofk_assignment',
        'uofk_attendance',
        'uofk_library',
        'uofk_parent',
        'uofk_exam',
        'web_uofk',
    ],
    'images': [
        'static/description/uofk_erp_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
