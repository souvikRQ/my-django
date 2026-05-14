#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myrevoltedjango.settings')
    
    # Load environment variables from .env file
    env_path = Path(__file__).resolve().parent / '.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split('=', 1)
                    if len(parts) == 2:
                        os.environ.setdefault(parts[0].strip(), parts[1].strip())

    try:
        from django.core.management import execute_from_command_line
        from django.core.management.commands.runserver import Command as runserver
        
        # Set default port to ENV's PORT or 8000
        runserver.default_port = os.environ.get('PORT', '8000')
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
