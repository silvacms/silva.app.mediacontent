# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from setuptools import setup, find_packages
import os

def read_file(path):
    fd = open(path, 'r')
    try:
        return fd.read()
    finally:
        fd.close()


version = '1.0dev'

tests_require = []

setup(name='silva.app.mediacontent',
      version=version,
      description="Media content types for Silva",
      long_description=read_file("README.txt") + "\n" +
                       read_file(os.path.join("docs", "HISTORY.txt")),
      classifiers=[
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: Zope Public License",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Framework :: Zope2",
          ],
      keywords='media silva infrae',
      author='Antonin Amand',
      author_email='info@infrae.com',
      url='https://hg.infrae.com/silva.app.mediacontent',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['silva', 'silva.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'docutils',
        'five.grok',
        'Products.Silva',
        'setuptools',
        'silva.core.conf',
        'zeam.form.silva',
        'zope.interface',
        'zope.schema',
        ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      )
