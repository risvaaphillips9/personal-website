# AI Prompts & Development Notes

This file logs some of the prompts I used with an AI assistant while building my personal portfolio for the AIDD course. It's a candid look at where AI was a huge help and where I still had to do the heavy lifting.

---

## Prompt Log

### Prompt 1: Making the Navigation Bar Sticky

* **My Prompt:** "I have a navigation bar at the top of my site with the class `topnav`. How can I make it stick to the top of the screen when the user scrolls down the page?"

* **AI Output:**
    ```css
    .topnav {
      position: sticky;
      top: 0;
      z-index: 100;
    }
    ```
    ```javascript
    const nav = document.querySelector('.topnav');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    });
    ```

* **My Notes:** **Accepted.** This was perfect. I was only expecting the CSS part (`position: sticky`), but the AI also gave me the JavaScript to add a `scrolled` class. This was a great suggestion because it allowed me to add a subtle shadow effect to the navigation bar only after the user starts scrolling, which is a nice, professional touch you see on many websites. I used this code directly in my `script.js` and `styles.css` files.

### Prompt 2: Animating Skill Cards on Hover

* **My Prompt:** "I want my skill cards to have a cool hover effect. Can you make them lift up and get a bigger shadow when you put the mouse over them?"

* **AI Output:**
    ```css
    .skill-card {
      transition: transform 300ms ease, box-shadow 300ms ease;
    }

    .skill-card:hover {
      transform: translateY(-6px) scale(1.03);
      box-shadow: 0 18px 36px rgba(38,22,16,0.22);
    }
    ```

* **My Notes:** **Accepted.** This was a huge time-saver. I could have spent a while fiddling with `transform` properties and `box-shadow` values to get the right feel. The AI gave me a snippet that worked immediately and looked great. The combination of moving the card up (`translateY`) and scaling it slightly (`scale`) gave it a satisfying, almost 3D feel. It was exactly what I had in mind.

### Prompt 3: Making Links Scroll Smoothly to Sections

* **My Prompt:** "When I click a link in my navigation bar, like 'Projects', it just jumps down the page instantly. How do I make it scroll down smoothly instead of jumping?"

* **AI Output:**
    ```javascript
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
    ```

* **My Notes:** **Modified.** The AI gave me two ways to do this: a simple CSS property (`scroll-behavior: smooth;`) and this more robust JavaScript solution. The JavaScript code was great because it gave me more control, but it didn't account for the navigation links in my `projects.html` file that needed to link back to sections on my `index.html` page. I ended up using the simple CSS `scroll-behavior: smooth;` on the `html` element for on-page scrolling and kept my regular links for navigating between pages. The AI's answer taught me both methods, and I chose the one that best fit my site's structure.

---

## Reflection

Using an AI assistant for this project was incredibly helpful, especially for saving time on CSS styling and common JavaScript effects. For tasks like creating the sticky navigation or the hover animations for cards, the AI provided clean, efficient code in seconds. This let me bypass a lot of tedious trial-and-error and focus more on the overall design and structure of my site. It was like having a senior developer I could ask for quick snippets.

The main place AI fell short was in understanding the full context of my project. For example, when I asked for smooth scrolling, it provided a script that worked perfectly for a single-page site but didn't consider my multi-page structure. I had to realize this limitation and adapt the solution myself.

Ultimately, I found a good balance by using the AI as a tool for acceleration, not a replacement for my own thinking. I would prompt it for specific, isolated features, but I always took the time to understand the code it provided. I was responsible for debugging, modifying, and ensuring its output integrated cleanly with the rest of my project. It handled the "how" for common patterns, which freed me up to focus on the "what" and "why" of my design choices.