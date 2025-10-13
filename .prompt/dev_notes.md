# AI Development Notes (.prompt/dev_notes.md)

This file documents prompts used with an AI assistant while building and refactoring the site. Each entry includes: the prompt, the AI output, and whether I accepted, modified, or rejected it. A 150+ word reflection follows at the end.

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

## Reflection (≈170 words)

AI assistance accelerated my workflow significantly. For UI polish like sticky nav behavior, hover effects, and subtle motion, the AI provided clean snippets that looked good immediately. This saved time I would have spent tuning values and researching patterns. During the Flask migration, the AI produced a solid scaffold—routes, base layout, and `url_for` usage—which let me focus on ensuring parity and organizing assets correctly.

AI also made small mistakes and omissions. Some text contained encoding glitches, and one closing tag was malformed in the generated template. The smooth‑scroll script initially assumed a single‑page setup, which didn’t fit my multi‑page structure. These issues were minor but reminded me to verify integration details and semantics.

I balanced AI help with deliberate review and targeted edits. I accepted boilerplate and common patterns to move quickly, but I validated accessibility, link paths, and template inheritance myself. In short, AI handled the “how” for standard solutions, while I kept ownership of the “what” and “why,” ensuring the code matched my design goals and worked coherently across pages.

