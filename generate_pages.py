import re

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | MeterPay Ecosystem</title>
    <link rel="stylesheet" href="styles/index.css?v=7">
    <style>
        .page-header {
            padding: 120px 0 60px;
            background: var(--light-pink);
            text-align: center;
        }
        .page-title {
            font-size: 3rem;
            margin-bottom: 20px;
        }
        .page-content {
            padding: 80px 0;
            max-width: 800px;
            margin: 0 auto;
        }
        .page-content h2 { margin-top: 40px; margin-bottom: 20px; font-size: 1.8rem; }
        .page-content p, .page-content li { margin-bottom: 16px; font-size: 1.1rem; line-height: 1.6; color: var(--gray); }
        .page-content ul { margin-left: 20px; margin-bottom: 24px; }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container nav-container">
            <a href="index.html" class="logo">
                <span class="logo-icon">M</span>
                MeterPay
            </a>
            <div class="nav-links">
                <a href="index.html#products">Products</a>
                <a href="index.html#how-it-works">How it works</a>
                <a href="index.html#investors">Investors</a>
                <a href="index.html#faq">FAQ</a>
                <a href="index.html#contact">Contact</a>
            </div>
            <div class="nav-actions">
                <a href="index.html#apply" class="btn-dark">Apply now</a>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <div class="container">
            <h1 class="page-title">{title}</h1>
            <p style="font-size: 1.2rem; color: var(--gray);">{subtitle}</p>
        </div>
    </header>

    <main class="page-content container">
{content}
    </main>
"""

FOOTER = """
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="index.html" class="logo footer-logo">
                        <span class="logo-icon-pink">M</span>
                        <div>MeterPay</div>
                    </a>
                    <p class="footer-desc">MeterPay is building Africa's leading digital platform for energy financing, helping households and businesses access electricity infrastructure through flexible, technology-driven payment solutions.</p>
                </div>
                <div class="footer-links">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="about.html">About us</a></li>
                        <li><a href="careers.html">Careers</a></li>
                        <li><a href="coming-soon.html">Resources</a></li>
                        <li><a href="index.html#contact">Contact us</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>For customers</h4>
                    <ul>
                        <li><a href="index.html#how-it-works">How it works</a></li>
                        <li><a href="index.html#products">Payment plans</a></li>
                        <li><a href="coming-soon.html">Help center</a></li>
                        <li><a href="coming-soon.html">Track installation</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>For partners</h4>
                    <ul>
                        <li><a href="coming-soon.html">Partner with us</a></li>
                        <li><a href="coming-soon.html">Become a distributor</a></li>
                        <li><a href="coming-soon.html">Join our network</a></li>
                        <li><a href="coming-soon.html">Partner portal</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="terms.html">Terms of use</a></li>
                        <li><a href="privacy.html">Privacy policy</a></li>
                        <li><a href="cookies.html">Cookie policy</a></li>
                        <li><a href="disclaimers.html">Disclaimers</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 MeterPay. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
    <script src="scripts/main.js"></script>
</body>
</html>
"""

PAGES = {
    "about.html": {
        "title": "About Us",
        "subtitle": "Powering Nigeria's energy infrastructure through accessible financing.",
        "content": """
        <h2>Our Mission</h2>
        <p>MeterPay is on a mission to democratize access to essential utility infrastructure across Africa. We believe that no household or business should be forced to endure estimated billing simply because of the upfront cost of a smart meter.</p>
        
        <h2>What We Do</h2>
        <p>We are a specialized fintech platform offering Buy Now, Pay Later (BNPL) solutions for electricity meters, solar panels, and smart energy devices. By partnering with leading financial institutions and certified Meter Asset Providers, we've created a seamless ecosystem that takes the friction out of acquiring essential infrastructure.</p>
        
        <h2>Why It Matters</h2>
        <p>With an estimated metering gap of over 7 million households in Nigeria alone, our platform is solving a critical national challenge. Meter ownership guarantees accurate billing, improves energy management, and permanently eliminates the frustration of estimated charges.</p>
        """
    },
    "careers.html": {
        "title": "Careers",
        "subtitle": "Join us in building Africa's leading digital energy financing platform.",
        "content": """
        <h2>Work at MeterPay</h2>
        <p>We are a fast-growing team of engineers, financial experts, and energy professionals passionate about solving real-world infrastructure challenges using technology.</p>
        
        <h2>Current Openings</h2>
        <p>While we don't have any open positions right this second, we are always on the lookout for exceptional talent in Engineering, Product, Sales, and Customer Success.</p>
        <p>Please send your resume to <a href="mailto:careers@meter-pay.com" style="color: var(--primary-dark); font-weight: 500;">careers@meter-pay.com</a> and we will reach out when a role opens up that matches your skillset.</p>
        """
    },
    "privacy.html": {
        "title": "Privacy Policy",
        "subtitle": "How we protect and manage your data.",
        "content": """
        <h2>1. Information We Collect</h2>
        <p>We collect personal information necessary to process your financing application, including your name, address, contact details, Bank Verification Number (BVN), and financial history. This allows our AI underwriting engine to provide instant eligibility decisions.</p>
        
        <h2>2. How We Use Your Data</h2>
        <p>Your data is strictly used to assess creditworthiness, manage your financing account, schedule installations, and comply with regulatory requirements mandated by the Central Bank of Nigeria and the Nigerian Electricity Regulatory Commission (NERC).</p>
        
        <h2>3. Data Security</h2>
        <p>We implement bank-grade encryption (AES-256) and adhere to the Nigeria Data Protection Regulation (NDPR) to ensure your personal and financial information is never compromised or sold to third parties.</p>
        """
    },
    "terms.html": {
        "title": "Terms of Use",
        "subtitle": "The rules and regulations for using MeterPay.",
        "content": """
        <h2>1. Acceptance of Terms</h2>
        <p>By accessing MeterPay, you agree to these Terms of Use. If you do not agree, please do not use our services.</p>
        
        <h2>2. Financing Agreement</h2>
        <p>When you are approved for meter financing, you enter into a legally binding repayment contract. You agree to make timely monthly payments via direct debit, card, or bank transfer for the duration of your chosen 6-36 month plan.</p>
        
        <h2>3. Installation Policy</h2>
        <p>Installations are strictly carried out by our network of authorized Meter Asset Providers. Unauthorized tampering with installed meters violates these terms and may result in the immediate termination of the financing agreement and possible legal action.</p>
        """
    },
    "cookies.html": {
        "title": "Cookie Policy",
        "subtitle": "Understanding how we use cookies.",
        "content": """
        <h2>What Are Cookies?</h2>
        <p>Cookies are small text files stored on your device when you visit our website. They help us understand how you interact with our platform and allow us to improve your experience.</p>
        
        <h2>How We Use Them</h2>
        <p>We use essential cookies to keep you logged in securely. We also use analytical cookies to measure website traffic and performance. You can disable non-essential cookies at any time through your browser settings.</p>
        """
    },
    "disclaimers.html": {
        "title": "Legal Disclaimers",
        "subtitle": "Important legal notices.",
        "content": """
        <h2>No Financial Advice</h2>
        <p>The information provided on this website does not constitute financial, investment, or legal advice. All financing decisions are subject to credit approval and verification.</p>
        
        <h2>Availability</h2>
        <p>MeterPay services are subject to the availability of meters from our Meter Asset Provider partners and the operational coverage of the respective Electricity Distribution Companies (DisCos) in your area.</p>
        """
    },
    "coming-soon.html": {
        "title": "Coming Soon",
        "subtitle": "We're currently building this feature.",
        "content": """
        <div style="text-align: center; padding: 40px 0;">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 24px;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            <h2>Under Construction</h2>
            <p>Our engineering team is working hard to launch this dashboard. Check back soon!</p>
            <a href="index.html" class="btn-dark mt-4" style="display: inline-block;">Return to Homepage</a>
        </div>
        """
    }
}

for filename, data in PAGES.items():
    with open(filename, "w") as f:
        header_text = HEADER.replace("{title}", data["title"]).replace("{subtitle}", data["subtitle"]).replace("{content}", data["content"])
        f.write(header_text + FOOTER)
        
print("Successfully generated all new pages!")

# Also update the index.html footer
with open("index.html", "r") as f:
    index_html = f.read()

# Replace the existing footer-links section
import re
new_links_html = """                <div class="footer-links">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="about.html">About us</a></li>
                        <li><a href="careers.html">Careers</a></li>
                        <li><a href="coming-soon.html">Resources</a></li>
                        <li><a href="index.html#contact">Contact us</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>For customers</h4>
                    <ul>
                        <li><a href="index.html#how-it-works">How it works</a></li>
                        <li><a href="index.html#products">Payment plans</a></li>
                        <li><a href="coming-soon.html">Help center</a></li>
                        <li><a href="coming-soon.html">Track installation</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>For partners</h4>
                    <ul>
                        <li><a href="coming-soon.html">Partner with us</a></li>
                        <li><a href="coming-soon.html">Become a distributor</a></li>
                        <li><a href="coming-soon.html">Join our network</a></li>
                        <li><a href="coming-soon.html">Partner portal</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="terms.html">Terms of use</a></li>
                        <li><a href="privacy.html">Privacy policy</a></li>
                        <li><a href="cookies.html">Cookie policy</a></li>
                        <li><a href="disclaimers.html">Disclaimers</a></li>
                    </ul>
                </div>"""

pattern = re.compile(r'<div class="footer-links">.*?<h4>Legal</h4>.*?</ul>\n                </div>', re.DOTALL)
index_html = pattern.sub(new_links_html, index_html)

with open("index.html", "w") as f:
    f.write(index_html)
print("Updated index.html footer.")
