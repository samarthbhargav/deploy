from fabric.api import run, sudo

def module_check(module_name):
    run("echo 'import {0}; print {0}.__version__' | python".format(module_name))

def pip(module_name):
    sudo("pip install {}".format(module_name))


def pip_install_check(modules):
    for mod in modules:
        pip(mod)
        module_check(mod)

def install_python27():
    sudo("apt-get install python")
    sudo("apt-get install build-essential python-dev python-setuptools libatlas-dev libatlas3gf-base")
    run("python --version")
    
def install_py_science():
    install_python27()
    modules = ["numpy", "scipy", "matplotlib"]
    pip_install_check(modules)    
    
    
def install_py_sklearn():
    install_py_science()
    modules = ["scikit-learn"]
    pip_install_check(modules)
    
def install_py_mongo():
    install_python27()
    modules = ["pymongo"]
    pip_install_check(modules)
    
    