"""Setup for spahqler."""
from setuptools import setup, Command
import os
import re

setup(
    name='spahqler',
    version='0.1',
    packages=[],
    scripts=['spahqler'],
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: Apache Software License",
                 "Operating System :: OS Independent", #is this true? know Linux & OS X ok
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3.3",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Topic :: Internet :: WWW/HTTP",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Environment :: Web Environment"],
    author='Simeon Warner',
    author_email='simeon.warner@cornell.edu',
    description='spahqler local SPARQL query',
    long_description=open('README.md').read(),
    url='http://github.com/zimeon/spahqler',
    install_requires=[
        "rdflib>=4.2.2"
    ],
    test_suite="tests",
    tests_require=[
    ]
)
