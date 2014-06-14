import config
from subprocess import check_call

check_call([
    'python', './ocb-server/openerp-server',
    '--stop-after-init', '--database=%s' % (config.DATABASE_NAME),
    '--addons-path=%s' % (config.ADDONS_LIST),
    '--init%s' % (config.MODULES_LIST))
