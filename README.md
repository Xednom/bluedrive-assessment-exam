# Bluedrive

Bluedrive assessment exam

[![Built with Cookiecutter Djangos Bvgels](https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Bvgels-ff69b4.svg?logo=cookiecutter)](https://github.com/Xednom/cookiecutter-django-bvgels)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Environment Configuration(settings)

The PLATFORM variable in the .env file determines which Django settings file to load based on the current environment. This allows the application to adapt to different configurations for development, testing, and production.

Available Platforms:

    local – Loads local.py for local development settings
    staging – Loads staging.py for the staging environment
    qa – Loads qa.py for quality assurance
    prod – Loads prod.py for production deployment

How to Set the Platform:

In the .env file, set the PLATFORM variable to the desired environment. For example:

`PLATFORM=local`

This will ensure Django loads settings/local.py. Adjust PLATFORM as needed for other environments:

```
PLATFORM=local   # For local development
PLATFORM=staging # For staging 
PLATFORM=qa      # For QA testing
PLATFORM=prod    # For production
```

By structuring settings in this way, the project maintains environment-specific configurations, keeping local development settings separate from production settings and reducing the risk of configuration errors.

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


# Generate secret key

- To generate a **secret key** and replace the existing one from the env.example, use this command:

      $ python manage.py generate_secret_key