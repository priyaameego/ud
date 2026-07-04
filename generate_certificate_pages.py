import os
import re

items = [
    # Column 1
    "Fire Licence",
    "PF Registration",
    "PT Registration",
    "GeM Registration",
    "GST Registration",
    "ISO Registration",
    "ZED Certification",
    "BIS Registration",
    
    # Column 2
    "DSC Registration",
    "ESI Registration",
    "RERA Registration",
    "Udyam Registration",
    "FCRA Registration",
    "Food Registration",
    "Darpan Registration",
    "Barcode Registration",
    
    # Column 3
    "Gumasta Registration",
    "ICEGATE Registration",
    "Only 80G Registration",
    "Only 12A Registration",
    "12A and 80G Registration",
    "ImportExport Registration",
    "Tax Exemption Certificate",
    "Startup India Registration"
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} | Udyog Suvidha Kendra</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
  
  <!-- FontAwesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
  
  <!-- GSAP & Lenis for Smooth Animations -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="https://unpkg.com/@studio-freight/lenis@1.0.33/dist/lenis.min.js"></script>

  <style>
    * {{ font-family: 'Inter', sans-serif; }}
    
    html.lenis {{ height: auto; }}
    .lenis.lenis-smooth {{ scroll-behavior: auto !important; }}
    
    .hero-bg {{
      background-image: url('overview_hero_bg.png');
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
      position: relative;
    }}
    .hero-overlay.amber {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to right, rgba(120, 53, 15, 0.95), rgba(217, 119, 6, 0.8));
      z-index: 1;
    }}
  </style>
</head>
<body class="bg-gray-50 text-gray-800">

<!-- Placeholder for dynamically injected header -->

<!-- HERO SECTION -->
<section class="hero-bg min-h-[55vh] flex items-center pt-32 pb-20 relative" id="hero">
  <div class="hero-overlay amber"></div>
  
  <div class="max-w-7xl mx-auto px-4 relative z-10 w-full text-center">
    <div class="gsap-reveal inline-flex items-center gap-2 bg-amber-900/30 border border-amber-400/20 rounded-full px-5 py-2 mb-8 backdrop-blur-md">
      <div class="w-2 h-2 bg-amber-400 rounded-full animate-ping"></div>
      <span class="text-xs font-bold tracking-widest text-amber-200 uppercase">LICENSES & REGISTRATIONS</span>
    </div>
    
    <h1 class="gsap-reveal text-5xl md:text-7xl font-black leading-tight mb-6 tracking-tighter max-w-5xl mx-auto text-white">
      <span class="bg-gradient-to-r from-amber-200 to-amber-400 bg-clip-text text-transparent">{title}</span>
    </h1>
    
    <p class="gsap-reveal text-xl text-amber-50/90 mb-0 leading-relaxed max-w-3xl mx-auto font-light">
      Fast and hassle-free processing for {title} to ensure your business is fully authorized and recognized.
    </p>
  </div>
</section>

<!-- CONTENT SECTION -->
<section class="py-24 bg-white relative">
  <div class="max-w-7xl mx-auto px-4">
    
    <div class="grid lg:grid-cols-2 gap-16 items-center mb-24">
      <div class="gsap-reveal-left">
        <h2 class="text-4xl font-black text-[#0f172a] mb-6">Secure Your {title}</h2>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          Acquiring the right licenses and registrations is crucial for legally operating your business in India. We simplify the entire process for your {title}.
        </p>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          From gathering the right documents to submitting applications and following up with authorities, our experts ensure a smooth and swift registration process.
        </p>
        <ul class="space-y-4 mt-8">
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-amber-600 text-xl"></i> Hassle-Free Document Preparation</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-amber-600 text-xl"></i> Quick Processing & Liaisoning</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-amber-600 text-xl"></i> Complete End-to-End Support</li>
        </ul>
      </div>
      <div class="gsap-reveal-right">
        <div class="bg-amber-50 p-10 rounded-[2rem] border border-amber-100 shadow-xl relative overflow-hidden text-center flex flex-col items-center justify-center h-full min-h-[400px]">
          <div class="absolute top-0 right-0 w-64 h-64 bg-amber-200 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/4"></div>
          <div class="w-24 h-24 bg-amber-100 rounded-2xl flex items-center justify-center text-amber-600 text-5xl mb-8 relative z-10 shadow-inner">
            <i class="fas fa-certificate"></i>
          </div>
          <h3 class="text-3xl font-bold text-[#78350f] mb-4 relative z-10">Get Authorized Quickly</h3>
          <p class="text-gray-600 relative z-10 text-lg">Don't let red tape slow you down. We get your certificates ready in record time.</p>
        </div>
      </div>
    </div>
    
    <div class="text-center mt-12 gsap-reveal">
      <h3 class="text-3xl font-black text-[#0f172a] mb-6">Need Your {title} Fast?</h3>
      <p class="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">Get in touch with our licensing experts today and start the process immediately.</p>
      <a href="contact.html" class="inline-block px-10 py-5 bg-[#d97706] text-white font-black text-xl rounded-2xl hover:bg-amber-700 transition-all transform hover:scale-105 shadow-2xl shadow-amber-900/30">
        Apply Now
      </a>
    </div>

  </div>
</section>

<!-- Placeholder for dynamically injected footer -->

<script>
  // Initialize Lenis Smooth Scrolling
  const lenis = new Lenis({{
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smooth: true,
  }});

  function raf(time) {{
    lenis.raf(time);
    requestAnimationFrame(raf);
  }}
  requestAnimationFrame(raf);

  // GSAP Animations
  gsap.registerPlugin(ScrollTrigger);

  // General Reveal
  gsap.utils.toArray('.gsap-reveal').forEach(el => {{
    gsap.fromTo(el, 
      {{ y: 50, opacity: 0 }},
      {{ y: 0, opacity: 1, duration: 1, ease: "power3.out", scrollTrigger: {{ trigger: el, start: "top 85%" }} }}
    );
  }});
  
  gsap.fromTo('.gsap-reveal-left', 
    {{ x: -50, opacity: 0 }},
    {{ x: 0, opacity: 1, duration: 1, ease: "power3.out", scrollTrigger: {{ trigger: '.gsap-reveal-left', start: "top 85%" }} }}
  );

  gsap.fromTo('.gsap-reveal-right', 
    {{ x: 50, opacity: 0 }},
    {{ x: 0, opacity: 1, duration: 1, ease: "power3.out", scrollTrigger: {{ trigger: '.gsap-reveal-right', start: "top 85%" }} }}
  );
</script>

</body>
</html>
"""

def slugify(text):
    text = text.lower()
    text = text.replace('(', '').replace(')', '').replace('&', 'and')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

for item in items:
    filename = slugify(item) + ".html"
    html_content = template.format(title=item)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
        print(f"Created {filename}")

print("All 24 pages generated.")
