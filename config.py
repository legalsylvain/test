# -*- encoding: utf-8 -*-
##############################################################################
#
#    Travis and Coveralls Configuration
#    Copyright (C) 2013-2014 GRAP (http://www.grap.coop)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

REPOSITORIES = [
    {
        'name': 'server-env-tools',
        'modules': [
            'auth_admin_passkey', 'disable_openerp_online']},
    {
        'name': 'web-addons',
        'modules': [
            'web_ckeditor4', 'web_confirm_window_close', 'web_export_view',
            'web_popup_large', 'web_widget_float_formula']},
    {
        'name': 'openerp-addons-cis',
        'modules': None},
    {
        'name': 'openerp-addons-grap',
        'modules': None},
]
