# Setup package (distutils)

```
python3 -m venv venv
source venv/bin/activate
(venv) python setup.py install
(venv) python -m palindrome  # no error
```

``` source distribution
python3 setup.py sdist --format zip
ls dist  # <package_name>.zip
```
