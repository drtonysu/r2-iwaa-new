# Assembles the static R2-IWAA pages from shared shell + per-page bodies.
import os

OUT = os.path.dirname(os.path.abspath(__file__))

LOGO = """<img class="brand__mark" src="img/logo-512.png" alt="" width="512" height="488">"""

FAVICON = "img/favicon.png"

NAV_ITEMS = [
    ("iv-therapy.html", "IV Therapy"),
    ("locations.html", "Locations"),
    ("founder.html", "Dr. Tony Su"),
    ("news.html", "News"),
]


def header(current):
    links = ""
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == current else ""
        links += f'\n      <a href="{href}"{cur}>{label}</a>'
    return f"""<header class="header">
    <a class="brand" href="index.html" aria-label="R2-IWAA home">
      {LOGO}
      <span class="brand-text">
        <span class="brand-mark">R2&#8202;-&#8202;IWAA</span>
        <span class="brand-sub">Wellness &amp; Anti-Aging</span>
      </span>
    </a>
    <button class="burger" type="button" aria-label="Menu" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
    </button>
    <nav class="nav" aria-label="Main">{links}
      <a class="btn" href="consultation.html">Consultation</a>
    </nav>
  </header>"""


FOOTER = """<footer class="footer">
    <div class="wrap">
      <div class="footer__grid">
        <div>
          <h4>R2-IWAA</h4>
          <p>R2 International Wellness &amp; Anti-Aging. Physician-led regenerative and anti-aging medicine, with its medical and training centre in Taipei.</p>
        </div>
        <div>
          <h4>Care</h4>
          <ul>
            <li><a href="iv-therapy.html">IV Therapy</a></li>
            <li><a href="advanced-care.html">Advanced Regenerative Care</a></li>
            <li><a href="founder.html">Dr. Tony Su</a></li>
          </ul>
        </div>
        <div>
          <h4>Visit</h4>
          <ul>
            <li><a href="locations.html">Taipei &middot; Yangon &middot; Ho Chi Minh City</a></li>
            <li><a href="news.html">News from the network</a></li>
            <li><a href="consultation.html">Request a consultation</a></li>
            <li><a href="mailto:care@r2-iwaa.com">care@r2-iwaa.com</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__base">
        <span>&copy; 2023 R2 International Wellness &amp; Anti-Aging</span>
        <span>Availability of individual therapies is confirmed at consultation and differs by location.</span>
      </div>
    </div>
  </footer>"""


def page(slug, title, desc, body, current=None):
    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <script>(function(){{try{{var m=document.cookie.match(/(?:^|; )r2th=(light|dark)/);if(m){{document.documentElement.setAttribute('data-theme',m[1]);}}}}catch(e){{}}}})();</script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <link rel="icon" type="image/png" href="{FAVICON}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
  <link href="https://api.fontshare.com/v2/css?f[]=switzer@300,400,500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  {header(current or slug)}
  <main>
{body}
  </main>
  {FOOTER}
  <script src="js/site.js" defer></script>
</body>
</html>
"""
    with open(os.path.join(OUT, slug), "w", encoding="utf-8") as f:
        f.write(html)


INVITE = """    <section class="band band--emerald">
      <div class="wrap invite reveal">
        <p class="eyebrow">One to one</p>
        <h2>Every plan begins with a <em>conversation</em>.</h2>
        <p>A private consultation with our medical team — your history, your goals, and an honest view of what is appropriate for you.</p>
        <a class="btn btn--solid" href="consultation.html">Request a consultation</a>
      </div>
    </section>"""

# ---------------------------------------------------------------- home

home = f"""    <section class="hero">
      <picture>
        <source media="(max-width: 720px)" srcset="img/hero-taipei-dusk-portrait.webp">
        <img class="hero__bg" src="img/hero-taipei-dusk.webp" alt="Taipei skyline at deep dusk with warm city lights beneath a navy and emerald sky">
      </picture>
      <div class="hero__inner">
        <p class="eyebrow reveal">Taiwan-based &middot; R2 International Wellness &amp; Anti-Aging</p>
        <h1 class="reveal">Longevity, <em>calibrated</em> to you.</h1>
        <p class="lead reveal">Physician-led regenerative care across Taipei, Yangon and Ho Chi Minh City.</p>
        <div class="hero__cta reveal">
          <a class="btn btn--solid" href="consultation.html">Request a consultation</a>
          <a class="btn" href="iv-therapy.html">IV therapy</a>
        </div>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap">
        <div class="pillars reveal">
          <div class="pillar">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><path d="M12 3v6M9 9h6l-1.2 9a1.8 1.8 0 0 1-3.6 0L9 9Z"/></svg>
            <h3>IV Therapy</h3>
            <p>Our foundation. Available at every R2 partner.</p>
          </div>
          <div class="pillar">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><circle cx="12" cy="12" r="8.4"/><circle cx="12" cy="12" r="3.2"/></svg>
            <h3>Regenerative Care</h3>
            <p>Advanced options, offered by physician consultation.</p>
          </div>
          <div class="pillar">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><path d="M4 19V7l8-3 8 3v12"/><path d="M9 19v-6h6v6"/></svg>
            <h3>Physician-Led</h3>
            <p>Founded and directed by Dr. Tony Su in Taipei.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="band band--navy">
      <div class="wrap split reveal">
        <div class="split__media split__media--tall"><img src="img/iv-detail.webp" alt="Close view of a golden droplet forming in an intravenous drip chamber"></div>
        <div class="split__body">
          <p class="eyebrow">The foundation</p>
          <h2>Intravenous therapy, <em>built around you</em>.</h2>
          <hr class="rule">
          <p class="lead">Hydration, vitamins, minerals and amino acids delivered directly — chosen from your bloodwork and how you actually live.</p>
          <a class="arrowlink" href="iv-therapy.html">See IV programmes &rarr;</a>
        </div>
      </div>
    </section>

    <section class="band band--hair band--ivory">
      <div class="wrap">
        <div class="band__head reveal">
          <p class="eyebrow">The difference</p>
          <h2>Why patients stay with us.</h2>
        </div>
        <hr class="rule">
        <div class="facts reveal">
          <div class="fact">
            <span class="fact__n">01</span>
            <p>Every plan is written by a physician after examination and bloodwork &mdash; never chosen from a menu.</p>
          </div>
          <div class="fact">
            <span class="fact__n">02</span>
            <p>One patient at a time, in a private suite, with unhurried time to ask anything.</p>
          </div>
          <div class="fact">
            <span class="fact__n">03</span>
            <p>Materials and protocols come from one source in Taipei, so quality does not change by city.</p>
          </div>
          <div class="fact">
            <span class="fact__n">04</span>
            <p>Mandarin, English and Myanmar spoken directly by your physician, with no interpreter in between.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="statement">
      <img src="img/abstract-cells.webp" alt="Abstract luminous cells connected by fine golden filaments">
      <div class="statement__inner reveal">
        <p class="eyebrow">Advanced regenerative care</p>
        <h2>Selected therapies, <em>by consultation</em>.</h2>
        <p>Where the evidence and your assessment support it, our medical team may discuss advanced regenerative options with you.</p>
        <hr class="rule rule--center">
        <a class="arrowlink" href="advanced-care.html">Learn more &rarr;</a>
      </div>
    </section>

    <section class="band">
      <div class="wrap split split--flip reveal">
        <div class="split__media"><img src="img/taipei-lab.webp" alt="A precise clinical laboratory with cryogenic storage and sterile preparation area"></div>
        <div class="split__body">
          <p class="eyebrow">Taipei</p>
          <h2>One standard, <em>three cities</em>.</h2>
          <hr class="rule">
          <p class="lead">Our Taipei centre trains every clinical team and prepares the materials used in Yangon and Ho Chi Minh City — so care does not change when the city does.</p>
          <a class="arrowlink" href="locations.html">Our locations &rarr;</a>
        </div>
      </div>

      <div class="wrap duo reveal">
        <figure class="duo__item">
          <img src="img/r2-training.webp" alt="An empty clinical training room with a long walnut table, microscopes and protocol binders">
          <figcaption><span class="card__label">Training</span>Clinical teams are taught and re-certified in Taipei before they treat anyone.</figcaption>
        </figure>
        <figure class="duo__item">
          <img src="img/r2-supply.webp" alt="Cold-chain transport cases with labelled vials prepared for dispatch">
          <figcaption><span class="card__label">Supply</span>Materials are prepared, checked and dispatched under cold chain to each clinic.</figcaption>
        </figure>
      </div>
    </section>

    <section class="band band--navy">
      <div class="wrap split reveal">
        <div class="split__body">
          <p class="eyebrow">Founder</p>
          <h2>Dr. Tony Su</h2>
          <hr class="rule">
          <p class="lead">Founder and Medical Director. He leads every clinical protocol at R2-IWAA and trains the teams that deliver it.</p>
          <div class="founder__meta" style="margin-top:1.4rem"><span>Mandarin</span><span>English</span><span>Myanmar</span></div>
          <a class="arrowlink" href="founder.html" style="margin-top:2rem;display:inline-flex">About Dr. Su &rarr;</a>
        </div>
        <div class="split__media">
          <img src="img/founder-lab.webp" alt="Gloved hands of a physician holding a small glass vial of amber regenerative serum in a warm laboratory setting">
        </div>
      </div>
    </section>

    <section class="band band--hair band--ivory">
      <div class="wrap">
        <div class="band__head reveal">
          <p class="eyebrow">Where to find us</p>
          <h2>Three clinics, <em>one network</em>.</h2>
        </div>
        <hr class="rule">
        <div class="locs reveal">
          <div class="loc">
            <span class="loc__tag">Main centre</span>
            <h3>Taipei &mdash; R2-IWAA</h3>
            <p>Shilin District, Taipei. R2-IWAA main center, clinical training and materials preparation.</p>
          </div>
          <div class="loc">
            <span class="loc__tag">Yangon</span>
            <h3>Beauty Bank Wellness Center</h3>
            <p>Kamaryut Township, Yangon. Assessment, IV therapy and procedures.</p>
          </div>
          <div class="loc">
            <span class="loc__tag">Ho Chi Minh City</span>
            <h3>Recover Health</h3>
            <p>Xuân Hòa Ward, Ho Chi Minh City. Assessment, IV therapy and procedures.</p>
          </div>
        </div>
      </div>
    </section>

{INVITE}
"""

# ---------------------------------------------------------------- iv therapy

iv_cards = [
    ("iv-anti-aging.html",       "01 &middot; Foundation", "Anti-Aging Drip", "Our entry formula for antioxidant support and everyday free-radical clearance.", "iv-01-antiaging.webp", "A guest reclining in a private R2 suite during an Anti-Aging Drip session &mdash; soft golden infusion in the morning light"),
    ("iv-premium-anti-aging.html", "02 &middot; Foundation", "Premium Anti-Aging Drip", "An amino-acid-based version of our foundation formula, for periods of depletion.", "iv-02-premium.webp", "A guest resting in a private R2 suite during a Premium Anti-Aging Drip session &mdash; a warm golden amino-acid infusion in a private suite"),
    ("iv-detox.html",             "03 &middot; Clearance", "Detox Drip", "Metabolic and hepatic support, closing with a slow, separately administered antioxidant infusion.", "iv-03-detox.webp", "Amber fluid separating from emerald fluid through a translucent membrane, golden threads dispersing"),
    ("iv-advanced-detox.html",    "04 &middot; Clearance", "Advanced Antioxidant &amp; Detox", "An escalated course for accumulated stress, sleep loss and prolonged fatigue.", "iv-04-advanced-detox.webp", "Golden intravenous drip chamber with a single amber droplet caught mid-fall in a warm treatment suite"),
    ("iv-vitamin-c.html",         "05 &middot; Foundation", "High-Dose Vitamin C", "A concentrated vitamin C infusion, dosed and paced under physician supervision.", "iv-05-vitc.webp", "Sliced orange and lemon cross-sections on dark stone, translucent flesh catching golden light"),
    ("iv-myers.html",             "06 &middot; Foundation", "Myers&rsquo; Cocktail", "The classic B-vitamin, vitamin C, magnesium and zinc infusion.", "iv-06-myers.webp", "An amber, a clear and a gold-capped pharmaceutical vial resting on folded dark navy velvet"),
    ("iv-neuro.html",             "07 &middot; Neurology", "NeuroVitality Drip", "A two-stage neuro-support protocol, offered after individual medical assessment.", "iv-07-neuro.webp", "Abstract golden neural filaments and glowing nodes suspended in dark navy fluid"),
    ("iv-sport.html",             "08 &middot; Recovery", "Sport Recovery Drip", "A fast amino-acid infusion for athletes and heavy training loads.", "iv-08-sport.webp", "A single amber vial beside a folded ivory linen towel on dark stone with a deep navy background"),
    ("iv-hangover.html",          "09 &middot; Recovery", "Post-Hangover Drip", "Fluid replacement followed by slower antioxidant support for hepatic recovery.", "iv-09-hangover.webp", "A crystal-cut carafe of amber liquid and lemon halves on a dark emerald marble slab"),
    ("iv-omega.html",             "10 &middot; Foundation", "Omega Drip", "An omega-3 emulsion with vitamin C and B-complex, for cerebral and cardiac support.", "iv-10-omega.webp", "A single golden omega oil droplet falling into a shallow crystal dish with warm gold bokeh"),
]

cards_html = ""
for slug, label, name, text, img, alt in iv_cards:
    cards_html += f"""
          <a class="card card--iv card--link" href="{slug}">
            <div class="card__media"><img src="img/{img}" alt="{alt}" loading="lazy"></div>
            <div class="card__body">
              <span class="card__label">{label}</span>
              <h3>{name}</h3>
              <p>{text}</p>
              <span class="card__more">See the formula &rarr;</span>
            </div>
          </a>"""

iv = f"""    <section class="hero hero--page">
      <img class="hero__bg" src="img/iv-detail.webp" alt="A golden droplet forming inside an intravenous drip chamber">
      <div class="hero__inner">
        <p class="eyebrow reveal">IV Therapy</p>
        <h1 class="reveal">Our foundation, <em>everywhere</em> we practise.</h1>
        <p class="lead reveal">The same protocols, the same materials, the same standard in Taipei, Yangon and Ho Chi Minh City.</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap">
        <div class="band__head reveal">
          <p class="eyebrow">Programmes</p>
          <h2>Chosen for you, <em>not from a menu</em>.</h2>
          <p class="lead">Every programme starts from your history, examination and bloodwork. Composition and pace are set by your physician.</p>
        </div>
        <div class="cards cards--iv reveal">{cards_html}
        </div>
      </div>
    </section>

    <section class="band band--navy band--hair">
      <div class="wrap">
        <div class="band__head reveal">
          <p class="eyebrow">How a visit runs</p>
          <h2>Unhurried, and never improvised.</h2>
        </div>
        <hr class="rule">
        <div class="facts reveal">
          <div><p class="fact__k">01</p><p class="fact__v">Consultation and review of your history and goals.</p></div>
          <div><p class="fact__k">02</p><p class="fact__v">Bloodwork where it changes the plan.</p></div>
          <div><p class="fact__k">03</p><p class="fact__v">Your programme, written and explained.</p></div>
          <div><p class="fact__k">04</p><p class="fact__v">Treatment in a private suite, 45&ndash;90 minutes.</p></div>
        </div>
      </div>
    </section>

    <section class="band">
      <div class="wrap split reveal">
        <div class="split__media split__media--tall"><img src="img/abstract-vesicles.webp" alt="Abstract golden mist of microscopic luminous spheres in dark fluid"></div>
        <div class="split__body">
          <p class="eyebrow">Beyond the foundation</p>
          <h2>Advanced <em>regenerative</em> care.</h2>
          <hr class="rule">
          <p class="lead">Some patients are assessed for options that go further than intravenous nutrition. These are discussed individually, never sold from a list.</p>
          <a class="arrowlink" href="advanced-care.html">Learn more &rarr;</a>
        </div>
      </div>
    </section>

{INVITE}
"""

# ---------------------------------------------------------------- advanced care

adv_rows = [
    (
        "adv-blood-purification.html",
        "Apheresis",
        "Therapeutic Plasma Exchange",
        "Blood plasma is separated and replaced with sterile albumin and saline; your blood cells are returned to circulation. Used to lower circulating inflammatory and metabolic factors.",
        "Adults with chronic inflammatory burden, elevated cardiometabolic markers, or persistent post-viral fatigue &mdash; where laboratory workup supports it.",
        [
            ("Setting", "Taipei clinic only, under continuous physician supervision"),
            ("Session", "Up to about 2 hours, Haemonetics MCS+ single-needle system"),
            ("Course", "Typically a short assessed course, spaced weekly or monthly"),
            ("Before", "Full blood panel, cardiac and coagulation screen required"),
        ],
        "adv-blood-purification.webp",
        "Golden and emerald plasma swirling through a translucent membrane",
    ),
    (
        "adv-mesenchymal-cells.html",
        "Regenerative",
        "Mesenchymal Cell Therapy",
        "An intravenous cell therapy using mesenchymal cells prepared under laboratory conditions. Studied for immunomodulatory and tissue-support effects.",
        "Selected regenerative and inflammatory profiles, and only where local regulation permits treatment. Not a routine service in every location.",
        [
            ("Setting", "Delivered at partner clinics where locally permitted"),
            ("Session", "Slow intravenous infusion, 1 to 2 hours"),
            ("Course", "Single infusion or short course, defined after assessment"),
            ("Before", "Cell product traceability documentation provided to the patient"),
        ],
        "adv-stem-cells.webp",
        "A luminous cluster of translucent cellular spheres with warm golden cores",
    ),
    (
        "adv-exosome-iv.html",
        "Regenerative",
        "Exosome Intravenous Therapy",
        "An intravenous course of extracellular vesicles (exosomes) from mesenchymal cells. Given as a short, physician-directed series, usually layered onto an IV hydration plan.",
        "Adults seeking regenerative support alongside a wider wellness plan. Availability depends on your assessment and on local regulation.",
        [
            ("Setting", "Delivered at partner clinics where locally permitted"),
            ("Session", "Intravenous infusion, approximately 60 to 90 minutes"),
            ("Course", "Typically 3 to 6 sessions, planned individually"),
            ("Pairs with", "Precision IV hydration and recovery protocols"),
        ],
        "adv-exosomes.webp",
        "Golden microscopic vesicles suspended in navy fluid with soft rays of light",
    ),
    (
        "adv-exosome-knee.html",
        "Orthopaedic",
        "Exosome Knee Programme",
        "An in-joint (intra-articular) exosome course for knee osteoarthritis, paired with a structured rehabilitation and load-management plan.",
        "Adults with imaging-confirmed knee osteoarthritis, aiming to reduce symptoms and support function. Not a substitute for surgical care where indicated.",
        [
            ("Setting", "Delivered at partner clinics where locally permitted"),
            ("Session", "Guided intra-articular injection under aseptic conditions"),
            ("Course", "Typically a short series over several weeks"),
            ("Includes", "Rehabilitation guidance and follow-up review"),
        ],
        "abstract-joint.webp",
        "Abstract translucent knee joint forms glowing with warm golden light",
    ),
    (
        "adv-iv-laser.html",
        "Photomedicine",
        "Intravenous Laser Therapy",
        "Low-level intravascular light at specific wavelengths, delivered through a fine intravenous line. Used as an adjunct to IV protocols &mdash; not a stand-alone treatment.",
        "Adults on a planned IV course seeking additional support alongside hydration or recovery protocols.",
        [
            ("Setting", "Available at Taipei and selected partner clinics"),
            ("Session", "Approximately 30 to 60 minutes, alongside IV therapy"),
            ("Course", "Short series, aligned with your IV plan"),
            ("Pairs with", "Precision IV hydration, recovery, neuro-support protocols"),
        ],
        "adv-iv-laser.webp",
        "A guest resting in a private R2 suite during an ILIB session &mdash; a fine laser fibre taped over the forearm vein, warm lamplight and cream linens",
    ),
]

rows_html = ""
for slug, label, name, what, who, meta, img, alt in adv_rows:
    meta_items = "".join(
        f'<div class="row__meta-item"><span class="row__meta-key">{k}</span><span class="row__meta-val">{v}</span></div>'
        for k, v in meta
    )
    rows_html += f"""
          <a class="row row--link" href="{slug}">
            <div class="row__media"><img src="img/{img}" alt="{alt}" loading="lazy"></div>
            <div class="row__body">
              <span class="card__label">{label}</span>
              <h3>{name}</h3>
              <p class="row__what">{what}</p>
              <p class="row__who"><span class="row__who-tag">Who it may suit</span> {who}</p>
              <div class="row__meta">{meta_items}</div>
              <span class="row__more">Read how it works &rarr;</span>
            </div>
          </a>"""

adv = f"""    <section class="hero hero--page">
      <img class="hero__bg" src="img/abstract-purify.webp" alt="Abstract golden and emerald fluid separating through a translucent membrane">
      <div class="hero__inner">
        <p class="eyebrow reveal">Advanced regenerative care</p>
        <h1 class="reveal">Discussed <em>individually</em>.</h1>
        <p class="lead reveal">These therapies are not for everyone, and they are not offered from a price list. Each is considered only after full medical assessment.</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap">
        <div class="band__head narrow reveal">
          <p class="eyebrow">What we may discuss</p>
          <h2>A short, <em>honest</em> list.</h2>
          <p class="lead">What is appropriate for you depends on your assessment, and what is available depends on where you are treated. Your physician will tell you both, plainly, before anything begins.</p>
        </div>
        <div class="rows reveal">{rows_html}
        </div>
      </div>
    </section>

    <section class="band band--navy band--hair">
      <div class="wrap split reveal">
        <div class="split__media"><img src="img/adv-honest-note.webp" alt="A physician's gloved hand writing careful notes in a leather clinical notebook under a warm brass lamp"></div>
        <div class="split__body">
          <p class="eyebrow">How we speak about outcomes</p>
          <h2>Considered, and <em>told plainly</em>.</h2>
          <hr class="rule">
          <p class="lead">Regenerative medicine is a developing field. We will tell you what is established, what is still being studied, and what we simply do not know &mdash; including when the honest answer is that a therapy is not right for you.</p>
        </div>
      </div>
    </section>

{INVITE}
"""

# ---------------------------------------------------------------- founder

founder = f"""    <section class="hero hero--page">
      <img class="hero__bg" src="img/founder-desk.webp" alt="A physician's desk with a folded white coat, stethoscope, notebook and brass lamp">
      <div class="hero__inner">
        <p class="eyebrow reveal">Founder &amp; Medical Director</p>
        <h1 class="reveal">Dr. Tony Su</h1>
        <p class="lead reveal">He writes the protocols, trains the teams, and sees patients himself.</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap founder reveal">
        <div class="portrait"><img src="img/founder-portrait.webp" alt="Dr. Tony Su, founder and medical director of R2-IWAA"></div>
        <div>
          <p class="eyebrow">Approach</p>
          <h2>Calibration over <em>catalogue</em>.</h2>
          <hr class="rule">
          <p class="lead">Dr. Su&rsquo;s position is simple: a patient receives what their biology asks for, at the pace their life allows &mdash; not the package on offer. Every protocol used across the network is written and reviewed by him, and reviewed again when the evidence moves.</p>
          <div class="founder__meta"><span>Internal medicine</span><span>Precision medicine</span><span>Cellular &amp; anti-aging medicine</span></div>
        </div>
      </div>
    </section>

    <section class="band band--navy band--hair">
      <div class="wrap">
        <div class="band__head reveal narrow">
          <p class="eyebrow">Publications &amp; Training</p>
          <h2>Trained where the margin for error is <em>smallest</em>.</h2>
          <p class="lead">General internal medicine, critical care, chest speciality and emergency medicine in Taiwan first &mdash; then cellular medicine in Japan. The order matters: acute-care judgement came before the regenerative medicine for longevity and healthspan.</p>
        </div>
        <hr class="rule">
        <ol class="pubs reveal">
          <li>
            <span class="pubs__tag">Board Certification</span>
            <span class="pubs__body">Internal Medicine &mdash; Taiwan</span>
            <span class="pubs__place">Taiwan</span>
          </li>
          <li>
            <span class="pubs__tag">Board Certification</span>
            <span class="pubs__body">Precision Medicine, since 2021</span>
            <span class="pubs__place">Taiwan</span>
          </li>
          <li>
            <span class="pubs__tag">Cellular Therapy Fellowship</span>
            <span class="pubs__body">Dendritic cell therapy under Prof. Hasumi</span>
            <span class="pubs__place">Japan, 2018</span>
          </li>
          <li>
            <span class="pubs__tag">Cellular Therapy Fellowship</span>
            <span class="pubs__body">Osaki Method NK cell therapy under Prof. Masuyama</span>
            <span class="pubs__place">Japan, 2022</span>
          </li>
          <li>
            <span class="pubs__tag">Postgraduate Training</span>
            <span class="pubs__body">Precision Oncology, Cancer Genomics &amp; Immuno-Oncology</span>
            <span class="pubs__place">Harvard Medical School</span>
          </li>
          <li>
            <span class="pubs__tag">Fellowship</span>
            <span class="pubs__body">American Academy of Anti-Aging Medicine (A4M)</span>
            <span class="pubs__place">2022</span>
          </li>
          <li>
            <span class="pubs__tag">Professional Memberships</span>
            <span class="pubs__body">American College of Physicians</span>
            <span class="pubs__place">Ongoing</span>
          </li>
        </ol>
      </div>
    </section>

    <section class="band">
      <div class="wrap quote-band reveal">
        <div class="quote-band__photo">
          <img src="img/founder-portrait-warm.webp" alt="Dr. Tony Su in a physician's white coat, mid-consultation with a patient, warm and attentive">
        </div>
        <figure class="quote-band__quote">
          <span class="quote-band__mark" aria-hidden="true">&ldquo;</span>
          <blockquote>A regenerative plan should follow bloodwork, not a brochure. That is the standard I hold every R2-IWAA physician to.</blockquote>
          <figcaption><span class="quote-band__name">Dr. Tony Su</span><span class="quote-band__role">Founder &amp; Medical Director</span></figcaption>
        </figure>
      </div>
    </section>

    <section class="band band--ivory band--hair">
      <div class="wrap pair reveal">
        <div class="pair__col">
          <p class="eyebrow">Languages</p>
          <ul class="pair__lines">
            <li><strong>Mandarin</strong><span>Native. First language of practice, in Taipei.</span></li>
            <li><strong>English</strong><span>Clinical fluency for international patients and referring physicians.</span></li>
            <li><strong>Myanmar</strong><span>Consultation-level, for patients from Yangon and the diaspora.</span></li>
          </ul>
        </div>
        <div class="pair__col">
          <p class="eyebrow">Training network</p>
          <ul class="pair__lines">
            <li><strong>Taipei</strong><span>Main centre. Protocols are written and materials prepared here.</span></li>
            <li><strong>Yangon</strong><span>Partner care at Beauty Bank Wellness &amp; Cell Therapy Center.</span></li>
            <li><strong>Ho Chi Minh City</strong><span>Partner care at Recover Health.</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="band band--navy band--hair">
      <div class="wrap reveal narrow">
        <p class="eyebrow">Protocols authored by Dr. Su</p>
        <h2>Every formula, <em>one physician&rsquo;s hand</em>.</h2>
        <hr class="rule">
        <p class="lead">The IV programme across every R2-IWAA location is authored by Dr. Su and reviewed each time the evidence moves. Every plan is set to a patient&rsquo;s bloodwork rather than a menu.</p>
        <p style="margin-top:1.8rem"><a class="arrowlink" href="iv-therapy.html">See the IV therapy programme &rarr;</a></p>
      </div>
    </section>

    <section class="band">
      <div class="wrap split reveal">
        <div class="split__media"><img src="img/consultation.webp" alt="A private consultation room with two emerald green armchairs and warm lamp light">
        </div>
        <div class="split__body">
          <p class="eyebrow">VIP service</p>
          <h2>One patient at a time.</h2>
          <hr class="rule">
          <p class="lead">Consultations are private and unhurried, in Mandarin, English or Myanmar. Travelling patients are looked after from the first message to the last review.</p>
          <a class="arrowlink" href="consultation.html">Request a consultation &rarr;</a>
        </div>
      </div>
    </section>
"""

# ---------------------------------------------------------------- locations

locations = f"""    <section class="hero hero--page">
      <img class="hero__bg" src="img/taipei-lab.webp" alt="A precise clinical laboratory with cryogenic storage and sterile preparation area">
      <div class="hero__inner">
        <p class="eyebrow reveal">Locations</p>
        <h1 class="reveal">Taipei, Yangon, Ho&nbsp;Chi&nbsp;Minh&nbsp;City.</h1>
        <p class="lead reveal">One clinical standard, prepared and trained in Taipei, delivered in all three cities.</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap split reveal">
        <div class="split__media"><img src="img/taipei-lab.webp" alt="Sterile preparation bench with laminar flow cabinet and cryogenic vessel"></div>
        <div class="split__body">
          <p class="eyebrow">Main centre</p>
          <h2>Taipei &mdash; R2-IWAA</h2>
          <hr class="rule">
          <p class="lead">No.&nbsp;516, Section&nbsp;5, Zhongshan North Road, Shilin District. Our R2-IWAA main center, and the hub of the network &mdash; where clinical teams are trained and where the materials used in every clinic are prepared and released.</p>
        </div>
      </div>
    </section>

    <section class="band band--navy band--hair">
      <div class="wrap">
        <div class="band__head reveal">
          <p class="eyebrow">Partner clinics</p>
          <h2>Cared for <em>close to home</em>.</h2>
        </div>
        <hr class="rule">
        <div class="locs locs--two reveal">
          <div class="loc">
            <span class="loc__tag">Yangon</span>
            <h3>Beauty Bank Wellness &amp; Cell Therapy Center</h3>
            <p class="loc__addr">Kamaryut Township, Yangon</p>
            <p>Assessment, IV therapy and procedures.</p>
            <p class="loc__meta">Tel <a href="tel:09886234234">09&nbsp;886&nbsp;234&nbsp;234</a></p>
          </div>
          <div class="loc">
            <span class="loc__tag">Ho Chi Minh City</span>
            <h3>Recover Health</h3>
            <p class="loc__addr">260&ndash;262A Điện Biên Phủ, Xuân Hòa Ward, Ho Chi Minh City</p>
            <p>Assessment, IV therapy and procedures.</p>
            <p class="loc__meta">Hotline <a href="tel:0902766786">0902&nbsp;766&nbsp;786</a><br><a href="mailto:info@recoverhealth.vn">info@recoverhealth.vn</a></p>
          </div>
        </div>
      </div>
    </section>

    <section class="statement">
      <img src="img/texture.webp" alt="Deep navy and emerald silk folds traced by a single thin line of gold light">
      <div class="statement__inner reveal">
        <p class="eyebrow">The network</p>
        <h2>Trained in Taipei. Delivered where you live.</h2>
        <p>Clinical training, protocols and prepared materials flow from Taipei to each clinic, so your care does not change with your city.</p>
      </div>
    </section>

{INVITE}
"""

# ---------------------------------------------------------------- consultation

consult = f"""    <section class="hero hero--page">
      <img class="hero__bg" src="img/consultation.webp" alt="A private consultation room with two emerald green armchairs facing a walnut table">
      <div class="hero__inner">
        <p class="eyebrow reveal">VIP consultation</p>
        <h1 class="reveal">One to one, <em>before anything</em> else.</h1>
        <p class="lead reveal">Tell us a little and our medical team will arrange a private consultation in Mandarin, English or Myanmar.</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap split reveal">
        <div class="split__body">
          <p class="eyebrow">Request</p>
          <h2>Start a <em>conversation</em>.</h2>
          <hr class="rule">
          <form class="form" novalidate>
            <div class="field">
              <label for="name">Name</label>
              <input id="name" name="name" type="text" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="contact">Email or WhatsApp</label>
              <input id="contact" name="contact" type="text" autocomplete="email" required>
            </div>
            <div class="field">
              <label for="city">Preferred location</label>
              <select id="city" name="city">
                <option>Taipei</option>
                <option>Yangon</option>
                <option>Ho Chi Minh City</option>
                <option>Not sure yet</option>
              </select>
            </div>
            <div class="field">
              <label for="lang">Consultation language</label>
              <select id="lang" name="lang">
                <option>English</option>
                <option>Mandarin</option>
                <option>Myanmar</option>
              </select>
            </div>
            <div class="field">
              <label for="msg">What would you like to address?</label>
              <textarea id="msg" name="msg"></textarea>
            </div>
            <button class="btn btn--solid" type="submit">Send request</button>
            <p class="form__note">Your request opens in WhatsApp so it reaches our team directly &mdash; press send there and we reply within one working day. Please do not include detailed medical records; we collect those securely once your consultation is arranged.</p>
            <div class="form__ok">
              <p>Thank you. Your request has been prepared in WhatsApp &mdash; press send there and our team will be in touch within one working day.</p>
              <p class="form__alt">WhatsApp did not open? <a class="form__fallback" href="mailto:care@r2-iwaa.com">Send it by email instead</a>.</p>
            </div>
          </form>
        </div>
        <div class="split__body">
          <p class="eyebrow">Direct</p>
          <h2>Or <em>reach us</em> now.</h2>
          <hr class="rule">
          <div class="contactlist">
            <div>
              <span>WhatsApp &amp; Viber</span>
              <div class="contact__icons">
                <a class="contact__icon" href="https://wa.me/886916196333" aria-label="Message us on WhatsApp" title="WhatsApp" target="_blank" rel="noopener">
                  <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.019-.458.13-.606.134-.133.298-.347.446-.52.15-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.096 3.2 5.077 4.487.709.306 1.263.489 1.695.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347zM12.05 21.5h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884a9.82 9.82 0 0 1 6.99 2.899 9.825 9.825 0 0 1 2.892 6.994c-.003 5.45-4.437 9.883-9.886 9.883zm8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
                </a>
                <a class="contact__icon" href="viber://chat?number=%2B886916196333" aria-label="Message us on Viber" title="Viber">
                  <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11.4 0C9.473.028 5.333.344 3.02 2.467 1.297 4.187.694 6.7.63 9.816c-.062 3.114-.138 8.952 5.49 10.537h.005l-.005 2.414s-.036.978.61 1.177c.777.243 1.234-.5 1.977-1.298.408-.437.972-1.08 1.397-1.575 3.845.323 6.798-.416 7.134-.525.775-.252 5.166-.816 5.881-6.643.735-6.014-.36-9.822-2.329-11.532h-.01c-.596-.549-2.984-2.292-8.322-2.313 0 0-.394-.026-1.257-.02L11.4 0zm.101 1.717c.732-.005 1.171.017 1.171.017 4.516.017 6.676 1.38 7.185 1.84 1.66 1.425 2.507 4.855 1.885 9.878-.596 4.867-4.156 5.175-4.81 5.386-.28.09-2.876.738-6.14.526 0 0-2.43 2.932-3.19 3.694-.117.121-.257.166-.35.146-.132-.033-.169-.19-.166-.416.003-.324.021-4.017.021-4.017-.003 0-.006 0 0 0-4.76-1.323-4.483-6.292-4.43-8.892.054-2.6.542-4.732 1.998-6.17 1.956-1.773 5.472-2.038 7.1-2.05l-.274.058zm.363 2.416a.44.44 0 0 0-.442.437.44.44 0 0 0 .442.44c1.238-.01 2.267.394 3.079 1.207.812.815 1.213 1.899 1.208 3.259a.442.442 0 0 0 .439.442h.005a.442.442 0 0 0 .437-.44c.008-1.586-.508-2.923-1.464-3.884-.957-.962-2.201-1.454-3.703-1.461zm-3.732.4a.9.9 0 0 0-.593.153h-.017c-.386.226-.735.51-1.045.891-.264.327-.407.657-.444.98a1.06 1.06 0 0 0 .039.402l.014.008c.164.483.478 1 .953 1.643.474.643 1.084 1.323 1.827 2.028.744.708 1.436 1.32 2.083 1.796.646.475 1.163.79 1.646.955l.014.02c.129.037.263.05.401.037.323-.037.652-.18.98-.444.379-.31.663-.66.888-1.046v-.017a.902.902 0 0 0 .155-.599.933.933 0 0 0-.362-.612 6.822 6.822 0 0 0-1.15-.729c-.375-.196-.75-.076-.906.13l-.324.409c-.164.208-.464.18-.464.18l-.01.007c-2.21-.564-2.798-2.799-2.798-2.799s-.024-.31.184-.463l.408-.325c.202-.156.325-.53.13-.906a6.792 6.792 0 0 0-.727-1.152.938.938 0 0 0-.612-.36l-.28-.001zm4.418 1.06a.44.44 0 0 0-.446.439.44.44 0 0 0 .44.443c.883.005 1.61.293 2.169.856.558.564.847 1.293.854 2.194a.44.44 0 0 0 .44.44h.005a.44.44 0 0 0 .439-.44 3.882 3.882 0 0 0-1.106-2.815 3.899 3.899 0 0 0-2.795-1.117zm.442 2.107a.44.44 0 0 0-.44.44.442.442 0 0 0 .44.44c.552 0 .845.293.85.853a.443.443 0 0 0 .441.437h.005a.44.44 0 0 0 .437-.446c-.008-1.045-.582-1.723-1.732-1.723z"/></svg>
                </a>
              </div>
            </div>
            <div>
              <span>Email</span>
              <a href="mailto:care@r2-iwaa.com">care@r2-iwaa.com</a>
            </div>
            <div>
              <span>Main centre</span>
              <p>No.&nbsp;516, Section&nbsp;5, Zhongshan N. Rd, Shilin District, Taipei</p>
            </div>
            <div>
              <span>Hours</span>
              <p class="muted">By appointment. Assessment and treatment days differ by location.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

# ---------------------------------------------------------------- iv drip detail subpages

# Schema per drip:
#   slug, label, name, hero_img, hero_alt,
#   aim (short single sentence), lead (one paragraph, 2-3 sentences),
#   ingredients: list of (name, dose_or_note, effect_sentence),
#   duration, course, suits (short paragraph on who this suits),
#   note (optional, italic caveat)

# Copy drawn directly from R2Liao-Cheng-2.0.xlsx (R2 treatment course workbook).
# Ingredients kept faithful to the workbook; explanatory sentences written for patients in plain English.
# Prices in NT$ as listed in the workbook.
iv_drips = {
    "iv-anti-aging.html": {
        "label": "IVF0001 &middot; Foundation",
        "name": "Anti-Aging Drip",
        "hero_img": "iv-01-antiaging.webp",
        "hero_alt": "A guest reclining in a private R2 suite during an Anti-Aging Drip session &mdash; a soft golden infusion in the morning light, an emerald plant behind",
        "editorial": {
            "img": "iv-01-antiaging-editorial.webp",
            "alt": "Editorial poster of the R2 Anti-Aging IV Drip: guest at rest with a golden infusion, seven key ingredients labelled &mdash; normal saline, vitamin C, B-complex, zinc, thiocan (\u03b1-lipoic acid), N-acetylcysteine and vitamin B12 &mdash; with potential benefits and who it suits",
        },
        "aim": "Everyday antioxidant support and free-radical clearance &mdash; the R2 foundation for cellular housekeeping.",
        "lead": "Our entry anti-aging infusion, built on a saline base with vitamin C, a full B-complex, N-acetylcysteine and &alpha;-lipoic acid. Together they replenish antioxidant capacity, help the liver clear metabolic waste, and give the body the cofactors it needs for daily energy production and repair.",
        "ingredients": [
            ("Normal saline", "", "Balanced electrolyte base that carries the actives and restores hydration at cell level."),
            ("Vitamin C", "", "A powerful antioxidant that supports collagen, skin and immunity, and helps regenerate other antioxidants in the body."),
            ("Vitamin B-complex", "", "Cofactors for energy metabolism, nerve function and red-blood-cell formation &mdash; the daily machinery of the cell."),
            ("Vitamin B12", "", "Supports nervous-system health and red-blood-cell production."),
            ("Zinc", "", "An essential trace mineral for immunity, skin repair and enzyme activity."),
            ("Thiocan (&alpha;-lipoic acid)", "", "A universal antioxidant with hepatoprotective effect; recycles glutathione and vitamin C."),
            ("Ancare (N-acetylcysteine)", "", "Precursor to glutathione &mdash; supports the body&rsquo;s own detoxification pathways and respiratory health."),
        ],
        "duration": "About 45 minutes in a private suite",
        "price": "NT$ 2,500 per session",
        "course": "Single session or a short series, set by your physician",
        "suits": "Adults looking for a well-tolerated regenerative baseline &mdash; for skin, energy and everyday recovery from stress, travel or a demanding week. A good first infusion for those new to IV therapy.",
        "note": "Composition and dose are confirmed at consultation and may be adjusted for your bloodwork and medical history.",
    },

    "iv-premium-anti-aging.html": {
        "label": "IVF0002 &middot; Foundation",
        "name": "Premium Anti-Aging Drip",
        "hero_img": "iv-02-premium.webp",
        "hero_alt": "A guest resting in a private R2 suite during a Premium Anti-Aging Drip session &mdash; a warm golden amino-acid infusion above a linen-white recliner",
        "editorial": {
            "img": "iv-02-premium-editorial.webp",
            "alt": "Science-for-a-younger-you editorial: the Premium Anti-Aging Drip beside a guest at rest, with each of the eight active ingredients &mdash; amino acids, vitamin C, B-complex, N-acetylcysteine, B12, B6, zinc and magnesium &mdash; labelled to the right",
        },
        "aim": "A stronger, amino-acid-based version of our anti-aging foundation &mdash; for periods of depletion, recovery and heavier restoration.",
        "lead": "Built on a full 250 ml amino-acid base (Aminogen-X) rather than plain saline. Amino acids are the raw material the body uses to build enzymes, hormones, muscle and skin, so this formula gives both the antioxidants and the substrates cells need to rebuild.",
        "ingredients": [
            ("Aminogen-X", "", "An amino-acid infusion base &mdash; the building blocks the body uses to make proteins, enzymes and neurotransmitters."),
            ("Vitamin C", "", "Antioxidant support for collagen, skin, immunity and vascular integrity."),
            ("Vitamin B-complex", "", "A fuller B-complex course for energy production and nervous-system support."),
            ("Vitamin B12", "", "Neurological support and red-blood-cell formation."),
            ("Pyridoxine (B6)", "", "Extra B6 for neurotransmitter synthesis and amino-acid metabolism."),
            ("Ancare (N-acetylcysteine)", "", "Precursor to glutathione for detoxification and antioxidant support."),
            ("Zinc", "", "For immunity, skin repair and hormonal balance."),
            ("Magneter (magnesium)", "", "For muscle relaxation, sleep quality and cardiovascular rhythm."),
        ],
        "duration": "45 to 60 minutes in a private suite",
        "price": "NT$ 5,000 per session",
        "course": "Single session or a physician-set course; may alternate with the High-Dose Vitamin C programme for oncology support",
        "suits": "Those recovering from prolonged fatigue, recent illness, heavy travel or intensive training. Also chosen by patients under long-term stress who want a fuller restorative infusion than the standard Anti-Aging Drip.",
        "note": "Composition and dose are confirmed at consultation and may be adjusted for your bloodwork and medical history.",
    },

    "iv-detox.html": {
        "label": "IVF0003 &middot; Clearance",
        "name": "Detox Drip",
        "hero_img": "iv-03-detox.webp",
        "hero_alt": "Amber fluid separating from emerald fluid through a translucent membrane, golden threads dispersing",
        "aim": "Metabolic and hepatic support &mdash; a clean, focused antioxidant infusion to help the body clear its own waste.",
        "lead": "A 250 ml saline infusion with B-complex, N-acetylcysteine and &alpha;-lipoic acid, closing with a slow glutathione IV push. This staged sequence protects the glutathione from oxidation, so the master antioxidant reaches the tissues intact.",
        "ingredients": [
            ("Normal saline", "", "Balanced hydration base to carry the actives at a steady pace."),
            ("Vitamin B-complex", "", "Cofactors for energy metabolism and nervous-system support during detoxification."),
            ("Ancare (N-acetylcysteine)", "", "Precursor to glutathione &mdash; supports the liver&rsquo;s Phase II detoxification pathways."),
            ("Thiocan (&alpha;-lipoic acid)", "", "Hepatoprotective antioxidant that recycles glutathione and vitamin C."),
            ("Glutathione", "slow IV push", "The body&rsquo;s master antioxidant. Given separately at the end of the session so the thiol group is not degraded by other nutrients in the bag."),
        ],
        "duration": "45 to 60 minutes in a private suite",
        "price": "NT$ 3,500 per session",
        "course": "Single session or a short course, set by your physician",
        "suits": "Those looking for periodic hepatic and antioxidant support &mdash; after a heavy work period, travel, or dietary indulgence. Also a common maintenance choice between Premium Anti-Aging sessions.",
        "note": "Glutathione is administered separately from the main bag so that its thiol group is not oxidised by other nutrients.",
        "principle": {
            "eyebrow": "A note on sequence",
            "text": (
                "Clear first, then build. A single stem cell infusion into an inflamed, burdened system is an expensive way to waste good biology.\n\n"
                "<em>Clearance first, regeneration second</em> &mdash; which is why the intensive programmes run across days rather than single sessions."
            ),
            "attrib": "Dr. Tony Su &middot; R2-IWAA",
        },
    },

    "iv-advanced-detox.html": {
        "label": "IVF0004 &middot; Clearance",
        "name": "Advanced Antioxidant &amp; Detox",
        "hero_img": "iv-04-advanced-detox.webp",
        "hero_alt": "Golden intravenous drip chamber with a single amber droplet caught mid-fall in a warm treatment suite",
        "aim": "An escalated antioxidant course &mdash; higher doses of vitamin C, &alpha;-lipoic acid and glutathione for periods of accumulated stress, sleep loss or prolonged fatigue.",
        "lead": "A three-bag infusion. Vitamin C and higher-dose &alpha;-lipoic acid are given first, followed by glutathione in a dedicated saline bag so the master antioxidant is delivered intact. This is the R2 protocol for guests who need to reinforce antioxidant defence rather than gentle maintenance.",
        "ingredients": [
            ("Normal saline", "three separate bags", "Three saline lines allow each active to be delivered on its own bag for stability and pace."),
            ("Vitamin C", "", "High-dose antioxidant support delivered on its own bag."),
            ("Thiocan (&alpha;-lipoic acid)", "high-dose infusion", "A stronger &alpha;-lipoic acid infusion for antioxidant recycling and hepatic support."),
            ("Glutathione", "dedicated bag", "The master antioxidant. Given in its own bag &mdash; never mixed with vitamin C or other nutrients &mdash; so the free thiol group is not oxidised before it reaches the tissues."),
        ],
        "duration": "45 to 60 minutes in a private suite",
        "price": "NT$ 5,000 per session",
        "course": "Programme course set by your physician; often paired with lifestyle review",
        "suits": "Guests dealing with recent high stress, poor sleep, work fatigue, or those who want to reinforce antioxidant defence beyond the standard Detox Drip.",
        "note": "Clinical note: glutathione is never mixed with high-dose vitamin C or multi-nutrient bags &mdash; the free thiol group would oxidise. R2 administers it alone in a dedicated 100 ml saline bag.",
        "principle": {
            "eyebrow": "A note on sequence",
            "text": (
                "Clear first, then build. A single stem cell infusion into an inflamed, burdened system is an expensive way to waste good biology.\n\n"
                "<em>Clearance first, regeneration second</em> &mdash; which is why the intensive programmes run across days rather than single sessions."
            ),
            "attrib": "Dr. Tony Su &middot; R2-IWAA",
        },
    },

    "iv-vitamin-c.html": {
        "label": "IVF0005 &middot; Foundation",
        "name": "High-Dose Vitamin C",
        "hero_img": "iv-05-vitc.webp",
        "hero_alt": "Sliced orange and lemon cross-sections on dark stone, translucent flesh catching golden light",
        "aim": "A concentrated vitamin C infusion, dosed and paced under physician supervision.",
        "lead": "A physician-set dose of intravenous vitamin C in a 250 ml saline base. Because oral vitamin C is capped by gut absorption, an IV can reach plasma levels many times higher &mdash; useful for antioxidant support, collagen and immunity. Dose is determined at consultation.",
        "ingredients": [
            ("Normal saline", "", "Balanced hydration base to deliver the vitamin C at a steady pace."),
            ("Vitamin C", "physician-set dose", "A concentrated antioxidant infusion. Supports collagen, skin, immunity and vascular integrity. Delivered slowly at a rate chosen by your physician."),
        ],
        "duration": "45 to 60 minutes in a private suite",
        "price": "NT$ 3,500 per session",
        "course": "Single session or a physician-set course; oncology patients may alternate with the Premium Anti-Aging formula",
        "suits": "Guests seeking a focused antioxidant programme, skin support, or additional vitamin C support around a period of physical stress. G6PD status is checked before high-dose vitamin C.",
        "note": "High-dose vitamin C requires G6PD screening. Composition and pace are confirmed by your physician.",
    },

    "iv-myers.html": {
        "label": "IVF0006 &middot; Foundation",
        "name": "Myers&rsquo; Cocktail",
        "hero_img": "iv-06-myers.webp",
        "hero_alt": "An amber, a clear and a gold-capped pharmaceutical vial resting on folded dark navy velvet",
        "aim": "The classic B-vitamin, magnesium, zinc and vitamin C infusion &mdash; a broad-spectrum restorative for fatigue and everyday depletion.",
        "lead": "A 250 ml saline base with a full B-complex, extra B6 and B12, magnesium, zinc and vitamin C. First developed by Dr. John Myers in the 1970s and refined for R2, this remains one of the most widely used maintenance drips worldwide.",
        "ingredients": [
            ("Normal saline", "", "Balanced hydration base."),
            ("Vitamin B-complex", "", "Cofactors for energy production and nervous-system function."),
            ("Pyridoxine (B6)", "", "Extra B6 for neurotransmitter synthesis."),
            ("Vitamin B12", "", "Neurological and haematological support."),
            ("Vitamin C", "", "Antioxidant support for immunity, collagen and vascular integrity."),
            ("Zinc", "", "Immunity, skin repair and enzyme activity."),
            ("Magneter (magnesium)", "", "For muscle relaxation, sleep quality and cardiovascular rhythm."),
        ],
        "duration": "45 to 60 minutes in a private suite",
        "price": "NT$ 3,500 per session",
        "course": "Single session or a maintenance rhythm set by your physician",
        "suits": "Everyday fatigue, low mood after illness, seasonal viral pressure, migraine tendency, muscle tension &mdash; the drip most patients use as a monthly reset.",
        "note": "Magnesium is delivered at a rate that avoids flushing; pace is set by your physician.",
    },

    "iv-neuro.html": {
        "label": "IVF0007 &middot; Neurology",
        "name": "NeuroVitality Drip",
        "hero_img": "iv-07-neuro.webp",
        "hero_alt": "Abstract golden neural filaments and glowing nodes suspended in dark navy fluid",
        "aim": "A two-stage neuro-support protocol &mdash; a B-complex and Ginkgo micro-circulation stage, followed by a Cerebrolysin stage for neurotrophic support.",
        "lead": "Given in two sequential 30-minute stages. The first stage delivers a taurine-based B-complex, vitamin C, B12, B6 and Ginkgo to support micro-circulation. The second stage delivers Cerebrolysin, a neuropeptide preparation used clinically for neurological support. Offered only after individual medical assessment.",
        "ingredients": [
            ("Stage 1 &mdash; Normal saline", "", "Hydration base for the vitamin and Ginkgo stage."),
            ("Mejuoline (taurine B-complex)", "", "A taurine-based B-complex with methionine &mdash; adds hepatic and neurological support to the standard B-vitamin base."),
            ("Vitamin C", "", "Antioxidant support for vascular integrity."),
            ("Vitamin B12", "", "Neurological and haematological support."),
            ("Pyridoxine (B6)", "", "For neurotransmitter synthesis."),
            ("Ginkgo biloba", "", "A cerebral circulation support used in vascular and cognitive medicine."),
            ("Stage 2 &mdash; Normal saline", "", "Fresh saline bag for the neurotrophic stage."),
            ("Cerebrolysin", "", "A neuropeptide preparation used clinically for neurological support; dose confirmed by your physician after assessment."),
        ],
        "duration": "About 60 minutes across two stages",
        "price": "NT$ 5,000 &ndash; 8,000 per session",
        "course": "Course length is set individually after medical assessment",
        "suits": "Considered on an individual basis. Not offered without a full consultation.",
        "note": "NeuroVitality is a medically supervised protocol &mdash; suitability, dose and course length are decided at consultation.",
    },

    "iv-sport.html": {
        "label": "IVF0008 &middot; Recovery",
        "name": "Sport Recovery Drip",
        "hero_img": "iv-08-sport.webp",
        "hero_alt": "A single amber vial beside a folded ivory linen towel on dark stone with a deep navy background",
        "aim": "A fast amino-acid infusion for athletes and heavy training loads &mdash; restores substrates for muscle repair, hydration and electrolyte balance.",
        "lead": "Built on a 250 ml amino-acid base (Aminogen) rather than plain saline, with a taurine-based B-complex, extra B6 and B12, zinc and magnesium. Often paired with ILIB (intravascular laser irradiation) for training-block recovery.",
        "ingredients": [
            ("Aminogen", "", "An amino-acid infusion base &mdash; substrate for muscle repair and enzyme synthesis after heavy training."),
            ("Mejuoline (taurine B-complex)", "", "Taurine-based B-complex with methionine for energy metabolism and muscle function."),
            ("Vitamin B12", "", "For red-blood-cell production and endurance recovery."),
            ("Vitamin B6", "", "Amino-acid metabolism and neurotransmitter synthesis."),
            ("Zinc", "", "For immunity and tissue repair."),
            ("Magneter (magnesium)", "", "For muscle relaxation and cramp prevention."),
        ],
        "duration": "About 30 minutes in a private suite",
        "price": "NT$ 3,500 per session",
        "course": "Around training blocks or competitions; often paired with ILIB laser therapy",
        "suits": "Endurance and strength athletes during heavy training blocks or competition weeks. Also chosen after long-haul travel where jet lag and dehydration interfere with training recovery.",
        "note": "Often paired with intravascular laser (ILIB) as a full recovery session &mdash; recommended by Dr. Su.",
    },

    "iv-hangover.html": {
        "label": "IVF009 &middot; Recovery",
        "name": "Post-Hangover Drip",
        "hero_img": "iv-09-hangover.webp",
        "hero_alt": "A crystal-cut carafe of amber liquid and lemon halves on a dark emerald marble slab",
        "aim": "Full rehydration followed by slower antioxidant and hepatic support &mdash; a physician-built recovery drip after a heavy evening.",
        "lead": "Two 250 ml saline bags for full rehydration, a taurine-based B-complex, extra B12 and B6, zinc, and a slow &alpha;-lipoic acid infusion for hepatic support. Often paired with ILIB (intravascular laser) to help oxidative recovery.",
        "ingredients": [
            ("Normal saline", "full rehydration", "Hangover physiology is largely a fluid and electrolyte deficit &mdash; two bags restore both."),
            ("Mejuoline (taurine B-complex)", "", "Taurine and methionine add hepatic and neurological support to the B-complex."),
            ("Vitamin B12", "", "Restores B12 depleted by alcohol; supports nervous-system recovery."),
            ("Vitamin B6 (Pyridoxine)", "", "For neurotransmitter recovery and nausea."),
            ("Zinc", "", "For immunity and enzyme recovery."),
            ("Thiocan (&alpha;-lipoic acid)", "separate slow line", "Given on its own line, over an hour, for hepatic antioxidant support after alcohol."),
        ],
        "duration": "45 to 60 minutes in a private suite",
        "price": "NT$ 3,500 per session",
        "course": "Single session as needed; often paired with ILIB laser therapy",
        "suits": "Guests recovering from a heavy evening, jet lag, or a period of poor sleep and heavy hospitality. Often booked the morning after a corporate event or wedding.",
        "note": "Often paired with intravascular laser (ILIB) for oxidative recovery &mdash; recommended by Dr. Su.",
    },

    "iv-omega.html": {
        "label": "IVF0010 &middot; Foundation",
        "name": "Omega Drip",
        "hero_img": "iv-10-omega.webp",
        "hero_alt": "A single golden omega oil droplet falling into a shallow crystal dish with warm gold bokeh",
        "aim": "An omega-3 fish-oil infusion with vitamin C and B-complex &mdash; for brain and cardiac support, and to help calm systemic inflammation and allergic reactivity.",
        "lead": "A fish-oil emulsion delivered through a side line, alongside a saline bag with vitamin C and a taurine-based B-complex. Intravenous omega-3 delivers EPA and DHA directly to plasma, bypassing gut absorption limits.",
        "ingredients": [
            ("Fish-oil infusion (omega-3)", "side-line delivery", "An intravenous omega-3 emulsion. EPA and DHA support brain and cardiac cell membranes and modulate inflammatory signalling."),
            ("Normal saline", "", "Hydration base for the vitamin and B-complex line."),
            ("Vitamin C", "", "Antioxidant support for vascular integrity."),
            ("Mejuoline (taurine B-complex)", "", "Taurine-based B-complex with methionine &mdash; adds hepatic and neurological support to the standard B-vitamin base."),
        ],
        "duration": "45 to 60 minutes in a private suite",
        "price": "NT$ 5,000 per session",
        "course": "Single session or a physician-set course",
        "suits": "Guests focused on brain and cardiac support, those with high inflammatory load, allergic reactivity, or a diet low in oily fish. Often combined with other formulas in a longer regenerative plan.",
        "note": "Fish-oil infusion is administered through a separate side line for pharmaceutical stability.",
    },
}


def render_principle(principle, band="navy"):
    """Optional sequence-principle pull-quote band.

    `principle` may be:
      - None / falsy         -> render nothing
      - str                  -> quote text only; default eyebrow/attrib
      - dict with keys       -> text (required), eyebrow (optional),
                                attrib (optional)

    Rendered as its own <section> so callers just interpolate the string.
    """
    if not principle:
        return ""
    if isinstance(principle, str):
        principle = {"text": principle}
    text = principle.get("text", "").strip()
    if not text:
        return ""
    eyebrow = principle.get("eyebrow", "A note on sequence")
    attrib = principle.get("attrib", "Dr. Tony Su &middot; R2-IWAA")
    band_cls = "band--navy" if band == "navy" else "band--ivory"
    # Split on double newlines into paragraphs for the blockquote
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    body = "".join(f"<p>{p}</p>" for p in paras) if paras else f"<p>{text}</p>"
    return f"""    <section class="band {band_cls} band--hair">
      <div class="principle reveal">
        <p class="principle__eyebrow">{eyebrow}</p>
        <span class="principle__mark" aria-hidden="true">&ldquo;</span>
        <blockquote>{body}</blockquote>
        <hr class="principle__rule">
        <p class="principle__attrib">{attrib}</p>
      </div>
    </section>"""


def render_drip(spec):
    ing_rows = "".join(
        f'''
              <li class="ing">
                <div class="ing__head">
                  <span class="ing__name">{n}</span>
                </div>
                <p class="ing__effect">{e}</p>
              </li>'''
        for n, _d, e in spec["ingredients"]
    )
    note_html = f'<p class="drip__note"><em>{spec["note"]}</em></p>' if spec.get("note") else ""
    principle_html = render_principle(spec.get("principle"), band="navy")
    editorial_html = ""
    if spec.get("editorial"):
        ed = spec["editorial"]
        editorial_html = f'''    <section class="band band--navy band--flush">
      <figure class="editorial reveal">
        <img src="img/{ed['img']}" alt="{ed['alt']}" loading="lazy">
      </figure>
    </section>
'''
    return f"""    <section class="hero hero--page hero--drip">
      <img class="hero__bg" src="img/{spec['hero_img']}" alt="{spec['hero_alt']}">
      <div class="hero__inner">
        <p class="eyebrow reveal">{spec['label']}</p>
        <h1 class="reveal">{spec['name']}.</h1>
        <p class="lead reveal">{spec['aim']}</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap drip reveal">
        <div class="drip__lead">
          <p class="eyebrow">The aim</p>
          <h2>What this <em>drip is for</em>.</h2>
          <hr class="rule">
          <p class="lead">{spec['lead']}</p>
        </div>

        <div class="drip__meta">
          <div><span class="drip__k">Time</span><span class="drip__v">{spec['duration']}</span></div>
          <div><span class="drip__k">Investment</span><span class="drip__v">By consultation</span></div>
          <div><span class="drip__k">Course</span><span class="drip__v">{spec['course']}</span></div>
          <div><span class="drip__k">Who it may suit</span><span class="drip__v">{spec['suits']}</span></div>
        </div>
      </div>
    </section>

    <section class="band band--navy band--hair">
      <div class="wrap reveal">
        <div class="band__head narrow">
          <p class="eyebrow">Inside the drip</p>
          <h2>The <em>formula</em>, ingredient by ingredient.</h2>
          <p class="lead">Each component is chosen for a specific effect. Nothing is here for weight or theatre &mdash; every line has a reason.</p>
        </div>
        <hr class="rule">
        <ul class="ings reveal">{ing_rows}
        </ul>
        {note_html}
      </div>
    </section>

{editorial_html}
{principle_html}

    <section class="band band--ivory band--hair">
      <div class="wrap reveal narrow">
        <p class="eyebrow">Next step</p>
        <h2>See if this <em>fits you</em>.</h2>
        <hr class="rule">
        <p class="lead">Every drip we give is confirmed at consultation. Composition, dose and pace are set by your physician after reviewing your history and, where it changes the plan, your bloodwork.</p>
        <div class="cta-row"><a class="btn btn--gold" href="consultation.html">Request a consultation</a><a class="arrowlink" href="iv-therapy.html">Back to IV programmes &rarr;</a></div>
      </div>
    </section>

{INVITE}
"""


def render_drip_stub(slug, label, name, hero_img, hero_alt):
    return f"""    <section class="hero hero--page hero--drip">
      <img class="hero__bg" src="img/{hero_img}" alt="{hero_alt}">
      <div class="hero__inner">
        <p class="eyebrow reveal">{label}</p>
        <h1 class="reveal">{name}.</h1>
        <p class="lead reveal">The full formula for this drip is being reviewed. Please request a consultation and our team will walk you through the composition in person.</p>
      </div>
    </section>

    <section class="band band--ivory band--hair">
      <div class="wrap reveal narrow">
        <p class="eyebrow">Next step</p>
        <h2>Speak with the <em>medical team</em>.</h2>
        <hr class="rule">
        <p class="lead">Every drip we give is confirmed at consultation. Composition, dose and pace are set by your physician after reviewing your history and, where it changes the plan, your bloodwork.</p>
        <div class="cta-row"><a class="btn btn--gold" href="consultation.html">Request a consultation</a><a class="arrowlink" href="iv-therapy.html">Back to IV programmes &rarr;</a></div>
      </div>
    </section>

{INVITE}
"""


# build a body per drip subpage, keyed by slug
drip_bodies = {}
for slug, label, name, _text, img, alt in iv_cards:
    spec = iv_drips.get(slug)
    if spec:
        drip_bodies[slug] = render_drip(spec)
    else:
        drip_bodies[slug] = render_drip_stub(slug, label, name, img, alt)


# ---------------------------------------------------------------- advanced care subpages

adv_pages = {
    "adv-blood-purification.html": {
        "label": "Apheresis &middot; Taipei only",
        "name": "Therapeutic Plasma Exchange",
        "hero_img": "adv-blood-purification.webp",
        "hero_alt": "Golden and emerald plasma swirling through a translucent membrane, backlit on deep navy",
        "aim": "A physician-supervised blood-purification session on the Haemonetics MCS+ apheresis system &mdash; single needle, one arm, up to two hours.",
        "lead": "Plasma exchange separates the fluid part of your blood (plasma) from your cells. The plasma is discarded, sterile replacement fluid is added, and your own red and white cells are returned to circulation through the same fine needle in one arm. The Haemonetics MCS+ system runs this as a cyclic draw&ndash;separate&ndash;return process.",
        "steps": [
            ("01", "Assessment &amp; consent", "A full physician review with recent bloodwork, cardiac and coagulation screen. We discuss what plasma exchange can and cannot do, and confirm suitability. Nothing is booked from a menu."),
            ("02", "Preparation", "You rest in a private suite. One fine intravenous access is placed in a single arm &mdash; there is no second needle in the opposite arm as with older systems. Vital signs are monitored continuously."),
            ("03", "Cyclic apheresis", "The MCS+ draws a small volume of blood, separates plasma from your blood cells, discards the plasma, and returns your cells to you &mdash; then repeats. The whole cycle runs through the one needle. A session takes about two hours at most."),
            ("04", "Fluid replacement", "As plasma is removed, sterile albumin and saline are infused as replacement so your blood volume stays balanced throughout the session."),
            ("05", "Recovery &amp; review", "Brief post-procedure observation, hydration, and a written summary. Follow-up bloodwork is scheduled to guide any further sessions."),
        ],
        "benefits": [
            ("Single-needle, one-arm access", "One fine cannula in one arm for the whole session. Two-access systems typically require a needle in each arm and take three to four hours."),
            ("Up to two hours per session", "Cyclic operation on the MCS+ keeps the session short and comfortable, under continuous physician supervision."),
            ("Continuous physician oversight", "Every session runs in the Taipei clinic under a supervising physician &mdash; not delegated to a technician."),
            ("Lower circulating burden", "Removes a portion of plasma-borne inflammatory and metabolic factors, so the load your liver, kidneys and immune system have to clear is reduced for a period after the session."),
            ("What the bag color can tell us", "The color of the removed plasma is a visible signal we look at during the session. A deeper, cloudier or more turbid bag can point to a higher circulating load of lipids, inflammatory mediators or metabolic waste &mdash; useful context, always read alongside your bloodwork by the physician."),
        ],
        "note": "Blood purification is offered only at the Taipei clinic. Bag color is one visual signal used during the session &mdash; it is interpreted by the physician together with your laboratory results, not on its own.",
        "meta": [
            ("Setting", "Taipei clinic only, private suite"),
            ("System", "Haemonetics MCS+ single-needle apheresis"),
            ("Session", "Up to about 2 hours"),
            ("Before", "Full blood panel, cardiac and coagulation screen"),
        ],
        "principle": {
            "eyebrow": "A note on sequence",
            "text": (
                "Clear first, then build. A single stem cell infusion into an inflamed, burdened system is an expensive way to waste good biology.\n\n"
                "<em>Clearance first, regeneration second</em> &mdash; which is why the intensive programmes run across days rather than single sessions."
            ),
            "attrib": "Dr. Tony Su &middot; R2-IWAA",
        },
    },
    "adv-mesenchymal-cells.html": {
        "label": "Regenerative",
        "name": "Mesenchymal Cell Therapy",
        "hero_img": "adv-stem-cells.webp",
        "hero_alt": "A luminous cluster of translucent cellular spheres with warm golden cores on deep navy",
        "aim": "An intravenous cell therapy using laboratory-prepared mesenchymal cells &mdash; studied for its immunomodulatory and tissue-support effects.",
        "lead": "Mesenchymal cells are a type of cell studied for their ability to modulate immune activity and support tissue repair signalling. They are prepared under laboratory conditions from certified sources, and delivered as a slow intravenous infusion under physician supervision.",
        "steps": [
            ("01", "Assessment &amp; consent", "A detailed medical review, including bloodwork and any relevant imaging. We discuss what is known and not known about the therapy, and what regulation allows in your treating location."),
            ("02", "Product traceability", "The cell product is documented from source through preparation. You receive traceability documentation as part of your medical record."),
            ("03", "Slow intravenous infusion", "The infusion is given in a private suite over one to two hours, with continuous physician monitoring throughout."),
            ("04", "Recovery &amp; follow-up", "Post-infusion observation, hydration and a written summary. Any subsequent session is discussed only after review."),
        ],
        "benefits": [
            ("Laboratory-prepared", "Prepared under controlled laboratory conditions, with source and preparation records shared with the patient."),
            ("Physician-supervised infusion", "Delivered under continuous physician monitoring in a private suite &mdash; not as an out-patient walk-in."),
            ("Personalised course", "A single infusion or short course, defined only after assessment. There is no fixed package."),
            ("Regional coordination", "Where locally permitted, delivered at our Taipei centre or at partner clinics that meet the same clinical standard."),
        ],
        "note": "Mesenchymal cell therapy is offered only where local regulation permits. It is not a routine service in every location, and it is never presented as a cure. Suitability, timing and any subsequent session are decided individually.",
        "meta": [
            ("Setting", "Taipei centre and partner clinics, where locally permitted"),
            ("Session", "Slow IV infusion, 1&ndash;2 hours"),
            ("Course", "Single infusion or a short course, defined after assessment"),
            ("Documentation", "Cell product traceability shared with the patient"),
        ],
        "principle": {
            "eyebrow": "A note on sequence",
            "text": (
                "Clear first, then build. A single stem cell infusion into an inflamed, burdened system is an expensive way to waste good biology.\n\n"
                "<em>Clearance first, regeneration second</em> &mdash; which is why the intensive programmes run across days rather than single sessions."
            ),
            "attrib": "Dr. Tony Su &middot; R2-IWAA",
        },
    },
    "adv-exosome-iv.html": {
        "label": "Regenerative",
        "name": "Exosome Intravenous Therapy",
        "hero_img": "adv-exosomes.webp",
        "hero_alt": "Golden microscopic vesicles suspended in navy fluid with soft rays of light",
        "aim": "A short physician-directed series of intravenous extracellular vesicles (exosomes), usually layered onto an IV hydration plan.",
        "lead": "Exosomes are small extracellular vesicles released by cells &mdash; carriers of signalling molecules used in cell-to-cell communication. In this therapy they are prepared from mesenchymal cell sources under laboratory conditions and given as a slow intravenous infusion.",
        "steps": [
            ("01", "Assessment &amp; consent", "A physician review with bloodwork. We explain what exosomes are and what current evidence supports, and check what regulation allows in your treating location."),
            ("02", "Product preparation", "The exosome preparation is drawn from a documented laboratory source. Product records are shared with the patient."),
            ("03", "Slow intravenous infusion", "Given in a private suite over 60 to 90 minutes, alongside an IV hydration base if indicated. Physician-monitored throughout."),
            ("04", "Series review", "After each session, response and tolerance are reviewed before the next is scheduled. Typically three to six sessions."),
        ],
        "benefits": [
            ("Layered onto IV protocols", "Usually delivered alongside a precision IV hydration or recovery plan, so a session serves more than one purpose."),
            ("Short, defined series", "Typically three to six sessions, planned individually rather than sold as a fixed package."),
            ("Physician-monitored", "Every infusion runs under physician supervision in a private suite."),
            ("Traceable preparation", "Product source and preparation records are shared with the patient as part of their medical record."),
        ],
        "note": "Exosome therapy is offered only where local regulation permits, and it is not a substitute for standard medical care. Suitability and course length are defined individually after assessment.",
        "meta": [
            ("Setting", "Taipei centre and partner clinics, where locally permitted"),
            ("Session", "IV infusion, 60&ndash;90 minutes"),
            ("Course", "Typically 3&ndash;6 sessions, planned individually"),
            ("Pairs with", "Precision IV hydration and recovery protocols"),
        ],
        "principle": {
            "eyebrow": "A note on sequence",
            "text": (
                "Clear first, then build. Signalling molecules given into an inflamed, burdened system land in noise rather than in a system ready to answer.\n\n"
                "<em>Clearance first, regeneration second</em> &mdash; which is why exosomes are given as a short series alongside a considered IV plan, not as a one-off infusion."
            ),
            "attrib": "Dr. Tony Su &middot; R2-IWAA",
        },
    },
    "adv-exosome-knee.html": {
        "label": "Orthopaedic",
        "name": "Exosome Knee Programme",
        "hero_img": "abstract-joint.webp",
        "hero_alt": "Abstract translucent knee joint forms glowing with warm golden light on deep navy",
        "aim": "An in-joint (intra-articular) exosome course for knee osteoarthritis, paired with a structured rehabilitation and load-management plan.",
        "lead": "For imaging-confirmed knee osteoarthritis, an exosome preparation is delivered directly into the joint under aseptic conditions. The injection is one part of a wider programme that includes rehabilitation guidance and follow-up review &mdash; the joint injection alone is not the treatment.",
        "steps": [
            ("01", "Imaging &amp; assessment", "Recent knee imaging (X-ray, MRI) and a functional assessment. We confirm the injection is appropriate and that surgical care is not indicated instead."),
            ("02", "Aseptic in-joint injection", "The exosome preparation is placed directly into the knee joint under aseptic conditions by the treating physician. Skin cleansing, sterile field and single-use materials throughout."),
            ("03", "Structured rehabilitation", "Individual rehabilitation guidance follows every injection: load management, movement, and strength work matched to your knee."),
            ("04", "Series &amp; review", "Typically a short series over several weeks, with a follow-up review to check symptoms, function, and whether to continue."),
        ],
        "benefits": [
            ("Direct in-joint delivery", "Delivered directly into the affected joint rather than systemically, which places the preparation where the target tissue is."),
            ("Rehabilitation-first mindset", "Injection is paired with structured rehabilitation, not offered as a stand-alone shot."),
            ("Imaging-guided decision", "Suitability is confirmed with recent imaging, not booked from a symptom list alone."),
            ("Physician-delivered", "The injection is performed by the treating physician, not delegated, under aseptic conditions."),
        ],
        "note": "This programme is offered only where local regulation permits, and it is not a substitute for surgical care where surgery is indicated. It aims to reduce symptoms and support function &mdash; not to reverse structural change.",
        "meta": [
            ("Setting", "Taipei centre and partner clinics, where locally permitted"),
            ("Session", "Guided intra-articular injection"),
            ("Course", "Short series over several weeks"),
            ("Includes", "Rehabilitation guidance and follow-up review"),
        ],
    },
    "adv-iv-laser.html": {
        "label": "Photomedicine",
        "name": "Intravenous Laser Therapy",
        "hero_img": "adv-iv-laser.webp",
        "hero_alt": "A guest resting in a private R2 suite during an ILIB session &mdash; a fine laser fibre taped over the forearm vein, warm lamplight and cream linens",
        "aim": "Low-level intravascular light at specific wavelengths, delivered through a fine intravenous line as an adjunct to IV protocols &mdash; never as a stand-alone treatment.",
        "lead": "Also known as ILIB (intravascular laser irradiation of blood), this photomedicine adjunct delivers low-level light at defined wavelengths through a fine intravenous fibre. It is used alongside an IV drip &mdash; for recovery, neurological support and hangover programmes &mdash; not as a treatment on its own.",
        "steps": [
            ("01", "Assessment &amp; planning", "A physician plans the laser session as part of your wider IV course &mdash; the two run together, not separately."),
            ("02", "IV access &amp; fibre placement", "A fine intravenous line is placed. The laser fibre is introduced through this line under aseptic conditions in a private suite."),
            ("03", "Low-level intravascular light", "Light at the chosen wavelength is delivered continuously for about 30 to 60 minutes, alongside your IV drip."),
            ("04", "Session review", "Post-session hydration and a brief written summary. Frequency is set as a short series aligned with your IV plan."),
        ],
        "benefits": [
            ("Adjunct, not stand-alone", "Delivered alongside a planned IV protocol &mdash; recovery, neuro-support, hangover &mdash; so the session serves the wider plan."),
            ("Physician-planned", "Wavelength, session length and frequency are set by the treating physician, not by a fixed package."),
            ("Comfortable and short", "About 30 to 60 minutes in a private suite alongside your drip, with no downtime."),
            ("Aseptic, single-use", "Sterile technique and single-use disposables throughout."),
        ],
        "note": "Intravenous laser is an adjunct to IV therapy, not a stand-alone treatment. It is offered at the Taipei centre and at selected partner clinics.",
        "meta": [
            ("Setting", "Taipei and selected partner clinics"),
            ("Session", "About 30&ndash;60 minutes, alongside IV therapy"),
            ("Course", "Short series, aligned with your IV plan"),
            ("Pairs with", "Precision IV hydration, recovery, neuro-support protocols"),
        ],
    },
}


def render_adv(spec):
    steps_html = "".join(
        f'''
              <li class="step">
                <span class="step__n">{n}</span>
                <div class="step__body">
                  <h3>{title}</h3>
                  <p>{text}</p>
                </div>
              </li>'''
        for n, title, text in spec["steps"]
    )
    benefits_html = "".join(
        f'''
              <li class="bene">
                <h4>{title}</h4>
                <p>{text}</p>
              </li>'''
        for title, text in spec["benefits"]
    )
    meta_html = "".join(
        f'<div><span class="drip__k">{k}</span><span class="drip__v">{v}</span></div>'
        for k, v in spec["meta"]
    )
    note_html = f'<p class="drip__note"><em>{spec["note"]}</em></p>' if spec.get("note") else ""
    principle_html = render_principle(spec.get("principle"), band="navy")
    return f"""    <section class="hero hero--page hero--drip">
      <img class="hero__bg" src="img/{spec['hero_img']}" alt="{spec['hero_alt']}">
      <div class="hero__inner">
        <p class="eyebrow reveal">{spec['label']}</p>
        <h1 class="reveal">{spec['name']}.</h1>
        <p class="lead reveal">{spec['aim']}</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap drip reveal">
        <div class="drip__lead">
          <p class="eyebrow">The therapy</p>
          <h2>What this <em>therapy is</em>.</h2>
          <hr class="rule">
          <p class="lead">{spec['lead']}</p>
        </div>

        <div class="drip__meta">
          {meta_html}
        </div>
      </div>
    </section>

    <section class="band band--navy band--hair">
      <div class="wrap reveal">
        <div class="band__head narrow">
          <p class="eyebrow">How the session runs</p>
          <h2>Step by <em>step</em>.</h2>
          <p class="lead">Every part of the session is decided by the treating physician. Nothing is booked from a menu.</p>
        </div>
        <hr class="rule">
        <ol class="steps">{steps_html}
        </ol>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap reveal">
        <div class="band__head narrow">
          <p class="eyebrow">Why it&rsquo;s built this way</p>
          <h2>The <em>advantages</em>.</h2>
        </div>
        <hr class="rule">
        <ul class="benes">{benefits_html}
        </ul>
        {note_html}
      </div>
    </section>

{principle_html}

    <section class="band band--ivory band--hair">
      <div class="wrap reveal narrow">
        <p class="eyebrow">Next step</p>
        <h2>See if this <em>fits you</em>.</h2>
        <hr class="rule">
        <p class="lead">Every advanced therapy is confirmed at consultation. Suitability, timing and any subsequent session are decided by your physician after reviewing your history and, where it changes the plan, your bloodwork.</p>
        <div class="cta-row"><a class="btn btn--gold" href="consultation.html">Request a consultation</a><a class="arrowlink" href="advanced-care.html">Back to Advanced Care &rarr;</a></div>
      </div>
    </section>

{INVITE}
"""


adv_bodies = {slug: render_adv(spec) for slug, spec in adv_pages.items()}


# ---------------------------------------------------------------- news

# Each item: (slug, category, date_display, date_iso, title, lede, hero_img, hero_alt, location)
news_items = [
    (
        "news-mvita-opening.html",
        "Cooperation \u00b7 Ho Chi Minh City",
        "11 September 2026",
        "2026-09-11",
        "M VITA Clinic opens in Ho Chi Minh City",
        "A new cooperating wellness clinic in central Ho Chi Minh City &mdash; standing beside our existing HCM partner and widening the network of physician-led rejuvenation care in the region.",
        "news/mvita-02-partnership-signing.jpg",
        "Dr. Tony Su shaking hands with the M VITA founder in the M VITA consultation room in front of the clinic team, formalising the R2-IWAA \u00b7 M VITA cooperation.",
        "Ho Chi Minh City",
    ),
]

# Full-detail bodies for each news story
news_pages = {
    "news-mvita-opening.html": {
        "category": "Cooperation \u00b7 Ho Chi Minh City",
        "date_display": "11 September 2026",
        "date_iso": "2026-09-11",
        "title": "M VITA Clinic opens in Ho Chi Minh City",
        "hero_img": "news/mvita-01-stage-toast.jpg",
        "hero_alt": "The M VITA founding team lined up on stage in front of the &lsquo;Grand Opening MVITA&rsquo; backdrop, raising champagne with sparklers on the floor.",
        "dek": "A new cooperating wellness clinic in central Ho Chi Minh City &mdash; standing beside our existing HCM partner and widening the network of physician-led rejuvenation care in the region.",
        "sections": [
            ("A new home for wellness in the city",
             ["M VITA Clinic &mdash; <em>Ph\u00f2ng Kh\u00e1m Tr\u1ebb H\u00f3a &amp; T\u00e1i T\u1ea1o To\u00e0n Di\u1ec7n</em>, a comprehensive rejuvenation &amp; regeneration clinic &mdash; opened its doors on 3/2 Street in central Ho Chi Minh City on 11 September 2026, in front of guests, patients and partners.",
              "The clinic is positioned as a Wellness &amp; Beauty Center, with a medical-standard dermatology practice and a physician-led approach to whole-body rejuvenation. Its founding team brings more than ten years of clinical experience in the field."]),
            ("What M VITA offers on day one",
             ["The clinic opens with a considered wellness menu &mdash; magnetic-wave therapy, hyperbaric oxygen, active-healthcare programmes and targeted work for headache, neck and spine, and everyday recovery. A complimentary wellness assessment is offered to introduce the space to new visitors.",
              "The interior follows the same visual language that patients across our network will recognise &mdash; warm gold, calm neutrals and quiet lighting, chosen so that clinical work happens in a room that already feels considered."]),
            ("What it means for R2-IWAA",
             ["M VITA joins us as a cooperating clinic in Ho Chi Minh City, alongside our existing partner care already offered in the city. The two settings serve different neighbourhoods and different patient needs; together they widen the map of places a patient can be seen without leaving the region.",
              "Dr. Tony Su joins M VITA as a visiting specialist consultant &mdash; <em>b\u00e1c s\u0129 c\u1ed1 v\u1ea5n chuy\u00ean khoa</em> &mdash; supporting the clinic&rsquo;s founding physicians on regenerative and anti-aging programmes.",
              "As with every location we cooperate with, availability of individual therapies is confirmed at consultation and differs by site. The IV programme and materials standards authored in Taipei remain the reference; local teams apply them to the room they run."]),
        ],
        "gallery": {
            "heading": "From the opening",
            "note": "Photographs courtesy of M VITA Clinic.",
            "images": [
                ("news/mvita-02-partnership-signing.jpg", "Dr. Tony Su in the M VITA consultation room shaking hands with the M VITA founder in front of the clinic team &mdash; formalising the cooperation between R2-IWAA and M VITA."),
                ("news/mvita-05-drsu-poster.jpg", "Grand-opening announcement introducing Dr. Tony Su (Taiwan) as visiting specialist consultant at M VITA Clinic, co-branded with R2-IWAA."),
                ("news/mvita-03-drsu-consultation.jpg", "Dr. Tony Su at the M VITA consultation desk reviewing an AI-assisted patient assessment."),
                ("news/mvita-04-red-carpet.jpg", "M VITA hosts on the red carpet in front of the M&nbsp;VITA installation and floral arrangements at the ceremony entrance."),
                ("news/mvita-01-stage-toast.jpg", "The M VITA founding team on stage during the toast, in front of the &lsquo;Grand Opening MVITA&rsquo; backdrop."),
            ],
        },
        "visit": {
            "name": "M VITA CLINIC \u00b7 Wellness &amp; Beauty Center",
            "address": "572A \u0110\u01b0\u1eddng 3/2, Ph\u01b0\u1eddng Di\u00ean H\u1ed3ng, Ho Chi Minh City, Vietnam",
            "hours": "Monday to Sunday, 09:00 \u2013 20:00",
            "hotline": "+84 90 569 8888",
            "website": ("mvitaclinic.vn", "https://mvitaclinic.vn/"),
        },
        "related": [
            ("See our locations", "locations.html"),
            ("Speak to the R2-IWAA team", "consultation.html"),
        ],
    },
}


def render_news_card(item):
    slug, category, date_display, date_iso, title, lede, hero_img, hero_alt, _location = item
    return f"""
          <a class="card card--iv card--link" href="{slug}">
            <div class="card__media"><img src="img/{hero_img}" alt="{hero_alt}" loading="lazy"></div>
            <div class="card__body">
              <span class="card__label">{category}</span>
              <h3>{title}</h3>
              <p><time datetime="{date_iso}">{date_display}</time> &middot; {lede}</p>
              <span class="card__more">Read the story &rarr;</span>
            </div>
          </a>"""


news_cards_html = "".join(render_news_card(item) for item in news_items)

news = f"""    <section class="hero hero--page">
      <picture>
        <source media="(max-width: 720px)" srcset="img/hero-taipei-dusk-portrait.webp">
        <img class="hero__bg" src="img/hero-taipei-dusk.webp" alt="Taipei skyline at deep dusk with warm city lights beneath a navy and emerald sky">
      </picture>
      <div class="hero__inner">
        <p class="eyebrow reveal">News from the network</p>
        <h1 class="reveal">Clinics, cooperations, and moments <em>from the practice</em>.</h1>
        <p class="lead reveal">Openings, partnerships and small moments across R2-IWAA and the clinics we cooperate with in Taipei, Yangon and Ho Chi Minh City.</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap">
        <div class="band__head reveal">
          <p class="eyebrow">Latest</p>
          <h2>What&rsquo;s <em>happening</em>.</h2>
        </div>
        <div class="cards cards--iv reveal">{news_cards_html}
        </div>
      </div>
    </section>
{INVITE}
"""


def render_news(spec):
    sections_html = ""
    for i, (heading, paras) in enumerate(spec["sections"]):
        paras_html = "".join(f"          <p>{p}</p>\n" for p in paras)
        band_class = "band--ivory" if i % 2 == 0 else "band--navy"
        sections_html += f"""
    <section class="band {band_class} band--hair">
      <div class="wrap wrap--reading reveal">
        <h2>{heading}</h2>
{paras_html}      </div>
    </section>
"""

    gallery_html = ""
    gallery = spec.get("gallery")
    if gallery:
        # First image is the feature; remainder go in a 2x2 grid
        feature_src, feature_alt = gallery["images"][0]
        rest = gallery["images"][1:]
        tiles_html = "".join(
            f'          <figure class="story__tile"><img src="img/{src}" alt="{alt}" loading="lazy"></figure>\n'
            for src, alt in rest
        )
        # Alternate band shade based on how many text sections came before
        gband = "band--navy" if len(spec["sections"]) % 2 == 0 else "band--ivory"
        gallery_html = f"""
    <section class="band {gband} band--hair">
      <div class="wrap reveal">
        <div class="band__head">
          <p class="eyebrow">Gallery</p>
          <h2>{gallery['heading']}</h2>
        </div>
        <div class="story__gallery">
          <figure class="story__feature">
            <img src="img/{feature_src}" alt="{feature_alt}" loading="lazy">
          </figure>
          <div class="story__tiles">
{tiles_html}          </div>
        </div>
        <p class="story__credit">{gallery['note']}</p>
      </div>
    </section>
"""

    visit = spec["visit"]
    website_label, website_url = visit["website"]
    visit_html = f"""
    <section class="band band--ivory band--hair">
      <div class="wrap wrap--reading reveal">
        <p class="eyebrow">Visit</p>
        <h3 class="story__visit-name">{visit['name']}</h3>
        <dl class="story__visit">
          <div><dt>Address</dt><dd>{visit['address']}</dd></div>
          <div><dt>Hours</dt><dd>{visit['hours']}</dd></div>
          <div><dt>Hotline</dt><dd><a href="tel:{visit['hotline'].replace(' ', '')}">{visit['hotline']}</a></dd></div>
          <div><dt>Website</dt><dd><a href="{website_url}" target="_blank" rel="noopener">{website_label}</a></dd></div>
        </dl>
      </div>
    </section>
"""

    related_html = "".join(
        f'          <a class="arrowlink" href="{href}">{label} &rarr;</a>\n'
        for label, href in spec["related"]
    )
    next_html = f"""
    <section class="band band--ivory band--hair">
      <div class="wrap wrap--reading reveal">
        <p class="eyebrow">Next step</p>
        <div class="story__related">
{related_html}          <a class="arrowlink" href="news.html">Back to News &rarr;</a>
        </div>
      </div>
    </section>
"""

    return f"""    <section class="hero hero--page hero--story">
      <img class="hero__bg" src="img/{spec['hero_img']}" alt="{spec['hero_alt']}">
      <div class="hero__inner">
        <p class="eyebrow reveal">{spec['category']} &middot; <time datetime="{spec['date_iso']}">{spec['date_display']}</time></p>
        <h1 class="reveal">{spec['title']}</h1>
        <p class="lead reveal">{spec['dek']}</p>
      </div>
    </section>
{sections_html}{gallery_html}{visit_html}{next_html}{INVITE}
"""


news_bodies = {slug: render_news(spec) for slug, spec in news_pages.items()}


pages = [
    ("index.html", "R2-IWAA &mdash; International Wellness &amp; Anti-Aging",
     "Physician-led regenerative and anti-aging medicine. IV therapy and advanced regenerative care in Taipei, Yangon and Ho Chi Minh City.", home, "index.html"),
    ("iv-therapy.html", "IV Therapy &mdash; R2-IWAA",
     "Intravenous therapy programmes built from your history and bloodwork, delivered to one standard in Taipei, Yangon and Ho Chi Minh City.", iv, "iv-therapy.html"),
    ("advanced-care.html", "Advanced Regenerative Care &mdash; R2-IWAA",
     "Selected advanced regenerative therapies at R2-IWAA, considered individually after full medical assessment.", adv, "advanced-care.html"),
    ("founder.html", "Dr. Tony Su &mdash; R2-IWAA",
     "Dr. Tony Su, founder and medical director of R2 International Wellness & Anti-Aging, practising in Mandarin, English and Myanmar.", founder, "founder.html"),
    ("locations.html", "Locations &mdash; R2-IWAA",
     "R2-IWAA clinics in Taipei, Yangon and Ho Chi Minh City, with clinical training and materials prepared at the Taipei centre.", locations, "locations.html"),
    ("consultation.html", "Request a Consultation &mdash; R2-IWAA",
     "Request a private one-to-one consultation with the R2-IWAA medical team in Mandarin, English or Myanmar.", consult, "consultation.html"),
    ("news.html", "News from the network &mdash; R2-IWAA",
     "Openings, cooperations and small moments across R2 International Wellness & Anti-Aging and the clinics we work with in Taipei, Yangon and Ho Chi Minh City.", news, "news.html"),
]

# append each drip subpage
for slug, _label, name, text, _img, _alt in iv_cards:
    display_name = name.replace("&rsquo;", "\u2019").replace("&amp;", "&")
    pages.append((
        slug,
        f"{display_name} &mdash; R2-IWAA",
        text,
        drip_bodies[slug],
        "iv-therapy.html",
    ))

# append each advanced-care subpage
for slug, spec in adv_pages.items():
    display_name = spec["name"].replace("&rsquo;", "\u2019").replace("&amp;", "&")
    pages.append((
        slug,
        f"{display_name} &mdash; R2-IWAA",
        spec["aim"].replace("&mdash;", "\u2014").replace("&nbsp;", " "),
        adv_bodies[slug],
        "advanced-care.html",
    ))

# append each news story detail page
for slug, spec in news_pages.items():
    display_title = spec["title"].replace("&rsquo;", "\u2019").replace("&amp;", "&")
    display_dek = spec["dek"].replace("&mdash;", "\u2014").replace("&nbsp;", " ").replace("&amp;", "&")
    pages.append((
        slug,
        f"{display_title} &mdash; R2-IWAA News",
        display_dek,
        news_bodies[slug],
        "news.html",
    ))

for slug, title, desc, body, cur in pages:
    page(slug, title, desc, body, cur)
    print("wrote", slug)
