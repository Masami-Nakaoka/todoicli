from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='todoicli',
    version='1.0.1',
    description='todoicli is a tool for using todoist from the command line.',
    long_description=long_description,
    url='https://github.com/Masami-Nakaoka/todoicli',
    license='MIT',
    author='Masami_Nakaoka',
    author_email='neti0326@gmail.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ],

    keywords='todoist command line',
    packages=find_packages(exclude=['todoicli']),
    install_requires=['todoist-python'],

    entry_points={
        'console_scripts': [
            'todoicli=todoi_cli.main:main',
        ],
    },
)