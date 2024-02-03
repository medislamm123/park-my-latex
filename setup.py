from setuptools import setup, find_packages

setup(
    name='parkmylatex',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['openai'],
    entry_points={
        'console_scripts': [
            'parkmylatex = parkmylatex.main:main',
        ],
    },
)
