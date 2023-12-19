# Devcontainer with Docker Compose
<br />
<p align="center">
  <a href="https://github.com/jgome284/devcontainer-w-compose">
    <img src="imgs/dev-container-stages.png" alt="Logo">
  </a>

  <h3 align="center">Foreword</h3>

  <p align="center">
    python:3.9-alpine development container setup with docker-compose for use on Visual Studio.
    <br />
    <a href="https://github.com/jgome284/devcontainer-w-compose/issues">Report Bug</a>
    ·
    <a href="https://github.com/jgome284/devcontainer-w-compose/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents
<div style='text-align:'>
  <ol>
    <li>
      <a href="#about">About</a>
    </li>
    <li>
      <a href="#prerequisites">Prerequisites</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#license">License</a>
    </li>
  </ol>
</details>
</div>


<!-- ABOUT THE PROJECT -->
## About
[Devcontainer with Compose](https://github.com/jgome284/devcontainer-w-compose)

This project serves as an example of how to setup a development container. A Development Container (or Dev Container for short) allows you to use a container as a full-featured development environment. It can be used to run an application, to separate tools, libraries, or runtimes needed for working with a codebase, and to aid in continuous integration and testing. Dev containers can be run locally or remotely, in a private or public cloud, in a variety of supporting tools and editors.

[This devcontainer](.devcontainer), is built IAW the [dev containers specification](https://containers.dev/implementors/spec/) and tailored for a build environment that runs on alpine linux and python with the cowsay library as an additional dependency for demonstration purposes. Additionally, the devcontainer has git for version control and several extensions installed for Visual Studio Code as development utilities.

<!-- PREREQUISITES -->
## Prerequisites
To start, you need to have Docker Engine and Docker Compose on your machine. You can either:
* Install Docker Desktop which includes both Docker Engine and Docker Compose
* Install Docker Engine and Docker Compose as standalone binaries

Additionally, this devcontainer is meant to work on Visual Studio Code. You should have it installed along with the [remote development pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) to enable the IDE's devcontainers functionality.

Create a `credentials.txt` file to host your git configuration settings. This file is utilized by the devcontainer's `postCreateCommand` as specified in `.devcontainer.json`. The format of this file should looks as such:
```sh
User:YOUR NAME
Email:YOUR EMAIL
```
All dependencies within your `requirements.txt` file will be handled during the build process with Docker.

<!-- GETTING STARTED -->
## Getting started
This project is setup to work with Docker on Visual Studio Code. Once the [remote development pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension is installed, start the development container by running `Dev Containers: Rebuild and Reopen In Container` in the command palette. It can be accessed with the keyboard shortcut `ctrl + shift + P` on your keyboard. The command shows as follows:

![Rebuild and Reopen In Container](imgs/rebuildAndReopenInContainer.png)

Doing so will start the build process for the devcontainer. Visual Studio will establish a remote connection to the development container with several common python extensions installed in the IDE. Of note when a successful connection is established to the container, info for the alpine-linux OS is displayed as shown below:

![Operating System Information](imgs/osInfo.png)


## License
Distributed under the MIT License. See `LICENSE` for more information.