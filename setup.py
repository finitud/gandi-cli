from setuptools import setup, find_packages

setup(
    name="gandi-cli",
    version="0.1.0",
    author="Alice Wyan",
    author_email="alice@finitud.org",
    description="A CLI tool for gandi.net",
    license="PSF",
    keywords="gandi cli gandi-cli",
    url="http://github.com/finitud/gandi-cli",
    packages=find_packages(),

    install_requires=[
        'Click',
        'click-config'
    ],
    entry_points='''
        [console_scripts]
        gandi=gandi:cli
    ''',

)
