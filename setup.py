#!/usr/bin/env python
# encoding: utf-8
'''
'''

from distutils.core import setup
def install():
    setup(name = 'othello',
          version = 0.0.1,
          package_dir = {'othello':'src/othello'},
          packages = ['othello'],
          author = 'Terry Yin',
          author_email = 'terry.yinze@gmail.com',
          url= 'https://github.com/terryyin/pythonTranslator',
          scripts=['dubShell.py'],
          data_files = [(RESOURCE_FOLDER, ['README.md'])]
          )

if __name__ == "__main__":
    install()
