# -*- encoding: utf-8 -*-
##############################################################################
#
#    Travis and Coveralls Configuration
#    Copyright (C) 2014 GRAP (http://www.grap.coop)
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
# Librairies
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

##############################################################################
# Source Code
##############################################################################

BZR_BRANCHES = [
    {'url': 'lp:~ocb/ocb-server/7.0', 'name': 'ocb-server'},
    {'url': 'lp:~ocb/ocb-addons/7.0', 'name': 'ocb-addons'},
    {'url': 'lp:~ocb/ocb-web/7.0', 'name': 'ocb-web'},
    {'url': 'lp:~openerp/openerp-command/7.0', 'name': 'openerp-command'},
    {'url': """http://bazaar.launchpad.net/~openerp-fr-core-editors/"""
        """openerp-french-localization/7.0/""",
        'name': 'openerp-french-localization'},
]

GIT_BRANCHES = [
    {'url': 'https://github.com/OCA/account-financial-reporting',
        'branch': '7.0', 'name': 'account-financial-reporting'},
    {'url': 'https://github.com/OCA/account-financial-tools',
        'branch': '7.0', 'name': 'account-financial-tools'},
    {'url': 'https://github.com/OCA/reporting-engine',
        'branch': '7.0', 'name': 'reporting-engine'},
    {'url': 'https://github.com/OCA/server-tools',
        'branch': '7.0', 'name': 'server-tools'},
    {'url': 'https://github.com/OCA/web',
        'branch': '7.0', 'name': 'web'},


    #    {'url': 'https://github.com/grap/odoo-addons-grap -b 7.0',
    #        'name': 'openerp-addons-grap'},
    #    {'url': 'https://github.com/grap/odoo-addons-cis.git -b 7.0',
    #        'name': 'openerp-addons-cis'},
    #    {'url': 'https://github.com/grap/odoo-addons-misc.git -b 7.0',
    #        'name': 'openerp-addons-misc'},
    #    {'url': 'https://github.com/grap/odoo-addons-cpo.git -b 7.0',
    #        'name': 'openerp-addons-cpo'},
]

CUSTOM_PIP_LIBRAIRIES = [
    'cairosvg',
]

COMPLETE_TEST = True

LOG_LEVEL = 'warn'

EXTRA_PYTHONPATH = './ocb-server/'

SERVER_PATH = './ocb-server/openerp-server'

DATABASE_NAME = 'test__all'

OFFICIAL_ADDONS = ['ocb-addons', 'ocb-web/addons']

CUSTOM_ADDONS = [
    {'name': 'account-financial-reporting',
        'module': 'account_financial_report_webkit'},
    {'name': 'account-financial-reporting',
        'module': 'account_financial_report_webkit_xls'},

    {'name': 'account-financial-tools', 'module': 'account_tax_update'},

    {'name': 'openerp-french-localization', 'module': 'l10n_fr_department'},
    {'name': 'openerp-french-localization', 'module': 'l10n_fr_state'},

    {'name': 'report-engine', 'module': 'report_xls'},

    {'name': 'server-tools', 'module': 'auth_admin_passkey'},
    {'name': 'server-tools', 'module': 'cron_run_manually'},
    {'name': 'server-tools', 'module': 'disable_openerp_online'},
    {'name': 'server-tools', 'module': 'mass_editing'},
    {'name': 'server-tools', 'module': 'module_parent_dependencies'},

    {'name': 'web', 'module': 'web_ckeditor4'},
    {'name': 'web', 'module': 'web_color'},
    {'name': 'web', 'module': 'web_confirm_window_close'},
    {'name': 'web', 'module': 'web_export_view'},
    {'name': 'web', 'module': 'web_popup_large'},
    {'name': 'web', 'module': 'web_widget_float_formula'},

    #    {'name': 'openerp-addons-cis', 'module': False},
    #    {'name': 'openerp-addons-grap', 'module': False},
    #    {'name': 'openerp-addons-cpo', 'module': False},
    #    {'name': 'openerp-addons-misc', 'module': False},
]

##############################################################################
# Computed params
##############################################################################

PIP_LIBRAIRIES = OFFICIAL_PIP_LIBRAIRIES + CUSTOM_PIP_LIBRAIRIES


tmp = [x['name'] for x in CUSTOM_ADDONS] + OFFICIAL_ADDONS
ADDONS_ARGS = './' + ',./'.join(list(set(tmp)))


def MODULES():
    res = []
    for addons in CUSTOM_ADDONS:
        if addons['module']:
            res.append({
                'repository': addons['name'],
                'name': addons['module']})
        else:
            for item in os.listdir('./%s' % (addons['name'])):
                if (os.path.isdir('./%s/%s' % (addons['name'], item))
                        and not item.startswith(".")):
                    res.append({
                        'repository': addons['name'],
                        'name': item})
    return res


def MODULES_ARGS():
    return ','.join([x['name'] for x in MODULES()])
