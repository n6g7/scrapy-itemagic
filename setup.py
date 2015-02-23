from setuptools import setup

def read(path):
	with open(path) as f:
		return f.read()

setup(name='scrapy-itemagic',
	version='0.1.3',
	description='Scrapy item parsing tools.',
	long_description=read('README.md'),
	author='as0n',
	author_email='as0n@gnab.fr',
	url='https://github.com/as0n/scrapy-itemagic',
	license='MIT',
	packages=[
		'itemagic',
		'itemagic.extractors',
		'itemagic.rules'
	],
	install_requires=[
		'Scrapy>=0.24.4'
	],
	extras_require={
		'test': ['green']
	},
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Framework :: Scrapy',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Operating System :: OS Independent'
	],
	keywords='scrapy item parse parsing'
)