# FLUC Recommenders API

This repository contains the FLUC Recommenders API. Follow these steps to get started:

## Prerequisites

- Python 3.11 or higher
- Git
- pip (Python package installer)

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fluc_recommenders.git
cd fluc_recommenders
```

Install Poetry (package manager):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Install dependencies:

```bash

poetry install
```

Activate the poetry shell:

```bash
poetry shell
```

## Running the API

Start the API server:

```bash
fastapi dev ./recommenders/app.py
```

The API will be available at `http://localhost:8000`

## API Documentation

Visit `http://localhost:8000/docs` for the complete API documentation.

## Development

For development purposes, you can run the API in debug mode:

```bash
fastapi dev app.py --debug
```
