#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='genconf_findref',
      version='0.0.2',
      description='A simple, proof-of-concept package allowing users to find general conference talks containing particular scriptures',
      author='Andrew Allen',
      author_email='andrewallen42@gmail.com',
      license='UNLICENSED',
      packages=['genconf_findref'],
      install_requires=[
          'requests',
          'regex',
          'beautifulsoup4',
          'pandas'
      ],
      zip_safe=False)