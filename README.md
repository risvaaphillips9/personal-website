# Personal Website (Flask)

This repository contains my personal website refactored from static HTML into a small Flask application.

## Project Structure 

- `app.py` – Flask app with routes for all pages 
- `templates/` – Jinja templates 
  - `base.html` (shared head/nav/footer) 
  - `index.html`, `about.html`, `resume.html`, `projects.html` (DB‑driven), `contact.html` (contact form → `/thankyou`), `add_project.html` (Add Project form), `thankyou.html` 
- `static/` – Static assets served by Flask 
  - `css/style.css` 
  - `js/script.js` 
  - `images/` (site images) 
  - `docs/Phillips_Risvaa_Resume.pdf` 
- `.prompt/dev_notes.md` – AI prompts + development notes (required course format) 
- `DAL.py` – SQLite data access layer (creates `projects.db`, provides read/insert/ensure‑baseline) 
- `projects.db` – SQLite database (auto-created on first run) 
- `scripts/` – maintenance helpers
  - `scripts/delete_latest.py` – deletes most recent non‑baseline project
  - `scripts/cleanup_images.py` – removes unreferenced images from `static/images/`

## Run Locally

1. Create and activate a virtual environment:
   - Windows (PowerShell):
     - `python -m venv .venv`
     - `./.venv/Scripts/Activate.ps1`
   - macOS/Linux (bash/zsh):
     - `python3 -m venv .venv`
     - `source .venv/bin/activate`
2. Install dependencies: 
   - `pip install -r requirements.txt` 
3. Start the development server (initializes `projects.db` automatically): 
   - `python app.py` 
4. Open the site: 
   - http://127.0.0.1:5000 

To deactivate the environment later, run `deactivate`. 

## Development Notes

- Navigation links use `url_for(...)` to generate URLs and set the active state.
- All assets are loaded via `url_for('static', filename=...)`.
- The Contact page remains and submits to `/thankyou` via GET (course requirement).
- The Add Project page lives at `/add-project` and inserts into the database (image upload required).
- Legacy root HTML files were removed in favor of templates under `templates/`. 

## Database-backed Projects

- The Projects page loads from a SQLite DB (`projects.db`). Baseline projects are ensured at startup and always present.
- Add Project (`/add-project`) inserts Title, Description, and an uploaded image; the image is saved to `static/images/`.
- Allowed image types: png, jpg, jpeg, gif, webp. Max size: 10 MB. Filename collisions are auto‑resolved with a numeric suffix.
- Newly added projects appear immediately on the Projects page.

## Admin Helpers (optional)

- Delete latest non‑baseline project: `python scripts/delete_latest.py`
- Remove unreferenced images (keeps baseline and in‑use files): `python scripts/cleanup_images.py`

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
