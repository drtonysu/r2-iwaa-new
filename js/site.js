/* R2-IWAA — shell behaviour: header state, mobile nav, scroll reveal, consultation form */
(function () {
  'use strict';

  // Sticky header state
  var header = document.querySelector('.header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 40);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Mobile navigation
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('.nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.classList.toggle('nav-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('is-open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('nav-open');
        document.body.style.overflow = '';
      }
    });
  }

  // Stagger grid children so groups arrive one after another, not all at once
  var groups = document.querySelectorAll('.facts.reveal, .cards.reveal, .duo.reveal, .locs.reveal, .rows.reveal');
  Array.prototype.forEach.call(groups, function (group) {
    var kids = group.children;
    if (kids.length < 2) return;
    group.classList.remove('reveal');
    Array.prototype.forEach.call(kids, function (kid, i) {
      kid.classList.add('reveal');
      kid.style.setProperty('--reveal-delay', i * 110 + 'ms');
    });
  });

  // Scroll reveal
  var targets = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && targets.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-in');
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: '0px 0px -12% 0px', threshold: 0.08 }
    );
    targets.forEach(function (t) {
      io.observe(t);
    });
  } else {
    targets.forEach(function (t) {
      t.classList.add('is-in');
    });
  }

  // Consultation request — delivered to the clinic over WhatsApp, with an email fallback
  var WHATSAPP = '886916196333';
  var EMAIL = 'care@r2-iwaa.com';

  var form = document.querySelector('.form');
  if (form) {
    var val = function (id) {
      var el = form.querySelector('#' + id);
      if (!el) return '';
      if (el.tagName === 'SELECT') return el.options[el.selectedIndex].text;
      return el.value.trim();
    };

    var compose = function () {
      var lines = [
        'Consultation request — r2-iwaa.com',
        '',
        'Name: ' + val('name'),
        'Contact: ' + val('contact'),
        'Preferred location: ' + val('city'),
        'Language: ' + val('lang')
      ];
      var msg = val('msg');
      if (msg) lines.push('', 'Notes:', msg);
      return lines.join('\n');
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (typeof form.reportValidity === 'function' && !form.reportValidity()) return;

      var body = compose();
      window.open('https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(body), '_blank', 'noopener');

      var ok = document.querySelector('.form__ok');
      if (ok) {
        var fallback = ok.querySelector('.form__fallback');
        if (fallback) {
          fallback.setAttribute(
            'href',
            'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Consultation request — ' + (val('name') || 'website')) + '&body=' + encodeURIComponent(body)
          );
        }
        ok.classList.add('is-on');
        ok.setAttribute('role', 'status');
      }
      form.querySelector('button[type="submit"]').disabled = true;
    });
  }
})();


/* Back-to-top button: reveal after scrolling past ~50% of viewport height. */
(function () {
  var btn = document.getElementById('backToTop');
  if (!btn) return;
  var threshold = Math.max(400, window.innerHeight * 0.6);
  var ticking = false;
  function update() {
    if (window.scrollY > threshold) btn.classList.add('is-visible');
    else btn.classList.remove('is-visible');
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) {
      window.requestAnimationFrame(update);
      ticking = true;
    }
  }, { passive: true });
  window.addEventListener('resize', function () {
    threshold = Math.max(400, window.innerHeight * 0.6);
    update();
  });
  btn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
  update();
})();
