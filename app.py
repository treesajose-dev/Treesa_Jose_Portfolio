from flask import Flask, render_template
import os

app = Flask(__name__)

# Configuration
# Compatible with PythonAnywhere - SECRET_KEY can be overridden via environment variable
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

@app.route('/')
def index():
    """Render the portfolio homepage"""
    portfolio_data = {
        'name': 'TREESA JOSE',
        'tagline': 'MCA Student | Aspiring Software Developer | Python & AI/ML Enthusiast',
        'email': 'treesajosemadathil@yahoo.com',
        'location': 'Kochi, Kerala',
        'linkedin': 'linkedin.com/in/treesajose-dev',
        'github': 'github.com/treesajose-dev',
        'about': 'Postgraduate MCA student passionate about building practical tech solutions using Python Flask, AI/ML, and web development. Skilled in hands-on projects, exploring new tools, and applying knowledge to real-world applications. Spiritual, grounded, and committed to continuous learning, open to internships, collaborations, and innovative opportunities.',
        'education': [
            {
                'degree': 'Master of Computer Applications',
                'institution': 'Rajagiri College of Social Sciences',
                'period': '2025–27',
                'status': 'Pursuing'
            },
            {
                'degree': 'Bachelor of Computer Applications',
                'institution': 'Rajagiri College of Management and Applied Sciences',
                'period': '2022–25',
                'status': 'Completed'
            },
            {
                'degree': 'CBSE 12th Standard',
                'institution': 'Sacred Heart CMI Public School',
                'period': '2022',
                'status': '96.2%'
            }
        ],
        'projects': [
            {
                'name': 'SpiceBazaar',
                'subtitle': 'Online Spices Store',
                'description': 'Created an e-commerce platform with product categories, search, cart, order processing, courier tracking, and management modules ensuring scalability and smooth operations.',
                'tech_stack': ['HTML', 'CSS', 'Python Flask', 'MySQL'],
                'github': 'https://github.com/treesajose-dev/Spice-Bazaar-Online-Spices-Store',
                'image': 'spicebazaar.png'
            },
            {
                'name': 'FilmCriticHub',
                'subtitle': 'Online Film Review System',
                'description': 'Developed a feature-rich movie review platform with user accounts, ratings, likes/dislikes, personalized watchlists, and recommendation features for enhanced movie discovery.',
                'tech_stack': ['HTML', 'CSS', 'JavaScript', 'PHP', 'MySQL'],
                'github': 'https://github.com/treesajose-dev/FilmCriticHub-Online-Film-Review-System',
                'image': 'filmcritichub.png'
            }
        ],
        'skills': {
            'Programming': ['Python', 'PHP', 'C', 'C++', 'JavaScript'],
            'Web': ['HTML5', 'CSS3', 'Bootstrap 5', 'JavaScript'],
            'Databases': ['MySQL', 'Oracle (SQL*Plus)', 'MS Access'],
            'Tools': ['VSCode', 'Android Studio', 'XAMPP'],
            'Version Control': ['Git', 'GitHub'],
            'Languages': ['English', 'Malayalam', 'Hindi']
        },
        'achievements': [
            {
                'title': 'Research Paper Presentation',
                'description': 'Presented "Beyond the Black Box: Comparing AI and XAI" at ICAET 2025',
                'year': '2025'
            },
            {
                'title': 'Generative AI Workshop',
                'description': '2-day workshop by GP3 Cloud Innovations',
                'year': '2025'
            },
            {
                'title': 'Advanced Python for Data Analytics',
                'description': 'Certification in Python data analytics',
                'year': '2024'
            },
            {
                'title': 'Microsoft Office Specialist',
                'description': 'Excel 2019 Associate Certification',
                'year': 'Feb 2024'
            },
            {
                'title': '75 AI Tools Workshop',
                'description': 'Workshop by Lore & ED',
                'year': 'Oct 2023'
            }
        ]
    }
    return render_template('index.html', data=portfolio_data)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Use environment variable for port (Render compatibility)
    port = int(os.environ.get('PORT', 5000))
    # Debug mode off in production
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
