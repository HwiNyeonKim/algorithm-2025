#!/bin/bash
poetry run isort .
poetry run flake8 .
poetry run black .