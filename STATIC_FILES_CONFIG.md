# PythonAnywhere Static Files Configuration

## Static Files Mapping

When configuring your web app on PythonAnywhere, add the following static files mapping in the "Web" tab under "Static files":

### URL: /static/
**Directory:** `/home/yourusername/portfolio_treesa_jose/static/`

**Important:** Replace `yourusername` with your actual PythonAnywhere username.

## What This Does

This configuration tells PythonAnywhere to serve all files in the `/static/` directory directly without going through the Flask application. This includes:

- CSS files (`/static/css/style.css`)
- JavaScript files (`/static/js/script.js`)
- Images (`/static/images/*.png`)

## Verification

After setting up the static files mapping and reloading your web app, verify that static files are loading correctly:

1. Open your browser's developer tools (F12)
2. Go to the Network tab
3. Reload your portfolio page
4. Check that all static files (CSS, JS, images) load with 200 status codes
5. If you see 404 errors, double-check the static files path in your PythonAnywhere configuration

## Directory Structure

Your PythonAnywhere directory should look like this:

```
/home/yourusername/portfolio_treesa_jose/
├── app.py
├── wsgi.py
├── requirements.txt
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       ├── spicebazaar.png
│       └── filmcritichub.png
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── 404.html
│   └── 500.html
└── venv/
```

## Troubleshooting

**Static files not loading:**
- Ensure the path in the static files mapping is absolute (starts with `/home/`)
- Check that the directory exists and contains your files
- Verify file permissions (should be readable)
- Clear your browser cache
- Check the error log in PythonAnywhere

**Images not displaying:**
- Verify image files are uploaded to `/static/images/`
- Check image file names match those referenced in `app.py`
- Ensure image files are not too large (free tier has disk space limits)
