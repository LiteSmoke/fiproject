#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""

    print("=============os.environ.get('DJANGO_SETTINGS_MODULE')=============")
    print(os.environ.get('DJANGO_SETTINGS_MODULE'))

    if os.environ.get('DJANGO_SETTINGS_MODULE') == 'fi_django_project.settings.prod':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fi_django_project.settings.prod')
        print("========== PROD ENVIRONMENT ===========")
    else:
        print("========== DEV ENVIRONMENT ===========")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fi_django_project.settings.dev')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
