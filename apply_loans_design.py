import os
import re

filepath = r"c:\Users\Priya\Documents\udyog\loans.html"

new_main_content = '''
<!-- HERO SECTION -->
<section class="min-h-screen bg-slate-900 relative pt-32 pb-20 flex items-center overflow-hidden" id="hero">
  <div class="absolute inset-0 bg-gradient-to-br from-indigo-900 via-slate-900 to-[#1a237e] opacity-90"></div>
  <div class="absolute inset-0 opacity-[0.03]" style="background-image: linear-gradient(rgba(255, 255, 255, 1) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 1) 1px, transparent 1px); background-size: 40px 40px;"></div>
  
  <div class="max-w-7xl mx-auto px-4 relative z-10 w-full mt-10">
    <div class="grid lg:grid-cols-2 gap-12 lg:gap-8 items-center">
      <!-- Left Content -->
      <div class="text-white gsap-reveal">
        <div class="inline-flex items-center gap-2 bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 rounded-full px-4 py-1.5 mb-6 shadow-[0_0_15px_rgba(99,102,241,0.2)]">
          <div class="w-2 h-2 bg-indigo-400 rounded-full animate-pulse shadow-[0_0_10px_rgba(99,102,241,0.8)]"></div>
          <span class="text-[10px] font-bold tracking-wider uppercase">Enterprise MSME Financing</span>
        </div>
        
        <h1 class="text-5xl md:text-6xl lg:text-[4.5rem] font-black leading-tight mb-6 tracking-tight">
          Unlock Growth with<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-300">Premium Financing</span>
        </h1>
        
        <p class="text-lg md:text-xl text-blue-100/70 mb-12 max-w-lg leading-relaxed font-light">
          Access high-value business loans with <strong class="text-white font-semibold">minimal documentation</strong> and lightning-fast disbursal. Scale your business to new heights today.
        </p>
        
        <div class="flex flex-wrap gap-4 mb-8">
          <div class="flex items-center gap-2 bg-white/5 backdrop-blur-sm border border-white/10 rounded-full px-4 py-2">
            <i class="fas fa-bolt text-yellow-400"></i>
            <span class="text-xs font-semibold">24hr Approval</span>
          </div>
          <div class="flex items-center gap-2 bg-white/5 backdrop-blur-sm border border-white/10 rounded-full px-4 py-2">
            <i class="fas fa-percentage text-green-400"></i>
            <span class="text-xs font-semibold">Lowest Rates</span>
          </div>
          <div class="flex items-center gap-2 bg-white/5 backdrop-blur-sm border border-white/10 rounded-full px-4 py-2">
            <i class="fas fa-shield-alt text-blue-400"></i>
            <span class="text-xs font-semibold">100% Secure</span>
          </div>
        </div>
      </div>
      
      <!-- Right Content: Glassmorphism Form -->
      <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-[2rem] p-8 md:p-10 shadow-2xl relative max-w-md w-full mx-auto lg:ml-auto gsap-reveal reveal-scale">
        <h2 class="text-2xl font-black text-white mb-2 tracking-tight">Apply for Loan</h2>
        <p class="text-sm text-blue-100/70 mb-8 font-medium">Check your eligibility in 60 seconds.</p>
        
        <form class="space-y-4">
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-building text-white/50"></i>
            </div>
            <input type="text" class="w-full pl-11 pr-4 py-3.5 bg-white/5 border border-white/10 rounded-xl text-sm text-white focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 transition-colors outline-none placeholder-white/50 font-medium" placeholder="Business Name" required>
          </div>
          
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-rupee-sign text-white/50"></i>
            </div>
            <select class="w-full pl-11 pr-10 py-3.5 bg-white/5 border border-white/10 rounded-xl text-sm text-white focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 transition-colors outline-none appearance-none font-medium" required>
              <option value="" class="text-gray-900" disabled selected>Loan Amount Required</option>
              <option value="1-10L" class="text-gray-900">₹1 Lakh - ₹10 Lakhs</option>
              <option value="10-50L" class="text-gray-900">₹10 Lakhs - ₹50 Lakhs</option>
              <option value="50L-1Cr" class="text-gray-900">₹50 Lakhs - ₹1 Crore</option>
              <option value="1Cr+" class="text-gray-900">Above ₹1 Crore</option>
            </select>
            <div class="absolute inset-y-0 right-0 pr-4 flex items-center pointer-events-none">
              <i class="fas fa-chevron-down text-white/50 text-xs"></i>
            </div>
          </div>
          
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-phone-alt text-white/50"></i>
            </div>
            <input type="tel" class="w-full pl-11 pr-4 py-3.5 bg-white/5 border border-white/10 rounded-xl text-sm text-white focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 transition-colors outline-none placeholder-white/50 font-medium" placeholder="Mobile Number" required>
          </div>
          
          <button type="submit" class="w-full bg-gradient-to-r from-indigo-500 to-blue-600 hover:from-indigo-600 hover:to-blue-700 text-white font-bold py-4 px-6 rounded-xl transition-all duration-300 shadow-[0_0_20px_rgba(79,70,229,0.3)] hover:shadow-[0_0_30px_rgba(79,70,229,0.5)] flex items-center justify-center gap-3 mt-4 group">
            Check Eligibility 
            <i class="fas fa-arrow-right text-sm transition-transform group-hover:translate-x-1"></i>
          </button>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- Financing Solutions -->
<section class="py-24 bg-gray-50/50 relative overflow-hidden">
  <div class="max-w-7xl mx-auto px-4">
    <div class="text-center mb-16 gsap-reveal">
      <div class="text-indigo-600 font-bold text-[10px] tracking-widest uppercase mb-2">Tailored Solutions</div>
      <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">Financing Designed for You</h2>
      <p class="text-gray-500 font-medium max-w-2xl mx-auto">Choose the perfect financing solution that aligns with your business goals.</p>
    </div>
    
    <div class="grid md:grid-cols-3 gap-8">
      <div class="bg-white rounded-[2rem] p-10 border border-gray-100 shadow-[0_4px_20px_rgba(0,0,0,0.03)] hover:shadow-[0_10px_40px_rgba(0,0,0,0.08)] transition-all duration-500 group gsap-reveal">
        <div class="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-blue-600 group-hover:text-white transition-colors">
          <i class="fas fa-chart-line text-2xl"></i>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3">Working Capital</h3>
        <p class="text-sm text-gray-500 leading-relaxed font-medium">Manage daily operations, inventory, and cash flow smoothly without hurdles.</p>
      </div>
      
      <div class="bg-white rounded-[2rem] p-10 border border-gray-100 shadow-[0_4px_20px_rgba(0,0,0,0.03)] hover:shadow-[0_10px_40px_rgba(0,0,0,0.08)] transition-all duration-500 group gsap-reveal">
        <div class="w-14 h-14 bg-indigo-50 text-indigo-600 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-indigo-600 group-hover:text-white transition-colors">
          <i class="fas fa-cogs text-2xl"></i>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3">Machinery Loan</h3>
        <p class="text-sm text-gray-500 leading-relaxed font-medium">Upgrade your equipment and technology to boost production and efficiency.</p>
      </div>
      
      <div class="bg-white rounded-[2rem] p-10 border border-gray-100 shadow-[0_4px_20px_rgba(0,0,0,0.03)] hover:shadow-[0_10px_40px_rgba(0,0,0,0.08)] transition-all duration-500 group gsap-reveal">
        <div class="w-14 h-14 bg-emerald-50 text-emerald-600 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-emerald-600 group-hover:text-white transition-colors">
          <i class="fas fa-city text-2xl"></i>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3">Term Loans</h3>
        <p class="text-sm text-gray-500 leading-relaxed font-medium">Long-term financing for major business expansions and infrastructure projects.</p>
      </div>
    </div>
  </div>
</section>

<!-- Loan Products -->
<section class="py-24 bg-white relative">
  <div class="max-w-7xl mx-auto px-4">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6 gsap-reveal">
      <div>
        <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">Premium Loan Products</h2>
        <p class="text-gray-500 font-medium">Compare our top financing products and pick what suits you.</p>
      </div>
      <a href="#hero" class="inline-flex items-center gap-2 text-indigo-600 font-bold hover:text-indigo-800 transition-colors">
        Apply Now <i class="fas fa-arrow-right"></i>
      </a>
    </div>
    
    <div class="grid lg:grid-cols-2 gap-8">
      <div class="border border-gray-100 rounded-[2rem] p-8 flex flex-col md:flex-row items-center gap-8 shadow-sm hover:shadow-lg transition-shadow gsap-reveal">
        <div class="w-full md:w-1/3 bg-gray-50 rounded-2xl p-6 text-center border border-gray-100 shrink-0">
          <div class="text-indigo-600 font-black text-3xl mb-1">Up to 50L</div>
          <div class="text-[10px] text-gray-400 font-bold uppercase tracking-wider">Unsecured</div>
        </div>
        <div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">Unsecured Business Loan</h3>
          <p class="text-sm text-gray-500 leading-relaxed mb-4">Collateral-free loans tailored for fast-growing SMEs. Minimal paperwork and quick disbursal.</p>
          <div class="flex gap-4 text-xs font-bold text-gray-700">
            <span class="flex items-center gap-1.5"><i class="fas fa-check-circle text-green-500"></i> No Collateral</span>
            <span class="flex items-center gap-1.5"><i class="fas fa-check-circle text-green-500"></i> Fast Approval</span>
          </div>
        </div>
      </div>
      
      <div class="border border-gray-100 rounded-[2rem] p-8 flex flex-col md:flex-row items-center gap-8 shadow-sm hover:shadow-lg transition-shadow gsap-reveal">
        <div class="w-full md:w-1/3 bg-gray-50 rounded-2xl p-6 text-center border border-gray-100 shrink-0">
          <div class="text-indigo-600 font-black text-3xl mb-1">Up to 5Cr</div>
          <div class="text-[10px] text-gray-400 font-bold uppercase tracking-wider">Secured</div>
        </div>
        <div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">Secured Business Loan</h3>
          <p class="text-sm text-gray-500 leading-relaxed mb-4">High-value financing backed by property or assets, offering the most competitive interest rates.</p>
          <div class="flex gap-4 text-xs font-bold text-gray-700">
            <span class="flex items-center gap-1.5"><i class="fas fa-check-circle text-green-500"></i> Lower Interest</span>
            <span class="flex items-center gap-1.5"><i class="fas fa-check-circle text-green-500"></i> Longer Tenure</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Eligibility Criteria -->
<section class="py-24 bg-gray-900 text-white relative overflow-hidden">
  <div class="absolute inset-0 opacity-10" style="background-image: radial-gradient(circle at 2px 2px, white 1px, transparent 0); background-size: 32px 32px;"></div>
  <div class="max-w-7xl mx-auto px-4 relative z-10">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black mb-4 tracking-tight">Eligibility Criteria</h2>
      <p class="text-gray-400 font-medium">Basic requirements to qualify for our business loans.</p>
    </div>
    
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="bg-white/5 border border-white/10 rounded-[1.5rem] p-8 backdrop-blur-sm gsap-reveal">
        <i class="fas fa-calendar-alt text-2xl text-indigo-400 mb-4"></i>
        <h3 class="text-lg font-bold mb-2">Business Vintage</h3>
        <p class="text-sm text-gray-400">Minimum 2 years of operational history in the same business.</p>
      </div>
      <div class="bg-white/5 border border-white/10 rounded-[1.5rem] p-8 backdrop-blur-sm gsap-reveal">
        <i class="fas fa-chart-pie text-2xl text-pink-400 mb-4"></i>
        <h3 class="text-lg font-bold mb-2">Annual Turnover</h3>
        <p class="text-sm text-gray-400">Minimum annual turnover of ₹10 Lakhs in the previous financial year.</p>
      </div>
      <div class="bg-white/5 border border-white/10 rounded-[1.5rem] p-8 backdrop-blur-sm gsap-reveal">
        <i class="fas fa-tachometer-alt text-2xl text-blue-400 mb-4"></i>
        <h3 class="text-lg font-bold mb-2">Credit Score</h3>
        <p class="text-sm text-gray-400">CIBIL score of 680 or above with a clean repayment track record.</p>
      </div>
      <div class="bg-white/5 border border-white/10 rounded-[1.5rem] p-8 backdrop-blur-sm gsap-reveal">
        <i class="fas fa-file-invoice text-2xl text-emerald-400 mb-4"></i>
        <h3 class="text-lg font-bold mb-2">ITR Returns</h3>
        <p class="text-sm text-gray-400">Filed Income Tax Returns (ITR) for the last 2 consecutive years.</p>
      </div>
    </div>
  </div>
</section>

<!-- Required Documents -->
<section class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4">
    <div class="grid lg:grid-cols-12 gap-16 items-center">
      <div class="lg:col-span-5 gsap-reveal">
        <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-6 tracking-tight">Required Documents</h2>
        <p class="text-gray-500 font-medium leading-relaxed mb-8">
          Keep these documents ready for a seamless and lightning-fast approval process. We've simplified our requirements to ensure you spend less time on paperwork.
        </p>
        <div class="bg-indigo-50 border border-indigo-100 rounded-2xl p-6 flex gap-4 items-start">
          <i class="fas fa-info-circle text-indigo-600 mt-1"></i>
          <p class="text-sm text-indigo-800 font-medium">Soft copies in PDF format are accepted for the initial digital approval process.</p>
        </div>
      </div>
      
      <div class="lg:col-span-7 grid sm:grid-cols-2 gap-6 gsap-reveal">
        <div class="border border-gray-100 rounded-2xl p-6 shadow-sm hover:border-indigo-100 transition-colors">
          <div class="w-10 h-10 bg-gray-50 rounded-lg flex items-center justify-center mb-4">
            <i class="fas fa-id-card text-gray-600"></i>
          </div>
          <h4 class="font-bold text-gray-900 mb-2">KYC Documents</h4>
          <ul class="text-sm text-gray-500 space-y-1">
            <li>&bull; PAN Card</li>
            <li>&bull; Aadhaar Card</li>
            <li>&bull; Passport size photos</li>
          </ul>
        </div>
        
        <div class="border border-gray-100 rounded-2xl p-6 shadow-sm hover:border-indigo-100 transition-colors">
          <div class="w-10 h-10 bg-gray-50 rounded-lg flex items-center justify-center mb-4">
            <i class="fas fa-briefcase text-gray-600"></i>
          </div>
          <h4 class="font-bold text-gray-900 mb-2">Business Proof</h4>
          <ul class="text-sm text-gray-500 space-y-1">
            <li>&bull; GST Registration</li>
            <li>&bull; Udyam Certificate</li>
            <li>&bull; Shop Act License</li>
          </ul>
        </div>
        
        <div class="border border-gray-100 rounded-2xl p-6 shadow-sm hover:border-indigo-100 transition-colors">
          <div class="w-10 h-10 bg-gray-50 rounded-lg flex items-center justify-center mb-4">
            <i class="fas fa-file-invoice-dollar text-gray-600"></i>
          </div>
          <h4 class="font-bold text-gray-900 mb-2">Financial Documents</h4>
          <ul class="text-sm text-gray-500 space-y-1">
            <li>&bull; Last 12 months Bank Statement</li>
            <li>&bull; Last 2 years ITR</li>
            <li>&bull; Audit Report (if applicable)</li>
          </ul>
        </div>
        
        <div class="border border-indigo-50 bg-indigo-50/30 rounded-2xl p-6 shadow-sm flex flex-col justify-center items-center text-center">
          <i class="fas fa-cloud-upload-alt text-3xl text-indigo-400 mb-3"></i>
          <h4 class="font-bold text-gray-900 mb-1">100% Digital</h4>
          <p class="text-xs text-gray-500">Upload securely online</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Timeline / Application Process -->
<section class="py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">How It Works</h2>
      <p class="text-gray-500 font-medium">A transparent and hassle-free 4-step process.</p>
    </div>
    
    <div class="relative max-w-4xl mx-auto gsap-reveal">
      <div class="hidden md:block absolute top-1/2 left-0 w-full h-1 bg-gray-200 -translate-y-1/2 rounded-full"></div>
      
      <div class="grid grid-cols-1 md:grid-cols-4 gap-12 md:gap-6 relative z-10">
        <div class="text-center">
          <div class="w-16 h-16 mx-auto bg-indigo-600 text-white rounded-full flex items-center justify-center text-2xl font-bold border-4 border-white shadow-lg mb-4">1</div>
          <h4 class="font-bold text-gray-900 mb-2">Apply Online</h4>
          <p class="text-xs text-gray-500">Submit your basic details through our secure form.</p>
        </div>
        <div class="text-center">
          <div class="w-16 h-16 mx-auto bg-white text-indigo-600 rounded-full flex items-center justify-center text-2xl font-bold border-4 border-gray-100 shadow-lg mb-4">2</div>
          <h4 class="font-bold text-gray-900 mb-2">Document Verification</h4>
          <p class="text-xs text-gray-500">Upload required KYC and financial proofs digitally.</p>
        </div>
        <div class="text-center">
          <div class="w-16 h-16 mx-auto bg-white text-indigo-600 rounded-full flex items-center justify-center text-2xl font-bold border-4 border-gray-100 shadow-lg mb-4">3</div>
          <h4 class="font-bold text-gray-900 mb-2">Instant Sanction</h4>
          <p class="text-xs text-gray-500">Get your loan approved based on AI-driven analysis.</p>
        </div>
        <div class="text-center">
          <div class="w-16 h-16 mx-auto bg-green-500 text-white rounded-full flex items-center justify-center text-2xl font-bold border-4 border-white shadow-lg mb-4"><i class="fas fa-check"></i></div>
          <h4 class="font-bold text-gray-900 mb-2">Quick Disbursal</h4>
          <p class="text-xs text-gray-500">Funds transferred directly to your bank account.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQs -->
<section class="py-24 bg-white" id="faq">
  <div class="max-w-4xl mx-auto px-4">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">Frequently Asked Questions</h2>
      <p class="text-gray-500 font-medium">Everything you need to know about our business loans.</p>
    </div>
    
    <div class="space-y-4 gsap-reveal">
      <div class="border border-gray-100 rounded-[1.5rem] overflow-hidden group hover:border-gray-200 transition-colors shadow-sm">
        <button class="w-full text-left px-8 py-6 flex items-center justify-between bg-white hover:bg-gray-50/50 transition-colors outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
          <span class="font-bold text-gray-900 text-lg">What is the minimum credit score required?</span>
          <div class="w-8 h-8 rounded-full bg-indigo-50 flex items-center justify-center shrink-0">
            <i class="fas fa-plus text-indigo-600 text-sm transition-transform"></i>
          </div>
        </button>
        <div class="px-8 pb-6 text-gray-500 text-sm leading-relaxed hidden font-medium">
          A CIBIL score of 680 or higher is generally required. However, we also look at other factors like your business cash flow and overall financial health.
        </div>
      </div>
      
      <div class="border border-gray-100 rounded-[1.5rem] overflow-hidden group hover:border-gray-200 transition-colors shadow-sm">
        <button class="w-full text-left px-8 py-6 flex items-center justify-between bg-white hover:bg-gray-50/50 transition-colors outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
          <span class="font-bold text-gray-900 text-lg">Do I need to provide collateral?</span>
          <div class="w-8 h-8 rounded-full bg-indigo-50 flex items-center justify-center shrink-0">
            <i class="fas fa-plus text-indigo-600 text-sm transition-transform"></i>
          </div>
        </button>
        <div class="px-8 pb-6 text-gray-500 text-sm leading-relaxed hidden font-medium">
          We offer both Secured and Unsecured loans. For Unsecured Business Loans up to ₹50 Lakhs, no collateral is required.
        </div>
      </div>
      
      <div class="border border-gray-100 rounded-[1.5rem] overflow-hidden group hover:border-gray-200 transition-colors shadow-sm">
        <button class="w-full text-left px-8 py-6 flex items-center justify-between bg-white hover:bg-gray-50/50 transition-colors outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
          <span class="font-bold text-gray-900 text-lg">How quickly will the funds be disbursed?</span>
          <div class="w-8 h-8 rounded-full bg-indigo-50 flex items-center justify-center shrink-0">
            <i class="fas fa-plus text-indigo-600 text-sm transition-transform"></i>
          </div>
        </button>
        <div class="px-8 pb-6 text-gray-500 text-sm leading-relaxed hidden font-medium">
          Once your application is approved and documents are verified, the funds are typically disbursed to your registered bank account within 24 to 48 hours.
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Testimonials -->
<section class="py-24 bg-[#0f172a] text-white">
  <div class="max-w-7xl mx-auto px-4">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black mb-4 tracking-tight">Trusted by Businesses</h2>
      <p class="text-gray-400 font-medium">See what our successful clients have to say.</p>
    </div>
    
    <div class="grid md:grid-cols-3 gap-8">
      <div class="bg-white/5 border border-white/10 rounded-[2rem] p-8 gsap-reveal">
        <div class="flex text-yellow-400 text-sm mb-4">
          <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
        </div>
        <p class="text-gray-300 text-sm leading-relaxed mb-6 italic">"The unsecured loan process was incredibly smooth. We got our funds in just 2 days, which helped us clear our inventory bottlenecks instantly."</p>
        <div class="flex items-center gap-4">
          <img src="https://i.pravatar.cc/100?img=11" alt="Rajesh K." class="w-12 h-12 rounded-full object-cover">
          <div>
            <div class="font-bold text-white text-sm">Rajesh K.</div>
            <div class="text-[10px] text-gray-400 uppercase tracking-wider">Manufacturer</div>
          </div>
        </div>
      </div>
      
      <div class="bg-white/5 border border-white/10 rounded-[2rem] p-8 gsap-reveal">
        <div class="flex text-yellow-400 text-sm mb-4">
          <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
        </div>
        <p class="text-gray-300 text-sm leading-relaxed mb-6 italic">"Outstanding customer support. They guided us through the entire secured loan process and offered us a highly competitive interest rate."</p>
        <div class="flex items-center gap-4">
          <img src="https://i.pravatar.cc/100?img=44" alt="Sneha Sharma" class="w-12 h-12 rounded-full object-cover">
          <div>
            <div class="font-bold text-white text-sm">Sneha Sharma</div>
            <div class="text-[10px] text-gray-400 uppercase tracking-wider">IT Services</div>
          </div>
        </div>
      </div>
      
      <div class="bg-white/5 border border-white/10 rounded-[2rem] p-8 gsap-reveal">
        <div class="flex text-yellow-400 text-sm mb-4">
          <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star-half-alt"></i>
        </div>
        <p class="text-gray-300 text-sm leading-relaxed mb-6 italic">"Minimal documentation and zero hidden charges. Highly recommend their financing solutions for any growing MSME."</p>
        <div class="flex items-center gap-4">
          <img src="https://i.pravatar.cc/100?img=33" alt="Amit Patel" class="w-12 h-12 rounded-full object-cover">
          <div>
            <div class="font-bold text-white text-sm">Amit Patel</div>
            <div class="text-[10px] text-gray-400 uppercase tracking-wider">Retail Chain</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA / WhatsApp -->
<section class="py-20 bg-gradient-to-r from-indigo-600 to-[#1a237e]">
  <div class="max-w-7xl mx-auto px-4 text-center gsap-reveal">
    <h2 class="text-3xl md:text-4xl font-black text-white mb-6 tracking-tight">Need Help Choosing the Right Loan?</h2>
    <p class="text-indigo-100 mb-10 max-w-2xl mx-auto font-medium">Talk directly to our financing experts and get personalized advice tailored to your business needs.</p>
    
    <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
      <a href="https://wa.me/919876543210" class="w-full sm:w-auto bg-[#25D366] hover:bg-[#20bd5a] text-white font-bold py-4 px-8 rounded-xl transition-colors shadow-lg flex items-center justify-center gap-3">
        <i class="fab fa-whatsapp text-xl"></i> Chat on WhatsApp
      </a>
      <a href="tel:+919876543210" class="w-full sm:w-auto bg-white hover:bg-gray-50 text-indigo-900 font-bold py-4 px-8 rounded-xl transition-colors shadow-lg flex items-center justify-center gap-3">
        <i class="fas fa-phone-alt"></i> Call an Expert
      </a>
    </div>
  </div>
</section>
'''

with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace everything between the first <section> and <!-- Footer -->
header_end = content.find('</header>') + len('</header>')
footer_start = content.find('<!-- Footer -->')
if footer_start == -1:
    footer_start = content.find('<footer')

if header_end != -1 and footer_start != -1:
    first_section = content.find('<section', header_end)
    if first_section != -1:
        new_content = content[:first_section] + new_main_content + '\n' + content[footer_start:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated loans.html!")
    else:
        print("Error: Could not find first <section>")
else:
    print("Error: Could not find header or footer")
