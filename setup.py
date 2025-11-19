##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import setup


setup(name='Products.MIMETools',
      version='5.1.dev0',
      url='https://github.com/zopefoundation/Products.MIMETools',
      project_urls={
          'Issue Tracker': ('https://github.com/zopefoundation'
                            '/Products.MIMETools/issues'),
          'Sources': 'https://github.com/zopefoundation/Products.MIMETools',
      },
      license='ZPL-2.1',
      description='MIMETools provides the ``dtml-mime`` tag for '
                  'DocumentTemplate.',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.dev',
      long_description=(open('README.rst').read() + '\n' +
                        open('CHANGES.txt').read()),
      classifiers=[
          'Development Status :: 6 - Mature',
          'Environment :: Web Environment',
          'Framework :: Zope',
          'Framework :: Zope :: 5',
          'License :: OSI Approved :: Zope Public License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Programming Language :: Python :: 3.13',
          'Programming Language :: Python :: 3.14',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Communications :: Email',
      ],
      python_requires='>=3.10',
      install_requires=[
          'ExtensionClass>=4.1a1',
          'DocumentTemplate>=3',
      ],
      include_package_data=True,
      )
