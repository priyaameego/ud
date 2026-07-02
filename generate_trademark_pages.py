import os

pages = [
    # Column 1
    {
        "filename": "trademark-registration.html",
        "title": "Trademark Registration",
        "badge": "IP PROTECTION",
        "description": "Secure your brand identity and protect your business name, logo, or slogan with our hassle-free Trademark Registration services.",
        "icon": "fa-trademark",
        "color": "indigo"
    },
    {
        "filename": "trademark-objection.html",
        "title": "Trademark Objection",
        "badge": "LEGAL RESOLUTION",
        "description": "Expert assistance in drafting and filing comprehensive replies to Trademark Examination Reports and Registrar objections.",
        "icon": "fa-file-signature",
        "color": "indigo"
    },
    {
        "filename": "trademark-certificate.html",
        "title": "Trademark Certificate",
        "badge": "IP PROTECTION",
        "description": "Obtain your final Trademark Registration Certificate seamlessly after successful publication in the TM Journal.",
        "icon": "fa-certificate",
        "color": "indigo"
    },
    {
        "filename": "trademark-opposition.html",
        "title": "Trademark Opposition",
        "badge": "LEGAL RESOLUTION",
        "description": "Protect your brand from infringement by filing or defending a Trademark Opposition effectively with our legal experts.",
        "icon": "fa-balance-scale",
        "color": "indigo"
    },
    {
        "filename": "trademark-hearing.html",
        "title": "Trademark Hearing",
        "badge": "LEGAL REPRESENTATION",
        "description": "Professional representation by experienced IP attorneys during your Trademark show-cause hearings.",
        "icon": "fa-gavel",
        "color": "indigo"
    },
    # Column 2
    {
        "filename": "trademark-rectification.html",
        "title": "Trademark Rectification",
        "badge": "LEGAL RESOLUTION",
        "description": "Apply for correction or cancellation of a wrongly registered trademark from the Trademark Register.",
        "icon": "fa-eraser",
        "color": "purple"
    },
    {
        "filename": "tm-infringement.html",
        "title": "TM Infringement Notice",
        "badge": "IP ENFORCEMENT",
        "description": "Take strict legal action against unauthorized use of your brand by sending a powerful Cease & Desist notice.",
        "icon": "fa-shield-alt",
        "color": "purple"
    },
    {
        "filename": "trademark-renewal.html",
        "title": "Trademark Renewal",
        "badge": "IP MAINTENANCE",
        "description": "Ensure lifetime protection for your brand by timely renewing your Trademark every 10 years.",
        "icon": "fa-sync-alt",
        "color": "purple"
    },
    {
        "filename": "trademark-transfer.html",
        "title": "Trademark Transfer",
        "badge": "ASSET MANAGEMENT",
        "description": "Legally assign, sell, or transfer the ownership of your registered trademark to another entity.",
        "icon": "fa-exchange-alt",
        "color": "purple"
    },
    {
        "filename": "expedited-trademark.html",
        "title": "Expedited Trademark Registration",
        "badge": "FAST-TRACK",
        "description": "Accelerate your trademark application process and get examination reports faster through the Tatkal scheme.",
        "icon": "fa-fighter-jet",
        "color": "purple"
    },
    # Column 3
    {
        "filename": "design-registration.html",
        "title": "Design Registration",
        "badge": "INDUSTRIAL DESIGN",
        "description": "Protect the unique visual appearance, shape, or pattern of your products from being copied.",
        "icon": "fa-drafting-compass",
        "color": "fuchsia"
    },
    {
        "filename": "design-objection.html",
        "title": "Design Objection",
        "badge": "LEGAL RESOLUTION",
        "description": "Resolve objections raised by the Design Office swiftly to ensure successful design registration.",
        "icon": "fa-comment-dots",
        "color": "fuchsia"
    },
    {
        "filename": "copyright-registration.html",
        "title": "Copyright Registration",
        "badge": "CREATIVE RIGHTS",
        "description": "Secure exclusive legal rights for your original literary, artistic, musical, or software creations.",
        "icon": "fa-copyright",
        "color": "fuchsia"
    },
    {
        "filename": "copyright-objection.html",
        "title": "Copyright Objection",
        "badge": "LEGAL RESOLUTION",
        "description": "Expert legal responses to discrepancies or objections raised during the copyright registration process.",
        "icon": "fa-exclamation-circle",
        "color": "fuchsia"
    },
    {
        "filename": "patent-registration.html",
        "title": "Patent Registration",
        "badge": "INVENTIONS",
        "description": "Protect your innovative ideas, products, and processes with our comprehensive Patent drafting and filing services.",
        "icon": "fa-lightbulb",
        "color": "fuchsia"
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
      background: linear-gradient(to right, rgba(17, 24, 39, 0.95), rgba(67, 56, 202, 0.8));
    }}
    .hero-overlay.purple {{
      background: linear-gradient(to right, rgba(17, 24, 39, 0.95), rgba(126, 34, 206, 0.8));
    }}
    .hero-overlay.fuchsia {{
      background: linear-gradient(to right, rgba(17, 24, 39, 0.95), rgba(192, 38, 211, 0.8));
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
      <span class="bg-gradient-to-r from-{color}-400 to-pink-400 bg-clip-text text-transparent">{title}</span>
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
          Intellectual Property is one of the most valuable assets of any modern business. Ensuring comprehensive legal protection through {title} prevents infringement and secures your competitive advantage.
        </p>
        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
          Our team of dedicated IP attorneys and experts provide end-to-end guidance, from comprehensive drafting and filing to robust legal representation during objections and hearings.
        </p>
        <ul class="space-y-4 mt-8">
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-{color}-600 text-xl"></i> Complete Legal Documentation</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-{color}-600 text-xl"></i> Expert IP Attorneys</li>
          <li class="flex items-center gap-4 text-gray-700 font-medium"><i class="fas fa-check-circle text-{color}-600 text-xl"></i> Transparent Tracking & Updates</li>
        </ul>
      </div>
      <div class="gsap-reveal-right">
        <div class="bg-{color}-50 p-10 rounded-[2rem] border border-{color}-100 shadow-xl relative overflow-hidden text-center flex flex-col items-center justify-center h-full min-h-[400px]">
          <div class="absolute top-0 right-0 w-64 h-64 bg-{color}-200 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/4"></div>
          <div class="w-24 h-24 bg-{color}-100 rounded-2xl flex items-center justify-center text-{color}-600 text-5xl mb-8 relative z-10 shadow-inner">
            <i class="fas {icon}"></i>
          </div>
          <h3 class="text-3xl font-bold text-[#1a237e] mb-4 relative z-10">Protect Your Assets</h3>
          <p class="text-gray-600 relative z-10 text-lg">Don't let competitors steal your hard-earned reputation and innovation.</p>
        </div>
      </div>
    </div>
    
    <div class="text-center mt-12 gsap-reveal">
      <h3 class="text-3xl font-black text-[#0f172a] mb-6">Secure Your Intellectual Property Today</h3>
      <p class="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">Get in touch with our IP consultants for a free consultation and strategy session.</p>
      <a href="contact.html" class="inline-block px-10 py-5 bg-[#1a237e] text-white font-black text-xl rounded-2xl hover:bg-blue-800 transition-all transform hover:scale-105 shadow-2xl shadow-blue-900/30">
        Consult an Expert
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
