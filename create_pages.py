import os

pages = [
    ('wholesale.html', 'Wholesale Inquiries', 'Interested in stocking Firecraft hot sauce? We offer competitive wholesale pricing for retailers, restaurants, and distributors. Contact us to learn more about our partner program.'),
    ('privacy-policy.html', 'Privacy Policy', 'Your privacy is critically important to us. We only collect the information necessary to process your orders and improve your shopping experience. We never sell your personal data.'),
    ('shipping.html', 'Shipping Information', 'We ship our sauces carefully packaged to ensure they arrive safely. Orders typically process within 1-2 business days. Standard shipping takes 3-5 business days.'),
    ('faqs.html', 'Frequently Asked Questions', 'Find answers to common questions about our ingredients, heat levels, and recommended pairings. If you have a specific question not covered here, feel free to reach out.'),
    ('terms.html', 'Terms & Conditions', 'By using the Firecraft website, you agree to these terms and conditions. We reserve the right to update our terms at any time. All content is protected by copyright.')
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title} | Firecraft Hot Sauce</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="assets/images/firecraft_logo.png">
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body {{
      background: #0b0908;
      color: #f7f2ea;
      font-family: 'Manrope', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin: 0;
      padding: 20px;
    }}
    html.light-theme body {{
      background: #f4ede3;
      color: #171513;
    }}
    .simple-page-card {{
      background: #151311;
      padding: 60px 40px;
      max-width: 600px;
      width: 100%;
      border: 1px solid rgba(247, 242, 234, 0.12);
      text-align: center;
      box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }}
    html.light-theme .simple-page-card {{
      background: #ffffff;
      border-color: rgba(23, 21, 19, 0.15);
      box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    }}
    .simple-page-card h1 {{
      font-family: 'DM Serif Display', serif;
      font-size: 36px;
      margin-bottom: 20px;
      color: #e63b2e;
    }}
    .simple-page-card p {{
      font-size: 16px;
      line-height: 1.8;
      color: #b6aaa0;
      margin-bottom: 40px;
    }}
    html.light-theme .simple-page-card p {{
      color: #5e5952;
    }}
    .back-home-btn {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 12px 24px;
      background: transparent;
      border: 1px solid #e63b2e;
      color: #e63b2e;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      text-decoration: none;
      transition: all 0.3s ease;
    }}
    .back-home-btn:hover {{
      background: #e63b2e;
      color: #fff;
    }}
    .logo-img {{
      height: 60px;
      margin-bottom: 20px;
    }}
  </style>
</head>
<body>
  
  <div class="simple-page-card">
    <img src="assets/images/firecraft_logo.png" alt="Firecraft Logo" class="logo-img">
    <h1>{title}</h1>
    <p>{content}</p>
    <a href="index.html" class="back-home-btn">
      <i class="fa-solid fa-arrow-left"></i>
      Back to Home
    </a>
  </div>

  <script>
    (function() {{
      const savedTheme = localStorage.getItem('firecraftTheme');
      if (savedTheme === 'light') {{
        document.documentElement.classList.add('light-theme');
      }}
    }})();
  </script>
</body>
</html>
"""

for filename, title, content in pages:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_template.format(title=title, content=content))
        print(f'Created {filename}')
