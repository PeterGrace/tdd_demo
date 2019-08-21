from setuptools import setup, find_packages

setup(
    name='tdd_demo',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'nose',
        'tox',
        'bddcli'
    ],
    entry_points='''
        [console_scripts]
        tdd_demo=tdd_demo.main:main
    ''',
)
