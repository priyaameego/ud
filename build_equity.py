import os

equity_main_content = '''
<!-- STICKY APPLY NOW BUTTON -->
<div class="fixed bottom-6 right-6 z-50 animate-bounce">
  <a href="#hero" class="bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white font-black py-4 px-8 rounded-full shadow-[0_10px_30px_rgba(16,185,129,0.4)] flex items-center gap-3 transition-transform hover:scale-105 border-2 border-white/20 backdrop-blur-md">
    Pitch Now <i class="fas fa-rocket"></i>
  </a>
</div>

<!-- HERO SECTION -->
<section class="min-h-screen relative pt-32 pb-20 flex items-center overflow-hidden" id="hero">
  <!-- Dynamic Unsplash Background -->
  <div class="absolute inset-0 bg-slate-900">
    <img src="https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Finance Boardroom" class="w-full h-full object-cover opacity-25 mix-blend-overlay">
  </div>
  <div class="absolute inset-0 bg-gradient-to-br from-slate-900 via-slate-900/95 to-[#064e3b]/80"></div>
  
  <div class="max-w-7xl mx-auto px-4 relative z-10 w-full mt-10">
    <div class="grid lg:grid-cols-2 gap-12 lg:gap-8 items-center">
      <!-- Left Content -->
      <div class="text-white gsap-reveal">
        <div class="inline-flex items-center gap-2 bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 rounded-full px-4 py-1.5 mb-6 shadow-[0_0_15px_rgba(16,185,129,0.2)]">
          <div class="w-2 h-2 bg-emerald-400 rounded-full animate-ping"></div>
          <span class="text-[10px] font-bold tracking-wider uppercase">Venture Capital & Equity Funding</span>
        </div>
        
        <h1 class="text-5xl md:text-6xl lg:text-[4.5rem] font-black leading-tight mb-6 tracking-tight">
          Scale Your Vision.<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-300">Raise Smart Capital.</span>
        </h1>
        
        <p class="text-lg md:text-xl text-gray-300 mb-12 max-w-lg leading-relaxed font-light">
          Connect with top-tier Angel Investors and VC firms. Secure equity funding from ₹1 Crore to ₹100 Crores to dominate your market.
        </p>
        
        <div class="flex flex-wrap gap-4 mb-8">
          <div class="flex items-center gap-2 bg-white/10 backdrop-blur-md border border-white/10 rounded-full px-5 py-2.5">
            <i class="fas fa-handshake text-emerald-400"></i>
            <span class="text-sm font-bold">Top 50+ VCs</span>
          </div>
          <div class="flex items-center gap-2 bg-white/10 backdrop-blur-md border border-white/10 rounded-full px-5 py-2.5">
            <i class="fas fa-chart-line text-amber-400"></i>
            <span class="text-sm font-bold">Strategic Growth</span>
          </div>
        </div>
      </div>
      
      <!-- Right Content: Glassmorphism Form -->
      <div class="bg-white/10 backdrop-blur-2xl border border-white/20 rounded-[2.5rem] p-8 md:p-10 shadow-2xl relative max-w-md w-full mx-auto lg:ml-auto gsap-reveal premium-form-anim">
        <h2 class="text-2xl font-black text-white mb-2 tracking-tight">Submit Your Pitch</h2>
        <p class="text-sm text-gray-300 mb-8 font-medium">Get your deck in front of active investors.</p>
        
        <form class="space-y-4">
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-rocket text-white/50"></i>
            </div>
            <input type="text" class="w-full pl-11 pr-4 py-4 bg-white/5 border border-white/10 rounded-xl text-sm text-white focus:ring-2 focus:ring-emerald-400 focus:border-emerald-400 transition-colors outline-none placeholder-white/50 font-medium" placeholder="Startup Name" required>
          </div>
          
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-money-bill-wave text-white/50"></i>
            </div>
            <select class="w-full pl-11 pr-4 py-4 bg-transparent border border-white/10 rounded-xl text-sm text-white focus:ring-2 focus:ring-emerald-400 focus:border-emerald-400 transition-colors outline-none font-medium appearance-none" style="background-color: rgba(255,255,255,0.05);">
              <option value="" disabled selected class="text-gray-900">Select Funding Stage</option>
              <option value="seed" class="text-gray-900">Seed Round (₹1Cr - ₹5Cr)</option>
              <option value="pre-series" class="text-gray-900">Pre-Series A (₹5Cr - ₹15Cr)</option>
              <option value="series-a" class="text-gray-900">Series A & Above (₹15Cr+)</option>
            </select>
          </div>
          
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-link text-white/50"></i>
            </div>
            <input type="url" class="w-full pl-11 pr-4 py-4 bg-white/5 border border-white/10 rounded-xl text-sm text-white focus:ring-2 focus:ring-emerald-400 focus:border-emerald-400 transition-colors outline-none placeholder-white/50 font-medium" placeholder="Link to Pitch Deck (G-Drive/DocSend)" required>
          </div>
          
          <button type="submit" class="w-full bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white font-bold py-4.5 px-6 rounded-xl transition-all duration-300 shadow-[0_0_20px_rgba(16,185,129,0.4)] hover:shadow-[0_0_30px_rgba(16,185,129,0.6)] flex items-center justify-center gap-3 mt-6 group">
            Upload Pitch Deck
            <i class="fas fa-arrow-right text-sm transition-transform group-hover:translate-x-1"></i>
          </button>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- About & Solutions (Split View) -->
<section class="py-24 bg-white overflow-hidden">
  <div class="max-w-7xl mx-auto px-4">
    <div class="grid lg:grid-cols-2 gap-16 items-center">
      <div class="gsap-reveal relative">
        <div class="absolute -inset-4 bg-emerald-50 rounded-[3rem] transform -rotate-3 z-0"></div>
        <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Startup Team" class="relative z-10 w-full h-[500px] object-cover rounded-[2.5rem] shadow-2xl">
      </div>
      
      <div class="gsap-reveal">
        <div class="text-emerald-600 font-bold text-[10px] tracking-widest uppercase mb-2">Beyond Just Capital</div>
        <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-6 tracking-tight">Why Equity Funding?</h2>
        <p class="text-gray-500 font-medium mb-10 leading-relaxed">Unlike debt, equity funding does not require monthly EMIs or collaterals. You partner with experienced investors who bring capital, deep industry connections, and strategic mentorship to exponentially scale your business.</p>
        
        <div class="space-y-6">
          <div class="flex gap-5 items-start p-4 bg-gray-50 rounded-2xl border border-gray-100 transition-colors hover:border-emerald-100 hover:bg-emerald-50/30">
            <div class="w-12 h-12 rounded-xl bg-emerald-100 text-emerald-600 flex items-center justify-center shrink-0">
              <i class="fas fa-seedling text-xl"></i>
            </div>
            <div>
              <h4 class="font-bold text-gray-900 mb-1">Seed & Angel Rounds</h4>
              <p class="text-sm text-gray-500">Early-stage capital to validate your product-market fit and build your core team.</p>
            </div>
          </div>
          
          <div class="flex gap-5 items-start p-4 bg-gray-50 rounded-2xl border border-gray-100 transition-colors hover:border-teal-100 hover:bg-teal-50/30">
            <div class="w-12 h-12 rounded-xl bg-teal-100 text-teal-600 flex items-center justify-center shrink-0">
              <i class="fas fa-chart-pie text-xl"></i>
            </div>
            <div>
              <h4 class="font-bold text-gray-900 mb-1">Series A, B & C</h4>
              <p class="text-sm text-gray-500">Growth capital to scale operations, expand into new markets, and acquire customers.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Benefits Grid -->
<section class="py-24 bg-slate-50">
  <div class="max-w-7xl mx-auto px-4">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">The Equity Advantage</h2>
      <p class="text-gray-500 font-medium max-w-2xl mx-auto">Supercharge your growth with strategic investor partnerships.</p>
    </div>
    
    <div class="grid md:grid-cols-3 gap-8">
      <div class="bg-white rounded-[2rem] p-8 shadow-sm border border-gray-100 hover:shadow-xl transition-shadow gsap-reveal">
        <div class="w-16 h-16 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center text-2xl mb-6">
          <i class="fas fa-shield-alt"></i>
        </div>
        <h3 class="font-black text-xl text-gray-900 mb-3">No Repayment Burden</h3>
        <p class="text-gray-500 text-sm leading-relaxed">Focus 100% of your cash flow on growth rather than servicing debt. Investors win only when you win.</p>
      </div>
      
      <div class="bg-white rounded-[2rem] p-8 shadow-sm border border-gray-100 hover:shadow-xl transition-shadow gsap-reveal">
        <div class="w-16 h-16 bg-purple-50 text-purple-600 rounded-2xl flex items-center justify-center text-2xl mb-6">
          <i class="fas fa-network-wired"></i>
        </div>
        <h3 class="font-black text-xl text-gray-900 mb-3">Strategic Networking</h3>
        <p class="text-gray-500 text-sm leading-relaxed">Unlock access to top-tier talent, potential B2B clients, and subsequent rounds of funding through your VC's network.</p>
      </div>
      
      <div class="bg-white rounded-[2rem] p-8 shadow-sm border border-gray-100 hover:shadow-xl transition-shadow gsap-reveal">
        <div class="w-16 h-16 bg-amber-50 text-amber-600 rounded-2xl flex items-center justify-center text-2xl mb-6">
          <i class="fas fa-chess-knight"></i>
        </div>
        <h3 class="font-black text-xl text-gray-900 mb-3">Expert Mentorship</h3>
        <p class="text-gray-500 text-sm leading-relaxed">Gain board members who have successfully scaled multiple startups and can guide your strategic vision.</p>
      </div>
    </div>
  </div>
</section>

<!-- Eligibility & Required Docs (Dark Theme) -->
<section class="py-24 bg-slate-900 text-white relative">
  <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')] opacity-5 bg-cover bg-center bg-fixed"></div>
  <div class="max-w-7xl mx-auto px-4 relative z-10">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black mb-4 tracking-tight">Are You Ready For Funding?</h2>
      <p class="text-slate-400 font-medium">What VCs look for before issuing a term sheet.</p>
    </div>
    
    <div class="grid lg:grid-cols-2 gap-8">
      <div class="bg-white/5 border border-white/10 rounded-[2.5rem] p-10 backdrop-blur-md gsap-reveal hover:bg-white/10 transition-colors">
        <h3 class="text-2xl font-black mb-8 text-emerald-400 flex items-center gap-3">
          <i class="fas fa-clipboard-check"></i> Key Evaluation Criteria
        </h3>
        <div class="space-y-6">
          <div class="flex items-start gap-4">
            <div class="w-10 h-10 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0 border border-emerald-500/30">1</div>
            <div>
              <h4 class="font-bold text-gray-100">Large Addressable Market</h4>
              <p class="text-sm text-slate-400 mt-1">Operating in a rapidly growing TAM (Total Addressable Market).</p>
            </div>
          </div>
          <div class="flex items-start gap-4">
            <div class="w-10 h-10 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0 border border-emerald-500/30">2</div>
            <div>
              <h4 class="font-bold text-gray-100">Strong Founding Team</h4>
              <p class="text-sm text-slate-400 mt-1">Founders with domain expertise and a proven track record of execution.</p>
            </div>
          </div>
          <div class="flex items-start gap-4">
            <div class="w-10 h-10 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0 border border-emerald-500/30">3</div>
            <div>
              <h4 class="font-bold text-gray-100">Traction & Moat</h4>
              <p class="text-sm text-slate-400 mt-1">Demonstrable early revenue, strong user retention, and a defensible competitive advantage.</p>
            </div>
          </div>
        </div>
      </div>
      
      <div class="bg-white/5 border border-white/10 rounded-[2.5rem] p-10 backdrop-blur-md gsap-reveal hover:bg-white/10 transition-colors">
        <h3 class="text-2xl font-black mb-8 text-teal-400 flex items-center gap-3">
          <i class="fas fa-folder-open"></i> Essential Documents
        </h3>
        <ul class="space-y-5">
          <li class="flex items-center gap-4 bg-slate-800/50 p-4 rounded-xl border border-white/5">
            <i class="fas fa-presentation text-2xl text-teal-500"></i>
            <div>
              <div class="font-bold text-gray-200">Pitch Deck (10-15 Slides)</div>
              <div class="text-xs text-slate-400">Problem, Solution, Market, Traction.</div>
            </div>
          </li>
          <li class="flex items-center gap-4 bg-slate-800/50 p-4 rounded-xl border border-white/5">
            <i class="fas fa-file-excel text-2xl text-teal-500"></i>
            <div>
              <div class="font-bold text-gray-200">Financial Projections</div>
              <div class="text-xs text-slate-400">3-Year detailed financial model & burn rate.</div>
            </div>
          </li>
          <li class="flex items-center gap-4 bg-slate-800/50 p-4 rounded-xl border border-white/5">
            <i class="fas fa-chart-pie text-2xl text-teal-500"></i>
            <div>
              <div class="font-bold text-gray-200">Cap Table</div>
              <div class="text-xs text-slate-400">Current shareholding structure.</div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- Timeline Section -->
<section class="py-24 bg-white relative">
  <div class="max-w-7xl mx-auto px-4">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">The Investment Journey</h2>
      <p class="text-gray-500 font-medium">Our streamlined process to get you funded.</p>
    </div>
    
    <div class="relative max-w-5xl mx-auto gsap-reveal">
      <!-- Line connecting steps -->
      <div class="hidden md:block absolute top-1/2 left-0 w-full h-1 bg-gradient-to-r from-emerald-100 via-teal-100 to-emerald-100 -translate-y-1/2"></div>
      
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8 relative z-10">
        <!-- Step 1 -->
        <div class="text-center group">
          <div class="w-16 h-16 mx-auto bg-white border-4 border-emerald-500 text-emerald-600 rounded-full flex items-center justify-center text-xl shadow-lg mb-4 group-hover:scale-110 transition-transform bg-clip-padding">1</div>
          <h4 class="font-bold text-gray-900 mb-1">Deck Screening</h4>
          <p class="text-xs text-gray-500">Initial review of your pitch and metrics.</p>
        </div>
        <!-- Step 2 -->
        <div class="text-center group">
          <div class="w-16 h-16 mx-auto bg-white border-4 border-teal-500 text-teal-600 rounded-full flex items-center justify-center text-xl shadow-lg mb-4 group-hover:scale-110 transition-transform bg-clip-padding">2</div>
          <h4 class="font-bold text-gray-900 mb-1">Partner Pitch</h4>
          <p class="text-xs text-gray-500">Present to the investment committee.</p>
        </div>
        <!-- Step 3 -->
        <div class="text-center group">
          <div class="w-16 h-16 mx-auto bg-white border-4 border-emerald-500 text-emerald-600 rounded-full flex items-center justify-center text-xl shadow-lg mb-4 group-hover:scale-110 transition-transform bg-clip-padding">3</div>
          <h4 class="font-bold text-gray-900 mb-1">Due Diligence</h4>
          <p class="text-xs text-gray-500">Legal and financial audit processes.</p>
        </div>
        <!-- Step 4 -->
        <div class="text-center group">
          <div class="w-16 h-16 mx-auto bg-white border-4 border-teal-500 text-teal-600 rounded-full flex items-center justify-center text-xl shadow-lg mb-4 group-hover:scale-110 transition-transform bg-clip-padding">4</div>
          <h4 class="font-bold text-gray-900 mb-1">Term Sheet</h4>
          <p class="text-xs text-gray-500">Deal closure and funds transferred.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQs & Testimonial -->
<section class="py-24 bg-slate-50 border-t border-gray-100">
  <div class="max-w-7xl mx-auto px-4">
    <div class="grid lg:grid-cols-2 gap-16">
      <!-- FAQs -->
      <div class="gsap-reveal">
        <h2 class="text-3xl font-black text-[#0f172a] mb-8 tracking-tight">Investment FAQs</h2>
        <div class="space-y-4">
          <div class="bg-white border border-gray-200 rounded-2xl overflow-hidden shadow-sm">
            <button class="w-full text-left px-6 py-5 flex items-center justify-between outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('rotate-45');">
              <span class="font-bold text-gray-900">How much equity do I need to dilute?</span>
              <i class="fas fa-plus text-emerald-600 transition-transform duration-300"></i>
            </button>
            <div class="px-6 pb-5 text-gray-500 text-sm hidden font-medium">
              Typically, seed stage companies dilute between 10% to 20% per round. The exact percentage depends entirely on your valuation and the amount raised.
            </div>
          </div>
          
          <div class="bg-white border border-gray-200 rounded-2xl overflow-hidden shadow-sm">
            <button class="w-full text-left px-6 py-5 flex items-center justify-between outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('rotate-45');">
              <span class="font-bold text-gray-900">How long does the funding process take?</span>
              <i class="fas fa-plus text-emerald-600 transition-transform duration-300"></i>
            </button>
            <div class="px-6 pb-5 text-gray-500 text-sm hidden font-medium">
              From the initial pitch to money in the bank, the process usually takes 2 to 4 months, heavily dependent on the speed of the due diligence process.
            </div>
          </div>
        </div>
      </div>
      
      <!-- Testimonial -->
      <div class="gsap-reveal">
        <h2 class="text-3xl font-black text-[#0f172a] mb-8 tracking-tight">Founder's Journey</h2>
        <div class="bg-slate-900 rounded-[2rem] p-10 shadow-2xl relative text-white">
          <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1553877522-43269d4ea984?ixlib=rb-4.0.3')] opacity-10 bg-cover bg-center rounded-[2rem]"></div>
          <i class="fas fa-quote-left text-5xl text-emerald-500/20 absolute top-8 right-8"></i>
          <div class="relative z-10">
            <div class="flex text-amber-400 text-sm mb-6">
              <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
            </div>
            <p class="text-slate-300 font-medium leading-relaxed mb-8 italic text-lg">"Securing our Series A completely transformed our trajectory. The expertise and network our investors brought to the board were even more valuable than the ₹25 Cr capital itself."</p>
            <div class="flex items-center gap-4">
              <img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Founder" class="w-14 h-14 rounded-full object-cover border-2 border-emerald-500">
              <div>
                <div class="font-black text-white">Priya Sharma</div>
                <div class="text-xs text-emerald-400 font-bold tracking-wider">CEO, FinTech Unicorn</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- WhatsApp CTA -->
<section class="py-20 bg-gradient-to-br from-slate-900 via-[#0f172a] to-emerald-900 border-t border-white/10">
  <div class="max-w-7xl mx-auto px-4 text-center gsap-reveal">
    <h2 class="text-3xl md:text-5xl font-black text-white mb-6 tracking-tight">Discuss Your Funding Needs</h2>
    <p class="text-emerald-100 mb-10 max-w-2xl mx-auto font-medium text-lg">Schedule a confidential consultation with our capital raising experts.</p>
    
    <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
      <a href="https://wa.me/919876543210" class="w-full sm:w-auto bg-[#25D366] hover:bg-[#20bd5a] text-white font-bold py-4.5 px-8 rounded-full transition-transform hover:scale-105 shadow-xl flex items-center justify-center gap-3 border border-white/20 text-lg">
        <i class="fab fa-whatsapp text-2xl"></i> Connect on WhatsApp
      </a>
    </div>
  </div>
</section>
'''

with open(r'c:\Users\Priya\Documents\udyog\equity.html', 'r', encoding='utf-8', errors='ignore') as f:
    html_content = f.read()

style_block = """
<style>
@keyframes floatForm {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}
@keyframes glowForm {
  0% { box-shadow: 0 0 15px rgba(16, 185, 129, 0.2), 0 20px 40px rgba(0,0,0,0.4); }
  50% { box-shadow: 0 0 40px rgba(16, 185, 129, 0.6), 0 30px 60px rgba(0,0,0,0.6); }
  100% { box-shadow: 0 0 15px rgba(16, 185, 129, 0.2), 0 20px 40px rgba(0,0,0,0.4); }
}
.premium-form-anim {
  animation: floatForm 6s ease-in-out infinite, glowForm 4s ease-in-out infinite;
  border: 1px solid rgba(255,255,255,0.15) !important;
}
</style>
"""
if "premium-form-anim" not in html_content:
    if "</head>" in html_content:
        html_content = html_content.replace("</head>", style_block + "\n</head>")

header_end = html_content.find('</header>') + len('</header>')
footer_start = html_content.find('<!-- Footer -->')
if footer_start == -1:
    footer_start = html_content.find('<footer')

if header_end != -1 and footer_start != -1:
    first_section = html_content.find('<section', header_end)
    if first_section != -1:
        new_content = html_content[:first_section] + equity_main_content + '\n' + html_content[footer_start:]
        with open(r'c:\Users\Priya\Documents\udyog\equity.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully built equity.html!")
    else:
        print("Error: Could not find first <section> in equity.html")
else:
    print("Error: Could not find header or footer in equity.html")
