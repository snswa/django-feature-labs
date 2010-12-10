import os
from setuptools import setup, find_packages

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

# Use the docstring of the __init__ file to be the description
DESC = " ".join(__import__('featurelabs').__doc__.splitlines()).strip()

setup(
    name = "django-feature-labs",
    version = __import__('featurelabs').get_version().replace(' ', '-'),
    url = 'https://github.com/gldnspud/django-feature-labs/',
    author = 'Matthew Scott',
    author_email = 'matt@11craft.com',
    description = DESC,
    long_description = read_file('README'),
    packages = find_packages(),
    include_package_data = True,
    install_requires=[
        'django-feature-flipper',
    ],
    classifiers = [
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Django',
    ],
)
