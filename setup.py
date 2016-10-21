import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'pythons3',
    version = '0.0.1',
    author = 'Shekhar Singh',
    author_email = 'shekhar.singh@msn.com',
    description = ('Quickest way to upload data on AWS S3.'),
    license = 'MIT',
    keywords = ['S3', 'python', 'AWS'],
    url = 'https://github.com/rootcss/pythons3',
    packages=['pythons3'],
    long_description=read('README'),
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
