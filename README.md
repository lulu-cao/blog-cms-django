# Blog Admin
This is the CMS and API for [Blog](https://github.com/lulu-cao/blog). Access the backend admin site at [https://blog-cms-django-abaff6e17c2a.herokuapp.com/admin](https://blog-cms-django-abaff6e17c2a.herokuapp.com/admin). Contact Lulu Cao for login information.

## API Structure
* BaseURL - https://blog-cms-django-abaff6e17c2a.herokuapp.com/api/
* `/blogs/` - user blogs
* `/featured-articles/` - a collection of articles selected by website editors
* `/rss-feeds/` - user RSS feeds
* `/users/` - user id

## Development
1. Install Docker VS Code extension
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
1. To run tests, use a command from below:
    ```python
    pytest                                                   # all 
    pytest a_directory                                       # directory
    pytest test_something.py                                 # tests file
    pytest test_something.py::single_test                    # single test function
    pytest -m "xfail and not slow" --strict-markers          # tests with Marks
    ``` 

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