# Personal Portfolio (Django)

A personal portfolio website built with Django, HTML, and CSS to showcase my background, projects, and skills. It includes Home, About, Projects, and Contact pages with a clean, responsive design.

## Run Locally

1. Install Python if needed.
2. Create and activate a virtual environment (recommended).
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open http://127.0.0.1:8000/ in your browser.

## Personalize It

- Replace placeholder text with your own information.
- Update the About page to reflect your interests and experience.
- Add links to your GitHub profile and projects.

## Contact Form

The contact form currently displays a demo confirmation and does not send emails. Email functionality can be added using Django's email settings and `send_mail()`.

## Deployment

Before deploying, configure a secure secret key, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and set up static files for production.
