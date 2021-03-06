#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='salmon',
    version='0.1.6-dev',
    description="A monitoring system built on top of Salt.",
    long_description=open('README.rst').read(),
    author="Peter Baumgarter",
    author_email='pete@lincolnloop.com',
    url='https://github.com/lincolnloop/salmon',
    license='LICENSE',
    install_requires=[
        'django==1.5.1',
        'django-discover-runner==0.4.0',
        'South==0.8.0',
        'pyyaml==3.10',
        'logan==0.5.5',
        'gunicorn>=0.17.2,<0.18.0',
        'whisper==0.9.10',
        'dj-static==0.0.5',
    ],
    entry_points={
        'console_scripts': [
            'salmon = salmon.core.runner:main',
        ],
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
