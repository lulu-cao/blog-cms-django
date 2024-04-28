# base image
# This installs a Python image into the Docker image. This is also the version of
# Python that will run the application in the container
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
# This will be the root directory of the Django app in the container
WORKDIR /code

# Install Pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile* /code/

# Install project dependencies
RUN pipenv install

# Copy the Django project code into the container
COPY . /code/

# Expose the default Django development server port
EXPOSE 8000

# Run the Django development server
CMD pipenv run python manage.py runserver 0.0.0.0:8000
