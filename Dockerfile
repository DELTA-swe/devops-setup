# Use the official slim-buster as a parent image
FROM python:3.8-slim

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

ADD . /app

# Set the working directory to /app
WORKDIR /app

RUN uv sync --frozen

# Expose the port on which the app will run
EXPOSE 8000

# Command to run the application
CMD ["uv", "run", "main.py"]