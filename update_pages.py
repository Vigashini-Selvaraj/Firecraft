wholesale_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Wholesale Inquiries | Firecraft Hot Sauce</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="assets/images/firecraft_logo.png">
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body { background: #0b0908; color: #f7f2ea; font-family: 'Manrope', sans-serif; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 60px 20px; margin: 0; }
    html.light-theme body { background: #f4ede3; color: #171513; }
    .page-card { background: #151311; padding: 60px 50px; max-width: 800px; width: 100%; border: 1px solid rgba(247, 242, 234, 0.12); box-shadow: 0 20px 40px rgba(0,0,0,0.3); border-radius: 8px; }
    html.light-theme .page-card { background: #ffffff; border-color: rgba(23, 21, 19, 0.15); }
    .logo-link { display: block; text-align: center; margin-bottom: 30px; text-decoration: none; }
    .logo-img { height: 75px; width: auto; object-fit: contain; margin: 0 auto; display: inline-block; }
    .page-card h1 { font-family: 'DM Serif Display', serif; font-size: 38px; color: #e63b2e; margin-bottom: 30px; text-align: center; }
    .content-box { font-size: 16px; line-height: 1.8; color: #b6aaa0; text-align: left; }
    html.light-theme .content-box { color: #5e5952; }
    .content-box h2 { color: #f7f2ea; font-size: 22px; margin-bottom: 15px; margin-top: 30px; font-weight: 700; border-bottom: 1px solid rgba(247,242,234,0.1); padding-bottom: 10px; }
    html.light-theme .content-box h2 { color: #171513; border-color: rgba(23,21,19,0.1); }
    .content-box ul { padding-left: 20px; margin-bottom: 20px; }
    .content-box li { margin-bottom: 12px; }
  </style>
</head>
<body>
  <div class="page-card">
    <a href="index.html" class="logo-link">
      <img src="assets/images/firecraft_logo.png" alt="Firecraft Logo" class="logo-img">
    </a>
    <h1>Wholesale Inquiries</h1>
    <div class="content-box">
      <h2>Partner with Firecraft</h2>
      <p>Bring the heat to your shelves! We partner with independent retailers, specialty food stores, and restaurants nationwide. Our wholesale program offers competitive pricing, fast shipping, and robust marketing support.</p>
      
      <h2>Wholesale Requirements</h2>
      <ul>
        <li><strong>Minimum Order Quantity:</strong> 4 cases (48 bottles total) per order.</li>
        <li><strong>Documentation:</strong> You must provide a valid Tax ID and a Reseller Certificate.</li>
        <li><strong>Lead Time:</strong> Most wholesale orders are fulfilled and shipped within 3-5 business days.</li>
        <li><strong>Payment Terms:</strong> Initial orders require payment upfront. Net-30 terms are available for established partners after 3 successful orders.</li>
        <li><strong>Pricing Integrity:</strong> Partners must agree to our MAP (Minimum Advertised Price) policy to maintain brand value.</li>
      </ul>
      
      <h2>How to Apply</h2>
      <p>Send an email to <strong>wholesale@firecraft.com</strong> with your business name, location, and a brief description of your store or restaurant. Our wholesale team will review your application and get back to you within 2 business days with our complete product catalog and pricing sheet.</p>
    </div>
  </div>
  <script>
    if (localStorage.getItem('firecraftTheme') === 'light') { document.documentElement.classList.add('light-theme'); }
  </script>
</body>
</html>"""

privacy_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Privacy Policy | Firecraft Hot Sauce</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="assets/images/firecraft_logo.png">
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body { background: #0b0908; color: #f7f2ea; font-family: 'Manrope', sans-serif; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 60px 20px; margin: 0; }
    html.light-theme body { background: #f4ede3; color: #171513; }
    .page-card { background: #151311; padding: 60px 50px; max-width: 800px; width: 100%; border: 1px solid rgba(247, 242, 234, 0.12); box-shadow: 0 20px 40px rgba(0,0,0,0.3); border-radius: 8px; }
    html.light-theme .page-card { background: #ffffff; border-color: rgba(23, 21, 19, 0.15); }
    .logo-link { display: block; text-align: center; margin-bottom: 30px; text-decoration: none; }
    .logo-img { height: 75px; width: auto; object-fit: contain; margin: 0 auto; display: inline-block; }
    .page-card h1 { font-family: 'DM Serif Display', serif; font-size: 38px; color: #e63b2e; margin-bottom: 30px; text-align: center; }
    .content-box { font-size: 15px; line-height: 1.8; color: #b6aaa0; text-align: left; }
    html.light-theme .content-box { color: #5e5952; }
    .content-box h2 { color: #f7f2ea; font-size: 20px; margin-bottom: 10px; margin-top: 25px; }
    html.light-theme .content-box h2 { color: #171513; }
    .agreement-section { margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(247, 242, 234, 0.2); }
    html.light-theme .agreement-section { border-color: rgba(23, 21, 19, 0.2); }
    .custom-checkbox { display: flex; align-items: flex-start; gap: 12px; cursor: pointer; margin-bottom: 20px; }
    .custom-checkbox input { display: none; }
    .checkmark { min-width: 20px; height: 20px; border: 1px solid rgba(247,242,234,0.4); display: flex; align-items: center; justify-content: center; margin-top: 3px; border-radius: 3px; }
    html.light-theme .checkmark { border-color: rgba(23,21,19,0.4); }
    .custom-checkbox input:checked ~ .checkmark { background: #e63b2e; border-color: #e63b2e; }
    .checkmark::after { content: '\\f00c'; font-family: 'Font Awesome 6 Free'; font-weight: 900; font-size: 12px; color: white; display: none; }
    .custom-checkbox input:checked ~ .checkmark::after { display: block; }
    .agree-btn { padding: 12px 30px; background: #e63b2e; color: white; border: none; font-size: 16px; font-weight: 700; cursor: pointer; transition: background 0.3s; opacity: 0.5; pointer-events: none; border-radius: 4px; }
    .agree-btn.active { opacity: 1; pointer-events: auto; }
    .agree-btn:hover { background: #c82c20; }
  </style>
</head>
<body>
  <div class="page-card">
    <a href="index.html" class="logo-link">
      <img src="assets/images/firecraft_logo.png" alt="Firecraft Logo" class="logo-img">
    </a>
    <h1>Privacy Policy</h1>
    <div class="content-box">
      <p>Last updated: October 2026</p>
      
      <h2>1. Introduction</h2>
      <p>Welcome to Firecraft Hot Sauce. We are committed to protecting your personal information and your right to privacy. If you have any questions or concerns about this privacy notice, or our practices with regards to your personal information, please contact us at privacy@firecraft.com.</p>
      
      <h2>2. Information We Collect</h2>
      <p>We collect personal information that you voluntarily provide to us when you register on the Website, express an interest in obtaining information about us or our products, or otherwise when you contact us. This includes names, phone numbers, email addresses, mailing addresses, and payment information.</p>
      
      <h2>3. How We Use Your Information</h2>
      <p>We use personal information collected via our Website for a variety of business purposes, such as to facilitate account creation, fulfill and manage your orders, post testimonials, and send administrative information to you.</p>
      
      <h2>4. Will Your Information Be Shared?</h2>
      <p>We only share information with your consent, to comply with laws, to provide you with services, to protect your rights, or to fulfill business obligations. We do not sell your personal data to third-party marketers.</p>

      <div class="agreement-section">
        <label class="custom-checkbox">
          <input type="checkbox" id="agree-check" onchange="toggleAgreeButton()">
          <span class="checkmark"></span>
          <span>I have read and agree to the Privacy Policy and terms regarding the handling of my personal data.</span>
        </label>
        <button type="button" class="agree-btn" id="agree-btn" onclick="submitAgreement()">Accept & Continue</button>
      </div>
    </div>
  </div>
  <script>
    if (localStorage.getItem('firecraftTheme') === 'light') { document.documentElement.classList.add('light-theme'); }
    function toggleAgreeButton() {
      const cb = document.getElementById('agree-check');
      const btn = document.getElementById('agree-btn');
      if (cb.checked) { btn.classList.add('active'); } else { btn.classList.remove('active'); }
    }
    function submitAgreement() {
      window.location.href = 'index.html';
    }
  </script>
</body>
</html>"""

faqs_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>FAQs | Firecraft Hot Sauce</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="assets/images/firecraft_logo.png">
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body { background: #0b0908; color: #f7f2ea; font-family: 'Manrope', sans-serif; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 60px 20px; margin: 0; }
    html.light-theme body { background: #f4ede3; color: #171513; }
    .page-card { background: #151311; padding: 60px 50px; max-width: 800px; width: 100%; border: 1px solid rgba(247, 242, 234, 0.12); box-shadow: 0 20px 40px rgba(0,0,0,0.3); border-radius: 8px; }
    html.light-theme .page-card { background: #ffffff; border-color: rgba(23, 21, 19, 0.15); }
    .logo-link { display: block; text-align: center; margin-bottom: 30px; text-decoration: none; }
    .logo-img { height: 75px; width: auto; object-fit: contain; margin: 0 auto; display: inline-block; }
    .page-card h1 { font-family: 'DM Serif Display', serif; font-size: 38px; color: #e63b2e; margin-bottom: 40px; text-align: center; }
    
    .faq-accordion { text-align: left; }
    .faq-item { border-bottom: 1px solid rgba(247, 242, 234, 0.1); margin-bottom: 10px; }
    html.light-theme .faq-item { border-color: rgba(23, 21, 19, 0.1); }
    .faq-header { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; cursor: pointer; font-size: 17px; font-weight: 600; color: #f7f2ea; transition: color 0.3s; }
    html.light-theme .faq-header { color: #171513; }
    .faq-header:hover { color: #e63b2e; }
    .faq-header i { font-size: 14px; transition: transform 0.3s; color: #e63b2e; }
    .faq-item.active .faq-header i { transform: rotate(180deg); }
    .faq-content { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; color: #b6aaa0; font-size: 15px; line-height: 1.6; }
    html.light-theme .faq-content { color: #5e5952; }
    .faq-content p { padding-bottom: 20px; margin: 0; }
  </style>
</head>
<body>
  <div class="page-card">
    <a href="index.html" class="logo-link">
      <img src="assets/images/firecraft_logo.png" alt="Firecraft Logo" class="logo-img">
    </a>
    <h1>Frequently Asked Questions</h1>
    
    <div class="faq-accordion">
      <div class="faq-item">
        <div class="faq-header" onclick="toggleFaq(this)">
          Do your sauces contain artificial preservatives?
          <i class="fa-solid fa-chevron-down"></i>
        </div>
        <div class="faq-content">
          <p>No, we use only natural preservatives like vinegar, salt, and citrus juices. We believe in keeping our ingredients as clean and natural as possible.</p>
        </div>
      </div>
      <div class="faq-item">
        <div class="faq-header" onclick="toggleFaq(this)">
          Are Firecraft sauces gluten-free and vegan?
          <i class="fa-solid fa-chevron-down"></i>
        </div>
        <div class="faq-content">
          <p>Yes! All of our core hot sauces are 100% gluten-free and certified vegan. They are made entirely from plant-based ingredients.</p>
        </div>
      </div>
      <div class="faq-item">
        <div class="faq-header" onclick="toggleFaq(this)">
          Do you ship internationally?
          <i class="fa-solid fa-chevron-down"></i>
        </div>
        <div class="faq-content">
          <p>Currently, we only ship within the United States and Canada. We hope to expand our shipping zones globally in the near future!</p>
        </div>
      </div>
      <div class="faq-item">
        <div class="faq-header" onclick="toggleFaq(this)">
          How long does a bottle last after opening?
          <i class="fa-solid fa-chevron-down"></i>
        </div>
        <div class="faq-content">
          <p>We recommend refrigerating our sauces after opening. Once refrigerated, a bottle will easily stay fresh and retain its heat for up to 6 months.</p>
        </div>
      </div>
      <div class="faq-item">
        <div class="faq-header" onclick="toggleFaq(this)">
          Which sauce is the hottest?
          <i class="fa-solid fa-chevron-down"></i>
        </div>
        <div class="faq-content">
          <p>The "Ghost Pepper Reserve" is currently our hottest offering, clocking in at over 500,000 Scoville Heat Units. Proceed with caution!</p>
        </div>
      </div>
      <div class="faq-item">
        <div class="faq-header" onclick="toggleFaq(this)">
          What happens if my bottle arrives broken?
          <i class="fa-solid fa-chevron-down"></i>
        </div>
        <div class="faq-content">
          <p>If your package arrives damaged, please email us a photo within 48 hours of delivery at support@firecraft.com, and we will ship a free replacement immediately.</p>
        </div>
      </div>
    </div>
  </div>
  
  <script>
    if (localStorage.getItem('firecraftTheme') === 'light') { document.documentElement.classList.add('light-theme'); }
    
    function toggleFaq(headerElement) {
      const item = headerElement.parentElement;
      const content = item.querySelector('.faq-content');
      
      // Close other open FAQs
      const allItems = document.querySelectorAll('.faq-item');
      allItems.forEach(i => {
        if (i !== item && i.classList.contains('active')) {
          i.classList.remove('active');
          i.querySelector('.faq-content').style.maxHeight = '0';
        }
      });
      
      // Toggle current FAQ
      item.classList.toggle('active');
      if (item.classList.contains('active')) {
        content.style.maxHeight = content.scrollHeight + "px";
      } else {
        content.style.maxHeight = "0";
      }
    }
  </script>
</body>
</html>"""

terms_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Terms & Conditions | Firecraft Hot Sauce</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="assets/images/firecraft_logo.png">
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body { background: #0b0908; color: #f7f2ea; font-family: 'Manrope', sans-serif; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 60px 20px; margin: 0; }
    html.light-theme body { background: #f4ede3; color: #171513; }
    .page-card { background: #151311; padding: 60px 50px; max-width: 800px; width: 100%; border: 1px solid rgba(247, 242, 234, 0.12); box-shadow: 0 20px 40px rgba(0,0,0,0.3); border-radius: 8px; }
    html.light-theme .page-card { background: #ffffff; border-color: rgba(23, 21, 19, 0.15); }
    .logo-link { display: block; text-align: center; margin-bottom: 30px; text-decoration: none; }
    .logo-img { height: 75px; width: auto; object-fit: contain; margin: 0 auto; display: inline-block; }
    .page-card h1 { font-family: 'DM Serif Display', serif; font-size: 38px; color: #e63b2e; margin-bottom: 30px; text-align: center; }
    .content-box { font-size: 15px; line-height: 1.8; color: #b6aaa0; text-align: left; }
    html.light-theme .content-box { color: #5e5952; }
    .content-box h2 { color: #f7f2ea; font-size: 20px; margin-bottom: 10px; margin-top: 25px; }
    html.light-theme .content-box h2 { color: #171513; }
    .agreement-section { margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(247, 242, 234, 0.2); }
    html.light-theme .agreement-section { border-color: rgba(23, 21, 19, 0.2); }
    .custom-checkbox { display: flex; align-items: flex-start; gap: 12px; cursor: pointer; margin-bottom: 20px; }
    .custom-checkbox input { display: none; }
    .checkmark { min-width: 20px; height: 20px; border: 1px solid rgba(247,242,234,0.4); display: flex; align-items: center; justify-content: center; margin-top: 3px; border-radius: 3px; }
    html.light-theme .checkmark { border-color: rgba(23,21,19,0.4); }
    .custom-checkbox input:checked ~ .checkmark { background: #e63b2e; border-color: #e63b2e; }
    .checkmark::after { content: '\\f00c'; font-family: 'Font Awesome 6 Free'; font-weight: 900; font-size: 12px; color: white; display: none; }
    .custom-checkbox input:checked ~ .checkmark::after { display: block; }
    .agree-btn { padding: 12px 30px; background: #e63b2e; color: white; border: none; font-size: 16px; font-weight: 700; cursor: pointer; transition: background 0.3s; opacity: 0.5; pointer-events: none; border-radius: 4px; }
    .agree-btn.active { opacity: 1; pointer-events: auto; }
    .agree-btn:hover { background: #c82c20; }
  </style>
</head>
<body>
  <div class="page-card">
    <a href="index.html" class="logo-link">
      <img src="assets/images/firecraft_logo.png" alt="Firecraft Logo" class="logo-img">
    </a>
    <h1>Terms & Conditions</h1>
    <div class="content-box">
      <p>Please read these terms carefully before using our website.</p>
      
      <h2>1. Agreement to Terms</h2>
      <p>By accessing or using our website, you agree to be bound by these Terms. If you disagree with any part of the terms, you may not access the service.</p>
      
      <h2>2. Intellectual Property</h2>
      <p>The service and its original content, features, and functionality are owned by Firecraft and are protected by international copyright, trademark, patent, trade secret, and other intellectual property laws.</p>
      
      <h2>3. Purchases</h2>
      <p>If you wish to purchase any product made available through the service, you may be asked to supply certain information relevant to your purchase, including your credit card number, the expiration date, your billing address, and your shipping information.</p>
      
      <h2>4. Refunds and Returns</h2>
      <p>Due to the consumable nature of our products, all sales are final. We only offer replacements for items that arrive damaged or defective.</p>

      <div class="agreement-section">
        <label class="custom-checkbox">
          <input type="checkbox" id="agree-check-terms" onchange="toggleAgreeButtonTerms()">
          <span class="checkmark"></span>
          <span>I have read and agree to the Terms & Conditions of Firecraft Hot Sauce.</span>
        </label>
        <button type="button" class="agree-btn" id="agree-btn-terms" onclick="submitAgreementTerms()">Accept Terms</button>
      </div>
    </div>
  </div>
  <script>
    if (localStorage.getItem('firecraftTheme') === 'light') { document.documentElement.classList.add('light-theme'); }
    function toggleAgreeButtonTerms() {
      const cb = document.getElementById('agree-check-terms');
      const btn = document.getElementById('agree-btn-terms');
      if (cb.checked) { btn.classList.add('active'); } else { btn.classList.remove('active'); }
    }
    function submitAgreementTerms() {
      window.location.href = 'index.html';
    }
  </script>
</body>
</html>"""

with open('wholesale.html', 'w', encoding='utf-8') as f: f.write(wholesale_html)
with open('privacy-policy.html', 'w', encoding='utf-8') as f: f.write(privacy_html)
with open('faqs.html', 'w', encoding='utf-8') as f: f.write(faqs_html)
with open('terms.html', 'w', encoding='utf-8') as f: f.write(terms_html)

print('Updated pages generated successfully!')
