# My Package

A short description of the package.

## Installation

You can install the package using pip:

```bash
pip install my_package
```


### **Prepare for Distribution**

Make sure you have the latest versions of `setuptools` and `wheel` installed:

```bash
pip install --upgrade setuptools wheel
```

### **To Create Distribution**

```bash
python setup.py sdist bdist_wheel
```


## To Upload Package to PyPI (Python Package Index), twine is required:

```bash
pip install twine
```

### Upload Package to 
```bash
twine upload dist/*
```

## To Install Package:
```bash
pip install my_package
```

```bash
from my_package.module import hello_world

print(hello_world())
```

