#!/usr/bin/env python

from setuptools import setup

setup(name='tap-salesforce-custom',
      version='1.4.39',
      description='Singer.io tap for extracting data from the Salesforce API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_salesforce_custom'],
      install_requires=[
          'requests==2.20.0',
          'singer-python==5.10.0',
          'xmltodict==0.11.0'
      ],
      entry_points='''
          [console_scripts]
          tap-salesforce-custom=tap_salesforce:main
      ''',
      packages=['tap_salesforce', 'tap_salesforce.salesforce'],
      package_data = {
          'tap_salesforce/schemas': [
              # add schema.json filenames here
          ]
      },
      include_package_data=True,
)
