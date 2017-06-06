# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Luc Saffre
# License: BSD (see file COPYING for details)

# $ python setup.py test -s tests.PackagesTests.test_packages

SETUP_INFO = dict(
    name='lino-riche',
    version='2017.2.0',
    install_requires=['lino-xl',
                      'channels',
                      'djangorestframework'],
    # tests_require=['pytest', 'mock'],
    test_suite='tests',
    description=("A offshoot from Lino noi to be used by devlopers to manage"
                 " tickets from clients and assign them to developers."),
    long_description="""\
.. image:: https://readthedocs.org/projects/lino/badge/?version=latest
    :alt: Documentation Status
    :target: http://lino.readthedocs.io/en/latest/?badge=latest

.. image:: https://coveralls.io/repos/github/lino-framework/riche/badge.svg?branch=master
    :target: https://coveralls.io/github/lino-framework/riche?branch=master

.. image:: https://travis-ci.org/lino-framework/riche.svg?branch=stable
    :target: https://travis-ci.org/lino-framework/riche?branch=stable

.. image:: https://img.shields.io/pypi/v/lino-riche.svg
    :target: https://pypi.python.org/pypi/lino-riche/

.. image:: https://img.shields.io/pypi/l/lino-riche.svg
    :target: https://pypi.python.org/pypi/lino-riche/

Lino Riche is a customizable ticket management and time tracking
system for when the line between projects and clients are blurred.

- The central project homepage is http://riche.lino-framework.org

- Technical documentation, including demo projects, API and tested
  specs see http://www.lino-framework.org/specs/riche

- For *introductions* and *commercial information* about Lino riche
  please see `www.saffre-rumma.net
  <http://www.saffre-rumma.net/riche/>`__.


""",
    author='Luc Saffre',
    author_email='luc@lino-framework.org',
    url="http://riche.lino-framework.org",
    license='BSD License',
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2
Development Status :: 4 - Beta
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
Intended Audience :: System Administrators
Intended Audience :: Information Technology
Intended Audience :: Customer Service
License :: OSI Approved :: GNU Affero General Public License v3
Operating System :: OS Independent
Topic :: Software Development :: Bug Tracking
""".splitlines())

SETUP_INFO.update(packages=[str(n) for n in """
lino_riche
lino_riche.lib
lino_riche.lib.riche
lino_riche.lib.riche.fixtures
lino_riche.lib.contacts
lino_riche.lib.public
lino_riche.lib.topics
lino_riche.lib.users
lino_riche.lib.users.fixtures
lino_riche.lib.cal
lino_riche.lib.cal.fixtures
lino_riche.lib.tickets
lino_riche.lib.clocking
lino_riche.lib.clocking.fixtures
""".splitlines() if n])

SETUP_INFO.update(message_extractors={
    'lino_riche': [
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**.js',                'javascript', None),
        ('**/config/**.html', 'jinja2', None),
    ],
})

SETUP_INFO.update(include_package_data=True, zip_safe=False)
# SETUP_INFO.update(package_data=dict())


# def add_package_data(package, *patterns):
#     l = SETUP_INFO['package_data'].setdefault(package, [])
#     l.extend(patterns)
#     return l

# l = add_package_data('lino_riche.lib.noi')
# for lng in 'de fr'.split():
#     l.append('locale/%s/LC_MESSAGES/*.mo' % lng)
