import os
import re

items = [
    # Column 1
    "Composition Return",
    "GST Cancellation",
    "GST Return Filing",
    "GST Nil Return",
    "ITR-1 (Only Salary)",
    "ITR-2 (Salary & Other)",
    
    # Column 2
    "ITR-3 Return Filing",
    "ITR-4 Return Filing",
    "ITR-5 Return Filing",
    "ITR-6 Return Filing",
    "ITR-7 Return Filing"
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
    .hero-overlay.indigo {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to right, rgba(30, 27, 75, 0.95), rgba(79, 70, 229, 0.7));
      z-index: 1;
    }}
  </style>
</head>
<body class="bg-gray-50 text-gray-800">

<!-- Placeholder for dynamically injected header -->

<!-- HERO SECTION -->
<section class="hero-bg min-h-[55vh] flex items-center pt-32 pb-20 relative" id="hero">
  <div class="hero-overlay indigo"></div>
  
  <div class="max-w-7xl mx-auto px-4 relative z-10 w-full text-center">
    <div class="gsap-reveal inline-flex items-center gap-2 bg-indigo-900/30 border border-indigo-400/20 rounded-full px-5 py-2 mb-8 backdrop-blur-md">
      <div class="w-2 h-2 bg-indigo-400 rounded-full animate-ping"></div>
      <span class="text-xs font-bold tracking-widest text-indigo-200 uppercase">TAXATION & COMPLIANCE</span>
    </div>
    
    <h1 class="gsap-reveal text-5xl md:text-7xl font-black leading-tight mb-6 tracking-tighter max-w-5xl mx-auto text-white">
      <span class="bg-gradient-to-r from-indigo-200 to-indigo-400 bg-clip-text text-transparent">{title}</span>
    </h1>
    
    <p class="gsap-reveal text-xl text-indigo-50/90 mb-0 leading-relaxed max-w-3xl mx-auto font-light">
      Expert assistance for {title} to ensure 100% compliance with government regulations and avoid heavy penalties.
    </p>
  </div>
</section>

<!-- CONTENT SECTION -->
<section class="py-24 bg-white relative">
  <div class="max-w-7xl mx-auto px-4">
    
    <div class="grid lg:grid-cols-2 gap-16 items-center mb-24">
      <div class="gsap-reveal-left">
        <h2 class="text-4xl font-black text-[#0f172a] mb-6">Seamless Tax Filing</h2>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          Staying compliant with {title} can be incredibly complex. Our certified Chartered Accountants and tax professionals simplify this process, guaranteeing accurate and timely submissions.
        </p>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          We handle data reconciliation, tax calculation, and portal filing. You get complete peace of mind knowing your financials are in expert hands.
        </p>
        <ul class="space-y-4 mt-8">
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-indigo-600 text-xl"></i> 100% Accuracy & Compliance</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-indigo-600 text-xl"></i> Timely Filing to Avoid Late Fees</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-indigo-600 text-xl"></i> Expert CA Consultation</li>
        </ul>
      </div>
      <div class="gsap-reveal-right">
        <div class="bg-indigo-50 p-10 rounded-[2rem] border border-indigo-100 shadow-xl relative overflow-hidden text-center flex flex-col items-center justify-center h-full min-h-[400px]">
          <div class="absolute top-0 right-0 w-64 h-64 bg-indigo-200 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/4"></div>
          <div class="w-24 h-24 bg-indigo-100 rounded-2xl flex items-center justify-center text-indigo-600 text-5xl mb-8 relative z-10 shadow-inner">
            <i class="fas fa-file-invoice-dollar"></i>
          </div>
          <h3 class="text-3xl font-bold text-[#312e81] mb-4 relative z-10">Stress-Free Compliance</h3>
          <p class="text-gray-600 relative z-10 text-lg">Leave the numbers to us. We optimize your taxes while ensuring strict adherence to the law.</p>
        </div>
      </div>
    </div>
    
    <div class="text-center mt-12 gsap-reveal">
      <h3 class="text-3xl font-black text-[#0f172a] mb-6">Ready to File Your {title}?</h3>
      <p class="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">Get in touch with our tax experts today and get it done effortlessly.</p>
      <a href="contact.html" class="inline-block px-10 py-5 bg-[#312e81] text-white font-black text-xl rounded-2xl hover:bg-indigo-900 transition-all transform hover:scale-105 shadow-2xl shadow-indigo-900/30">
        Start Filing Now
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

print("All 11 pages generated.")
