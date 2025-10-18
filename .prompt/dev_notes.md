# AI Development Notes (.prompt/dev_notes.md)

This file documents prompts used with an AI assistant while building and refactoring the site. Each entry includes: the prompt, the AI output, and whether I accepted, modified, or rejected it. A single reflection summarizing the whole effort follows at the end.

---

## Prompt 1: Make the navigation bar sticky on scroll

- Prompt
  "I have a navigation bar at the top of my site with the class `topnav`. How can I make it stick to the top of the screen when the user scrolls down the page?"

- AI Output
  CSS:
  ```css
  .topnav { position: sticky; top: 0; z-index: 100; }
  ```
  JavaScript:
  ```javascript
  const nav = document.querySelector('.topnav');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) { nav.classList.add('scrolled'); }
    else { nav.classList.remove('scrolled'); }
  });
  ```

- Decision
  Accepted. Used both CSS and JS for a subtle shadow effect after scrolling begins.

---

## Prompt 2: Hover lift and shadow for skill cards

- Prompt
  "I want my skill cards to lift up slightly and show a stronger shadow on hover. Can you provide the CSS?"

- AI Output
  ```css
  .skill-card { transition: transform 300ms ease, box-shadow 300ms ease; }
  .skill-card:hover { transform: translateY(-6px) scale(1.03); box-shadow: 0 18px 36px rgba(38,22,16,0.22); }
  ```

- Decision
  Accepted. Dropped straight into my stylesheet; matched the site’s motion feel.

---

## Prompt 3: Smooth scrolling for in‑page anchor links

- Prompt
  "When I click a link to an in‑page section, it jumps instantly. How do I make it scroll smoothly?"

- AI Output
  JavaScript approach:
  ```javascript
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      const t = document.querySelector(a.getAttribute('href'));
      if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
  ```
  Alt CSS:
  ```css
  html { scroll-behavior: smooth; }
  ```

- Decision
  Modified. Used the CSS property for same‑page sections; kept normal links between pages.

---

## Prompt 4: Convert static site to Flask (templates + static)

- Prompt
  "Convert my personal website to Flask with an `app.py`, routes for each page, a `templates/` folder using a shared base layout, and a `static/` folder for css/js/images. Keep styling and JS behavior."

- AI Output
  - Scaffolded `app.py` with routes: `/`, `/about`, `/resume`, `/projects`, `/contact`, `/thankyou`.
  - Created `templates/base.html` and migrated each page to a template extending it.
  - Moved assets into `static/css`, `static/js`, `static/images`, and resume PDF to `static/docs/`.
  - Updated links to use `url_for(...)`; wired contact form to `/thankyou`.

- Decision
  Accepted with small edits (fixed a closing tag, normalized text, and improved the footer © symbol). Verified parity, then deleted legacy root HTML files.

---

## Prompt 5: Add SQLite DAL and make Projects page DB‑driven

- Prompt
  "Add a simple SQLite data access layer (DAL.py) with functions to init the DB, insert rows, and fetch all projects. Convert the Projects page to read from the database instead of hardcoded HTML. Seed two baseline projects so they always appear."

- AI Output
  - Created `DAL.py` with `init_db()`, `get_all_projects()`, and `insert_project(...)` using `sqlite3`.
  - Added `ensure_baseline_projects()` to guarantee two baseline entries.
  - Updated `app.py` to call `init_db()` and `ensure_baseline_projects()` on startup; modified `/projects` route to pass `projects` into the template.
  - Replaced static markup in `templates/projects.html` with a table that loops over DB rows.

- Decision
  Accepted. Migrated content to the database while preserving my two original projects.

---

## Prompt 6: Add form to insert projects with image upload to static/images

- Prompt
  "Add a page to submit new projects (Title, Description, and an image). Upload should save files to `static/images/` safely and store the filename in the DB."

- AI Output
  - Added upload handling to `app.py` with `secure_filename`, `UPLOAD_FOLDER`, allowed extensions, 10MB limit, and collision‑safe naming.
  - Created `templates/add_project.html` with a multipart form and a file input.
  - On success, inserts the new row and redirects to `/projects`.

- Decision
  Accepted. Works well and keeps images organized in `static/images/`.

---

## Prompt 7: Restore Contact page and separate Add Project route

- Prompt
  "Restore the original `/contact` page that submits to `/thankyou` (GET). Move the add‑project form to `/add-project` so both exist. Update navigation accordingly."

- AI Output
  - Restored `templates/contact.html` to the original contact form.
  - Added `/add-project` route with upload logic and created `templates/add_project.html`.
  - Updated `templates/base.html` nav to include both Contact and Add Project.

- Decision
  Accepted. Satisfies course requirements and keeps project submission separate.

---

## Prompt 8: Improve Projects page visuals (bigger images, styled table)

- Prompt
  "Make the Projects page images larger and style the table to match the site theme, with mobile‑friendly layout."

- AI Output
  - Added CSS classes `.projects-table`, `.project-thumb`, `.projects-intro` in `static/css/style.css`.
  - Updated `templates/projects.html` to use the classes and remove inline image sizing.
  - Included responsive rules to stack rows on small screens.

- Decision
  Accepted. The page looks cleaner and images are large enough to preview.

---

## Prompt 9: Maintenance helpers (delete latest test project, clean orphan images)

- Prompt
  "Add a small helper to delete the most recent non‑baseline project and an optional script to remove unreferenced images from `static/images/`."

- AI Output
  - Added `DAL.delete_latest_project(exclude_titles=...)` and scripts: `scripts/delete_latest.py`, `scripts/delete_latest_and_image.py`, and `scripts/cleanup_images.py`.
  - Cleanup script keeps baseline and any in‑use files; deletes only orphans.

- Decision
  Accepted with caution. Used it for test cleanup; ensured existing site images remained intact.

---

## Reflection (≈170+ words)

AI assistance noticeably accelerated both design polish and structural changes. For UI work (sticky nav, hover motion, smooth scrolling), the AI provided succinct, high‑quality snippets that matched the site’s tone, reducing time spent on research and trial‑and‑error. The bigger lift—migrating from static pages to a Flask app—also benefited: a clean scaffold with routes, template inheritance, and `url_for` conventions let me focus on content parity, accessibility, and consistent styling.

Introducing a SQLite DAL and converting the Projects page to be data‑driven improved maintainability: projects now live in a database, two baseline items are ensured at startup, and new projects appear instantly. Adding an upload workflow made images self‑contained within `static/images/`, with safe filenames and size/type checks. Separating the restored Contact page from the new Add Project route kept course requirements intact while clarifying intent. I also added simple maintenance helpers to remove test entries and orphan images when appropriate.

There were a few lessons: be careful with file cleanup (protect known assets and verify references), and expect small integration edits (encoding and template fixes). Overall, the AI handled common “how” patterns quickly; I kept ownership of the “what” and “why,” ensuring the final result is cohesive, stable, and easy to extend.

