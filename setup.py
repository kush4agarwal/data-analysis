from setuptools import setup, find_packages

setup (
	name='data-analysis',
	version='0.0.1',
	url='www.github.com/kush4agarwal/data-analysis',
	license='BSD',	
	author='Kush Agarwal',
	packages=find_packages(),
	install_requires=['PyQt5', 'pandas', 'numpy', 'SQLAlchemy', 'nltk', 'python-twitter', 'jupyter'],
	entry_points={},
	extras_require={'dev': ['flake8',]}, 
)
