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
from subprocess import check_call, CalledProcessError


def _check_folder(path, flake8_except):
    try:
        check_call(["flake8", path, "--filename=__init__.py", "--ignore=F401"])
        if flake8_except:
            check_call([
                "flake8", path, "--exclude=__init__.py",
                "--ignore=%s" % (flake8_except)])
        else:
            check_call(["flake8", path, "--exclude=__init__.py"])
        return True
    except CalledProcessError:
        return False

ok = True

for addons in config.CUSTOM_ADDONS:
    if addons.get('flake8', True):
        if addons['module']:
                ok = _check_folder(
                    './%s/%s' % (addons['name'], addons['module']),
                    addons.get('flake8-except', None)) and ok
        else:
            ok = _check_folder(
                './%s' % (addons['name']),
                addons.get('flake8-except', None)) and ok

if not ok:
    raise Exception('Flake8 Error')
