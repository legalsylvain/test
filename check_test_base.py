import config
from subprocess import check_call

# create new db
module = 'product'
db_name = 'test__%s' %(module)
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
