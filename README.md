# Blog Admin
This is the CMS and API for [Blog](https://github.com/lulu-cao/blog). Access the backend admin site at [https://blog-cms-django-abaff6e17c2a.herokuapp.com/admin](https://blog-cms-django-abaff6e17c2a.herokuapp.com/admin). Contact Lulu Cao for login information.

## API Structure
* BaseURL - https://blog-cms-django-abaff6e17c2a.herokuapp.com/api/
* `/blogs/` - user blogs
* `/featured-articles/` - a collection of articles selected by website editors
* `/rss-feeds/` - user RSS feeds
* `/users/` - user id

## Development
1. Install Docker and Docker VS Code extension
2. Reopen the repo in the docker container using Dockerfile
3. Install dependencies, apply database migrations, and start the app
    ```
    pipenv shell
    pipenv install
    pipenv run python manage.py migrate
    pipenv run python manage.py runserver
    pipenv run python manage.py createsuperuser
    ```
4. CMS will be running at http://localhost:8000/admin/. API can be accessed at http://localhost:8000/api/.

## Tests
1. To run tests in the current Docker container, use a command from below:
    ```python
    pytest                                                   # all 
    pytest a_directory                                       # directory
    pytest test_something.py                                 # tests file
    pytest test_something.py::single_test                    # single test function
    pytest -m "xfail and not slow" --strict-markers          # tests with Marks
    ``` 

2. To run tests in a separate Docker container, build a new Dcoker image with the tag `django-tests`.
    ```
    docker build -f Dockerfile.test -t django-tests .
    ```

    Then start a Docker container based on the previously built image. 
    ```
    docker run --rm django-tests
    ```
    `-rm` automatically removes the container after it stops.

## Deployment
Contact Lulu Cao for access to heroku app.
```
git push
git push heroku
```

## Useful Documentation
### Pytest
1. [Pytest Official Documentation](https://docs.pytest.org/en/stable/getting-started.html#get-started)
2. [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)

### Pytest-Django
1. [Pytest-Django Official Documentation](https://pytest-django.readthedocs.io/en/stable/)
2. [Testing Your Django App With Pytest](https://djangostars.com/blog/django-pytest-testing/), pay special attention to `Testing Django REST Framework with Pytest`
3. [How to Provide Test Fixtures for Django Models in Pytest](https://realpython.com/django-pytest-fixtures/)

### Docker
1. [Running Unit Tests With Docker](https://medium.com/swlh/running-unit-tests-inside-a-docker-container-ec68c2274522)
2. [How to run PyTest in docker container](https://medium.com/@harishpillai1994/how-to-run-pytest-in-docker-container-and-publish-the-results-in-allure-reporting-a96499f28f9f), this article also provides an example workflow yml for GitHub Actions