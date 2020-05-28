Testing
===

unittest
---


pytest
---

- fixtures
```
pytest --fixtures
```

- markers
```
pytest --markers
pytest -m "not slow"  # exclude "slow" test
```

- coverage (with pytest-cov)
```
pytest --cov-report html[:<dir>] --cov=<module> .
pytest --cov-branch --cov-report html[:<dir>] --cov=<module> .
```


coverage
---

- install
```
pip install --user coverage
```

- run tests
```
coverage run --source . -m unittest <unittest args>  # source: directory to be covered
```

- report
```
coverage report  # console
coverage report -m  # missing
coverage html  # html, default output dir: ./htmlcov
```
