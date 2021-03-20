"""
My Personal Website setup
"""

from setuptools import setup

setup(
    name='WebsiteGenerator',
    version='0.1.0',
    packages=['WebsiteGenerator'],
    include_package_data=True,
    install_requires=[
        'bs4==0.0.1',
        'click==7.0',
        'jinja2==2.11.3',
        'requests==2.22.0',
        'sh==1.12.14',
    ],
    entry_points={
        'console_scripts': [
            'WebsiteGenerator = WebsiteGenerator.__main__:main'
        ]
    },
)
