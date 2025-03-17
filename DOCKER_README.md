# OpenGeoTech Docker Guide

This guide explains how to use the OpenGeoTech Docker image.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your system

## Quick Start

### Pull the Docker image

```bash
docker pull jadinata/opengeotech
```

### Run the Docker container

```bash
docker run --rm jadinata/opengeotech
```

This will run the container and show the installed OpenGeoTech version.

## Using OpenGeoTech in Docker

To use OpenGeoTech interactively:

```bash
docker run -it --rm jadinata/opengeotech python
```

Then in the Python interpreter:

```python
import opengeotech
# Use OpenGeoTech functions here
```

## Building the Docker Image Locally

If you want to build the Docker image locally:

```bash
docker build -t jadinata/opengeotech .
```

## Publishing to Docker Hub

To publish the image to Docker Hub:

1. Make sure you're logged in to Docker Hub:
   ```bash
   docker login
   ```

2. Run the provided script:
   ```bash
   chmod +x docker_publish.sh
   ./docker_publish.sh
   ``` 