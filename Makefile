# Use bump2version before creating a new release.
#
release:
	python3 setup.py sdist bdist_wheel

# In order to upload to PyPI you'll need to have an API key set up in ~/.pypirc.
#
upload:
	python3 -m twine upload dist/*
