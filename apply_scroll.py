import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('_')]

new_script = '''
<script>
  // Mobile Nav Toggle
  const mobToggle = document.getElementById('mob-nav-toggle');
  const mobNav = document.getElementById('mobile-nav');
  if(mobToggle && mobNav) {
    mobToggle.addEventListener('click', () => {
      mobNav.classList.toggle('hidden');
    });
  }
  const oldMobToggle = document.getElementById('mob-toggle');
  if(oldMobToggle && mobNav) {
    oldMobToggle.addEventListener('click', () => {
      mobNav.classList.toggle('hidden');
    });
  }

  // Smart Sticky Navbar (Hide on scroll down, show on scroll up)
  let lastScrollTop = 0;
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    navbar.style.transition = 'transform 0.3s ease-in-out';
    window.addEventListener('scroll', function() {
      let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      if (scrollTop > lastScrollTop && scrollTop > 80) {
        // Scroll Down
        navbar.style.transform = 'translateY(-100%)';
      } else {
        // Scroll Up
        navbar.style.transform = 'translateY(0)';
      }
      lastScrollTop = scrollTop;
    });
  }
</script>
</body>
'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove old scripts right before </body>
    pattern = r'<script>.*?mob-nav-toggle.*?</script>\s*</body>'
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, '</body>', content, flags=re.DOTALL)
    
    # Also clean up any generic trailing script if it exists
    pattern2 = r'<script>\s*document\.getElementById\(\'mob-nav-toggle\'\).*?</script>\s*</body>'
    if re.search(pattern2, content, flags=re.DOTALL):
        content = re.sub(pattern2, '</body>', content, flags=re.DOTALL)
        
    # Replace </body> with the new script
    content = content.replace('</body>', new_script)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
