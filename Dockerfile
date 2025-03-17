FROM python:3.9-slim

LABEL maintainer="OpenGeotech Contributors <opengeotechnical@gmail.com>"
LABEL org.opencontainers.image.source="https://github.com/OpenGeotechnical/opengeotech-python"
LABEL org.opencontainers.image.description="OpenGeoTech Python package for geotechnical engineering"

WORKDIR /app

# Copy the project files
COPY . /app/

# Install the package
RUN pip install --no-cache-dir -e .

# Set the entrypoint
CMD ["python", "-c", "import opengeotech; print(f'OpenGeoTech version {opengeotech.__version__} installed successfully!')"] 