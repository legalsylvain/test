import config
from subprocess import check_call

for module in config.MODULES:
    check_call([
        'coverage', 'run', './openerp-command/oe', 'run-tests',
        '--database=%s' % (config.DATABASE_NAME),
        '--addons=%s' % (config.ADDONS_LIST),
        '--module=%s' % (module)])
