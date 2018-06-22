all: publish-test

publish-test:
	rm -rf dist
	python setup.py sdist
	twine upload --repository pypitest dist/*

install-test:
	pip install --index-url https://test.pypi.org/simple/ ga_segment_pusher

publish:
	rm -rf dist
	python setup.py sdist
	twine upload --repository pypi dist/*