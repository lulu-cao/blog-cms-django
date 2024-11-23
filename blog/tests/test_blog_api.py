import pytest

# Fixtures for client and data setup
# Fixtures are functions that run before and after each test, used for data configuration, 
# connection/disconnection of databases, calling extra actions, etc.
@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def create_blog(db):
    from blog.models import Blog
    return Blog.objects.create(title="Test", body="", pub_date="2024-11-23T12:09:00Z")

@pytest.fixture
def create_user(db):
    from blog.models import User
    return User.objects.create(uid="123456")

# Test the /api/blogs/ Endpoint
@pytest.mark.django_db
def test_get_blogs(api_client, create_blog):
    # Make a GET request to retrieve blogs
    response = api_client.get("/api/blogs/")
    assert response.status_code == 200
    assert response.data[0]["title"] == "Test"

@pytest.mark.django_db
def test_create_blog(api_client):
    # Make a POST request to create a new blog
    payload = {
        "title": "New Blog",
        "body": "This is a blog post.",
        "pub_date": "2024-11-23T12:09:00Z",
    }
    response = api_client.post("/api/blogs/", payload)

    assert response.status_code == 201
    assert response.data["title"] == "New Blog"

# Test the /api/featured-articles/ Endpoint
@pytest.mark.django_db
def test_get_featured_articles(api_client):
    response = api_client.get("/api/featured-articles/")
    assert response.status_code == 200
    assert isinstance(response.data, list)

# Test the /api/cache-rss-feed/ Endpoint
@pytest.mark.django_db
def test_cache_rss_feed(api_client, create_user):
    response = api_client.post("/api/cache-rss-feed/", {"url": "https://medium.com/feed/@lcao_5526", "user": 1})
    assert response.status_code == 201  

# Test the /api/users/ Endpoint
@pytest.mark.django_db
def test_get_users(api_client, create_user):
    response = api_client.get("/api/users/")

    assert response.status_code == 200
    assert response.data[0]["id"] == 1
