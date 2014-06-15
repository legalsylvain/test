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

##############################################################################
# Params
##############################################################################

OFFICIAL_PIP_LIBRAIRIES = [
    'python-dateutil', 'feedparser', 'gdata', 'python-ldap', 'lxml', 'mako',
    'python-openid', 'psycopg2', 'babel', 'pydot', 'pyparsing', 'reportlab',
    'simplejson', 'vatnumber', 'vobject', 'python-webdav', 'werkzeug', 'xlwt',
    'unittest2', 'docutils', 'jinja2', 'mock', 'psutil', 'pygments', 'roman',
    'fpconst', 'soappy', 'http://download.gna.org/pychart/PyChart-1.39.tar.gz',
]

CUSTOM_PIP_LIBRAIRIES = [
    'cairosvg',
]

OFFICIAL_BZR_BRANCHES = [
    {'url': 'lp:~ocb/ocb-server/7.0', 'name': 'ocb-server'},
    {'url': 'lp:~ocb/ocb-addons/7.0', 'name': 'ocb-addons'},
    {'url': 'lp:~ocb/ocb-web/7.0', 'name': 'ocb-web'},
    {'url': 'lp:~openerp/openerp-command/7.0', 'name': 'openerp-command'},
]

CUSTOM_BZR_BRANCHES = [
    {'url': 'lp:server-env-tools/7.0', 'name': 'server-env-tools'},
    {'url': 'lp:web-addons/7.0', 'name': 'web-addons'},
#    {'url': 'lp:openerp-addons-cis/7.0', 'name': 'openerp-addons-cis'},
#    {'url': 'lp:openerp-addons-grap/7.0', 'name': 'openerp-addons-grap'},
]

CUSTOM_PIP_LIBRAIRIES = [
    'cairosvg',
]

COMPLETE_TEST = True

SERVER_PATH = './ocb-server/openerp-server'

DATABASE_NAME = 'test__all'

OFFICIAL_ADDONS = ['ocb-addons', 'ocb-web/addons']

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
#    {'name': 'openerp-addons-cis', 'module': None,
#        'flake8': False},
#    {'name': 'openerp-addons-grap', 'module': None,
#        'flake8': False},
]

##############################################################################
# Computed params
##############################################################################

PIP_LIBRAIRIES = OFFICIAL_PIP_LIBRAIRIES + CUSTOM_PIP_LIBRAIRIES
BZR_BRANCHES = OFFICIAL_BZR_BRANCHES + CUSTOM_BZR_BRANCHES


tmp = [x['name'] for x in CUSTOM_ADDONS] + OFFICIAL_ADDONS
ADDONS_ARGS = './' + ',./'.join(list(set(tmp)))

MODULES = []
for addons in CUSTOM_ADDONS:
    if addons['module']:
        MODULES += {'repository': addons['name'], 'name': addons['module']}
    else:
        for item in os.listdir('./%s' % (addons['name'])):
            if (os.path.isdir('./%s/%s' % (addons['name'], item))
                    and not item.startswith(".")):
                MODULES.append({'repository': addons['name'], 'name': item})

MODULES_ARGS = ','.join([x['name'] for x in MODULES])
