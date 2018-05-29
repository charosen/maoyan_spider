try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This python spider is designed to crawl the top 100 movies of maoyan website, using
                   requests module and regex.',
    'author': 'Charosen',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'charosen@bupt.edu.cn',
    'version': '0.1',
    'install_requires': ['nose', 'requests'],
    'packages': ['maoyan_spider'],
    'scripts': [],
    'name': 'maoyan_spider'
}

setup(**config)
