from setuptools import setup, find_packages

install_requires = ['oauth2client']

setup(name='notegoogle',
      version='0.0.1',
      description='notegoogle',
      author='niuliangtao',
      author_email='1007530194@qq.com',
      url='https://github.com/1007530194',

      packages=find_packages(),
      install_requires=install_requires
      )
