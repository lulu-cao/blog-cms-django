# Use Python 3.11 as the base image
# The base image provides a lightweight Python runtime environment for our application.
FROM python:3.11

# Set environment variables
# PYTHONUNBUFFERED=1: Ensures Python outputs logs directly to the terminal (stdout/stderr) without buffering.
# PYTHONDONTWRITEBYTECODE=1: Prevents Python from generating `.pyc` files to reduce clutter in the container.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
# All subsequent commands will be executed relative to this directory.
# This serves as the root directory for the Django application within the container.
WORKDIR /code

# Install Pipenv, a dependency manager for Python
RUN pip install pipenv

# Copy the dependency declaration files into the container
# Using COPY allows Docker to leverage layer caching when dependencies remain unchanged.
COPY Pipfile* /code/

# Install project dependencies
RUN pipenv install

# Copy the entire project codebase into the container
# Using a separate step after dependencies ensures we rebuild only when code changes.
COPY . /code/

# Expose the default Django development server port
EXPOSE 8000

# Default command to run the application
# This command launches the Django development server, binding to all network interfaces (`0.0.0.0`)
# so it can be accessed from outside the container.
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
