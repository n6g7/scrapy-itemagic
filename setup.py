from distutils.core import setup

setup(name='scrapy-itemagic',
	version='0.0',
	description='Scrapy item parsing tools.',
	author='as0n',
	author_email='as0n@gnab.fr',
	url='https://github.com/as0n/scrapy-itemagic',
	license='MIT',
	packages=['itemagic', 'itemagic.extractors', 'itemagic.rules'],
	requires=[
		'Scrapy(>=0.24.4)'
	],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Framework :: Scrapy',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	]
)