import config
from flake8 import main as flake8_lib
from subprocess import call

def _check_folder(path):
        call(["flake8", path, "--filename=__init__.py", "--ignore=F401"])
        call(["flake8", path,"--exclude=__init__.py", "--ignore=F841"])

for rep in config.REPOSITORIES:
    if rep['modules']:
        for mod in rep['modules']:
            _check_folder('./%s/%s' % (rep['name'], mod))
    else:
        _check_folder('./%s' % (rep['name']))
