#!/bin/bash

# Check if .env file exists, if not, create it by copying env.example
if [ ! -f .env ]; then
    echo "Creating .env file from env.example..."
    cp env.example .env
else
    echo ".env file already exists. Skipping creation."
fi

echo "Locking dependencies without updating..."
poetry lock --no-update

echo "Starting Poetry shell..."
poetry shell

echo "Installing dependencies (excluding the project root package)..."
poetry install --no-root

echo "Applying database migrations..."
python manage.py migrate

echo "Starting the Django development server..."
python manage.py runserver
