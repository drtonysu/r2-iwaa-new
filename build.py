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
      <button class="theme-toggle" type="button" aria-label="Toggle light and dark theme" title="Toggle theme">
        <svg class="theme-toggle__moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        <svg class="theme-toggle__sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
      </button>
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
        <span>&copy; 2026 R2 International Wellness &amp; Anti-Aging</span>
        <span>Availability of individual therapies is confirmed at consultation and differs by location.</span>
      </div>
    </div>
  </footer>"""


def page(slug, title, desc, body, current=None):
    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <script>(function(){{try{{var t=localStorage.getItem('r2-theme');if(t==='light'||t==='dark'){{document.documentElement.setAttribute('data-theme',t);}}}}catch(e){{}}}})();</script>
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
        <h2>Every plan begins with a conversation.</h2>
        <p>A private consultation with our medical team — your history, your goals, and an honest view of what is appropriate for you.</p>
        <a class="btn btn--solid" href="consultation.html">Request a consultation</a>
      </div>
    </section>"""

# ---------------------------------------------------------------- home

home = f"""    <section class="hero">
      <img class="hero__bg" src="img/hero-taipei-dusk.webp" alt="Taipei skyline at deep dusk with warm city lights beneath a navy and emerald sky">
      <div class="hero__inner">
        <p class="eyebrow reveal">R2 International Wellness &amp; Anti-Aging</p>
        <h1 class="reveal">Medicine, calibrated to you.</h1>
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
          <h2>Intravenous therapy, built around you.</h2>
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
        <h2>Selected therapies, by consultation.</h2>
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
          <h2>One standard, three cities.</h2>
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
      <div class="wrap">
        <div class="band__head reveal" style="max-width:640px">
          <p class="eyebrow">Founder</p>
          <h2>Dr. Tony Su</h2>
          <hr class="rule">
          <p class="lead">Founder and Medical Director. He leads every clinical protocol at R2-IWAA and trains the teams that deliver it.</p>
          <div class="founder__meta" style="margin-top:1.4rem"><span>Mandarin</span><span>English</span><span>Myanmar</span></div>
          <a class="arrowlink" href="founder.html" style="margin-top:2rem;display:inline-flex">About Dr. Su &rarr;</a>
        </div>
      </div>
    </section>

    <section class="band band--hair band--ivory">
      <div class="wrap">
        <div class="band__head reveal">
          <p class="eyebrow">Where to find us</p>
          <h2>Three clinics, one network.</h2>
        </div>
        <hr class="rule">
        <div class="locs reveal">
          <div class="loc">
            <span class="loc__tag">Main centre</span>
            <h3>Taipei &mdash; R2-IWAA</h3>
            <p>Shilin District, Taipei. Full-service medical centre, clinical training and materials preparation.</p>
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
    ("01 &middot; Foundation", "Anti-Aging Drip", "Our entry formula for antioxidant support and everyday free-radical clearance.", "iv-vials.webp", "Three amber ampoules on a brushed gold tray"),
    ("02 &middot; Foundation", "Premium Anti-Aging Drip", "An amino-acid-based version of our foundation formula, for periods of depletion.", "iv-glow.webp", "A luminous pearl-white vial with a gold cap on emerald stone"),
    ("03 &middot; Clearance", "Detox Drip", "Metabolic and hepatic support, closing with a slow, separately administered antioxidant infusion.", "abstract-purify.webp", "Abstract golden fluid separating from dark fluid through a translucent membrane"),
    ("04 &middot; Clearance", "Advanced Antioxidant &amp; Detox", "An escalated course for accumulated stress, sleep loss and prolonged fatigue.", "iv-plan.webp", "A physician's desk with a hand-drawn chart, pen and clear vials"),
    ("05 &middot; Foundation", "High-Dose Vitamin C", "A concentrated vitamin C infusion, dosed and paced under physician supervision.", "reception.webp", "A emerald marble counter with a white orchid in a matte black vase"),
    ("06 &middot; Foundation", "Myers&rsquo; Cocktail", "The classic B-vitamin, vitamin C, magnesium and zinc infusion.", "iv-myers.webp", "A single amber ampoule with a gold foil band on dark navy velvet"),
    ("07 &middot; Neurology", "NeuroVitality Drip", "A two-stage neuro-support protocol, offered after individual medical assessment.", "iv-neuro.webp", "Golden light refracting through an intravenous fluid bag against dark emerald"),
    ("08 &middot; Recovery", "Sport Recovery Drip", "A fast amino-acid infusion for athletes and heavy training loads.", "iv-rest.webp", "An ivory cashmere throw over a dark leather treatment chair"),
    ("09 &middot; Recovery", "Post-Hangover Drip", "Fluid replacement followed by slower antioxidant support for hepatic recovery.", "iv-recovery2.webp", "A lemon slice and a small glass dropper bottle on dark emerald marble"),
    ("10 &middot; Foundation", "Omega Drip", "An omega-3 emulsion with vitamin C and B-complex, for cerebral and cardiac support.", "iv-omega.webp", "Golden droplets suspended in dark navy fluid"),
]

cards_html = ""
for label, name, text, img, alt in iv_cards:
    cards_html += f"""
          <article class="card">
            <img src="img/{img}" alt="{alt}">
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
        <h1 class="reveal">Our foundation, everywhere we practise.</h1>
        <p class="lead reveal">The same protocols, the same materials, the same standard in Taipei, Yangon and Ho Chi Minh City.</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap">
        <div class="band__head reveal">
          <p class="eyebrow">Programmes</p>
          <h2>Chosen for you, not from a menu.</h2>
          <p class="lead">Every programme starts from your history, examination and bloodwork. Composition and pace are set by your physician.</p>
        </div>
        <div class="cards reveal">{cards_html}
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
          <h2>Advanced regenerative care.</h2>
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
            <img src="img/{img}" alt="{alt}">
            <div>
              <span class="card__label">{label}</span>
              <h3>{name}</h3>
              <p class="row__what">{what}</p>
              <p class="row__who"><span class="row__who-tag">Who it may suit</span> {who}</p>
              <div class="row__meta">{meta_items}</div>
            </div>
            <span class="row__note">Availability confirmed<br>at consultation</span>
          </article>"""

adv = f"""    <section class="hero hero--page">
      <img class="hero__bg" src="img/abstract-purify.webp" alt="Abstract golden and emerald fluid separating through a translucent membrane">
      <div class="hero__inner">
        <p class="eyebrow reveal">Advanced regenerative care</p>
        <h1 class="reveal">Discussed individually.</h1>
        <p class="lead reveal">These therapies are not for everyone, and they are not offered from a price list. Each is considered only after full medical assessment.</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap">
        <div class="band__head narrow reveal">
          <p class="eyebrow">What we may discuss</p>
          <h2>A short, honest list.</h2>
          <p class="lead">What is appropriate for you depends on your assessment, and what is available depends on where you are treated. Your physician will tell you both, plainly, before anything begins.</p>
        </div>
        <div class="rows reveal">{rows_html}
        </div>
      </div>
    </section>

    <section class="band band--navy band--hair">
      <div class="wrap narrow reveal">
        <p class="eyebrow">How we speak about outcomes</p>
        <h2>No promises we cannot keep.</h2>
        <hr class="rule">
        <p class="lead">Regenerative medicine is a developing field. We will tell you what is established, what is still being studied, and what we simply do not know &mdash; including when the honest answer is that a therapy is not right for you.</p>
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
          <h2>Calibration over catalogue.</h2>
          <hr class="rule">
          <p class="lead">Dr. Su&rsquo;s position is simple: a patient receives what their biology asks for, at the pace their life allows &mdash; not the package on offer. Every protocol used across the network is written and reviewed by him, and reviewed again when the evidence moves.</p>
          <div class="founder__meta"><span>Internal medicine</span><span>Precision medicine</span><span>Cellular &amp; anti-aging medicine</span></div>
        </div>
      </div>
    </section>

    <section class="band">
      <div class="wrap quote-band reveal">
        <div class="quote-band__photo">
          <img src="img/founder-portrait-warm.webp" alt="Dr. Tony Su in a physician's white coat, hands clasped, natural studio light">
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
          <h2>Trained where the margin for error is smallest.</h2>
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
        <h2>Ten intravenous formulas, one physician&rsquo;s hand.</h2>
        <hr class="rule">
        <p class="lead">The IV programme across every R2-IWAA location is authored by Dr. Su and reviewed each time the evidence moves. Every plan is set to a patient&rsquo;s bloodwork rather than a menu.</p>
        <ol class="protolist">
          <li><em>01</em><span>Anti-Aging Drip</span></li>
          <li><em>02</em><span>Premium Anti-Aging Drip</span></li>
          <li><em>03</em><span>Detox Drip</span></li>
          <li><em>04</em><span>Advanced Antioxidant &amp; Detox</span></li>
          <li><em>05</em><span>High-Dose Vitamin C</span></li>
          <li><em>06</em><span>Myers&rsquo; Cocktail</span></li>
          <li><em>07</em><span>NeuroVitality Drip</span></li>
          <li><em>08</em><span>Sport Recovery Drip</span></li>
          <li><em>09</em><span>Post-Hangover Drip</span></li>
          <li><em>10</em><span>Omega Drip</span></li>
        </ol>
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
        <h1 class="reveal">Taipei, Yangon, Ho Chi Minh City.</h1>
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
          <p class="lead">No.&nbsp;516, Section&nbsp;5, Zhongshan North Road, Shilin District. Our full-service medical centre, and the hub of the network &mdash; where clinical teams are trained and where the materials used in every clinic are prepared and released.</p>
        </div>
      </div>
    </section>

    <section class="band band--navy band--hair">
      <div class="wrap">
        <div class="band__head reveal">
          <p class="eyebrow">Partner clinics</p>
          <h2>Cared for close to home.</h2>
        </div>
        <hr class="rule">
        <div class="locs reveal">
          <div class="loc">
            <span class="loc__tag">Yangon</span>
            <h3>Beauty Bank Wellness &amp; Cell Therapy Center</h3>
            <p>Kamaryut Township, Yangon. Assessment, IV therapy and procedures, with Myanmar-language consultation.</p>
            <p class="lang-my" lang="my">အမှတ် ၁၀၃(D)၊ သံလွင်လမ်း၊ ကမာရွတ်မြိုနယ်၊ ရန်ကုန်မြို။</p>
            <p class="loc__meta">Tel <a href="tel:09886234234">09 886 234 234</a></p>
          </div>
          <div class="loc">
            <span class="loc__tag">Ho Chi Minh City</span>
            <h3>Recover Health</h3>
            <p>260&ndash;262A Điện Biên Phủ, Xuân Hòa Ward, Ho Chi Minh City. Assessment, IV therapy and procedures.</p>
            <p class="loc__meta">Hotline <a href="tel:0902766786">0902 766 786</a> &middot; <a href="mailto:info@recoverhealth.vn">info@recoverhealth.vn</a></p>
          </div>
          <div class="loc">
            <span class="loc__tag">Please note</span>
            <h3>Before you travel</h3>
            <p>Assessment and treatment days differ by city, and not every therapy is offered at every location. Confirm your appointment with us first.</p>
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
        <h1 class="reveal">One to one, before anything else.</h1>
        <p class="lead reveal">Tell us a little and our medical team will arrange a private consultation in Mandarin, English or Myanmar.</p>
      </div>
    </section>

    <section class="band band--ivory">
      <div class="wrap split reveal">
        <div class="split__body">
          <p class="eyebrow">Request</p>
          <h2>Start a conversation.</h2>
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
          <h2>Or reach us now.</h2>
          <hr class="rule">
          <div class="contactlist">
            <div>
              <span>WhatsApp &amp; Viber</span>
              <a href="https://wa.me/886916196333">+886 916 196 333</a>
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
