import pytest
from django.contrib.auth.models import User

# Each test will run in its own transaction that will be rolled back at the end of the test. 
@pytest.mark.django_db
# Marks is a helper using which you can set metadata on your test functions
# django_db Mark accesses the Django test database
def test_user_create():
  User.objects.create_user(username="testuser", password="password123")
  assert User.objects.count() == 1


  