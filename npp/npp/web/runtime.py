"""
N++ Web Interactive Client Runtime
Provides instant client-side interactivity with zero external dependencies.
Features: toast notifications, modal dialogs, tab switcher, counters,
live search filter, theme switcher, parallax, typewriter, accordions,
ripple buttons, lazy images, progress bars, tooltips, scroll-to-top.
"""

# ── CSS injected into every N++ webpage ───────────────────────────────────────
INTERACTIVE_RUNTIME_CSS = """
/* ===== N++ Interactive Runtime CSS ===== */

/* --- Toasts --- */
#npp-toast-container { position:fixed; bottom:24px; right:24px; z-index:10000;
  display:flex; flex-direction:column; gap:10px; pointer-events:none; }
.npp-toast { padding:14px 22px; border-radius:12px;
  box-shadow:0 12px 40px rgba(0,0,0,0.4);
  font-weight:600; display:flex; align-items:center; gap:10px;
  transform:translateY(30px); opacity:0;
  transition:transform 0.35s cubic-bezier(0.16,1,0.3,1), opacity 0.35s ease;
  pointer-events:auto; font-size:0.95rem; min-width:220px; max-width:380px; }
.npp-toast.npp-toast-show { transform:translateY(0); opacity:1; }
.npp-toast-icon { font-size:1.2rem; }

/* --- Modal Overlay --- */
.npp-modal {
  display:none; position:fixed; inset:0; z-index:9000;
  background:rgba(0,0,0,0.7); backdrop-filter:blur(6px);
  align-items:center; justify-content:center;
  opacity:0; transition:opacity 0.25s ease; }
.npp-modal.open { opacity:1; }
.npp-modal-box {
  background:var(--npp-surface, #1e293b); border-radius:20px;
  padding:36px 40px; max-width:560px; width:90%; position:relative;
  box-shadow:0 30px 80px rgba(0,0,0,0.6);
  transform:scale(0.88) translateY(30px);
  transition:transform 0.3s cubic-bezier(0.16,1,0.3,1);
  border:1px solid var(--npp-border, #334155); }
.npp-modal.open .npp-modal-box { transform:scale(1) translateY(0); }
.npp-modal-close {
  position:absolute; top:14px; right:18px; background:none; border:none;
  font-size:1.6rem; cursor:pointer; color:var(--npp-text-muted, #94a3b8);
  line-height:1; transition:color 0.2s, transform 0.2s; }
.npp-modal-close:hover { color:var(--npp-text, #fff); transform:rotate(90deg); }
.npp-modal-title { font-size:1.4rem; font-weight:700; margin:0 0 14px;
  color:var(--npp-text, #fff); }
.npp-modal-body { color:var(--npp-text-muted, #94a3b8); line-height:1.7; }
.npp-modal-footer { margin-top:24px; display:flex; gap:12px; justify-content:flex-end; }

/* --- Tabs --- */
.npp-tabs-container { width:100%; }
.npp-tab-bar {
  display:flex; gap:4px; background:var(--npp-surface, #1e293b);
  border-radius:12px 12px 0 0; padding:6px 6px 0;
  border-bottom:2px solid var(--npp-border, #334155); overflow-x:auto; }
.npp-tab-button {
  padding:10px 22px; border:none; background:transparent; cursor:pointer;
  font-size:0.9rem; font-weight:600; border-radius:8px 8px 0 0;
  color:var(--npp-text-muted, #94a3b8);
  transition:background 0.2s, color 0.2s; white-space:nowrap; }
.npp-tab-button:hover { background:rgba(255,255,255,0.06); color:var(--npp-text,#fff); }
.npp-tab-button.active {
  background:var(--npp-primary, #6366f1); color:#fff;
  box-shadow:0 4px 18px rgba(99,102,241,0.35); }
.npp-tab-panel {
  display:none; padding:28px; background:var(--npp-surface, #1e293b);
  border-radius:0 0 12px 12px; border:1px solid var(--npp-border, #334155);
  border-top:none; animation:nppFadeIn 0.25s ease; }
.npp-tab-panel.active { display:block; }

/* --- Accordion --- */
.npp-accordion { border:1px solid var(--npp-border,#334155);
  border-radius:12px; overflow:hidden; }
.npp-accordion-item { border-bottom:1px solid var(--npp-border,#334155); }
.npp-accordion-item:last-child { border-bottom:none; }
.npp-accordion-header {
  width:100%; background:var(--npp-surface,#1e293b); border:none;
  padding:18px 24px; text-align:left; cursor:pointer; display:flex;
  justify-content:space-between; align-items:center;
  font-size:1rem; font-weight:600; color:var(--npp-text,#fff);
  transition:background 0.2s; }
.npp-accordion-header:hover { background:rgba(255,255,255,0.05); }
.npp-accordion-arrow { transition:transform 0.3s; font-size:0.85rem; }
.npp-accordion-header.open .npp-accordion-arrow { transform:rotate(180deg); }
.npp-accordion-body {
  max-height:0; overflow:hidden;
  transition:max-height 0.4s cubic-bezier(0.16,1,0.3,1), padding 0.3s; }
.npp-accordion-body.open { max-height:600px; }
.npp-accordion-content {
  padding:18px 24px; color:var(--npp-text-muted,#94a3b8); line-height:1.7; }

/* --- Tooltip --- */
[data-npp-tip] { position:relative; cursor:help; }
[data-npp-tip]::after {
  content:attr(data-npp-tip); position:absolute; bottom:calc(100% + 8px);
  left:50%; transform:translateX(-50%) scale(0.9); white-space:nowrap;
  background:#1e293b; color:#fff; padding:6px 12px; border-radius:8px;
  font-size:0.82rem; font-weight:500; pointer-events:none; opacity:0;
  transition:opacity 0.2s, transform 0.2s; z-index:5000;
  box-shadow:0 6px 20px rgba(0,0,0,0.4);
  border:1px solid rgba(255,255,255,0.1); }
[data-npp-tip]:hover::after { opacity:1; transform:translateX(-50%) scale(1); }

/* --- Ripple Button --- */
.npp-button { position:relative; overflow:hidden; }
.npp-ripple {
  position:absolute; border-radius:50%; background:rgba(255,255,255,0.25);
  transform:scale(0); animation:nppRipple 0.6s linear; pointer-events:none; }

/* --- Progress Bar animated --- */
.npp-progress {
  width:100%; height:10px; background:var(--npp-surface,#1e293b);
  border-radius:999px; overflow:hidden; margin:8px 0; }
.npp-progress-bar {
  height:100%; background:linear-gradient(90deg,var(--npp-primary,#6366f1),#a855f7);
  border-radius:999px; transition:width 0.8s cubic-bezier(0.16,1,0.3,1);
  width:0%; background-size:200% 100%; animation:nppShimmer 2s infinite; }

/* --- Scroll to top button --- */
#npp-scroll-top {
  position:fixed; bottom:24px; left:24px; width:44px; height:44px;
  background:var(--npp-primary,#6366f1); color:#fff; border:none;
  border-radius:12px; cursor:pointer; font-size:1.2rem; z-index:8000;
  box-shadow:0 6px 24px rgba(99,102,241,0.4);
  transition:opacity 0.3s, transform 0.3s;
  opacity:0; transform:translateY(20px); display:flex;
  align-items:center; justify-content:center; }
#npp-scroll-top.visible { opacity:1; transform:translateY(0); }
#npp-scroll-top:hover { transform:scale(1.1) translateY(0); }

/* --- Typewriter --- */
.npp-typewriter::after {
  content:'|'; animation:nppBlink 0.75s step-end infinite;
  color:var(--npp-primary,#6366f1); }

/* --- Lazy image fade-in --- */
.npp-lazy { opacity:0; transition:opacity 0.6s ease; }
.npp-lazy.loaded { opacity:1; }

/* --- Counter display --- */
.npp-counter-display {
  font-size:2.5rem; font-weight:800; color:var(--npp-primary,#6366f1);
  display:inline-block; min-width:60px; text-align:center; }

/* --- Keyframes --- */
@keyframes nppFadeIn { from { opacity:0; transform:translateY(10px); }
  to { opacity:1; transform:translateY(0); } }
@keyframes nppRipple { to { transform:scale(4); opacity:0; } }
@keyframes nppShimmer {
  0% { background-position:200% center; }
  100% { background-position:-200% center; } }
@keyframes nppBlink { 50% { opacity:0; } }
@keyframes nppSlideIn {
  from { opacity:0; transform:translateX(-20px); }
  to { opacity:1; transform:translateX(0); } }
@keyframes nppPop {
  0% { transform:scale(1); }
  50% { transform:scale(1.12); }
  100% { transform:scale(1); } }
"""

# ── JavaScript injected at bottom of every N++ webpage ────────────────────────
INTERACTIVE_RUNTIME_JS = """
// ╔══════════════════════════════════════════════════════╗
// ║        N++ Interactive Web Runtime  v2.0             ║
// ║  Zero dependencies. Pure JS. Fully interactive.      ║
// ╚══════════════════════════════════════════════════════╝
(function() {
  'use strict';

  // ── 1. Toast Notification System ─────────────────────────────────────────
  function showToast(message, type) {
    type = type || 'success';
    var icons = { success:'✅', error:'❌', info:'💡', warning:'⚠️' };
    var colors = { success:'#10b981', error:'#ef4444', info:'#6366f1', warning:'#f59e0b' };
    var bg = colors[type] || colors.info;
    var icon = icons[type] || icons.info;

    var container = document.getElementById('npp-toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'npp-toast-container';
      document.body.appendChild(container);
    }
    var toast = document.createElement('div');
    toast.className = 'npp-toast';
    toast.style.cssText = 'background:' + bg + ';color:#fff;';
    toast.innerHTML = '<span class="npp-toast-icon">' + icon + '</span><span>' + message + '</span>';
    container.appendChild(toast);
    requestAnimationFrame(function() { toast.classList.add('npp-toast-show'); });
    setTimeout(function() {
      toast.classList.remove('npp-toast-show');
      setTimeout(function() { toast.remove(); }, 400);
    }, 4000);
  }
  window.nppToast = showToast;

  // ── 2. Interactive Form Handler ───────────────────────────────────────────
  document.addEventListener('submit', function(e) {
    var form = e.target;
    var action = form.getAttribute('action') || '#';
    if (action === '#' || action === '' || action.indexOf('javascript:') === 0) {
      e.preventDefault();
      var submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
      var originalText = submitBtn ? submitBtn.innerText : '';
      if (submitBtn) { submitBtn.disabled = true; submitBtn.innerText = 'Sending…'; }
      setTimeout(function() {
        showToast('Form submitted! Thank you 🎉', 'success');
        if (submitBtn) { submitBtn.disabled = false; submitBtn.innerText = originalText; }
        form.reset();
      }, 800);
    }
  });

  // ── 3. Theme Switcher ────────────────────────────────────────────────────
  var THEMES = {
    'dark':           { '--npp-bg':'#090d16','--npp-surface':'#111827','--npp-surface-card':'#172033','--npp-text':'#f8fafc','--npp-text-muted':'#94a3b8','--npp-primary':'#6366f1','--npp-border':'#1e293b' },
    'modern':         { '--npp-bg':'#f8fafc','--npp-surface':'#ffffff','--npp-surface-card':'#ffffff','--npp-text':'#0f172a','--npp-text-muted':'#64748b','--npp-primary':'#4f46e5','--npp-border':'#e2e8f0' },
    'glassmorphism':  { '--npp-bg':'linear-gradient(135deg,#0f172a,#1e1b4b,#311042)','--npp-surface':'rgba(255,255,255,0.07)','--npp-surface-card':'rgba(255,255,255,0.08)','--npp-text':'#ffffff','--npp-text-muted':'#cbd5e1','--npp-primary':'#a855f7','--npp-border':'rgba(255,255,255,0.15)' },
    'cyberpunk':      { '--npp-bg':'#050508','--npp-surface':'#0d0e15','--npp-surface-card':'#121420','--npp-text':'#00ffcc','--npp-text-muted':'#8892b0','--npp-primary':'#ff0055','--npp-border':'#25283d' }
  };
  function applyTheme(name) {
    var palette = THEMES[name]; if (!palette) return;
    var root = document.documentElement;
    for (var k in palette) { if (palette.hasOwnProperty(k)) root.style.setProperty(k, palette[k]); }
    if (palette['--npp-bg'] && palette['--npp-bg'].indexOf('gradient') > -1)
      document.body.style.backgroundImage = palette['--npp-bg'];
    else
      document.body.style.backgroundColor = palette['--npp-bg'];
    localStorage.setItem('npp_theme', name);
    showToast('Theme: ' + name + ' ✨', 'info');
    // Update switcher dropdown
    var sel = document.getElementById('npp-theme-sel');
    if (sel) sel.value = name;
  }
  window.nppSetTheme = applyTheme;
  // Restore saved theme
  var savedTheme = localStorage.getItem('npp_theme');
  if (savedTheme && THEMES[savedTheme]) applyTheme(savedTheme);

  // ── 4. Tab Switcher ──────────────────────────────────────────────────────
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('.npp-tab-button');
    if (!btn) return;
    var container = btn.closest('.npp-tabs-container');
    if (!container) return;
    var targetId = btn.getAttribute('data-target');
    container.querySelectorAll('.npp-tab-button').forEach(function(b) { b.classList.remove('active'); });
    container.querySelectorAll('.npp-tab-panel').forEach(function(p) { p.classList.remove('active'); });
    btn.classList.add('active');
    var panel = document.getElementById(targetId);
    if (panel) panel.classList.add('active');
  });
  // Auto-activate first tab in every tabs container
  document.querySelectorAll('.npp-tabs-container').forEach(function(tc) {
    var firstBtn = tc.querySelector('.npp-tab-button');
    if (firstBtn && !tc.querySelector('.npp-tab-button.active')) firstBtn.click();
  });

  // ── 5. Modal System ──────────────────────────────────────────────────────
  document.addEventListener('click', function(e) {
    // Open
    var trigger = e.target.closest('[data-npp-modal]');
    if (trigger) {
      var id = trigger.getAttribute('data-npp-modal');
      var modal = document.getElementById(id);
      if (modal) { modal.style.display = 'flex'; requestAnimationFrame(function() { modal.classList.add('open'); }); }
    }
    // Close via button
    var closeBtn = e.target.closest('.npp-modal-close, [data-npp-modal-close]');
    if (closeBtn) {
      var m = closeBtn.closest('.npp-modal');
      if (m) { m.classList.remove('open'); setTimeout(function() { m.style.display = 'none'; }, 260); }
    }
    // Close by clicking backdrop
    if (e.target.classList.contains('npp-modal')) {
      e.target.classList.remove('open');
      setTimeout(function() { e.target.style.display = 'none'; }, 260);
    }
  });
  // Close modal on Escape
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.npp-modal.open').forEach(function(m) {
        m.classList.remove('open'); setTimeout(function() { m.style.display='none'; }, 260);
      });
    }
  });

  // ── 6. Accordion ─────────────────────────────────────────────────────────
  document.addEventListener('click', function(e) {
    var hdr = e.target.closest('.npp-accordion-header');
    if (!hdr) return;
    var item = hdr.closest('.npp-accordion-item');
    var body = item ? item.querySelector('.npp-accordion-body') : null;
    if (!body) return;
    var isOpen = hdr.classList.contains('open');
    // Close all in same accordion
    var acc = hdr.closest('.npp-accordion');
    if (acc) {
      acc.querySelectorAll('.npp-accordion-header.open').forEach(function(h) {
        h.classList.remove('open');
        var b = h.closest('.npp-accordion-item').querySelector('.npp-accordion-body');
        if (b) b.classList.remove('open');
      });
    }
    if (!isOpen) { hdr.classList.add('open'); body.classList.add('open'); }
  });

  // ── 7. Counter Buttons ───────────────────────────────────────────────────
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('[data-npp-counter]');
    if (!btn) return;
    var targetId = btn.getAttribute('data-npp-counter');
    var step = parseInt(btn.getAttribute('data-npp-step') || '1', 10);
    var display = document.getElementById(targetId);
    if (display) {
      var val = parseInt(display.innerText || '0', 10); val += step;
      display.innerText = val;
      display.style.animation = 'none';
      requestAnimationFrame(function() { display.style.animation = 'nppPop 0.3s ease'; });
    }
    btn.style.transform = 'scale(0.93)';
    setTimeout(function() { btn.style.transform = ''; }, 120);
  });

  // ── 8. Live Search Filter ────────────────────────────────────────────────
  document.addEventListener('input', function(e) {
    var inp = e.target.closest('[data-npp-filter]');
    if (!inp) return;
    var selector = inp.getAttribute('data-npp-filter');
    var query = inp.value.toLowerCase().trim();
    document.querySelectorAll(selector).forEach(function(el) {
      el.style.display = el.innerText.toLowerCase().includes(query) ? '' : 'none';
    });
  });

  // ── 9. Ripple Effect on Buttons ──────────────────────────────────────────
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('.npp-button');
    if (!btn) return;
    var ripple = document.createElement('span');
    ripple.className = 'npp-ripple';
    var rect = btn.getBoundingClientRect();
    var size = Math.max(rect.width, rect.height);
    ripple.style.cssText = 'width:'+size+'px;height:'+size+'px;left:'+(e.clientX-rect.left-size/2)+'px;top:'+(e.clientY-rect.top-size/2)+'px;';
    btn.appendChild(ripple);
    setTimeout(function() { ripple.remove(); }, 700);
  });

  // ── 10. Animated Progress Bars ───────────────────────────────────────────
  function animateProgressBars() {
    document.querySelectorAll('.npp-progress-bar[data-value]').forEach(function(bar) {
      var val = bar.getAttribute('data-value');
      setTimeout(function() { bar.style.width = val + '%'; }, 200);
    });
  }

  // ── 11. Scroll-to-Top Button ─────────────────────────────────────────────
  var scrollTopBtn = document.createElement('button');
  scrollTopBtn.id = 'npp-scroll-top';
  scrollTopBtn.innerHTML = '↑';
  scrollTopBtn.title = 'Back to top';
  scrollTopBtn.addEventListener('click', function() {
    window.scrollTo({ top:0, behavior:'smooth' });
  });
  document.body.appendChild(scrollTopBtn);
  window.addEventListener('scroll', function() {
    if (window.scrollY > 300) scrollTopBtn.classList.add('visible');
    else scrollTopBtn.classList.remove('visible');
  }, { passive:true });

  // ── 12. Lazy Image Loading ────────────────────────────────────────────────
  if ('IntersectionObserver' in window) {
    var lazyObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var img = entry.target;
          if (img.dataset.src) { img.src = img.dataset.src; delete img.dataset.src; }
          img.classList.add('loaded');
          lazyObs.unobserve(img);
        }
      });
    }, { threshold:0.1 });
    document.querySelectorAll('img.npp-lazy').forEach(function(img) { lazyObs.observe(img); });
  }

  // ── 13. Typewriter Effect ────────────────────────────────────────────────
  function typeWriter(el, text, speed) {
    speed = speed || 60;
    var i = 0;
    el.textContent = '';
    el.classList.add('npp-typewriter');
    var t = setInterval(function() {
      el.textContent += text[i++];
      if (i >= text.length) { clearInterval(t); el.classList.remove('npp-typewriter'); }
    }, speed);
  }
  window.nppTypeWriter = typeWriter;
  document.querySelectorAll('[data-npp-type]').forEach(function(el) {
    var delay = parseInt(el.getAttribute('data-npp-delay') || '500', 10);
    setTimeout(function() { typeWriter(el, el.getAttribute('data-npp-type')); }, delay);
  });

  // ── 14. Scroll Reveal Animations ────────────────────────────────────────
  if ('IntersectionObserver' in window) {
    var revealObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.style.animation = 'nppSlideIn 0.5s ease forwards';
          revealObs.unobserve(entry.target);
        }
      });
    }, { threshold:0.12 });
    document.querySelectorAll('[data-npp-reveal]').forEach(function(el) {
      el.style.opacity = '0';
      revealObs.observe(el);
    });
  }

  // ── 15. Inject Theme Switcher Dropdown into Navbar ──────────────────────
  document.addEventListener('DOMContentLoaded', function() {
    var nav = document.querySelector('.npp-navbar');
    if (nav && !document.getElementById('npp-theme-switcher')) {
      var sw = document.createElement('div');
      sw.id = 'npp-theme-switcher';
      sw.style.cssText = 'display:flex;align-items:center;gap:8px;margin-left:auto;padding-right:8px;';
      sw.innerHTML = '<select id="npp-theme-sel" onchange="window.nppSetTheme(this.value)" '
        + 'style="background:var(--npp-surface);color:var(--npp-text);border:1px solid var(--npp-border);'
        + 'padding:6px 12px;border-radius:8px;font-size:0.85rem;cursor:pointer;">'
        + '<option value="dark">🌙 Dark</option>'
        + '<option value="modern">☀️ Modern</option>'
        + '<option value="glassmorphism">🔮 Glass</option>'
        + '<option value="cyberpunk">⚡ Cyber</option>'
        + '</select>';
      nav.appendChild(sw);
      var cur = localStorage.getItem('npp_theme') || 'dark';
      var sel = document.getElementById('npp-theme-sel');
      if (sel) sel.value = cur;
    }
    // Animate progress bars on load
    animateProgressBars();
  });

  // ── 16. Copy-to-Clipboard Buttons ────────────────────────────────────────
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('[data-npp-copy]');
    if (!btn) return;
    var targetId = btn.getAttribute('data-npp-copy');
    var el = targetId ? document.getElementById(targetId) : btn.previousElementSibling;
    var text = el ? (el.value || el.innerText || el.textContent) : '';
    if (!text) return;
    navigator.clipboard.writeText(text.trim()).then(function() {
      showToast('Copied to clipboard! 📋', 'success');
      var orig = btn.innerText;
      btn.innerText = '✓ Copied';
      setTimeout(function() { btn.innerText = orig; }, 2000);
    });
  });

  // ── 17. Smooth Number Counting Animation ────────────────────────────────
  function animateCount(el, target, duration) {
    duration = duration || 1800;
    var start = 0; var startTime = null;
    function step(ts) {
      if (!startTime) startTime = ts;
      var p = Math.min((ts - startTime) / duration, 1);
      var ease = 1 - Math.pow(1 - p, 4);
      el.innerText = Math.floor(ease * target).toLocaleString();
      if (p < 1) requestAnimationFrame(step);
      else el.innerText = target.toLocaleString();
    }
    requestAnimationFrame(step);
  }
  window.nppAnimateCount = animateCount;
  if ('IntersectionObserver' in window) {
    var countObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          var target = parseInt(el.getAttribute('data-npp-count') || '0', 10);
          animateCount(el, target);
          countObs.unobserve(el);
        }
      });
    }, { threshold:0.3 });
    document.querySelectorAll('[data-npp-count]').forEach(function(el) { countObs.observe(el); });
  }

  // ── Done ──────────────────────────────────────────────────────────────────
  console.log('%c N++ Web Runtime v2.0 loaded ⚡ ', 'background:#6366f1;color:#fff;padding:4px 10px;border-radius:4px;font-weight:bold;');

})();
"""
