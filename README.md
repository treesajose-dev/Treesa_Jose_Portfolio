# Treesa Jose - Portfolio Website

A modern, visually stunning portfolio website built with Flask, featuring a vibrant colorful design with futuristic elements and inspired by Google Antigravity's aesthetic.

![Portfolio Preview](static/images/spicebazaar.png)

## 🌟 Features

- **Vibrant Colorful Design**: Professional dark theme enhanced with vibrant gradients (teal, cyan, coral, sunset, ocean, rainbow)
- **Futuristic Hero Section**: Animated particle background with floating geometric shapes and glowing orbs
- **Fully Responsive**: Optimized for desktop, tablet, and mobile devices
- **Interactive Sections**:
  - Hero section with futuristic animated background
  - About Me with contact information
  - Education timeline with purple gradients
  - Project showcase with teal glow effects and GitHub links
  - Technical skills with rainbow gradient badges
  - Achievements with sunset gradient icons
  - Contact cards with ocean gradient effects
- **Smooth Animations**: Scroll-triggered fade-in effects and micro-interactions
- **SEO Optimized**: Proper meta tags and semantic HTML
- **Production Ready**: Configured for deployment on PythonAnywhere

## 🚀 Technology Stack

- **Backend**: Flask 3.0.0 (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Google Fonts (Inter, Space Grotesk)
- **Icons**: Font Awesome 6.5.1
- **Deployment**: PythonAnywhere (Python hosting platform)
- **Server**: Gunicorn (WSGI HTTP Server for production)

## 📦 Installation & Local Setup

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

## 🌐 Deployment on PythonAnywhere

This portfolio is configured for easy deployment on PythonAnywhere. Follow the comprehensive guide in [`PYTHONANYWHERE_DEPLOYMENT.md`](PYTHONANYWHERE_DEPLOYMENT.md) for detailed step-by-step instructions.

### Quick Start

1. **Create a PythonAnywhere account** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload your code**:
   - Via Git (recommended):
     ```bash
     git clone https://github.com/yourusername/portfolio_treesa_jose.git
     cd portfolio_treesa_jose
     ```
   - Or upload files manually via the Files tab

3. **Set up virtual environment**:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure Web App**:
   - Create a new web app (Manual configuration, Python 3.10)
   - Set WSGI file path to your `wsgi.py`
   - Configure virtual environment path
   - Add static files mapping: `/static/` → `/home/yourusername/portfolio_treesa_jose/static/`

5. **Update `wsgi.py`**:
   - Change `project_home` to your actual PythonAnywhere path
   - Example: `/home/yourusername/portfolio_treesa_jose`

6. **Reload** your web app

Your portfolio will be live at: `https://yourusername.pythonanywhere.com`

### Deployment Files

- **`wsgi.py`**: WSGI configuration for PythonAnywhere
- **`PYTHONANYWHERE_DEPLOYMENT.md`**: Complete deployment guide with troubleshooting
- **`STATIC_FILES_CONFIG.md`**: Static files configuration instructions

## 📁 Project Structure

```
portfolio_treesa_jose/
├── app.py                      # Main Flask application
├── wsgi.py                     # WSGI configuration for PythonAnywhere
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render deployment configuration (alternative)
├── .gitignore                  # Git ignore file
├── README.md                   # This file
├── PYTHONANYWHERE_DEPLOYMENT.md # PythonAnywhere deployment guide
├── STATIC_FILES_CONFIG.md      # Static files configuration guide
├── static/
│   ├── css/
│   │   ├── style.css           # Main colorful professional styles
│   │   └── futuristic_hero.css # Futuristic hero background styles
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

## 🎨 Design Features

### Enhanced Color Palette
- **Primary Background**: `#0a0e27` (Deep Navy)
- **Secondary Background**: `#141b3d` (Dark Blue)
- **Vibrant Accents**: Cyan (`#00f2fe`), Teal (`#20e3b2`), Coral (`#ff6b6b`), Orange (`#ff8c42`), Purple (`#a78bfa`), Pink (`#f093fb`)

### Gradient Variations
- **Primary**: Purple to Violet (`#667eea` → `#764ba2`)
- **Sunset**: Orange to Pink (`#ff8c42` → `#f093fb`)
- **Ocean**: Cyan to Teal (`#00f2fe` → `#20e3b2`)
- **Teal**: Teal to Blue (`#20e3b2` → `#4facfe`)
- **Coral**: Coral to Orange (`#ff6b6b` → `#ff8c42`)
- **Rainbow**: Multi-color gradient (blue → teal → purple → pink → orange)

### Typography
- **Headings**: Space Grotesk (Bold, Modern)
- **Body**: Inter (Clean, Readable)

### Visual Effects
- **Futuristic Hero**: Animated particles, floating geometric shapes, glowing orbs
- **Glassmorphism**: Backdrop blur effects on cards
- **Gradient Text**: Colorful gradient text on headings
- **Colorful Glows**: Cyan, coral, and teal glow shadows
- **Smooth Animations**: Scroll-triggered fade-ins and hover transformations
- **Parallax Effects**: Subtle parallax on hero background

### Component-Specific Styling
- **Buttons**: Sunset gradient (primary), Ocean gradient (secondary)
- **Project Cards**: Teal border glow on hover
- **Skill Badges**: Rainbow gradient on hover
- **Tech Badges**: Teal gradient background
- **Achievement Icons**: Sunset gradient with drop shadow
- **Contact Icons**: Ocean gradient with enhanced glow
- **Timeline Badges**: Purple gradient

## 📱 Responsive Breakpoints

- **Mobile**: < 480px
- **Tablet**: 481px - 768px
- **Desktop**: > 768px

## 🔗 Live Links

- **GitHub Projects**:
  - [SpiceBazaar](https://github.com/treesajose-dev/Spice-Bazaar-Online-Spices-Store)
  - [FilmCriticHub](https://github.com/treesajose-dev/FilmCriticHub-Online-Film-Review-System)

- **Social Media**:
  - [LinkedIn](https://linkedin.com/in/treesajose-dev)
  - [GitHub](https://github.com/treesajose-dev)

## 📧 Contact

- **Email**: treesajosemadathil@yahoo.com
- **Location**: Kochi, Kerala

## 🛠️ Development

### Running Locally
```bash
python app.py
```
The app will run on `http://localhost:5000` in debug mode.

### Production Deployment
For production deployment on PythonAnywhere, the app uses:
- WSGI server configuration
- Production environment variables
- Static files served directly by PythonAnywhere

## 📄 License

This project is open source and available for personal and educational use.

## 🙏 Acknowledgments

- Design inspiration: [Google Antigravity](https://antigravity.google/)
- Icons: [Font Awesome](https://fontawesome.com/)
- Fonts: [Google Fonts](https://fonts.google.com/)
- Hosting: [PythonAnywhere](https://www.pythonanywhere.com/)

---

**Built with ❤️ by Treesa Jose**
