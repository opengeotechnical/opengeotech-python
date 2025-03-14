# Guide to Upload OpenGeoTech to PyPI

This guide will help you upload the OpenGeoTech package to PyPI so that others can install it using pip.

## Prerequisites

Make sure you have the following installed:
- Python 3.6 or higher
- pip
- twine (`pip install twine`)
- build (`pip install build`)

## Steps to Upload to PyPI

### 1. Create a PyPI Account

If you don't already have one, create an account on [PyPI](https://pypi.org/account/register/).

### 2. Update Package Information

Before uploading, make sure to update the following files with your information:
- `setup.py`: Update author, author_email, url, etc.
- `LICENSE`: Update the year and copyright holder if needed
- `README.md`: Make any necessary changes to the documentation

### 3. Build the Package

Run the following command to build the package:

```bash
python -m build
```

This will create a `dist` directory containing the package distribution files.

### 4. Upload to TestPyPI (Optional but Recommended)

Before uploading to the main PyPI repository, you can test your package on TestPyPI:

```bash
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

You'll be prompted for your TestPyPI username and password.

To test the installation from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ opengeotech
```

### 5. Upload to PyPI

Once you're satisfied with the package, upload it to the main PyPI repository:

```bash
python -m twine upload dist/*
```

You'll be prompted for your PyPI username and password.

### 6. Verify the Upload

After uploading, verify that your package is available on PyPI by visiting:
https://pypi.org/project/opengeotech/

You can also test the installation:

```bash
pip install opengeotech
```

## Updating the Package

To update the package:

1. Update the version number in `setup.py` and `opengeotech/__init__.py`
2. Make your changes to the code
3. Build the package again: `python -m build`
4. Upload to PyPI: `python -m twine upload dist/*`

## Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/en/latest/) 