# Webscraping for Business

<br />
<p align="center">
  <a href="https://github.com/jgome284/Webscraping-for-Business">
    <img src="imgs/scrapy_playwright.png" alt="Logo">
  </a>

  <h3 align="center">Foreword</h3>

  <p align="center">
    Webscraping for business with Scrapy and Playwright, Ubuntu devcontainer for development on Visual Studio Code.
    <br />
    <a href="https://github.com/jgome284/Webscraping-for-Business/issues">Report Bug</a>
    ·
    <a href="https://github.com/jgome284/Webscraping-for-Business/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Webscraping for Business](#webscraping-for-business)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
    - [Setup](#setup)
    - [Scrapy](#scrapy)
  - [Prerequisites](#prerequisites)
  - [Getting started](#getting-started)
  - [License](#license)

<!-- ABOUT THE PROJECT -->
## About

### Setup

This project includes a Dev Container for Visual Studio Code. It serves as a full-featured development environment with everything needed to run the application. Dev Containers separate tools, libraries, or runtimes needed for working with a codebase. They aid in continuous integration and testing. Dev containers can be run locally or remotely, in a private or public cloud, in a variety of supporting tools and editors.

[This devcontainer](.devcontainer), is built IAW the [dev containers specification](https://containers.dev/implementors/spec/) and tailored for a build environment that runs Ubuntu version 22.04 and Python. Software libraries are installed in accordance with [requirements.txt](./.devcontainer/requirements.txt). Additionally, the devcontainer has git for version control and several extensions installed for Visual Studio Code as development utilities.

### Scrapy

Scrapy is the bread and butter of this project. It is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival. To understand Scrapy, it's helpful to reference it's architecture. For more information, check the [docs](https://docs.scrapy.org/en/latest/topics/architecture.html#spider-middlewares) and the image below.

![Scrapy Architecture](imgs/scrapy_architecture.png)

<!-- PREREQUISITES -->
## Prerequisites

To start, you need to have Docker Engine and Docker Compose on your machine. You can either:

- Install Docker Desktop which includes both Docker Engine and Docker Compose
- Install Docker Engine and Docker Compose as standalone binaries

This devcontainer is setup for development on Visual Studio Code. You should have it installed along with the [remote development pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) to enable the IDE's devcontainers functionality.

Create a `credentials.txt` file to host your git configuration settings. This file is utilized by the devcontainer's `postCreateCommand` as specified in `.devcontainer.json`. The format of this file should looks as such:

```sh
User:"YOUR NAME"
Email:"YOUR EMAIL"
```

All dependencies within your [requirements.txt](./.devcontainer/requirements.txt) file will be handled during the build process with Docker.

<!-- GETTING STARTED -->
## Getting started

Open Docker Desktop to run the Docker daemon, a background process that manages and coordinates Docker containers on your system. On VS Code, start the development container by running `Dev Containers: Rebuild and Reopen In Container` in the command palette. It can be accessed with the keyboard shortcut `ctrl + shift + P` on your keyboard. The command shows up as follows:

![Rebuild and Reopen In Container](imgs/rebuildAndReopenInContainer.png)

Doing so will start the build process for the devcontainer. Visual Studio will establish a remote connection to the development container with several common python extensions installed in the IDE. Of note, when a successful connection is established to the container, info for the Ubuntu OS is displayed as shown below:

![Operating System Information](imgs/osInfo.png)

Scrapy doesn’t support JavaScript execution by default. So [Playwright](https://playwright.dev/python/) is used to prerender websites. Doing so gives [Scrapy](https://docs.scrapy.org/en/latest/intro/overview.html) access it would otherwise lack to dynamically load content via JavaScript on an installed browser.

When the container launches successfully, you will have a Chromium browser installed for [Playwright](https://playwright.dev/python/). Chromium is a free, open-source web browser created by Google. Several modern browsers - Edge, Chrome, Brave, Opera, Vivaldi, etc. - are built off Chromium. If you please, you can also run webscraping by downloading different browsers for your container. [Playwright](https://playwright.dev/python/) offers installation for chrome, chrome-beta, msedge, msedge-beta, msedge-dev, firefox, firefox-asan, and webkit. You can run the following commands or add them to the Dockerfile:

``` sh
# Install a subset of available browsers for Playwright
playwright install <YOUR PREFERRED BROWSER(S)>

# Complete Playwright configuration by installing all system dependencies
playwright install-deps <YOUR PREFERRED BROWSER(S)>
```

This project includes several spiders. They are found in `./doral/doral/spiders`. Some are for testing, others are still in development. Spiders can be run via their name, for example, try the following command to verify that the doral spider works:

```sh
scrapy crawl doral
```

## License

Distributed under the MIT License. See `LICENSE` for more information.
