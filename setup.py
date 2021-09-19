from setuptools import setup, find_packages
import os

version = "TODO"


BASE_PATH = os.path.dirname(__file__)


def get_requirements(suffix=''):
    with open(os.path.join(BASE_PATH, f'requirements{suffix}.txt')) as f:
        rv = f.read().splitlines()
    return rv

setup(
    name='Ikim',
    version=version,
    url='https://github.com/Python-Mastery/ikim',
    license='MIT',
    author='The PSG',
    description='A flask reusable blog extension',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=get_requirements(),
    classifiers=[
        'Development Status :: Pre Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
