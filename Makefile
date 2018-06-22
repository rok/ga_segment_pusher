all: publish

publish:
	rm -rf dist
	python setup.py sdist
	twine upload --repository pypi dist/*