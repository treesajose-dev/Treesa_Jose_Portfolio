# Treesa Jose - Portfolio Website

A modern, visually stunning portfolio website built with Flask, featuring a vibrant colorful design with futuristic elements.


## Features

- **Vibrant Colorful Design**: Professional dark theme enhanced with vibrant gradients (teal, cyan, coral, sunset, ocean, rainbow)
  - Education timeline with purple gradients
  - Project showcase with teal glow effects and GitHub links
  - Technical skills with rainbow gradient badges
  - Achievements with sunset gradient icons
  - Contact cards with ocean gradient effects
- **Smooth Animations**: Scroll-triggered fade-in effects and micro-interactions
- **SEO Optimized**: Proper meta tags and semantic HTML
- **Production Ready**: Configured for deployment on PythonAnywhere

## Technology Stack

- **Backend**: Flask 3.0.0 (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Google Fonts (Inter, Space Grotesk)
- **Icons**: Font Awesome 6.5.1
- **Deployment**: PythonAnywhere (Python hosting platform)
- **Server**: Gunicorn (WSGI HTTP Server for production)

## Installation & Local Setup

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Steps

1. **Clone or navigate to the repository**:
   ```bash
   cd portfolio_treesa_jose
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```
## Project Structure

```
portfolio_treesa_jose/
├── app.py                      # Main Flask application
├── wsgi.py                     # WSGI configuration for PythonAnywhere
├── requirements.txt            # Python dependencies
│   ├── js/
│   │   └── script.js           # Interactive features
│   └── images/
│       ├── spicebazaar.png
│       └── filmcritichub.png
└── templates/
    ├── base.html               # Base template with nav & footer
    ├── index.html              # Homepage with all sections
    ├── 404.html                # 404 error page
    └── 500.html                # 500 error page
```

## Live Links

- **GitHub Projects**:
  - [SpiceBazaar](https://github.com/treesajose-dev/Spice-Bazaar-Online-Spices-Store)
  - [FilmCriticHub](https://github.com/treesajose-dev/FilmCriticHub-Online-Film-Review-System)

- **Social Media**:
  - [LinkedIn](https://linkedin.com/in/treesajose-dev)
  - [GitHub](https://github.com/treesajose-dev)

## Contact

- **Email**: treesajosemadathil@yahoo.com
- **Location**: Kochi, Kerala

**Built by Treesa Jose**
