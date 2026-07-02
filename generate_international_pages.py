import os

pages = [
    {
        "filename": "dubai-freezone.html",
        "title": "Dubai Freezone Company",
        "badge": "DUBAI BUSINESS SETUP",
        "description": "Establish your business in one of Dubai's premier Free Zones with 100% foreign ownership and zero tax benefits.",
        "icon": "fa-building",
        "color": "blue"
    },
    {
        "filename": "dubai-mainland.html",
        "title": "Dubai Mainland Company",
        "badge": "DUBAI BUSINESS SETUP",
        "description": "Register an LLC in Dubai Mainland to trade anywhere in the UAE and locally without restrictions.",
        "icon": "fa-city",
        "color": "blue"
    },
    {
        "filename": "dubai-offshore.html",
        "title": "Dubai Offshore Company",
        "badge": "DUBAI BUSINESS SETUP",
        "description": "Protect your assets and optimize your taxes with a secure Dubai offshore company setup.",
        "icon": "fa-shield-alt",
        "color": "blue"
    },
    {
        "filename": "dubai-vat.html",
        "title": "Dubai VAT Registration",
        "badge": "TAX & COMPLIANCE",
        "description": "Seamless VAT registration, filing, and compliance services tailored for UAE businesses.",
        "icon": "fa-file-invoice-dollar",
        "color": "blue"
    },
    {
        "filename": "dubai-visa.html",
        "title": "Dubai Visa Services",
        "badge": "IMMIGRATION",
        "description": "Comprehensive visa services including Golden Visa, Investor Visa, and Employment Visas for the UAE.",
        "icon": "fa-passport",
        "color": "blue"
    },
    {
        "filename": "dubai-incorporation.html",
        "title": "Dubai Company Incorporation",
        "badge": "BUSINESS SETUP",
        "description": "End-to-end company incorporation services in Dubai, tailored for startups and global enterprises.",
        "icon": "fa-briefcase",
        "color": "blue"
    },
    {
        "filename": "dubai-loans.html",
        "title": "Dubai Business Loans",
        "badge": "CORPORATE FINANCE",
        "description": "Secure capital for your UAE business with our expert assistance in acquiring corporate loans.",
        "icon": "fa-hand-holding-usd",
        "color": "blue"
    },
    {
        "filename": "dubai-trademark.html",
        "title": "Dubai Trademark Registration",
        "badge": "IP PROTECTION",
        "description": "Protect your brand identity in the Middle East with comprehensive UAE Trademark registration.",
        "icon": "fa-trademark",
        "color": "blue"
    },
    {
        "filename": "dubai-license.html",
        "title": "Dubai License Services",
        "badge": "LEGAL & COMPLIANCE",
        "description": "Acquire or renew your Commercial, Professional, or Industrial licenses in Dubai smoothly.",
        "icon": "fa-id-card",
        "color": "blue"
    },
    {
        "filename": "us-incorporation.html",
        "title": "US Incorporation",
        "badge": "GLOBAL EXPANSION",
        "description": "Form your US LLC or C-Corp from anywhere in the world and access global markets.",
        "icon": "fa-flag-usa",
        "color": "indigo"
    },
    {
        "filename": "singapore-incorporation.html",
        "title": "Singapore Incorporation",
        "badge": "GLOBAL EXPANSION",
        "description": "Set up a company in Asia's financial hub with low taxes and immense ease of doing business.",
        "icon": "fa-globe-asia",
        "color": "indigo"
    },
    {
        "filename": "uk-incorporation.html",
        "title": "UK Incorporation",
        "badge": "GLOBAL EXPANSION",
        "description": "Establish your UK Limited Company quickly and efficiently with our expert incorporation services.",
        "icon": "fa-chess-rook",
        "color": "indigo"
    },
    {
        "filename": "netherlands-incorporation.html",
        "title": "Netherlands Incorporation",
        "badge": "GLOBAL EXPANSION",
        "description": "Gain a strategic foothold in Europe by incorporating a Dutch BV with favorable tax treaties.",
        "icon": "fa-euro-sign",
        "color": "indigo"
    },
    {
        "filename": "hong-kong-incorporation.html",
        "title": "Hong Kong Incorporation",
        "badge": "GLOBAL EXPANSION",
        "description": "Access the massive Chinese market and benefit from a territorial tax system by incorporating in Hong Kong.",
        "icon": "fa-landmark",
        "color": "indigo"
    }
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
    .hero-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to right, rgba(15, 23, 42, 0.95), rgba(30, 58, 138, 0.8));
      z-index: 1;
    }}
    .hero-overlay.indigo {{
      background: linear-gradient(to right, rgba(15, 23, 42, 0.95), rgba(49, 46, 129, 0.8));
    }}
  </style>
</head>
<body class="bg-gray-50 text-gray-800">

<!-- Placeholder for dynamically injected header -->

<!-- HERO SECTION -->
<section class="hero-bg min-h-[55vh] flex items-center pt-32 pb-20 relative" id="hero">
  <div class="hero-overlay {color}"></div>
  
  <div class="max-w-7xl mx-auto px-4 relative z-10 w-full text-center">
    <div class="gsap-reveal inline-flex items-center gap-2 bg-{color}-900/30 border border-{color}-400/20 rounded-full px-5 py-2 mb-8 backdrop-blur-md">
      <div class="w-2 h-2 bg-{color}-400 rounded-full animate-ping"></div>
      <span class="text-xs font-bold tracking-widest text-{color}-200 uppercase">{badge}</span>
    </div>
    
    <h1 class="gsap-reveal text-5xl md:text-7xl font-black leading-tight mb-6 tracking-tighter max-w-5xl mx-auto text-white">
      <span class="bg-gradient-to-r from-{color}-400 to-indigo-400 bg-clip-text text-transparent">{title}</span>
    </h1>
    
    <p class="gsap-reveal text-xl text-{color}-100/90 mb-0 leading-relaxed max-w-3xl mx-auto font-light">
      {description}
    </p>
  </div>
</section>

<!-- CONTENT SECTION -->
<section class="py-24 bg-white relative">
  <div class="max-w-7xl mx-auto px-4">
    
    <div class="grid lg:grid-cols-2 gap-16 items-center mb-24">
      <div class="gsap-reveal-left">
        <h2 class="text-4xl font-black text-[#0f172a] mb-6">Expert {title} Services</h2>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          Expanding your business internationally requires careful planning, compliance, and execution. Our team of global experts provides end-to-end assistance for your incorporation and setup needs.
        </p>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          From legal documentation and bank account opening to tax structuring and visa processing, we handle the complexities so you can focus on growing your business globally.
        </p>
        <ul class="space-y-4 mt-8">
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-{color}-600 text-xl"></i> Dedicated Account Manager</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-{color}-600 text-xl"></i> 100% Remote Process Available</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-{color}-600 text-xl"></i> Post-Incorporation Support</li>
        </ul>
      </div>
      <div class="gsap-reveal-right">
        <div class="bg-{color}-50 p-10 rounded-[2rem] border border-{color}-100 shadow-xl relative overflow-hidden text-center flex flex-col items-center justify-center h-full min-h-[400px]">
          <div class="absolute top-0 right-0 w-64 h-64 bg-{color}-200 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/4"></div>
          <div class="w-24 h-24 bg-{color}-100 rounded-2xl flex items-center justify-center text-{color}-600 text-5xl mb-8 relative z-10 shadow-inner">
            <i class="fas {icon}"></i>
          </div>
          <h3 class="text-3xl font-bold text-[#1a237e] mb-4 relative z-10">Fast & Secure Setup</h3>
          <p class="text-gray-600 relative z-10 text-lg">We guarantee transparency, speed, and strict compliance with local laws.</p>
        </div>
      </div>
    </div>
    
    <div class="text-center mt-12 gsap-reveal">
      <h3 class="text-3xl font-black text-[#0f172a] mb-6">Start Your Global Journey Today</h3>
      <p class="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">Contact our international incorporation specialists for a free initial consultation and customized setup strategy.</p>
      <a href="contact.html" class="inline-block px-10 py-5 bg-[#1a237e] text-white font-black text-xl rounded-2xl hover:bg-blue-800 transition-all transform hover:scale-105 shadow-2xl shadow-blue-900/30">
        Get Started Now
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

for page in pages:
    html_content = template.format(
        title=page["title"],
        badge=page["badge"],
        description=page["description"],
        icon=page["icon"],
        color=page["color"]
    )
    with open(page["filename"], "w", encoding="utf-8") as f:
        f.write(html_content)
        print(f"Created {page['filename']}")
