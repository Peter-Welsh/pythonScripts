from distutils.core import setup
import py2exe
setup(console=['cn.py'])

options = {"py2exe": { "dll_excludes": ["msvcr90.dll"]}}
options = {"py2exe": { "dll_excludes": ["msvcp90.dll"]}}