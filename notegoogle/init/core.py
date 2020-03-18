import os

from google.colab import drive

dir_root = '/content/drive/My Drive/home'
workspace = '/root/workspace'


def run(cmd):
    print(cmd)
    os.system(cmd)


def install_drive():
    drive.mount('/content/drive')
    run('mkdir {}'.format(workspace))
    os.chdir(workspace)


def install_bash():
    run('source notegoogle/init/bashrc.sh')


def packages():
    # run("pip install -U --target='/content/drive/My Drive/home/packages' git+https://github.com/notechats/notetool.git")
    # run("pip install -U --target='/content/drive/My Drive/home/packages' kaggle")
    run("pip install -U  git+https://github.com/notechats/notetool.git")
    run("pip install -U  kaggle")
    pass


def default_import():
    import pandas as pd
    import sys

    sys.path.append(dir_root + '/packages')
    print('pd:{}'.format(pd.__version__))


def copy_files():
    path_f = dir_root + '/local_files/'
    path_t = '/root/'
    run("cp -r '{}' {}".format(path_f, path_t))
    run("cp -r '{}.' {}".format(path_f, path_t))


def init():
    install_drive()
    packages()
    copy_files()
    default_import()
