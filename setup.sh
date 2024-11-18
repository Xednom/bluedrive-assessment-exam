#!/bin/bash

# Function to install Poetry
install_poetry() {
    echo "Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"  # Ensure Poetry is in the PATH
}

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Installing it now..."
    install_poetry
else
    echo "Poetry is already installed."
fi

# Check if .env file exists, if not, create it by copying env.example
if [ ! -f .env ]; then
    echo "Creating .env file from env.example..."
    cp env.example .env
else
    echo ".env file already exists. Skipping creation."
fi

echo "Locking dependencies without updating..."
poetry lock --no-update

echo "Installing dependencies (excluding the project root package)..."
poetry install --no-root

echo "Applying database migrations..."
poetry run python manage.py migrate

echo "Starting the Django development server..."
poetry run python manage.py runserver
