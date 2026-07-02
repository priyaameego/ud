import os

pages = {
    "events.html": {
        "title": "Events & Webinars",
        "subtitle": "Join our latest events",
        "desc": "Discover upcoming webinars, workshops, and compliance events hosted by industry experts.",
        "icon": "fa-calendar-alt",
        "img": "https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=800&q=80"
    },
    "products.html": {
        "title": "Our Products",
        "subtitle": "Compliance Made Easy",
        "desc": "Explore our premium software and SaaS solutions for business registration, taxation, and accounting.",
        "icon": "fa-box-open",
        "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80"
    },
    "blogs.html": {
        "title": "Business Insights",
        "subtitle": "Latest News & Blogs",
        "desc": "Stay updated with the latest in Indian taxation, compliance laws, and business growth strategies.",
        "icon": "fa-newspaper",
        "img": "https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=800&q=80"
    },
    "about.html": {
        "title": "About Us",
        "subtitle": "Our Mission",
        "desc": "We are on a mission to simplify business compliance in India, empowering entrepreneurs to focus on growth.",
        "icon": "fa-info-circle",
        "img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80"
    },
    "documentation.html": {
        "title": "Documentation",
        "subtitle": "Developer & API Docs",
        "desc": "Integrate our compliance and taxation APIs directly into your software. Read the full documentation.",
        "icon": "fa-book",
        "img": "https://images.unsplash.com/photo-1555949963-aa79dcee57d5?w=800&q=80"
    },
    "careers.html": {
        "title": "Careers",
        "subtitle": "Join Our Team",
        "desc": "We are always looking for talented CAs, CSs, and developers to join our fast-growing startup.",
        "icon": "fa-briefcase",
        "img": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&q=80"
    },
    "refer.html": {
        "title": "Refer and Earn",
        "subtitle": "Partner Program",
        "desc": "Refer clients to Udyog Suvidha Kendra and earn exciting commissions on every successful registration.",
        "icon": "fa-hand-holding-usd",
        "img": "https://images.unsplash.com/photo-1556740738-b6a63e27c4df?w=800&q=80"
    },
    "partner.html": {
        "title": "Partner With Us",
        "subtitle": "B2B Collaborations",
        "desc": "Are you a CA/CS firm or a legal consultant? Partner with us to scale your services across India.",
        "icon": "fa-handshake",
        "img": "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=800&q=80"
    },
    "experts.html": {
        "title": "Connect with Experts",
        "subtitle": "Free Consultation",
        "desc": "Book a 1-on-1 session with our senior Chartered Accountants and get customized advice for your business.",
        "icon": "fa-user-tie",
        "img": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=800&q=80"
    }
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} | Udyog Suvidha Kendra</title>
  
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
  
  <!-- GSAP & Lenis -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="https://unpkg.com/@studio-freight/lenis@1.0.33/dist/lenis.min.js"></script>

  <style>
    * {{ font-family: 'Inter', sans-serif; }}
    html.lenis {{ height: auto; }}
    .lenis.lenis-smooth {{ scroll-behavior: auto !important; }}
    
    .hero-bg {{
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      position: relative;
      overflow: hidden;
    }}
    .hero-bg::after {{
      content: '';
      position: absolute;
      inset: 0;
      background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px);
      background-size: 40px 40px;
      z-index: 1;
    }}
    
    .glass-card {{
      background: rgba(255, 255, 255, 0.7);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.4);
      box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .glass-card:hover {{
      background: rgba(255, 255, 255, 0.95);
      transform: translateY(-8px);
      box-shadow: 0 20px 40px rgba(30, 58, 138, 0.1);
      border-color: rgba(255, 255, 255, 0.8);
    }}
    
    .reveal-up {{ opacity: 0; transform: translateY(40px); }}
    .reveal-scale {{ opacity: 0; transform: scale(0.9); }}
  </style>
</head>
<body class="bg-gray-50 text-gray-800">

<!-- Placeholder for dynamic header injection -->
<header id="main-header"></header>

<!-- HERO SECTION -->
<section class="hero-bg text-white pt-40 pb-24 relative z-10">
  <div class="absolute inset-0 z-0 opacity-30">
    <div class="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-500 rounded-full mix-blend-screen filter blur-[100px] animate-pulse"></div>
  </div>
  
  <div class="max-w-7xl mx-auto px-4 grid lg:grid-cols-2 gap-12 items-center relative z-20">
    <!-- Left Text -->
    <div>
      <div class="reveal-up inline-flex items-center gap-2 bg-blue-900/30 border border-blue-400/20 rounded-full px-5 py-2 mb-8 backdrop-blur-md">
        <i class="fas {icon} text-blue-400"></i>
        <span class="text-xs font-bold tracking-widest text-blue-200 uppercase">{subtitle}</span>
      </div>
      
      <h1 class="reveal-up text-5xl lg:text-7xl font-black leading-tight mb-6 tracking-tighter">
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-300 to-indigo-200">{title}</span>
      </h1>
      
      <p class="reveal-up text-xl text-blue-100/80 mb-10 max-w-xl font-light">
        {desc}
      </p>
      
      <div class="reveal-up flex gap-4">
        <a href="contact.html" class="px-8 py-4 bg-white text-[#0f172a] font-bold text-lg rounded-2xl shadow-xl hover:shadow-2xl hover:scale-105 transition-all">
          Get Started
        </a>
      </div>
    </div>
    
    <!-- Right Graphic -->
    <div class="reveal-scale relative z-20 rounded-3xl overflow-hidden shadow-2xl border border-white/20">
       <img src="{img}" alt="{title}" class="w-full h-[400px] object-cover hover:scale-105 transition-transform duration-700"/>
       <div class="absolute inset-0 bg-gradient-to-t from-[#0f172a] via-transparent to-transparent opacity-80"></div>
       <div class="absolute bottom-6 left-6 right-6">
         <h3 class="text-2xl font-bold text-white mb-2">Premium Experience</h3>
         <p class="text-blue-200 text-sm">Empowering your business with state-of-the-art solutions.</p>
       </div>
    </div>
  </div>
</section>

<!-- CONTENT SECTION -->
<section class="py-24 bg-white relative">
  <div class="max-w-4xl mx-auto px-4 text-center reveal-up">
    <h2 class="text-4xl font-black text-[#0f172a] mb-6 tracking-tight">Everything You Need to Know</h2>
    <p class="text-lg text-gray-500 mb-12">
      [Placeholder: Paste your actual detailed content for this page here.]
    </p>
    
    <!-- Example Glass Cards -->
    <div class="grid sm:grid-cols-2 gap-8 text-left mt-16">
      <div class="glass-card p-8 rounded-3xl bg-gray-50">
        <h3 class="text-xl font-bold text-gray-900 mb-4"><i class="fas fa-check-circle text-blue-600 mr-2"></i> Key Features</h3>
        <ul class="text-gray-600 space-y-2">
          <li>- Feature point 1 goes here</li>
          <li>- Feature point 2 goes here</li>
          <li>- Feature point 3 goes here</li>
        </ul>
      </div>
      <div class="glass-card p-8 rounded-3xl bg-gray-50">
        <h3 class="text-xl font-bold text-gray-900 mb-4"><i class="fas fa-star text-yellow-500 mr-2"></i> Why Choose Us?</h3>
        <ul class="text-gray-600 space-y-2">
          <li>- Fast turnaround time</li>
          <li>- Dedicated CA/CS support</li>
          <li>- 100% online process</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<script>
  const lenis = new Lenis({{ duration: 1.2, smooth: true }});
  function raf(time) {{ lenis.raf(time); requestAnimationFrame(raf); }}
  requestAnimationFrame(raf);

  gsap.registerPlugin(ScrollTrigger);

  gsap.to(".reveal-up", {{ y: 0, opacity: 1, duration: 1, stagger: 0.2, ease: "power4.out", delay: 0.2 }});
  gsap.to(".reveal-scale", {{ scale: 1, opacity: 1, duration: 0.8, ease: "back.out(1.7)", delay: 0.4 }});
</script>

</body>
</html>
"""

for filename, data in pages.items():
    content = template.format(
        title=data["title"],
        subtitle=data["subtitle"],
        desc=data["desc"],
        icon=data["icon"],
        img=data["img"]
    )
    filepath = os.path.join(r"c:\Users\Priya\Documents\udyog", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename}")
