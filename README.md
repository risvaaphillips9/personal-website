# Personal Website (Flask)

This repository contains my personal website refactored from static HTML into a small Flask application.

## Project Structure

- `app.py` — Flask app with routes for all pages
- `templates/` — Jinja templates
  - `base.html` (shared head/nav/footer)
  - `index.html`, `about.html`, `resume.html`, `projects.html`, `contact.html`, `thankyou.html`
- `static/` — Static assets served by Flask
  - `css/style.css`
  - `js/script.js`
  - `images/` (site images)
  - `docs/Phillips_Risvaa_Resume.pdf`
- `.prompt/dev_notes.md` — AI prompts + development notes (required course format)

## Run Locally

1. Install dependencies:
   - `pip install -r requirements.txt`
2. Start the development server:
   - `python app.py`
3. Open the site:
   - http://127.0.0.1:5000

## Development Notes

- Navigation links use `url_for(...)` to generate URLs and set the active state.
- All assets are loaded via `url_for('static', filename=...)`.
- The contact form submits with GET to `/thankyou` and renders submitted fields if present.
- Legacy root HTML files were removed in favor of templates under `templates/`.

## Add a New Page

1. Create a template in `templates/`, e.g. `faq.html` and extend `base.html`.
2. Add a route in `app.py`:
   ```python
   @app.route('/faq')
   def faq():
       return render_template('faq.html')
   ```
3. Add a nav link in `templates/base.html` (optional) using `url_for('faq')`.

## License

No license specified. All rights reserved.
