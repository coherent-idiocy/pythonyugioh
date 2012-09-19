try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'Python version of the Yugioh trading card game': 'pythonyugioh',
    'author': 'Joshua Rowe',
    'url': 'https://github.com/coherent-idiocy/pythonyugioh.git',
    'download_url': 'https://github.com/coherent-idiocy/pythonyugioh.git',
    'author_email': 'joshua@wired.com.au',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['game','cards','input','termcolor'],
    'scripts': [],
    'name': 'pythonyugioh'
}

setup(**config)