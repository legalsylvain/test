import config
from flake8 import main as flake8_lib
from subprocess import check_call, CalledProcessError
import os

print os.listdir('.')

def _check_folder(path):
    try:
        check_call(["flake8", path, "--filename=__init__.py", "--ignore=F401"])
        chekc_call(["flake8", path,"--exclude=__init__.py", "--ignore=F841"])
        return True
    except CalledProcessError:
        return False

ok = True

for rep in config.REPOSITORIES:
    if rep['modules']:
        for mod in rep['modules']:
            ok = _check_folder('./%s/%s' % (rep['name'], mod)) and ok
    else:
        ok = _check_folder('./%s' % (rep['name'])) and ok

if not ok:
    raise Exception('Flake8 Error')
