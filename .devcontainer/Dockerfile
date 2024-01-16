# syntax=docker/dockerfile:1

# Use the official Ubuntu 22.04 base image
ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}

# Set environment variables...

# disable interactive prompts during package installation, making the installation non-interactive.
ENV DEBIAN_FRONTEND=noninteractive \ 
    # specifies the "C" locale with UTF-8 character encoding
    LC_ALL=C.UTF-8 \
    # Similar to LC_ALL, the LANG environment variable also sets the default locale. 
    LANG=C.UTF-8

# Setting both LC_ALL and LANG to the same value helps ensure consistency
# in the character encoding and language settings...

# Set the working directory in the container
WORKDIR /doral_prospecting

# Update and install necessary packages...

RUN apt-get update && \
    # This command updates the package lists for the APT (Advanced Package Tool) package manager. 
    # It fetches the latest information about available packages from the configured repositories.
    apt-get install -y \
        python3 \
        python3-pip \
        git && \
    # This command installs the specified packages (python3 and python3-pip). 
    # The -y flag is used to automatically confirm any prompts 
    # during the installation process without requiring user interaction.
    apt-get clean && \
    # After installing packages, the apt-get clean command is used to clean up the APT package cache. This removes downloaded package files (.deb) that are no longer needed, reducing the size of the Docker image.
    rm -rf /var/lib/apt/lists/*
    # This command removes the package lists in /var/lib/apt/lists/. 
    # These lists are no longer needed after the package installation is complete, 
    # and removing them helps reduce the size of the Docker image. 
    # The use of rm -rf removes the files and directories forcefully.

# Leverage a bind mount to requirements.txt to avoid having to copy them into this layer.
RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    # Install Python dependencies
    pip3 install --no-cache-dir -r requirements.txt

# Specify the default command to run on container startup
CMD ["python3"]
