from setuptools import find_packages, setup

setup(
    name='util',
    packages=find_packages(include=['util']),
    version='0.1.0',
    description='Small utility functions',
    author='Lydia-Rose Kesich',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)