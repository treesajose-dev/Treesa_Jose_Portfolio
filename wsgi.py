"""
WSGI Configuration for PythonAnywhere Deployment
================================================

This file configures the Flask application for deployment on PythonAnywhere.

Setup Instructions:
1. Upload your project to PythonAnywhere (via Git or file upload)
2. In the PythonAnywhere web app configuration, set the WSGI file path to this file
3. Configure static files mapping (see PYTHONANYWHERE_DEPLOYMENT.md)
4. Reload the web app

Important: Update the project_home path below to match your PythonAnywhere directory structure.
"""

import sys
import os

# Add your project directory to the sys.path
# IMPORTANT: Change this path to match your PythonAnywhere username and project location
# Example: /home/yourusername/portfolio_treesa_jose
project_home = '/home/yourusername/portfolio_treesa_jose'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables for production
os.environ['FLASK_ENV'] = 'production'

# Import the Flask app
from app import app as application

# For debugging (remove in production if not needed)
# application.debug = False
