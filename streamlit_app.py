echo "streamlit>=1.32.0" > ~/flabil\ landing\ page/requirements.txt
cat > ~/flabil\ landing\ page/app.py << 'PYEOF'
import streamlit as st

st.set_page_config(page_title="Flabil – Clean. Relax. Repeat.", page_icon="🧺", layout="wide")

WHATSAPP_URL = "https://wa.me/message/SQZLWTGYYF5QG1"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; background: #fff !important; color: #0a0a0a; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; max-width: 1080px !important; }
.hero { text-align: center; padding: 3.5rem 1rem 1rem; }
.badge { display: inline-block; font-size: .72rem; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; border: 1.5px solid #0a0a0a; border-radius: 100px; padding: .28rem .9rem; margin-bottom: 1.2rem; }
.h1 { font-size: clamp(3.2rem,9vw,6.5rem); font-weight: 900; letter-spacing: -.03em; line-height: 1; margin: 0 0 .5rem; }
.tagline { font-size: clamp(1rem,3vw,1.5rem); font-weight: 300; letter-spacing: .05em; color: #444; }
.sub { font-size: .95rem; color: #888; margin: .4rem 0 1.8rem; }
.divider { width: 56px; height: 3px; background: #0a0a0a; border-radius: 2px; margin: 2rem auto; }
.trust { display: flex; justify-content: center; gap: 2.5rem; flex-wrap: wrap; padding: 1.6rem 1rem; border-top: 1.5px solid #f0f0f0; border-bottom: 1.5px solid #f0f0f0; margin: 1.5rem 0 2.5rem; }
.trust-num { font-size: 1.5rem; font-weight: 900; display: block; }
.trust-lbl { font-size: .68rem; color: #888; text-transform: uppercase; letter-spacing: .08em; }
.sec-lbl { text-align: center; font-size: .68rem; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: #888; }
.sec-title { text-align: center; font-size: clamp(1.4rem,4vw,2.1rem); font-weight: 800; letter-spacing: -.02em; margin: .2rem 0 .3rem; }
.sec-sub { text-align: center; font-size: .9rem; color: #888; margin-bottom: 2rem; }
.card { border: 1.5px solid #0a0a0a; border-radius: 18px; padding: 1.7rem 1.5rem 1.5rem; display: flex; flex-direction: column; gap: .8rem; height: 100%; transition: box-shadow .2s, transform .2s; }
.card:hover { box-shadow: 6px 6px 0 #0a0a0a; transform: translate(-3px,-3px); }
.c-emoji { font-size: 2rem; }
.c-title { font-size: 1.05rem; font-weight: 700; }
.c-prices { display: flex; align-items: baseline; gap: .5rem; flex-wrap: wrap; }
.p-new { font-size: 1.55rem; font-weight: 900; }
.p-old { font-size: .9rem; color: #aaa; text-decoration: line-through; }
.save { font-size: .66rem; font-weight: 700; background: #0a0a0a; color: #fff; border-radius: 100px; padding: .2rem .6rem; }
.c-note { font-size: .7rem; color: #bbb; font-style: italic; }
.c-desc { font-size: .83rem; color: #666; line-height: 1.55; flex: 1; }
.btn { display: block; width: 100%; padding: .72rem 1rem; font-family: 'Inter',sans-serif; font-size: .85rem; font-weight: 700; letter-spacing: .05em; text-align: center; text-decoration: none; color: #fff; background: #0a0a0a; border: 2px solid #0a0a0a; border-radius: 12px; margin-top: auto; transition: background .2s, color .2s; }
.btn:hover { background: #fff; color: #0a0a0a; }
.steps { display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 1.4rem; }
.step { text-align: center; max-width: 190px; }
.s-circle { width: 50px; height: 50px; border: 2px solid #0a0a0a; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; margin: 0 auto .65rem; }
.s-title { font-size: .88rem; font-weight: 700; margin-bottom: .15rem; }
.s-desc { font-size: .73rem; color: #777; }
.cta { background: #0a0a0a; color: #fff; text-align: center; border-radius: 18px; padding: 2.5rem 1.5rem; margin: 3rem 0 2rem; }
.cta h2 { font-size: clamp(1.3rem,3.5vw,1.9rem); font-weight: 800; margin: 0 0 .5rem; color: #fff; }
.cta p { font-size: .9rem; color: #aaa; margin: 0 0 1.3rem; }
.cta-btn { display: inline-block; padding: .82rem 2rem; font-family: 'Inter',sans-serif; font-size: .9rem; font-weight: 700; letter-spacing: .04em; text-decoration: none; color: #0a0a0a; background: #fff; border-radius: 12px; }
.footer { text-align: center; padding: 2rem 1rem 1rem; font-size: .78rem; color: #bbb; border-top: 1.5px solid #f0f0f0; margin-top: 1.5rem; }
.footer strong { color: #0a0a0a; }
.footer a { color: #0a0a0a; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero">
  <div class="badge">✦ Home Services</div>
  <div class="h1">Flabil</div>
  <div class="tagline">Clean. Relax. Repeat.</div>
  <div class="sub">We handle your daily needs — so you don't have to.</div>
  <a href="{WHATSAPP_URL}" target="_blank" class="btn" style="display:inline-block;width:auto;padding:.82rem 2.2rem;font-size:.92rem;">💬 &nbsp;Chat on WhatsApp</a>
  <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="trust">
  <div><span class="trust-num">500+</span><span class="trust-lbl">Happy Customers</span></div>
  <div><span class="trust-num">4.9 ★</span><span class="trust-lbl">Average Rating</span></div>
  <div><span class="trust-num">₹29</span><span class="trust-lbl">Starting Price</span></div>
  <div><span class="trust-num">2 hrs</span><span class="trust-lbl">Avg Service Time</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sec-lbl">What We Offer</div>
<div class="sec-title">Our Services</div>
<p class="sec-sub">First-time customer? Enjoy exclusive introductory prices.</p>
""", unsafe_allow_html=True)

services = [
    ("🧺", "Clothes Washing",   29, 39, 10, True,  "Fresh, clean laundry picked up and delivered to your door."),
    ("💆", "Body Therapy",      99,149, 50, True,  "Rejuvenating full-body therapy by certified professionals."),
    ("💆‍♂️","Head Massage",    49, 79, 30, True,  "Soothing scalp massage to relieve tension and refresh your mind."),
    ("👔", "Washing + Ironing", 59, 79, 20, False, "Complete laundry — washed, perfectly ironed, ready to wear."),
]

cols = st.columns(4, gap="medium")
for col, (emoji, title, new, old, save, ft, desc) in zip(cols, services):
    note = '<div class="c-note">* First-time customer price</div>' if ft else ""
    col.markdown(f"""
    <div class="card">
      <div class="c-emoji">{emoji}</div>
      <div class="c-title">{title}</div>
      <div class="c-prices">
        <span class="p-new">₹{new}</span>
        <span class="p-old">₹{old}</span>
        <span class="save">Save ₹{save}</span>
      </div>
      {note}
      <div class="c-desc">{desc}</div>
      <a href="{WHATSAPP_URL}" target="_blank" class="btn">Order Now →</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="margin-top:3rem;">
  <div class="sec-lbl">Process</div>
  <div class="sec-title">How It Works</div>
  <p class="sec-sub">Three simple steps to a cleaner, happier you.</p>
  <div class="steps">
    <div class="step"><div class="s-circle">💬</div><div class="s-title">1. Chat with Us</div><div class="s-desc">Reach out on WhatsApp and tell us what you need.</div></div>
    <div class="step"><div class="s-circle">📅</div><div class="s-title">2. Pick a Slot</div><div class="s-desc">Choose a convenient time and we'll be there.</div></div>
    <div class="step"><div class="s-circle">✨</div><div class="s-title">3. Sit Back & Enjoy</div><div class="s-desc">We handle everything. You just relax.</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="cta">
  <h2>Ready to Experience Flabil?</h2>
  <p>Join hundreds of happy customers. Your first order comes with a special discount.</p>
  <a href="{WHATSAPP_URL}" target="_blank" class="cta-btn">💬 &nbsp;Order on WhatsApp</a>
</div>
<div class="footer">
  <strong>Flabil</strong> &nbsp;·&nbsp; Clean. Relax. Repeat. &nbsp;·&nbsp;
  <a href="{WHATSAPP_URL}" target="_blank">WhatsApp Us</a><br><br>
  © 2026 Flabil. All rights reserved.
</div>
""", unsafe_allow_html=True)
PYEOF
cd ~/flabil\ landing\ page && streamlit run app.py
