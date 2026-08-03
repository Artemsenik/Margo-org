/* ============================================================
   Margo Animal Care Initiative — site.js
   Zugängliche Mobile-Navigation: Fokusbindung, Escape,
   aria-expanded, Scroll-Sperre. Ohne Abhängigkeiten.
   ============================================================ */
(function () {
  'use strict';

  var burger = document.querySelector('[data-nav-toggle]');
  var drawer = document.querySelector('[data-nav-drawer]');
  if (!burger || !drawer) return;

  var lastFocused = null;

  function focusable() {
    // Kein offsetParent-Filter: Das Menü ist während der Einblend-Transition
    // noch visibility:hidden, wäre also fälschlich leer.
    return Array.prototype.slice.call(
      drawer.querySelectorAll('a[href], button:not([disabled])')
    );
  }

  function open() {
    lastFocused = document.activeElement;
    drawer.setAttribute('data-open', 'true');
    burger.setAttribute('aria-expanded', 'true');
    document.body.setAttribute('data-nav-open', 'true');
    document.addEventListener('keydown', onKeydown);
    // Fokus erst setzen, wenn das Menü tatsächlich sichtbar ist
    requestAnimationFrame(function () {
      var items = focusable();
      if (items.length) items[0].focus();
    });
  }

  function close(returnFocus) {
    drawer.setAttribute('data-open', 'false');
    burger.setAttribute('aria-expanded', 'false');
    document.body.removeAttribute('data-nav-open');
    document.removeEventListener('keydown', onKeydown);
    if (returnFocus !== false) {
      (lastFocused || burger).focus();
    }
  }

  function isOpen() {
    return burger.getAttribute('aria-expanded') === 'true';
  }

  function onKeydown(e) {
    if (e.key === 'Escape' || e.key === 'Esc') {
      e.preventDefault();
      close();
      return;
    }
    if (e.key !== 'Tab') return;

    // Fokusbindung innerhalb des Menüs
    var items = focusable();
    if (!items.length) return;
    var first = items[0];
    var last = items[items.length - 1];

    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }

  burger.addEventListener('click', function () {
    isOpen() ? close() : open();
  });

  // Nach Navigation im Menü schliessen
  drawer.addEventListener('click', function (e) {
    if (e.target.closest('a')) close(false);
  });

  // Beim Wechsel auf Desktopbreite zurücksetzen
  var mq = window.matchMedia('(min-width:900px)');
  var onChange = function (e) { if (e.matches && isOpen()) close(false); };
  mq.addEventListener ? mq.addEventListener('change', onChange)
                      : mq.addListener(onChange);
})();
