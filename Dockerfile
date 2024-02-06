FROM python:3.8.18-slim

# to install pipenv
RUN pip install pipenv

# to create directory
WORKDIR /app

# to copy the Pipfile and Pipfile.lock and put it in the directory, /app
COPY ["Pipfile", "Pipfile.lock", "./"]

# to run pipenv install without creating another virtual environment
RUN pipenv install --system --deploy