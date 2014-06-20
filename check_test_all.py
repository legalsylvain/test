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
import config
from subprocess import check_call

# Write .coveragerc file
text = []
for module in config.CUSTOM_ADDONS:
    if module['module']:
        text.append('*/%s/%s/*' % (module['name'], module['module']))
    else:
        text.append('*/%s/*' % (module['name']))
content = open('./coveragerc.template', 'r').read()
content = content.replace('{include}', '\n    '.join(text))

fo = open("./.coveragerc", "w")
fo.write(content)
fo.close()

# Realize test and coverage
for module in config.MODULES():
    if os.path.isdir('./%s/%s/tests' % (module['repository'], module['name'])):
        print "Testing '%s' on global database" % (module['name'])
        check_call([
            'coverage', 'run', './openerp-command/oe', 'run-tests',
            '--database=%s' % (config.DATABASE_NAME),
            '--addons=%s' % (config.ADDONS_ARGS),
            '--module=%s' % (module['name'])])
