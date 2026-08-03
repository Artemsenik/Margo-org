/* ============================================================
   Zwei-Klick-Video (datenschutzfreundlich)
   Lädt den Vimeo-Player erst nach aktivem Klick. Vorher besteht
   keine Verbindung zum Anbieter. Ohne data-vimeo-id passiert nichts.
   ============================================================ */
(function () {
  'use strict';

  var frame = document.getElementById('margo-video-frame');
  if (!frame) return;

  var id = (frame.getAttribute('data-vimeo-id') || '').trim();
  var ready = frame.getAttribute('data-video-ready') === 'true';
  var trigger = frame.querySelector('[data-video-trigger]');
  var badge = frame.querySelector('[data-video-badge]');
  var note = frame.querySelector('[data-video-note]');
  var ph = frame.querySelector('.mw-video__ph');

  // Kein Video hinterlegt: Platzhalter bleibt unverändert stehen.
  if (!ready || !id) return;

  // Vorschaubild setzen (falls vorhanden)
  var poster = 'assets/hero/margo-video-poster.webp';
  var probe = new Image();
  probe.onload = function () {
    ph.style.backgroundImage = 'url("' + poster + '")';
    ph.setAttribute('data-poster', '');
  };
  probe.src = poster;

  if (badge) badge.textContent = 'Video ansehen';
  if (note) note.textContent = 'Klicken zum Abspielen. Erst dann wird der Player von Vimeo geladen.';

  function load() {
    var title = frame.getAttribute('data-video-title') || 'Video';
    // Datensparsame Parameter: do-not-track, kein Zuschauer-Zubehör
    var src = 'https://player.vimeo.com/video/' + encodeURIComponent(id) +
              '?dnt=1&title=0&byline=0&portrait=0&badge=0&autoplay=1';
    var wrap = document.createElement('div');
    wrap.className = 'mw-video__embed';
    var iframe = document.createElement('iframe');
    iframe.src = src;
    iframe.title = title;
    iframe.setAttribute('loading', 'lazy');
    iframe.setAttribute('allow', 'autoplay; fullscreen; picture-in-picture');
    iframe.setAttribute('allowfullscreen', '');
    wrap.appendChild(iframe);
    ph.replaceWith(wrap);
  }

  trigger.addEventListener('click', load);
  trigger.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); load(); }
  });
})();
