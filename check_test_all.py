import config
from subprocess import check_call

check_call([
    'coverage', 'run', './openerp-command/oe', 'run-tests'
    '--database=%s' % (config.DATABASE_NAME),
    '--addons=%s' % (config.ADDONS_LIST),
    '--module=%s' % (config.MODULES_LIST)])
