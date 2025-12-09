# Treesa Jose - Portfolio Website

A modern, visually stunning portfolio website built with Flask and inspired by Google Antigravity's design aesthetic.

![Portfolio Preview](static/images/spicebazaar.png)

## 🌟 Features

- **Antigravity-Inspired Design**: Dark theme with vibrant gradients, glassmorphism effects, and smooth animations
- **Fully Responsive**: Optimized for desktop, tablet, and mobile devices
- **Interactive Sections**:
  - Hero section with animated background
  - About Me with contact information
  - Education timeline
  - Project showcase with GitHub links
  - Technical skills categorized display
  - Achievements and certifications
  - Contact cards with direct links
- **Smooth Animations**: Scroll-triggered fade-in effects and micro-interactions
- **SEO Optimized**: Proper meta tags and semantic HTML
- **Production Ready**: Configured for deployment on Render

## 🚀 Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Google Fonts (Inter, Space Grotesk)
- **Icons**: Font Awesome 6.5.1
- **Deployment**: Render (Platform as a Service)
- **Server**: Gunicorn (WSGI HTTP Server)

## 📦 Installation & Local Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone or navigate to the repository**:
   ```bash
   cd d:\portfolio_treesa_jose
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

## 🌐 Deployment on Render

### Method 1: Using Render Dashboard (Recommended)

1. **Create a GitHub repository** and push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Flask portfolio website"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Sign up/Login to Render**: Visit [render.com](https://render.com)

3. **Create a New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure the service:
     - **Name**: `treesa-portfolio` (or your preferred name)
     - **Environment**: `Python`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Instance Type**: Free

4. **Environment Variables** (Optional):
   - Add `FLASK_ENV` = `production`
   - Render will auto-generate `SECRET_KEY`

5. **Deploy**: Click "Create Web Service"

Your portfolio will be live at: `https://treesa-portfolio.onrender.com` (or your chosen name)

### Method 2: Using render.yaml (Infrastructure as Code)

The repository includes a `render.yaml` file for automatic deployment:

1. Push your code to GitHub
2. In Render dashboard, go to "Blueprint" → "New Blueprint Instance"
3. Connect your repository
4. Render will automatically detect `render.yaml` and deploy

## 📁 Project Structure

```
portfolio_treesa_jose/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── render.yaml            # Render deployment configuration
├── .gitignore             # Git ignore file
├── README.md              # This file
├── static/
│   ├── css/
│   │   └── style.css      # Antigravity-inspired styles
│   ├── js/
│   │   └── script.js      # Interactive features
│   └── images/
│       ├── spicebazaar.png
│       └── filmcritichub.png
└── templates/
    ├── base.html          # Base template with nav & footer
    ├── index.html         # Homepage with all sections
    ├── 404.html           # 404 error page
    └── 500.html           # 500 error page
```

## 🎨 Design Features

### Color Palette
- **Primary Background**: `#0a0e27` (Deep Navy)
- **Secondary Background**: `#141b3d` (Dark Blue)
- **Gradients**: Purple to Pink (`#667eea` → `#764ba2`)
- **Accent Gradients**: Blue to Cyan (`#4facfe` → `#00f2fe`)

### Typography
- **Headings**: Space Grotesk (Bold, Modern)
- **Body**: Inter (Clean, Readable)

### Effects
- Glassmorphism with backdrop blur
- Gradient text and borders
- Smooth scroll animations
- Hover state transformations
- Parallax hero background

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
- **Phone**: 91+ 8281783716
- **Location**: Kochi, Kerala

## 📄 License

This project is open source and available for personal and educational use.

## 🙏 Acknowledgments

- Design inspiration: [Google Antigravity](https://antigravity.google/)
- Icons: [Font Awesome](https://fontawesome.com/)
- Fonts: [Google Fonts](https://fonts.google.com/)

---

**Built with ❤️ by Treesa Jose**
