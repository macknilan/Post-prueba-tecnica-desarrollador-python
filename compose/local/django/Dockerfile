# GET THE IMAGE SLIM-bullseye
FROM python:3.9.7-slim-bullseye

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building Python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev


# FORCE STDIN, STDOUT AND STDERR TO BE TOTALLY UNBUFFERED. ON SY>STEMS WHERE IT MATTERS, ALSO PUT STDIN, STDOUT AND STDERR IN BINARY MODE.
# SET DEFAULT ENVIRONMENT VARIABLES
ENV PYTHONUNBUFFERED 1
# PYTHON FROM COPYING PYC FILES TO THE CONTAINER
ENV PYTHONDONTWRITEBYTECODE 1

# Create and set working directory
WORKDIR /app

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN python3 -m pip install --no-cache-dir -r /requirements/local.txt

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building Python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev \
    # Translations dependencies
    gettext \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Copy application code to WORKDIR
COPY . /app

ENTRYPOINT ["/entrypoint"]
