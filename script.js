// Enhanced JavaScript effects and animations
(function () {
  // Smooth fade-in on scroll using IntersectionObserver
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1 }
  );

  document.querySelectorAll('.fade-in').forEach((el) => observer.observe(el));

  // Sticky navigation with scroll effect
  const nav = document.querySelector('.topnav');
  if (nav) {
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', () => {
      const currentScrollY = window.scrollY;
      
      if (currentScrollY > 50) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
      
      lastScrollY = currentScrollY;
    });
  }

  // Smooth scroll for internal links
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

  // Enhanced hover effects for skill cards with staggered animation
  document.querySelectorAll('.skill-card').forEach((card, index) => {
    // Staggered fade-in animation
    setTimeout(() => {
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    }, index * 150);

    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-6px) scale(1.03)';
      this.style.boxShadow = '0 15px 30px rgba(38,22,16,0.2)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0) scale(1)';
      this.style.boxShadow = '0 2px 8px rgba(38,22,16,0.08)';
    });
  });

  // Hero box animation
  const heroBox = document.querySelector('.hero-box');
  if (heroBox) {
    setTimeout(() => {
      heroBox.classList.add('visible');
    }, 500);
  }

  // Parallax effect for hero section
  const heroSection = document.querySelector('.hero-section');
  if (heroSection) {
    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      const rate = scrolled * -0.2;
      heroSection.style.transform = `translateY(${rate}px)`;
    });
  }

  // Enhanced project card animations
  document.querySelectorAll('.project-card').forEach((card, index) => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-6px) scale(1.03)';
      this.style.boxShadow = '0 15px 30px rgba(38,22,16,0.2)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0) scale(1)';
      this.style.boxShadow = '0 2px 8px rgba(38,22,16,0.08)';
    });
  });

  // Form validation enhancement
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    const inputs = form.querySelectorAll('input, textarea');
    inputs.forEach(input => {
      input.addEventListener('blur', function() {
        if (this.checkValidity()) {
          this.style.borderColor = '#261610';
          this.style.boxShadow = '0 0 0 3px rgba(38,22,16,0.15)';
        } else {
          this.style.borderColor = '#b91c1c';
          this.style.boxShadow = '0 0 0 3px rgba(185,28,28,0.15)';
        }
      });
    });
  });

  // Enhanced CTA button animations
  document.querySelectorAll('.cta-button').forEach(button => {
    button.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-2px) scale(1.05)';
    });
    
    button.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0) scale(1)';
    });
  });

  // Add loading animation for page transitions
  window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.8s ease';
    setTimeout(() => {
      document.body.style.opacity = '1';
    }, 100);
  });

  // Smooth scroll for anchor links
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

  // Thank you page special animation
  const checkmark = document.querySelector('.checkmark');
  if (checkmark) {
    setTimeout(() => {
      checkmark.style.opacity = '1';
    }, 500);
  }

  // Enhanced resume button animations
  document.querySelectorAll('.resume-btn').forEach(button => {
    button.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-3px) scale(1.05)';
    });
    
    button.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0) scale(1)';
    });

    // Add click animation
    button.addEventListener('click', function(e) {
      // Create ripple effect
      const ripple = document.createElement('span');
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size / 2;
      const y = e.clientY - rect.top - size / 2;
      
      ripple.style.width = ripple.style.height = size + 'px';
      ripple.style.left = x + 'px';
      ripple.style.top = y + 'px';
      ripple.classList.add('ripple');
      
      this.appendChild(ripple);
      
      setTimeout(() => {
        ripple.remove();
      }, 600);
    });
  });

  // Add ripple effect styles
  const style = document.createElement('style');
  style.textContent = `
    .resume-btn {
      position: relative;
      overflow: hidden;
    }
    
    .ripple {
      position: absolute;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.3);
      transform: scale(0);
      animation: ripple-animation 0.6s linear;
      pointer-events: none;
    }
    
    @keyframes ripple-animation {
      to {
        transform: scale(4);
        opacity: 0;
      }
    }
  `;
  document.head.appendChild(style);
})();


