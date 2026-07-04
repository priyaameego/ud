import os
import re

filepath = r"c:\Users\Priya\Documents\udyog\grants.html"

new_main_content = '''
<!-- HERO SECTION -->
<section class="min-h-screen bg-[#1a237e] relative pt-32 pb-20 flex items-center overflow-hidden" id="hero">
  <!-- Subtle grid/pattern overlay -->
  <div class="absolute inset-0 opacity-[0.03]" style="background-image: linear-gradient(rgba(255, 255, 255, 1) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 1) 1px, transparent 1px); background-size: 40px 40px;"></div>
  
  <div class="max-w-7xl mx-auto px-4 relative z-10 w-full mt-10">
    <div class="grid lg:grid-cols-2 gap-12 lg:gap-8 items-center">
      <!-- Left Content -->
      <div class="text-white gsap-reveal">
        <div class="inline-flex items-center gap-2 bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 rounded-full px-4 py-1.5 mb-6 shadow-[0_0_15px_rgba(16,185,129,0.2)]">
          <div class="w-2 h-2 bg-emerald-400 rounded-full animate-pulse shadow-[0_0_10px_rgba(16,185,129,0.8)]"></div>
          <span class="text-[10px] font-bold tracking-wider uppercase">Government Grants & Business Funding Assistance</span>
        </div>
        
        <h1 class="text-5xl md:text-6xl lg:text-[4.5rem] font-black leading-tight mb-6 tracking-tight">
          Maximize Your<br>Grant Potential
        </h1>
        
        <p class="text-lg md:text-xl text-blue-100/70 mb-12 max-w-lg leading-relaxed font-light">
          Access <strong class="text-white font-semibold">Government Grants & Subsidies</strong> without equity dilution. From Startup India to MSME schemes, we help you identify and secure the funds your business deserves.
        </p>
        
        <div class="flex items-center gap-5">
          <div class="flex -space-x-3">
            <img class="w-12 h-12 rounded-full border-2 border-[#1a237e] object-cover shadow-md" src="https://i.pravatar.cc/100?img=68" alt="Avatar">
            <img class="w-12 h-12 rounded-full border-2 border-[#1a237e] object-cover shadow-md" src="https://i.pravatar.cc/100?img=59" alt="Avatar">
            <img class="w-12 h-12 rounded-full border-2 border-[#1a237e] object-cover shadow-md" src="https://i.pravatar.cc/100?img=47" alt="Avatar">
            <div class="w-12 h-12 rounded-full border-2 border-[#1a237e] bg-white flex items-center justify-center text-xs font-bold text-[#1a237e] shadow-md z-10">+65k</div>
          </div>
          <div>
            <div class="flex text-yellow-400 text-sm gap-0.5">
              <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
            </div>
            <div class="text-xs font-bold mt-1.5 text-blue-100/90 tracking-wide">Over 65,000+ Business Onboarded</div>
          </div>
        </div>
      </div>
      
      <!-- Right Content: Form Card -->
      <div class="bg-white rounded-[2rem] p-8 md:p-10 shadow-2xl relative max-w-md w-full mx-auto lg:ml-auto gsap-reveal reveal-scale">
        <div class="absolute -top-4 right-8 bg-green-700 text-white text-[11px] font-bold px-4 py-1.5 rounded-full shadow-lg tracking-wider">Step 1/2</div>
        
        <h2 class="text-2xl font-black text-gray-900 mb-2 tracking-tight">Start Your Application</h2>
        <p class="text-sm text-gray-500 mb-8 font-medium">Fill in the form and complete process to receive your certificate.</p>
        
        <!-- Progress Bar -->
        <div class="w-full bg-gray-100 h-1 rounded-full mb-8 relative">
          <div class="absolute top-0 left-0 h-full rounded-full bg-gradient-to-r from-[#1a237e] to-orange-500 w-1/2"></div>
        </div>
        
        <form class="space-y-4">
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-building text-gray-400"></i>
            </div>
            <input type="text" class="w-full pl-11 pr-4 py-3.5 border border-gray-200 rounded-xl text-sm focus:ring-2 focus:ring-[#1a237e] focus:border-[#1a237e] transition-colors bg-white outline-none placeholder-gray-400 font-medium" placeholder="Organization / Firm Name" required>
          </div>
          
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-university text-gray-400"></i>
            </div>
            <select class="w-full pl-11 pr-10 py-3.5 border border-gray-200 rounded-xl text-sm text-gray-500 focus:ring-2 focus:ring-[#1a237e] focus:border-[#1a237e] transition-colors bg-white outline-none appearance-none font-medium" required>
              <option value="" disabled selected>Select Organization Type</option>
              <option value="Private Limited">Private Limited</option>
              <option value="LLP">LLP</option>
              <option value="Partnership">Partnership</option>
              <option value="Proprietorship">Proprietorship</option>
            </select>
            <div class="absolute inset-y-0 right-0 pr-4 flex items-center pointer-events-none">
              <i class="fas fa-chevron-down text-gray-400 text-xs"></i>
            </div>
          </div>
          
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-phone-alt text-gray-400"></i>
            </div>
            <input type="tel" class="w-full pl-11 pr-4 py-3.5 border border-gray-200 rounded-xl text-sm focus:ring-2 focus:ring-[#1a237e] focus:border-[#1a237e] transition-colors bg-white outline-none placeholder-gray-400 font-medium" placeholder="Mobile Number" required>
          </div>
          
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <i class="fas fa-envelope text-gray-400"></i>
            </div>
            <input type="email" class="w-full pl-11 pr-4 py-3.5 border border-gray-200 rounded-xl text-sm focus:ring-2 focus:ring-[#1a237e] focus:border-[#1a237e] transition-colors bg-white outline-none placeholder-gray-400 font-medium" placeholder="Email Address" required>
          </div>
          
          <button type="submit" class="w-full bg-[#171c5a] hover:bg-[#1a237e] text-white font-bold py-4 px-6 rounded-xl transition-all duration-300 shadow-md hover:shadow-lg flex items-center justify-center gap-3 mt-4 group">
            Submit your application 
            <i class="fas fa-arrow-right text-sm transition-transform group-hover:translate-x-1"></i>
          </button>
        </form>
        
        <div class="mt-6 flex items-center justify-center gap-2 text-[10px] font-bold tracking-wider text-gray-400 uppercase">
          <i class="fas fa-shield-alt text-green-500 text-sm"></i> 100% SECURE & CONFIDENTIAL
        </div>
      </div>
    </div>
  </div>
</section>

<!-- General Eligibility Criteria -->
<section class="py-24 bg-gray-50/30">
  <div class="max-w-7xl mx-auto px-4">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">General Eligibility Criteria</h2>
      <p class="text-gray-500 font-medium">Most government grants require startups to meet these baseline standards.</p>
    </div>
    
    <div class="grid md:grid-cols-3 gap-6">
      <!-- Card 1 -->
      <div class="bg-gray-50 rounded-[2rem] p-10 text-center border border-gray-100 hover:border-gray-200 transition-all duration-300 gsap-reveal">
        <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm border border-gray-100">
          <i class="fas fa-building text-blue-600 text-xl"></i>
        </div>
        <h3 class="text-xl font-black text-[#0f172a] mb-4 tracking-tight">DPIIT Recognized</h3>
        <p class="text-sm text-gray-500 leading-relaxed font-medium">Must be a DPIIT recognized startup (Private Limited, LLP, or Registered Partnership).</p>
      </div>
      
      <!-- Card 2 -->
      <div class="bg-gray-50 rounded-[2rem] p-10 text-center border border-gray-100 hover:border-gray-200 transition-all duration-300 gsap-reveal">
        <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm border border-gray-100">
          <i class="fas fa-rocket text-orange-500 text-xl"></i>
        </div>
        <h3 class="text-xl font-black text-[#0f172a] mb-4 tracking-tight">Innovation Focus</h3>
        <p class="text-sm text-gray-500 leading-relaxed font-medium">Product or service should work towards innovation, development or improvement of products.</p>
      </div>
      
      <!-- Card 3 -->
      <div class="bg-gray-50 rounded-[2rem] p-10 text-center border border-gray-100 hover:border-gray-200 transition-all duration-300 gsap-reveal">
        <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm border border-gray-100">
          <i class="fas fa-history text-green-600 text-xl"></i>
        </div>
        <h3 class="text-xl font-black text-[#0f172a] mb-4 tracking-tight">Entity Age</h3>
        <p class="text-sm text-gray-500 leading-relaxed font-medium">Period of existence and operations should not be exceeding 10 years from the Date of Incorporation.</p>
      </div>
    </div>
  </div>
</section>

<!-- Search & Disclaimer -->
<section class="py-20 bg-gray-50 relative overflow-hidden">
  <div class="max-w-7xl mx-auto px-4 relative z-10">
    
    <!-- Disclaimer -->
    <div class="bg-white rounded-[1.5rem] p-6 md:p-8 shadow-sm border border-gray-100 mb-10 gsap-reveal">
      <p class="text-xs text-gray-500 leading-relaxed font-medium">
        <strong class="text-gray-700">Disclaimer:</strong> We are a fast-growing online business-services platform dedicated to helping people start and grow their businesses at an affordable cost. Our aim is to support entrepreneurs with their regulatory requirements at every stage, so their business stays compliant and continues to grow. Udyog Suvidha Kendra is a privately owned consultancy and is not associated with, endorsed by, or operated by any government department or official government portal. Many of the registrations and certificates referenced on this website can be applied for directly by the applicant on the relevant official portals, often free of cost or at lower government fees. Any fee charged by us is solely for our professional and application-assistance services, and is separate from any government fee. Udyog Suvidha Kendra&reg; is a registered trademark.
      </p>
    </div>
    
    <!-- Grants Search -->
    <div class="bg-white rounded-[3rem] p-8 md:p-12 shadow-[0_4px_20px_rgba(0,0,0,0.03)] border border-gray-50 flex flex-col md:flex-row md:items-center justify-between gap-8 gsap-reveal">
      <div>
        <div class="text-orange-500 font-bold text-[10px] tracking-widest uppercase mb-2">CURATED LIST</div>
        <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] tracking-tight">Available <span class="text-[#1a237e]">Grants & Funding</span></h2>
      </div>
      
      <div class="relative max-w-sm w-full">
        <div class="absolute inset-y-0 left-0 pl-5 flex items-center pointer-events-none">
          <i class="fas fa-search text-gray-400"></i>
        </div>
        <input type="text" class="w-full pl-12 pr-4 py-4 bg-gray-50/50 border border-gray-100 rounded-full text-sm focus:ring-2 focus:ring-[#1a237e] focus:border-[#1a237e] transition-colors outline-none font-medium text-gray-700" placeholder="Search grants...">
      </div>
    </div>
  </div>
</section>

<!-- Frequently Asked Questions -->
<section class="py-24 bg-white" id="faq">
  <div class="max-w-4xl mx-auto px-4">
    <div class="text-center mb-16 gsap-reveal">
      <h2 class="text-3xl md:text-[2.5rem] font-black text-[#0f172a] mb-4 tracking-tight">Frequently Asked Questions</h2>
      <p class="text-gray-500 font-medium">Everything you need to know about Government Grants.</p>
    </div>
    
    <div class="space-y-4 gsap-reveal">
      <!-- FAQ 1 -->
      <div class="border border-gray-100 rounded-[1.5rem] overflow-hidden group hover:border-gray-200 transition-colors shadow-sm">
        <button class="w-full text-left px-8 py-6 flex items-center justify-between bg-white hover:bg-gray-50/50 transition-colors outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
          <span class="font-bold text-gray-900 text-lg">What is a DPIIT Recognized Startup?</span>
          <div class="w-8 h-8 rounded-full bg-blue-50 flex items-center justify-center shrink-0">
            <i class="fas fa-plus text-[#1a237e] text-sm transition-transform"></i>
          </div>
        </button>
        <div class="px-8 pb-6 text-gray-500 text-sm leading-relaxed hidden font-medium">
          A startup recognized by the Department for Promotion of Industry and Internal Trade (DPIIT) is eligible for various government grants, tax exemptions, and faster patent registrations. It must be a Private Limited Company, LLP, or a Registered Partnership incorporated within the last 10 years.
        </div>
      </div>
      
      <!-- FAQ 2 -->
      <div class="border border-gray-100 rounded-[1.5rem] overflow-hidden group hover:border-gray-200 transition-colors shadow-sm">
        <button class="w-full text-left px-8 py-6 flex items-center justify-between bg-white hover:bg-gray-50/50 transition-colors outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
          <span class="font-bold text-gray-900 text-lg">How long does it take to secure a grant?</span>
          <div class="w-8 h-8 rounded-full bg-blue-50 flex items-center justify-center shrink-0">
            <i class="fas fa-plus text-[#1a237e] text-sm transition-transform"></i>
          </div>
        </button>
        <div class="px-8 pb-6 text-gray-500 text-sm leading-relaxed hidden font-medium">
          The processing time varies depending on the specific scheme. Typically, it can take anywhere from a few weeks to several months. Proper documentation and a strong business plan can significantly speed up the approval process.
        </div>
      </div>
      
      <!-- FAQ 3 -->
      <div class="border border-gray-100 rounded-[1.5rem] overflow-hidden group hover:border-gray-200 transition-colors shadow-sm">
        <button class="w-full text-left px-8 py-6 flex items-center justify-between bg-white hover:bg-gray-50/50 transition-colors outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
          <span class="font-bold text-gray-900 text-lg">Do I have to give up equity for government grants?</span>
          <div class="w-8 h-8 rounded-full bg-blue-50 flex items-center justify-center shrink-0">
            <i class="fas fa-plus text-[#1a237e] text-sm transition-transform"></i>
          </div>
        </button>
        <div class="px-8 pb-6 text-gray-500 text-sm leading-relaxed hidden font-medium">
          No, government grants and subsidies are non-dilutive funding, meaning you do not have to give up any equity or ownership in your business to receive the funds.
        </div>
      </div>
      
      <!-- FAQ 4 -->
      <div class="border border-gray-100 rounded-[1.5rem] overflow-hidden group hover:border-gray-200 transition-colors shadow-sm">
        <button class="w-full text-left px-8 py-6 flex items-center justify-between bg-white hover:bg-gray-50/50 transition-colors outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
          <span class="font-bold text-gray-900 text-lg">Can I apply for multiple grants simultaneously?</span>
          <div class="w-8 h-8 rounded-full bg-blue-50 flex items-center justify-center shrink-0">
            <i class="fas fa-plus text-[#1a237e] text-sm transition-transform"></i>
          </div>
        </button>
        <div class="px-8 pb-6 text-gray-500 text-sm leading-relaxed hidden font-medium">
          Yes, you can apply for multiple grants provided you meet the eligibility criteria for each specific scheme. However, some grants may prohibit double-dipping for the exact same project expense.
        </div>
      </div>
      
      <!-- FAQ 5 -->
      <div class="border border-gray-100 rounded-[1.5rem] overflow-hidden group hover:border-gray-200 transition-colors shadow-sm">
        <button class="w-full text-left px-8 py-6 flex items-center justify-between bg-white hover:bg-gray-50/50 transition-colors outline-none" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('fa-plus'); this.querySelector('i').classList.toggle('fa-minus');">
          <span class="font-bold text-gray-900 text-lg">What documents are typically required?</span>
          <div class="w-8 h-8 rounded-full bg-blue-50 flex items-center justify-center shrink-0">
            <i class="fas fa-plus text-[#1a237e] text-sm transition-transform"></i>
          </div>
        </button>
        <div class="px-8 pb-6 text-gray-500 text-sm leading-relaxed hidden font-medium">
          Standard documents include your Certificate of Incorporation, PAN card, Aadhaar, detailed business plan, financial projections, and DPIIT recognition certificate. Specific schemes may have additional requirements.
        </div>
      </div>
    </div>
  </div>
</section>
'''

with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# To be perfectly safe, let's locate `</header>` and `<footer` and replace everything in between.
header_end = content.find('</header>') + len('</header>')
footer_start = content.find('<!-- Footer -->')
if footer_start == -1:
    footer_start = content.find('<footer')

if header_end != -1 and footer_start != -1:
    # First, let's keep the Javascript blocks that exist right after </header> if any.
    # Actually, we can just replace the whole body. The Javascript blocks for Navbar
    # are usually at the end of the file, or maybe just after header.
    # Let's extract the JS between header and footer just in case it contains navbar JS.
    # Wait, the navbar JS is already in the file.
    
    # Just replace everything between the first <section> and the footer.
    first_section = content.find('<section', header_end)
    if first_section != -1:
        new_content = content[:first_section] + new_main_content + '\n' + content[footer_start:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated grants.html!")
    else:
        print("Error: Could not find first <section>")
else:
    print("Error: Could not find header or footer")
