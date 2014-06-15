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

import config
from subprocess import check_call

if config.COMPLETE_TEST:
    for module in config.MODULES:
        # create new db
        db_name = 'test__%s' % (module)
        check_call(['createdb', db_name])

        # Install Module
        check_call([
            'python', './ocb-server/openerp-server',
            '--stop-after-init', '--database=%s' % (db_name),
            '--addons-path=%s' % (config.ADDONS_LIST),
            '--init=%s' % (module)])

        # Test (without coverage)
        check_call([
            'python', './openerp-command/oe', 'run-tests',
            '--database=%s' % (db_name),
            '--addons=%s' % (config.ADDONS_LIST),
            '--module=%s' % (module)])
