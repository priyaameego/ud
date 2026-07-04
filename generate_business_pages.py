import os
import re

items = [
    # Column 1
    "Partnership",
    "Nidhi Company",
    "Proprietorship",
    "Producer Company",
    "MCA Name Approval",
    
    # Column 2
    "Section 8 Company",
    "One Person Company",
    "Trust Registration",
    "Private Limited Company",
    "Proprietor to LLP",
    
    # Column 3
    "Partnership to LLP",
    "Proprietor to Pvt Ltd",
    "Partnership to Pvt Ltd",
    "Proprietor to OPC",
    "Limited Liability Partnership"
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
    .hero-overlay.sky {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to right, rgba(12, 74, 110, 0.95), rgba(2, 132, 199, 0.8));
      z-index: 1;
    }}
  </style>
</head>
<body class="bg-gray-50 text-gray-800">

<!-- Placeholder for dynamically injected header -->

<!-- HERO SECTION -->
<section class="hero-bg min-h-[55vh] flex items-center pt-32 pb-20 relative" id="hero">
  <div class="hero-overlay sky"></div>
  
  <div class="max-w-7xl mx-auto px-4 relative z-10 w-full text-center">
    <div class="gsap-reveal inline-flex items-center gap-2 bg-sky-900/30 border border-sky-400/20 rounded-full px-5 py-2 mb-8 backdrop-blur-md">
      <div class="w-2 h-2 bg-sky-400 rounded-full animate-ping"></div>
      <span class="text-xs font-bold tracking-widest text-sky-200 uppercase">BUSINESS REGISTRATION</span>
    </div>
    
    <h1 class="gsap-reveal text-5xl md:text-7xl font-black leading-tight mb-6 tracking-tighter max-w-5xl mx-auto text-white">
      <span class="bg-gradient-to-r from-sky-200 to-sky-400 bg-clip-text text-transparent">{title}</span>
    </h1>
    
    <p class="gsap-reveal text-xl text-sky-50/90 mb-0 leading-relaxed max-w-3xl mx-auto font-light">
      Start your entrepreneurial journey with our seamless and entirely online {title} services.
    </p>
  </div>
</section>

<!-- CONTENT SECTION -->
<section class="py-24 bg-white relative">
  <div class="max-w-7xl mx-auto px-4">
    
    <div class="grid lg:grid-cols-2 gap-16 items-center mb-24">
      <div class="gsap-reveal-left">
        <h2 class="text-4xl font-black text-[#0f172a] mb-6">Incorporate with Confidence</h2>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          Choosing the right business structure is the first critical step toward success. We make {title} quick, transparent, and completely hassle-free.
        </p>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          Our team of chartered accountants and corporate lawyers handle everything—from digital signatures to MCA approvals—so you can focus entirely on building your business.
        </p>
        <ul class="space-y-4 mt-8">
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-sky-600 text-xl"></i> 100% Online & Paperless Process</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-sky-600 text-xl"></i> Complete Post-Incorporation Support</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-sky-600 text-xl"></i> No Hidden Fees or Surprises</li>
        </ul>
      </div>
      <div class="gsap-reveal-right">
        <div class="bg-sky-50 p-10 rounded-[2rem] border border-sky-100 shadow-xl relative overflow-hidden text-center flex flex-col items-center justify-center h-full min-h-[400px]">
          <div class="absolute top-0 right-0 w-64 h-64 bg-sky-200 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/4"></div>
          <div class="w-24 h-24 bg-sky-100 rounded-2xl flex items-center justify-center text-sky-600 text-5xl mb-8 relative z-10 shadow-inner">
            <i class="fas fa-building"></i>
          </div>
          <h3 class="text-3xl font-bold text-[#0c4a6e] mb-4 relative z-10">Your Dream, Registered.</h3>
          <p class="text-gray-600 relative z-10 text-lg">Launch your company today with our expert guidance and lightning-fast registration.</p>
        </div>
      </div>
    </div>
    
    <div class="text-center mt-12 gsap-reveal">
      <h3 class="text-3xl font-black text-[#0f172a] mb-6">Ready to Register Your {title}?</h3>
      <p class="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">Get in touch with our business setup experts today and turn your idea into a legal entity.</p>
      <a href="contact.html" class="inline-block px-10 py-5 bg-[#0284c7] text-white font-black text-xl rounded-2xl hover:bg-sky-700 transition-all transform hover:scale-105 shadow-2xl shadow-sky-900/30">
        Start Incorporation Now
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

print("All 15 pages generated.")
