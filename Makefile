SCSS = {{ project_name }}/static/scss
STATIC = {{ project_name }}/static

.PHONY: collectstatics compile-scss compile-scss-debug isort isort-check run install test

collectstatics: compile-scss
	./manage.py collectstatic --noinput

compile-scss:
	sassc $(SCSS)/main.scss $(STATIC)/css/main.css -s compressed

compile-scss-debug:
	sassc $(SCSS)/main.scss $(STATIC)/css/main.css --sourcemap

watch-scss:
	watchmedo shell-command --patterns=*.scss --recursive --command="make compile-scss-debug" $(SCSS)

isort:
	isort */*.py

isort-check:
	isort -c */*.py

run:
	python manage.py runserver 0.0.0.0:8000

install:
	pip install -r requirements/dev.txt

test:
	@coverage run --source=. manage.py test -v2
