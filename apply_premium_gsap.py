import os
import re

css_to_add = """
    :root {
      --primary: #1a237e;
      --primary-light: #283593;
      --secondary: #84cc16;
    }
    .page-transition { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background-color: var(--primary); z-index: 99999; display: flex; justify-content: center; align-items: center; pointer-events: none; }
    #scroll-progress { position: fixed; top: 0; left: 0; width: 0%; height: 4px; background: linear-gradient(90deg, var(--secondary), var(--primary-light)); z-index: 99998; box-shadow: 0 0 10px rgba(132, 204, 22, 0.5); }
    #back-to-top { position: fixed; bottom: -60px; right: 30px; width: 50px; height: 50px; border-radius: 50%; background: var(--primary); color: white; display: flex; justify-content: center; align-items: center; cursor: pointer; z-index: 99990; box-shadow: 0 10px 25px rgba(26, 35, 126, 0.4); transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
    #back-to-top:hover { transform: translateY(-5px); background: var(--primary-light); }
    .gsap-reveal { opacity: 0; transform: translateY(50px); }
"""

dom_to_add = """
<!-- Page Transition overlay -->
<div class="page-transition">
  <div class="w-12 h-12 border-4 border-white border-t-transparent rounded-full animate-spin"></div>
</div>
<div id="scroll-progress"></div>
<!-- Back to top -->
<div id="back-to-top" class="magnetic-btn-wrap">
  <i class="fas fa-arrow-up"></i>
</div>
"""

js_to_add = """
<script>
  if (typeof lenis === 'undefined') {
    window.lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smooth: true,
    });
    function raf(time) {
      window.lenis.raf(time);
      if (typeof ScrollTrigger !== 'undefined') ScrollTrigger.update();
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
  }

  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    window.addEventListener('load', () => {
      const tl = gsap.timeline();
      tl.to('.page-transition', {
        opacity: 0, duration: 0.8, ease: "power2.inOut", onComplete: () => {
          const pt = document.querySelector('.page-transition');
          if (pt) pt.style.display = 'none';
        }
      });
    });

    gsap.to('#scroll-progress', {
      width: '100%',
      ease: 'none',
      scrollTrigger: {
        trigger: document.body,
        start: 'top top',
        end: 'bottom bottom',
        scrub: 0.3
      }
    });

    const bttBtn = document.getElementById('back-to-top');
    if (bttBtn) {
      window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
          gsap.to(bttBtn, { bottom: 30, duration: 0.5, ease: "back.out(1.5)", overwrite: "auto" });
        } else {
          gsap.to(bttBtn, { bottom: -60, duration: 0.5, ease: "power2.in", overwrite: "auto" });
        }
      });
      bttBtn.addEventListener('click', () => {
        window.lenis.scrollTo(0, { duration: 1.5, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
      });
    }

    const revealElements = document.querySelectorAll('.gsap-reveal, .reveal-up, .reveal-scale');
    revealElements.forEach(el => {
      gsap.to(el, {
        y: 0, scale: 1, opacity: 1, duration: 1, ease: "power3.out",
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: "play none none reverse"
        }
      });
    });
  }
</script>
"""

skip_files = ['events.html', 'products.html', 'blogs.html']

for f in os.listdir('.'):
    if f.endswith('.html') and not f.startswith('_') and f not in skip_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if already applied
        if 'page-transition' in content and 'scroll-progress' in content:
            print(f"Skipping {f}, already applied.")
            continue

        # Inject CSS
        if '</style>' in content:
            content = content.replace('</style>', css_to_add + '\n  </style>')
        else:
            content = content.replace('</head>', '<style>' + css_to_add + '</style>\n</head>')

        # Inject DOM
        body_pattern = r'(<body.*?>)'
        content = re.sub(body_pattern, r'\1\n' + dom_to_add, content, count=1)

        # Inject JS - Replace existing lenis logic if present to avoid conflicts, or just append before </body>
        # Actually appending before </body> is safest, and I used `if (typeof lenis === 'undefined')` so it won't crash if duplicated.
        # But old raf might run twice. Let's just append and it's mostly fine, or we can strip old lenis init.
        # Stripping old lenis init:
        content = re.sub(r'const lenis = new Lenis\(\{.*?requestAnimationFrame\(raf\);', '', content, flags=re.DOTALL)
        
        content = content.replace('</body>', js_to_add + '\n</body>')

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Applied premium GSAP scaffolding to {f}")
