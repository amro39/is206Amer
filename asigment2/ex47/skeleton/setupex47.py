try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Amer Karahasan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'Amer.khn@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'ex47': 'projectex47'
}

setup(**config)