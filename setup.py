# setup.py

from setuptools import setup, find_packages

setup(
    name='python-test-package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package needs
    ],
    test_suite='tests',
    tests_require=[
        'unittest2',  # For example, if you are using unittest2
    ],
    # Metadata
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of the package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',
)
