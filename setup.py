#!/usr/bin/env python
"""
The MIT License (MIT)
Copyright (c) 2017 AOUtils-Team

For full license details please see the LICENSE file located in the root folder
of the project.
"""

from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages


install_reqs = [str(ir.req) for ir in
                parse_requirements('requirements.txt', session=PipSession())]

setup(
    name='AOUtils-Dashboard',
    author="AOUtils-Team",
    description='Dashboard for the Albion Online utilities tool suite.',
    url='https://github.com/AOUtils-Team/dashboard',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={
        'dashboard': ['config.yml']
    },
    package_dir={'dashboard': 'dashboard'},
    install_requires=install_reqs,
    entry_points={
        'console_scripts': [
            'aoutils-dashboard-server = dasboard.server:main'
        ]
    }
)
