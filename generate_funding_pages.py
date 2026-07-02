import os

pages = [
    {
        "filename": "seed-funding.html",
        "title": "Seed Funding",
        "badge": "STARTUP CAPITAL",
        "description": "Kickstart your innovative startup with initial capital to develop your prototype and validate your business model.",
        "icon": "fa-seedling",
        "color": "emerald"
    },
    {
        "filename": "angel-investment.html",
        "title": "Angel Investment",
        "badge": "STARTUP FUNDING",
        "description": "Connect with high-net-worth individuals who provide financial backing for small startups or entrepreneurs.",
        "icon": "fa-user-tie",
        "color": "emerald"
    },
    {
        "filename": "venture-capital.html",
        "title": "Venture Capital",
        "badge": "STARTUP FUNDING",
        "description": "Scale your business rapidly by securing institutional funding for startups with long-term growth potential.",
        "icon": "fa-chart-pie",
        "color": "emerald"
    },
    {
        "filename": "mudra-loan.html",
        "title": "Mudra Loan",
        "badge": "GOVT SCHEMES",
        "description": "Avail collateral-free loans up to ₹10 Lakhs for non-corporate, non-farm small/micro enterprises.",
        "icon": "fa-rupee-sign",
        "color": "emerald"
    },
    {
        "filename": "cgtmse-scheme.html",
        "title": "CGTMSE Scheme",
        "badge": "GOVT SCHEMES",
        "description": "Credit Guarantee Fund Trust for Micro and Small Enterprises provides collateral-free credit to the MSME sector.",
        "icon": "fa-shield-alt",
        "color": "emerald"
    },
    {
        "filename": "startup-india-seed-fund.html",
        "title": "Startup India Seed Fund",
        "badge": "GOVT SCHEMES",
        "description": "Financial assistance to startups for proof of concept, prototype development, product trials, and commercialization.",
        "icon": "fa-flag-inida", # Using a generic icon if flag-india doesn't exist, will just use fa-landmark
        "color": "emerald"
    }
]

# Quick fix for icon
pages[5]["icon"] = "fa-landmark"

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
    .hero-overlay.emerald {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to right, rgba(2, 44, 34, 0.95), rgba(16, 185, 129, 0.7));
      z-index: 1;
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
      <span class="bg-gradient-to-r from-{color}-200 to-{color}-400 bg-clip-text text-transparent">{title}</span>
    </h1>
    
    <p class="gsap-reveal text-xl text-{color}-50/90 mb-0 leading-relaxed max-w-3xl mx-auto font-light">
      {description}
    </p>
  </div>
</section>

<!-- CONTENT SECTION -->
<section class="py-24 bg-white relative">
  <div class="max-w-7xl mx-auto px-4">
    
    <div class="grid lg:grid-cols-2 gap-16 items-center mb-24">
      <div class="gsap-reveal-left">
        <h2 class="text-4xl font-black text-[#0f172a] mb-6">Empower Your Business</h2>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          Accessing the right kind of capital at the right time is crucial for business expansion. Whether you need early-stage support, working capital, or institutional backing, our financial experts connect you with the best avenues through {title}.
        </p>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          We provide end-to-end assistance: from preparing solid pitch decks and detailed project reports (DPR) to navigating complex government procedures and negotiating terms with investors.
        </p>
        <ul class="space-y-4 mt-8">
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-{color}-600 text-xl"></i> Project & Pitch Deck Preparation</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-{color}-600 text-xl"></i> Liaison with Authorities & Investors</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-{color}-600 text-xl"></i> Documentation & Compliance</li>
        </ul>
      </div>
      <div class="gsap-reveal-right">
        <div class="bg-{color}-50 p-10 rounded-[2rem] border border-{color}-100 shadow-xl relative overflow-hidden text-center flex flex-col items-center justify-center h-full min-h-[400px]">
          <div class="absolute top-0 right-0 w-64 h-64 bg-{color}-200 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/4"></div>
          <div class="w-24 h-24 bg-{color}-100 rounded-2xl flex items-center justify-center text-{color}-600 text-5xl mb-8 relative z-10 shadow-inner">
            <i class="fas {icon}"></i>
          </div>
          <h3 class="text-3xl font-bold text-[#064e3b] mb-4 relative z-10">Smart Capital</h3>
          <p class="text-gray-600 relative z-10 text-lg">We help you choose the funding structure that minimizes dilution and maximizes growth.</p>
        </div>
      </div>
    </div>
    
    <div class="text-center mt-12 gsap-reveal">
      <h3 class="text-3xl font-black text-[#0f172a] mb-6">Ready to Secure Your Funding?</h3>
      <p class="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">Get in touch with our financial advisors today to evaluate your eligibility for {title}.</p>
      <a href="contact.html" class="inline-block px-10 py-5 bg-[#064e3b] text-white font-black text-xl rounded-2xl hover:bg-green-900 transition-all transform hover:scale-105 shadow-2xl shadow-green-900/30">
        Assess Eligibility
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
