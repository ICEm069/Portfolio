# Personal Portfolio (Django)

A minimal Django portfolio with Home, About, and Contact pages. The styling uses a muted charcoal/forest palette and a scenic homepage background.

## Run locally

1. Install Python if needed.
2. In this folder, create and activate a virtual environment (optional but recommended).
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the site:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Open http://127.0.0.1:8000/

## Personalize it

Search the project for:
- `YOUR FULL NAME` and replace it with your full name.
- `YOUR-GITHUB-USERNAME` and replace it with your GitHub username.

Update the About page text to match your real interests and experience.

## Contact form note

The contact form currently validates required fields and shows a demo confirmation. It does **not** send email yet. Configure Django email settings and use `send_mail()` in `pages/views.py` when you are ready to receive messages.

Before deployment, set `DEBUG = False`, use a secure secret key from an environment variable, and configure `ALLOWED_HOSTS`.
