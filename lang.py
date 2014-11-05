from fabric.api import run, sudo
from general import pkgmgr

####### Python ##############################################################
def _py_module_check(module_name):
    run("echo 'import {0}; print {0}.__version__' | python".format(module_name))

def _pip(module_name):
    sudo("pip install {}".format(module_name))


def _pip_install_check(modules):
    for mod in modules:
        _pip(mod)
        _py_module_check(mod)

def install_python27():
    pkgmgr("install python")
    pkgmgr("install build-essential python-dev python-setuptools libatlas-dev libatlas3gf-base")
    run("python --version")
    
def install_py_science():
    install_python27()
    modules = ["numpy", "scipy", "matplotlib"]
    _pip_install_check(modules)    
    
    
def install_py_sklearn():
    install_py_science()
    modules = ["scikit-learn"]
    _pip_install_check(modules)
    
def install_py_mongo():
    install_python27()
    
    module = "pymongo"
    _pip(module)
    # pymongo doesn't have __version__ for some reason - weird
    run("echo 'import {0}; print {0}.version' | python".format(module))    
#############################################################################


###### Java #################################################################

def java_version_check():
    run("java --version")

def install_open_jdk6():
    pkgmgr("install openjdk-6-jdk")
    
def install_open_jre6():
    pkgmgr("install openjdk-6-jre")
    
def install_open_java6():
    install_open_jdk6()
    
def install_open_jdk7():
    pkgmgr("install openjdk-7-jdk")
    
def install_open_jre7():
    pkgmgr("install openjdk-7-jre")
#############################################################################