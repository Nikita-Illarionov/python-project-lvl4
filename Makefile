lint:
	poetry run flake8 users tasks labels statuses task_manager

install:
	poetry install

test:
	poetry run coverage run --omit '.venv/*' --source '.' manage.py test

test-coverage-report: test
	poetry run coverage report

test-coverage-report-xml:
	poetry run coverage xml
