from setuptools import setup

setup(
    name='MultiplesOfYandX',
    version='1.0.0',
    author='Mr. M',
    description='Practice',
    py_modules=['multples_of_y_and_x'],
    install_requires=[],
    entry_points={
        'console_scripts': ['multiples = multples_of_y_and_x:cli']
    }
)
