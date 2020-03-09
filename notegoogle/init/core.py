import os

from google.colab import drive

dir_root = '/content/drive/My Drive/home'


def install_drive():
    drive.mount('/content/drive')
    os.chdir(dir_root)


def install_bash():
    os.system('source notegoogle/init/bashrc.sh')


def packages():
    os.system("pip install --target='/content/drive/My Drive/home/packages'    notetool")
    os.system("pip install --target='/content/drive/My Drive/home/packages'    kaggle")


def default_import():
    import pandas as pd
    import sys

    sys.path.append(dir_root + '/packages')
    print('pd:{}'.format(pd.__version__))


def copy_files():
    path_f = dir_root + '/local_files'
    path_t = '~'
    os.system("cp '{}' {}".format(path_f, path_t))


def init():
    install_drive()
    packages()
    copy_files()
    default_import()
