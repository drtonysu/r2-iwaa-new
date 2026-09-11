# Assembles the static R2-IWAA pages from shared shell + per-page bodies.
import os

OUT = os.path.dirname(os.path.abspath(__file__))

LOGO = """<img class="brand__mark" src="img/logo-512.png" alt="" width="512" height="488">"""

FAVICON = "img/favicon.png"

NAV_ITEMS = [
    ("iv-therapy.html", "IV Therapy"),
    ("locations.html", "Locations"),
    ("founder.html", "Dr. Tony Su"),
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
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Noto+Sans+Myanmar:wght@400;500&display=swap" rel="stylesheet">
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
      <img class="hero__bg" src="img/hero-taipei-dusk.webp" alt="Taipei skyline at deep dusk with warm city lights beneath a navy and emerald sky">
      <div class="hero__inner">
        <p class="eyebrow reveal">R2 International Wellness &amp; Anti-Aging</p>
        <h1 class="reveal">Medicine, <em>calibrated</em> to you.</h1>
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
            <p>Our foundation. Available at every R2 location.</p>
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
    ("01 &middot; Foundation", "Anti-Aging Drip", "Our entry formula for antioxidant support and everyday free-radical clearance.", "iv-01-antiaging.webp", "Three amber ampoules on a brushed gold tray, warm side light on deep navy velvet"),
    ("02 &middot; Foundation", "Premium Anti-Aging Drip", "An amino-acid-based version of our foundation formula, for periods of depletion.", "iv-02-premium.webp", "A tall pearl-white amino acid vial with a gold cap on polished emerald marble"),
    ("03 &middot; Clearance", "Detox Drip", "Metabolic and hepatic support, closing with a slow, separately administered antioxidant infusion.", "iv-03-detox.webp", "Amber fluid separating from emerald fluid through a translucent membrane, golden threads dispersing"),
    ("04 &middot; Clearance", "Advanced Antioxidant &amp; Detox", "An escalated course for accumulated stress, sleep loss and prolonged fatigue.", "iv-04-advanced-detox.webp", "Golden intravenous drip chamber with a single amber droplet caught mid-fall in a warm treatment suite"),
    ("05 &middot; Foundation", "High-Dose Vitamin C", "A concentrated vitamin C infusion, dosed and paced under physician supervision.", "iv-05-vitc.webp", "Sliced orange and lemon cross-sections on dark stone, translucent flesh catching golden light"),
    ("06 &middot; Foundation", "Myers&rsquo; Cocktail", "The classic B-vitamin, vitamin C, magnesium and zinc infusion.", "iv-06-myers.webp", "An amber, a clear and a gold-capped pharmaceutical vial resting on folded dark navy velvet"),
    ("07 &middot; Neurology", "NeuroVitality Drip", "A two-stage neuro-support protocol, offered after individual medical assessment.", "iv-07-neuro.webp", "Abstract golden neural filaments and glowing nodes suspended in dark navy fluid"),
    ("08 &middot; Recovery", "Sport Recovery Drip", "A fast amino-acid infusion for athletes and heavy training loads.", "iv-08-sport.webp", "A single amber vial beside a folded ivory linen towel on dark stone with a deep navy background"),
    ("09 &middot; Recovery", "Post-Hangover Drip", "Fluid replacement followed by slower antioxidant support for hepatic recovery.", "iv-09-hangover.webp", "A crystal-cut carafe of amber liquid and lemon halves on a dark emerald marble slab"),
    ("10 &middot; Foundation", "Omega Drip", "An omega-3 emulsion with vitamin C and B-complex, for cerebral and cardiac support.", "iv-10-omega.webp", "A single golden omega oil droplet falling into a shallow crystal dish with warm gold bokeh"),
]

cards_html = ""
for label, name, text, img, alt in iv_cards:
    cards_html += f"""
          <article class="card card--iv">
            <div class="card__media"><img src="img/{img}" alt="{alt}" loading="lazy"></div>
            <div class="card__body">
              <span class="card__label">{label}</span>
              <h3>{name}</h3>
              <p>{text}</p>
            </div>
          </article>"""

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
        "Apheresis",
        "Therapeutic Plasma Exchange",
        "Blood plasma is separated and replaced with sterile albumin and saline; your blood cells are returned to circulation. Used to lower circulating inflammatory and metabolic factors.",
        "Adults with chronic inflammatory burden, elevated cardiometabolic markers, or persistent post-viral fatigue &mdash; where laboratory workup supports it.",
        [
            ("Setting", "Taipei clinic only, under continuous physician supervision"),
            ("Session", "About 2 to 3 hours per procedure, cyclic apheresis system"),
            ("Course", "Typically a short assessed course, spaced weekly or monthly"),
            ("Before", "Full blood panel, cardiac and coagulation screen required"),
        ],
        "adv-blood-purification.webp",
        "Golden and emerald plasma swirling through a translucent membrane",
    ),
    (
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
        "A slender gold-emerald laser beam refracting through a translucent IV chamber",
    ),
]

rows_html = ""
for label, name, what, who, meta, img, alt in adv_rows:
    meta_items = "".join(
        f'<div class="row__meta-item"><span class="row__meta-key">{k}</span><span class="row__meta-val">{v}</span></div>'
        for k, v in meta
    )
    rows_html += f"""
          <article class="row">
            <div class="row__media"><img src="img/{img}" alt="{alt}" loading="lazy"></div>
            <div class="row__body">
              <span class="card__label">{label}</span>
              <h3>{name}</h3>
              <p class="row__what">{what}</p>
              <p class="row__who"><span class="row__who-tag">Who it may suit</span> {who}</p>
              <div class="row__meta">{meta_items}</div>
            </div>
          </article>"""

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

    <section class="band band--navy band--hair">
      <div class="wrap">
        <div class="band__head reveal narrow">
          <p class="eyebrow">Publications &amp; Training</p>
          <h2>Trained where the margin for error is <em>smallest</em>.</h2>
          <p class="lead">Critical care, chest and emergency medicine in Taiwan first &mdash; then cellular medicine in Japan and precision medicine at Harvard Medical School. The order matters: acute-care judgement came before the aesthetics.</p>
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
            <span class="pubs__body">NK cell therapy &amp; Osaki Method under Prof. Masuyama</span>
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
            <span class="pubs__body">American College of Physicians &middot; IASCT</span>
            <span class="pubs__place">Ongoing</span>
          </li>
        </ol>
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
]

for slug, title, desc, body, cur in pages:
    page(slug, title, desc, body, cur)
    print("wrote", slug)
