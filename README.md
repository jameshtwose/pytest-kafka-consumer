# pytest-kafka-consumer
A demo Kafka consumer to help show off unit testing in python.

![Coverage Badge](./docs/source/_static/coverage-badge.svg)

## Setup
- `pip install -r requirements.txt`

## Running pre-commit checks
- `pre-commit run --all-files`

## Detailed commands
The following commands are useful for running the tests and generating the coverage report.
They are included in the `.pre-commit-config.yaml` file.
#### Running the tests (various ways)
- `python -m pytest --verbose`
- `coverage run -m pytest`
- `python -m pytest tests/test_utils.py::TestUtils`
- `python -m pytest tests/test_utils.py::TestUtils::test_serialize_message`

#### Creating/ viewing the coverage report
- `python -m pytest --cov=. --cov-report=html:docs/source/_static/coverage`

#### Documentation install/ setup
- `mkdir docs && cd docs` (run once)
- `sphinx-quickstart` (run once)
- `sphinx-apidoc consumer --output-dir docs/source --force --separate --no-toc --implicit-namespaces && sphinx-build docs/source docs/build` (run every time you want to update the docs) (this is included in the `.pre-commit-config.yaml` file)