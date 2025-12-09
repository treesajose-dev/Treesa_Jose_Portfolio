# PythonAnywhere Deployment Guide

This guide will help you deploy your portfolio website on PythonAnywhere.

## Prerequisites

- A PythonAnywhere account (free tier works fine)
- Your portfolio code uploaded to PythonAnywhere

## Step-by-Step Deployment

### 1. Upload Your Code to PythonAnywhere

**Option A: Using Git (Recommended)**
1. Open a Bash console on PythonAnywhere
2. Clone your repository:
   ```bash
   git clone https://github.com/yourusername/portfolio_treesa_jose.git
   cd portfolio_treesa_jose
   ```

**Option B: Manual Upload**
1. Use the "Files" tab in PythonAnywhere
2. Upload all project files to a directory (e.g., `/home/yourusername/portfolio_treesa_jose`)

### 2. Install Dependencies

1. Open a Bash console on PythonAnywhere
2. Navigate to your project directory:
   ```bash
   cd ~/portfolio_treesa_jose
   ```
3. Create a virtual environment:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   ```
4. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Create a Web App

1. Go to the "Web" tab in PythonAnywhere
2. Click "Add a new web app"
3. Choose "Manual configuration" (not Flask wizard)
4. Select Python 3.10 (or your preferred version)

### 4. Configure WSGI File

1. In the "Web" tab, find the "Code" section
2. Click on the WSGI configuration file link
3. **Delete all existing content** in the file
4. Copy the contents of your `wsgi.py` file into it
5. **Important**: Update the `project_home` variable to match your actual path:
   ```python
   project_home = '/home/yourusername/portfolio_treesa_jose'
   ```
   Replace `yourusername` with your actual PythonAnywhere username

### 5. Configure Virtual Environment

1. In the "Web" tab, find the "Virtualenv" section
2. Enter the path to your virtual environment:
   ```
   /home/yourusername/portfolio_treesa_jose/venv
   ```
   Replace `yourusername` with your actual PythonAnywhere username

### 6. Configure Static Files

In the "Web" tab, scroll to the "Static files" section and add the following mappings:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/yourusername/portfolio_treesa_jose/static/` |

Replace `yourusername` with your actual PythonAnywhere username.

### 7. Set Environment Variables (Optional)

If you want to set environment variables:
1. Edit your WSGI file
2. Add environment variables before importing the app:
   ```python
   os.environ['SECRET_KEY'] = 'your-secret-key-here'
   ```

### 8. Reload Your Web App

1. Go back to the "Web" tab
2. Click the green "Reload" button
3. Your app should now be live at `yourusername.pythonanywhere.com`

## Troubleshooting

### Error: "ImportError: No module named app"
- Check that the `project_home` path in your WSGI file is correct
- Ensure your virtual environment is properly configured
- Verify that `app.py` exists in your project directory

### Static Files Not Loading
- Verify the static files mapping in the "Web" tab
- Check that the paths are absolute (start with `/home/`)
- Make sure the static directory exists and contains your CSS, JS, and images

### 500 Internal Server Error
- Check the error log (link in the "Web" tab)
- Common causes:
  - Missing dependencies (run `pip install -r requirements.txt`)
  - Incorrect file paths in WSGI configuration
  - Python version mismatch

### Application Not Updating
- After making changes, always click "Reload" in the "Web" tab
- Clear your browser cache
- Check the error and server logs for issues

## Updating Your Application

When you make changes to your code:

1. Upload the new files or pull from Git:
   ```bash
   cd ~/portfolio_treesa_jose
   git pull origin main
   ```
2. If you updated `requirements.txt`:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Reload the web app from the "Web" tab

## Important Notes

- **Free tier limitations**: The free tier has some limitations (e.g., your app goes to sleep after inactivity)
- **Custom domain**: Paid plans allow custom domain names
- **HTTPS**: PythonAnywhere provides HTTPS by default for `*.pythonanywhere.com` domains
- **File storage**: Free tier has limited disk space (512 MB)

## Security Recommendations

1. **Change the SECRET_KEY**: Update the secret key in `app.py` or set it as an environment variable
2. **Don't commit secrets**: Never commit API keys or passwords to Git
3. **Use environment variables**: For sensitive data, use environment variables in the WSGI file

## Support

- PythonAnywhere Help: https://help.pythonanywhere.com/
- PythonAnywhere Forums: https://www.pythonanywhere.com/forums/
- Flask Documentation: https://flask.palletsprojects.com/

## Your Application Details

- **Application Name**: Treesa Jose Portfolio
- **Framework**: Flask 3.0.0
- **Python Version**: 3.10+ recommended
- **Main File**: `app.py`
- **WSGI File**: `wsgi.py`
- **Static Files**: `/static/` directory

---

**Congratulations!** Your portfolio should now be live on PythonAnywhere! 🎉
