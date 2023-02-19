# Pull base image
FROM python:3.10

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
COPY .env /
RUN apt-get update
RUN pip install -r requirements.txt
COPY ./entrypoint.sh /
# Copy project
COPY . .

ENTRYPOINT ["sh", "/entrypoint.sh"]