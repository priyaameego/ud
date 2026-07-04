import os
import re

# 1. Update grants.html
with open(r'c:\Users\Priya\Documents\udyog\grants.html', 'r', encoding='utf-8') as f:
    grants = f.read()

grants_image_html = '''
      <p class="text-gray-500 font-medium mb-12">Most government grants require startups to meet these baseline standards.</p>
      <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Business Grant Meeting" class="w-full max-w-5xl mx-auto h-[350px] object-cover rounded-[2rem] shadow-2xl mb-12 gsap-reveal">
    </div>
'''
grants = grants.replace('''<p class="text-gray-500 font-medium">Most government grants require startups to meet these baseline standards.</p>\n    </div>''', grants_image_html)
with open(r'c:\Users\Priya\Documents\udyog\grants.html', 'w', encoding='utf-8') as f:
    f.write(grants)


# 2. Update loans.html
with open(r'c:\Users\Priya\Documents\udyog\loans.html', 'r', encoding='utf-8') as f:
    loans = f.read()

loans_image_html = '''
      <p class="text-gray-500 font-medium max-w-2xl mx-auto mb-12">Choose the perfect financing solution that aligns with your business goals.</p>
      <img src="https://images.unsplash.com/photo-1556761175-5973dc0f32d7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Corporate Finance" class="w-full max-w-5xl mx-auto h-[350px] object-cover rounded-[2rem] shadow-2xl mb-12 gsap-reveal">
    </div>
'''
loans = loans.replace('''<p class="text-gray-500 font-medium max-w-2xl mx-auto">Choose the perfect financing solution that aligns with your business goals.</p>\n    </div>''', loans_image_html)
with open(r'c:\Users\Priya\Documents\udyog\loans.html', 'w', encoding='utf-8') as f:
    f.write(loans)


# 3. Create nbfc.html new main content
nbfc_main_content = '''
<!-- STICKY APPLY NOW BUTTON -->
<div class="fixed bottom-6 right-6 z-50 animate-bounce">
  <a href="#hero" class="bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-700 hover:to-pink-700 text-white font-black py-4 px-8 rounded-full shadow-[0_10px_30px_rgba(225,29,72,0.4)] flex items-center gap-3 transition-transform hover:scale-105 border-2 border-white/20 backdrop-blur-md">
    Apply Now <i class="fas fa-arrow-up"></i>
  </a>
</div>

<!-- HERO SECTION -->
<section class="min-h-screen relative pt-32 pb-20 flex items-center overflow-hidden" id="hero">
  <!-- Dynamic Unsplash Background -->
  <div class="absolute inset-0 bg-gray-900">
    <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Cityscape" class="w-full h-full object-cover opacity-30 mix-blend-overlay">
  </div>
  <div class="absolute inset-0 bg-gradient-to-br from-gray-900 via-gray-900/90 to-[#1a237e]/80"></div>
  
  <div class="max-w-7xl mx-auto px-4 relative z-10 w-full mt-10">
    <div class="grid lg:grid-cols-2 gap-12 lg:gap-8 items-center">
      <!-- Left Content -->
      <div class="text-white gsap-reveal">
        <div class="inline-flex items-center gap-2 bg-rose-500/20 text-rose-300 border border-rose-500/30 rounded-full px-4 py-1.5 mb-6 shadow-[0_0_15px_rgba(225,29,72,0.2)]">
          <div class="w-2 h-2 bg-rose-400 rounded-full animate-ping"></div>
          <span class="text-[10px] font-bold tracking-wider uppercase">NBFC Business Loans</span>
        </div>
        
        <h1 class="text-5xl md:text-6xl lg:text-[4.5rem] font-black leading-tight mb-6 tracking-tight">
          Smarter Funding,<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-rose-400 to-orange-300">Faster Growth.</span>
        </h1>
        
        <p class="text-lg md:text-xl text-gray-300 mb-12 max-w-lg leading-relaxed font-light">
          Get collateral-free business loans up to ₹5 Crores. NBFC financing offers higher flexibility, minimal documentation, and approval within 48 hours.
        </p>
        
        <div class="flex flex-wrap gap-4 mb-8">
          <div class="flex items-center gap-2 bg-white/10 backdrop-blur-md border border-white/10 rounded-full px-5 py-2.5">
            <i class="fas fa-rocket text-orange-400"></i>
            <span class="text-sm font-bold">48hr Disbursal</span>
          </div>
          <div class="flex items-center gap-2 bg-white/10 backdrop-blur-md border border-white/10 rounded-full px-5 py-2.5">
            <i class="fas fa-file-signature text-rose-400"></i>
            <span class="text-sm font-bold">Less Paperwork</span>
          </div>
        </div>
      </div>
      
      <!-- Right Content: Glassmorphism Form -->
      <div class="bg-white/10 backdrop-blur-2xl border border-white/20 rounded-[2.5rem] p-8 md:p-10 shadow-2xl relative max-w-md w-full mx-auto lg:ml-auto gsap-reveal premium-form-anim">
        <h2 class="text-2xl font-black text-white mb-2 tracking-tight">Check NBFC Eligibility</h2>
        <p class="text-sm text-gray-300 mb-8 font-medium">Quick digital approval with zero physical visits.</p>
        
        <form class="space-y-4">
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-building text-white/50"></i>
            </div>
            <input type="text" class="w-full pl-11 pr-4 py-4 bg-white/5 border border-white/10 rounded-xl text-sm text-white focus:ring-2 focus:ring-rose-400 focus:border-rose-400 transition-colors outline-none placeholder-white/50 font-medium" placeholder="Business Name" required>
          </div>
          
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-rupee-sign text-white/50"></i>
            </div>
            <input type="number" class="w-full pl-11 pr-4 py-4 bg-white/5 border border-white/10 rounded-xl text-sm text-white focus:ring-2 focus:ring-rose-400 focus:border-rose-400 transition-colors outline-none placeholder-white/50 font-medium" placeholder="Annual Turnover (₹)" required>
          </div>
          
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-phone-alt text-white/50"></i>
            </div>
            <input type="tel" class="w-full pl-11 pr-4 py-4 bg-white/5 border border-white/10 rounded-xl text-sm text-white focus:ring-2 focus:ring-rose-400 focus:border-rose-400 transition-colors outline-none placeholder-white/50 font-medium" placeholder="Mobile Number" required>
          </div>
          
          <button type="submit" class="w-full bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-700 hover:to-pink-700 text-white font-bold py-4.5 px-6 rounded-xl transition-all duration-300 shadow-[0_0_20px_rgba(225,29,72,0.4)] hover:shadow-[0_0_30px_rgba(225,29,72,0.6)] flex items-center justify-center gap-3 mt-6 group">
            Apply Now 
            <i class="fas fa-arrow-right text-sm transition-transform group-hover:translate-x-1"></i>
          </button>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- Why Choose NBFC (Comparison) -->
<section class="py-24 bg-white relative overflow-hidden">
  <div class="max-w-7xl mx-auto px-4 relative z-10">
    <div class="text-center mb-16 gsap-reveal">
      <div class="text-rose-600 font-bold text-[10px] tracking-widest uppercase mb-2">The NBFC Advantage</div>
      <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">NBFC vs Traditional Banks</h2>
      <p class="text-gray-500 font-medium max-w-2xl mx-auto">Why modern businesses prefer NBFCs for their urgent financing needs.</p>
    </div>
    
    <div class="max-w-5xl mx-auto bg-white rounded-[2rem] shadow-[0_10px_50px_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden gsap-reveal">
      <div class="grid grid-cols-3 bg-gray-50 border-b border-gray-100 p-6 text-center font-black text-sm uppercase tracking-wider">
        <div class="text-left text-gray-400">Features</div>
        <div class="text-gray-900">Traditional Banks</div>
        <div class="text-rose-600">NBFC Loans</div>
      </div>
      
      <div class="grid grid-cols-3 p-6 text-center border-b border-gray-50 hover:bg-gray-50/50 transition-colors">
        <div class="text-left font-bold text-gray-700 text-sm">Processing Speed</div>
        <div class="text-gray-500 text-sm font-medium">15 - 30 Days</div>
        <div class="text-gray-900 text-sm font-black">24 - 48 Hours</div>
      </div>
      <div class="grid grid-cols-3 p-6 text-center border-b border-gray-50 hover:bg-gray-50/50 transition-colors">
        <div class="text-left font-bold text-gray-700 text-sm">Documentation</div>
        <div class="text-gray-500 text-sm font-medium">Heavy & Physical</div>
        <div class="text-gray-900 text-sm font-black">Minimal & Digital</div>
      </div>
      <div class="grid grid-cols-3 p-6 text-center border-b border-gray-50 hover:bg-gray-50/50 transition-colors">
        <div class="text-left font-bold text-gray-700 text-sm">Collateral</div>
        <div class="text-gray-500 text-sm font-medium">Strictly Required</div>
        <div class="text-gray-900 text-sm font-black">Unsecured Options</div>
      </div>
      <div class="grid grid-cols-3 p-6 text-center hover:bg-gray-50/50 transition-colors">
        <div class="text-left font-bold text-gray-700 text-sm">Credit Score Flex</div>
        <div class="text-gray-500 text-sm font-medium">Very Rigid (750+)</div>
        <div class="text-gray-900 text-sm font-black">Flexible (650+)</div>
      </div>
    </div>
  </div>
</section>

<!-- Products with Split Image -->
<section class="py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4">
    <div class="grid lg:grid-cols-2 gap-16 items-center">
      <div class="gsap-reveal">
        <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Business Growth" class="w-full h-[500px] object-cover rounded-[2.5rem] shadow-2xl">
      </div>
      
      <div class="gsap-reveal">
        <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-6 tracking-tight">Flexible Loan Products</h2>
        <p class="text-gray-500 font-medium mb-10 leading-relaxed">NBFCs provide tailored credit products that adapt to your specific business cycles rather than forcing a one-size-fits-all approach.</p>
        
        <div class="space-y-6">
          <div class="flex gap-5">
            <div class="w-14 h-14 rounded-2xl bg-white shadow-sm flex items-center justify-center shrink-0 border border-gray-100 text-rose-500">
              <i class="fas fa-sync-alt text-2xl"></i>
            </div>
            <div>
              <h4 class="font-bold text-gray-900 mb-1">Working Capital Demand Loans</h4>
              <p class="text-sm text-gray-500">Short-term credit lines to cover payroll, inventory, and operational cash crunches.</p>
            </div>
          </div>
          
          <div class="flex gap-5">
            <div class="w-14 h-14 rounded-2xl bg-white shadow-sm flex items-center justify-center shrink-0 border border-gray-100 text-orange-500">
              <i class="fas fa-truck-loading text-2xl"></i>
            </div>
            <div>
              <h4 class="font-bold text-gray-900 mb-1">Supply Chain Finance</h4>
              <p class="text-sm text-gray-500">Invoice discounting and vendor financing to keep your supply chain moving rapidly.</p>
            </div>
          </div>
          
          <div class="flex gap-5">
            <div class="w-14 h-14 rounded-2xl bg-white shadow-sm flex items-center justify-center shrink-0 border border-gray-100 text-indigo-500">
              <i class="fas fa-store text-2xl"></i>
            </div>
            <div>
              <h4 class="font-bold text-gray-900 mb-1">Merchant Cash Advance</h4>
              <p class="text-sm text-gray-500">Loans based on your POS machine swipe volumes, perfect for retail businesses.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Required Documents & Eligibility -->
<section class="py-24 bg-gray-900 text-white relative">
  <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')] opacity-10 bg-cover bg-center bg-fixed"></div>
  <div class="max-w-7xl mx-auto px-4 relative z-10">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black mb-4 tracking-tight">Minimum Eligibility & Docs</h2>
      <p class="text-gray-400 font-medium">NBFCs require far less paperwork. Here is what you need.</p>
    </div>
    
    <div class="grid md:grid-cols-2 gap-8">
      <div class="bg-white/5 border border-white/10 rounded-[2rem] p-10 backdrop-blur-md gsap-reveal">
        <h3 class="text-2xl font-black mb-6 text-rose-400">Basic Eligibility</h3>
        <ul class="space-y-4">
          <li class="flex items-start gap-3 text-gray-300 font-medium">
            <i class="fas fa-check-circle text-rose-500 mt-1"></i> Minimum 1 year of business vintage.
          </li>
          <li class="flex items-start gap-3 text-gray-300 font-medium">
            <i class="fas fa-check-circle text-rose-500 mt-1"></i> Annual turnover of at least ₹10 Lakhs.
          </li>
          <li class="flex items-start gap-3 text-gray-300 font-medium">
            <i class="fas fa-check-circle text-rose-500 mt-1"></i> CIBIL score of 650 or higher.
          </li>
          <li class="flex items-start gap-3 text-gray-300 font-medium">
            <i class="fas fa-check-circle text-rose-500 mt-1"></i> Promoter's age between 21 and 65 years.
          </li>
        </ul>
      </div>
      
      <div class="bg-white/5 border border-white/10 rounded-[2rem] p-10 backdrop-blur-md gsap-reveal">
        <h3 class="text-2xl font-black mb-6 text-orange-400">Required Documents</h3>
        <ul class="space-y-4">
          <li class="flex items-start gap-3 text-gray-300 font-medium">
            <i class="fas fa-file-pdf text-orange-500 mt-1"></i> PAN Card & Aadhaar Card (Promoters).
          </li>
          <li class="flex items-start gap-3 text-gray-300 font-medium">
            <i class="fas fa-file-pdf text-orange-500 mt-1"></i> GST Registration / Udyam Certificate.
          </li>
          <li class="flex items-start gap-3 text-gray-300 font-medium">
            <i class="fas fa-file-pdf text-orange-500 mt-1"></i> Last 6-12 months Bank Statement.
          </li>
          <li class="flex items-start gap-3 text-gray-300 font-medium">
            <i class="fas fa-file-pdf text-orange-500 mt-1"></i> Last 1 year ITR (Only for loans > 10L).
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- Process Timeline -->
<section class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">Lightning Fast Process</h2>
      <p class="text-gray-500 font-medium">Get funded in 3 simple steps.</p>
    </div>
    
    <div class="relative max-w-4xl mx-auto gsap-reveal">
      <div class="hidden md:block absolute top-1/2 left-0 w-full h-1 bg-gray-100 -translate-y-1/2 rounded-full"></div>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-6 relative z-10">
        <div class="text-center group">
          <div class="w-20 h-20 mx-auto bg-white text-rose-600 rounded-2xl flex items-center justify-center text-3xl shadow-[0_10px_30px_rgba(225,29,72,0.15)] mb-6 group-hover:-translate-y-2 transition-transform border border-rose-50"><i class="fas fa-mobile-alt"></i></div>
          <h4 class="font-black text-gray-900 mb-2 text-lg">1. Digital Application</h4>
          <p class="text-sm text-gray-500">Apply online in 2 minutes and upload your PDFs.</p>
        </div>
        <div class="text-center group">
          <div class="w-20 h-20 mx-auto bg-white text-orange-500 rounded-2xl flex items-center justify-center text-3xl shadow-[0_10px_30px_rgba(249,115,22,0.15)] mb-6 group-hover:-translate-y-2 transition-transform border border-orange-50"><i class="fas fa-robot"></i></div>
          <h4 class="font-black text-gray-900 mb-2 text-lg">2. AI Assessment</h4>
          <p class="text-sm text-gray-500">Our algorithms analyze your cash flow instantly.</p>
        </div>
        <div class="text-center group">
          <div class="w-20 h-20 mx-auto bg-white text-green-500 rounded-2xl flex items-center justify-center text-3xl shadow-[0_10px_30px_rgba(34,197,94,0.15)] mb-6 group-hover:-translate-y-2 transition-transform border border-green-50"><i class="fas fa-money-check-alt"></i></div>
          <h4 class="font-black text-gray-900 mb-2 text-lg">3. Direct Disbursal</h4>
          <p class="text-sm text-gray-500">Funds hit your bank account within 24-48 hours.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQs & Testimonials -->
<section class="py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4">
    <div class="grid lg:grid-cols-2 gap-16">
      <!-- FAQs -->
      <div class="gsap-reveal">
        <h2 class="text-3xl font-black text-[#0f172a] mb-8 tracking-tight">NBFC Loan FAQs</h2>
        <div class="space-y-4">
          <div class="bg-white border border-gray-100 rounded-[1.5rem] overflow-hidden group shadow-sm">
            <button class="w-full text-left px-6 py-5 flex items-center justify-between outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
              <span class="font-bold text-gray-900">Are NBFC loans safe?</span>
              <div class="w-8 h-8 rounded-full bg-rose-50 flex items-center justify-center shrink-0">
                <i class="fas fa-plus text-rose-600 text-sm transition-transform"></i>
              </div>
            </button>
            <div class="px-6 pb-5 text-gray-500 text-sm leading-relaxed hidden font-medium">
              Yes, all registered NBFCs are strictly regulated by the Reserve Bank of India (RBI) and follow rigorous compliance and data security protocols.
            </div>
          </div>
          
          <div class="bg-white border border-gray-100 rounded-[1.5rem] overflow-hidden group shadow-sm">
            <button class="w-full text-left px-6 py-5 flex items-center justify-between outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
              <span class="font-bold text-gray-900">Is the interest rate higher than banks?</span>
              <div class="w-8 h-8 rounded-full bg-rose-50 flex items-center justify-center shrink-0">
                <i class="fas fa-plus text-rose-600 text-sm transition-transform"></i>
              </div>
            </button>
            <div class="px-6 pb-5 text-gray-500 text-sm leading-relaxed hidden font-medium">
              While sometimes marginally higher, NBFCs compensate by offering loans without collateral, much faster processing, and extreme flexibility which banks often deny.
            </div>
          </div>
        </div>
      </div>
      
      <!-- Testimonial -->
      <div class="gsap-reveal">
        <h2 class="text-3xl font-black text-[#0f172a] mb-8 tracking-tight">Success Stories</h2>
        <div class="bg-white rounded-[2rem] p-10 shadow-[0_10px_40px_rgba(0,0,0,0.04)] border border-gray-100 relative">
          <i class="fas fa-quote-left text-5xl text-gray-100 absolute top-8 right-8"></i>
          <div class="flex text-yellow-400 text-sm mb-6">
            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
          </div>
          <p class="text-gray-600 font-medium leading-relaxed mb-8 italic text-lg">"We had a massive export order but our bank took 3 weeks just to process the file. We applied for an NBFC loan and got ₹35 Lakhs disbursed in just 2 days. It saved our contract."</p>
          <div class="flex items-center gap-4">
            <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Arjun Mehta" class="w-14 h-14 rounded-full object-cover shadow-sm">
            <div>
              <div class="font-black text-gray-900">Arjun Mehta</div>
              <div class="text-xs text-rose-600 font-bold uppercase tracking-wider">Garment Exporter</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- WhatsApp CTA -->
<section class="py-20 bg-gradient-to-br from-rose-600 to-[#1a237e]">
  <div class="max-w-7xl mx-auto px-4 text-center gsap-reveal">
    <h2 class="text-3xl md:text-5xl font-black text-white mb-6 tracking-tight">Fast Track Your Business Funding</h2>
    <p class="text-rose-100 mb-10 max-w-2xl mx-auto font-medium text-lg">Connect with our NBFC funding experts on WhatsApp and get your application processed on priority.</p>
    
    <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
      <a href="https://wa.me/919876543210" class="w-full sm:w-auto bg-[#25D366] hover:bg-[#20bd5a] text-white font-bold py-4.5 px-8 rounded-full transition-transform hover:scale-105 shadow-xl flex items-center justify-center gap-3 border border-white/20 text-lg">
        <i class="fab fa-whatsapp text-2xl"></i> Connect on WhatsApp
      </a>
    </div>
  </div>
</section>
'''

with open(r'c:\Users\Priya\Documents\udyog\nbfc.html', 'r', encoding='utf-8', errors='ignore') as f:
    nbfc_content = f.read()

# Add the premium form animation CSS to nbfc.html
style_block = """
<style>
@keyframes floatForm {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
  100% { transform: translateY(0px); }
}
@keyframes glowForm {
  0% { box-shadow: 0 0 15px rgba(225, 29, 72, 0.2), 0 20px 40px rgba(0,0,0,0.4); }
  50% { box-shadow: 0 0 40px rgba(225, 29, 72, 0.6), 0 30px 60px rgba(0,0,0,0.6); }
  100% { box-shadow: 0 0 15px rgba(225, 29, 72, 0.2), 0 20px 40px rgba(0,0,0,0.4); }
}
.premium-form-anim {
  animation: floatForm 6s ease-in-out infinite, glowForm 4s ease-in-out infinite;
  border: 1px solid rgba(255,255,255,0.2) !important;
}
</style>
"""
if "premium-form-anim" not in nbfc_content:
    if "</head>" in nbfc_content:
        nbfc_content = nbfc_content.replace("</head>", style_block + "\n</head>")
    else:
        nbfc_content = style_block + "\n" + nbfc_content

header_end = nbfc_content.find('</header>') + len('</header>')
footer_start = nbfc_content.find('<!-- Footer -->')
if footer_start == -1:
    footer_start = nbfc_content.find('<footer')

if header_end != -1 and footer_start != -1:
    first_section = nbfc_content.find('<section', header_end)
    if first_section != -1:
        new_content = nbfc_content[:first_section] + nbfc_main_content + '\n' + nbfc_content[footer_start:]
        with open(r'c:\Users\Priya\Documents\udyog\nbfc.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully built nbfc.html and updated grants/loans with images!")
    else:
        print("Error: Could not find first <section> in nbfc")
else:
    print("Error: Could not find header or footer in nbfc")
