import os
import sys
import setuptools

with open("readme.md", "r") as fh:
	long_description = fh.read()


if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("rm -rf dist")
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()


setuptools.setup(
	name="djangoelasticsearch",
	version="0.5.1",
	author="Robin Tissot",
	author_email="aj3sshh@gmail.com",
	description="Simple wrapper around py-elasticsearch to index/search a django Model.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/liberation/django_elasticsearch",
	packages=setuptools.find_packages(),
    install_requires=[
        'elasticsearch==2.3.0',
        'elasticsearch-dsl==5.4.0',
    ],
	classifiers=[

		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	
	],
)