#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip

from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

parsed_requirements = parse_requirements(
    'requirements.txt',
    session=pip.download.PipSession()
)

requirements = [str(ir.req) for ir in parsed_requirements]

setup(
    name='geo',
    version='0.1.0',
    description="repo for geography based logic",
    long_description=readme + '\n\n' + history,
    author="Franklin Sarkett",
    author_email='franklin.sarkett@gmail.com',
    url='https://github.com/franc3000/geo',
    packages=[
        'geo',
    ],
    package_dir={'geo':
                 'geo'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='geo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
)
