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
