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

import os

COMPLETE_TEST = True

DATABASE_NAME = 'test__all'

_OFFICIAL_ADDONS = ['ocb-addons', 'ocb-web/addons']

CUSTOM_ADDONS = [
    {'name': 'server-env-tools', 'module': 'auth_admin_passkey',
        'flake8': False, 'flake8-except': 'F841'},
    {'name': 'server-env-tools', 'module': 'disable_openerp_online',
        'flake8': False},
    {'name': 'web-addons', 'module': 'web_ckeditor4',
        'flake8': False},
    {'name': 'web-addons', 'module': 'web_confirm_window_close'},
    {'name': 'web-addons', 'module': 'web_export_view',
        'flake8': False},
    {'name': 'web-addons', 'module': 'web_popup_large'},
    {'name': 'web-addons', 'module': 'web_widget_float_formula',
        'flake8': False},
    {'name': 'openerp-addons-cis', 'module': None,
        'flake8': False},
    {'name': 'openerp-addons-grap', 'module': None,
        'flake8': False},
]

tmp = [x['name'] for x in CUSTOM_ADDONS] + _OFFICIAL_ADDONS

ADDONS_ARGS = './' + ',./'.join(list(set(tmp)))



#MODULES = []
#for rep in REPOSITORIES:
#    if rep['modules']:
#        MODULES += rep['modules']
#    else:
#        for item in os.listdir('./%s' % (rep['name'])):
#            if (os.path.isdir('./%s/%s' % (rep['name'], item))
#                    and not item.startswith(".")):
#                MODULES.append(item)
#MODULES_LIST = ','.join(MODULES)
