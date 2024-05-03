# Blog Admin
This is the CMS and API for [Blog](https://github.com/lulu-cao/blog). Access the backend admin site at [https://blog-cms-django-abaff6e17c2a.herokuapp.com/admin](https://blog-cms-django-abaff6e17c2a.herokuapp.com/admin). Contact Lulu Cao for login information.

## API Structure
* BaseURL - https://blog-cms-django-abaff6e17c2a.herokuapp.com/api/
* `/blogs/` - user blogs
* `/featured-articles/` - a collection of articles selected by website editors
* `/rss-feeds/` - user RSS feeds
* `/users/` - user id

## Start the App
1. Install Docker VS Code extension
2. Reopen the repo in the docker container
3. Install dependencies, apply database migrations, and start the app
    ```
    pipenv shell
    pipenv install
    pipenv run python manage.py migrate
    pipenv run python manage.py runserver
    ```

## Deployment
Contact Lulu Cao for access to heroku app.
```
git push
git push heroku
```
