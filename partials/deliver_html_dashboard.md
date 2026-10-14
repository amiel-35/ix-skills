# Reference: HTML dashboard in presentation mode (v2)

## Purpose of this reference

Applies when the `deliver` skill runs with `target_format: html` AND the brief contains keywords such as: dashboard, metrics, KPIs, charts, analytics, monitoring, tracking, indicators, projected, presentation.

Produces an **HTML dashboard in presentation mode** — slides that advance by keyboard or automatically, full screen, projectable in a meeting. Not a scrolling page.

For other HTML deliverables (editorial document, narrative slides, landing page, one-pager), use `deliver_html.md`.

---

## Guiding principle

A dashboard projected in a meeting is a succession of views, not a page. Each slide = a self-contained view, legible from a distance. Keyboard navigation, native fullscreen, optional auto-advance.

If a `Delivery branding` context is injected:

- it takes precedence over the visual suggestions in this reference
- palette, typography, logos, footer and iconography must come from the `brand_pack`
- HTML icons, if used, must respect `brand_pack.iconography`
- never use emoji

**Typical structure of a dashboard in 4-6 slides:**
```
Slide 1: Title + context + key figures (summary)
Slide 2: KPI cards — the main indicators
Slide 3: Trend charts (line/bar)
Slide 4: Detail / table / breakdown
Slide 5: Alerts and points of vigilance
Slide 6: Next steps / governance
```
Adapt to the source content — remove slides with no material.

---

## Step 1 — Analyze the source content

Before coding, identify:
1. **The title and context** (slide 1)
2. **The key KPIs** (3-6 max) → KPI cards slide
3. **Time-series data** → line chart
4. **Categorical comparisons** → bar chart
5. **Compositions/shares** → doughnut
6. **Identified alerts / problems** → dedicated slide
7. **Governance / next steps** → final slide

---

## Step 2 — Visual direction

Consistent palette for a projected dashboard (dark background recommended — better contrast in a room):

If a `brand_pack` is injected, use its tokens first and use the examples below only in the absence of explicit branding.

- **Dark pro**: background `#0f172a`, surface `#1e293b`, accent `#0ea5e9` — SaaS/tech
- **Navy corporate**: background `#0f2d52`, surface `#1a3a5c`, accent `#f97316` — leadership/finance
- **Charcoal**: background `#1a1a2e`, surface `#2d2d44`, accent `#4C72B0` — versatile
- **Dark green**: background `#0d1f0f`, surface `#1a3320`, accent `#22c55e` — growth/health

A light background is possible for a printed context or a shared document — adapt to the brief.

Recommended Google Fonts for projection:
- `DM Sans` + `DM Mono` — legible from a distance, modern
- `IBM Plex Sans` + `IBM Plex Mono` — precise corporate
- `Syne` + `Epilogue` — startup

If `brand_pack.typography` is provided, it replaces these suggestions.

---

## HTML architecture — slide system

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Dashboard title]</title>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
  <style>/* see CSS section */</style>
</head>
<body>

  <!-- Slides container -->
  <div class="deck">

    <!-- Slide 1: Title -->
    <div class="slide active" id="slide-1">
      <div class="slide-inner">
        <!-- content -->
      </div>
    </div>

    <!-- Slide 2: KPIs -->
    <div class="slide" id="slide-2">
      <div class="slide-inner">
        <!-- metric cards -->
      </div>
    </div>

    <!-- ... other slides ... -->

  </div>

  <!-- Navigation -->
  <div class="nav">
    <button class="nav-btn" id="btn-prev" onclick="prevSlide()">←</button>
    <div class="progress-dots" id="dots"></div>
    <button class="nav-btn" id="btn-next" onclick="nextSlide()">→</button>
  </div>

  <!-- Toolbar -->
  <div class="toolbar">
    <span class="slide-counter" id="counter">1 / N</span>
    <button class="toolbar-btn" onclick="toggleFullscreen()" title="Fullscreen">⛶</button>
    <button class="toolbar-btn" id="btn-auto" onclick="toggleAuto()" title="Auto-advance">▶</button>
  </div>

  <script>/* see JS section */</script>
</body>
</html>
```

---

## CSS — fullscreen slides

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:      #0f172a;   /* adapt to the visual direction */
  --surface: #1e293b;
  --accent:  #0ea5e9;
  --text:    #f1f5f9;
  --muted:   #94a3b8;
  --border:  rgba(255,255,255,0.08);
  --positive: #22c55e;
  --warning:  #f59e0b;
  --negative: #ef4444;
  --gap: 1.5rem;
  --radius: 12px;
}

html, body {
  width: 100%; height: 100%;
  font-family: 'DM Sans', system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  overflow: hidden;
}

/* Deck */
.deck {
  width: 100vw; height: 100vh;
  position: relative;
}

/* Slides */
.slide {
  position: absolute;
  inset: 0;
  padding: 3rem 4rem 5rem;
  display: flex;
  flex-direction: column;
  opacity: 0;
  pointer-events: none;
  transition: opacity .3s ease;
}
.slide.active {
  opacity: 1;
  pointer-events: all;
}
.slide-inner {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Eyebrow label */
.eyebrow {
  font-size: .7rem;
  font-weight: 500;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: .75rem;
}

/* Headings */
.slide h1 { font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 700; line-height: 1.1; margin-bottom: 1rem; }
.slide h2 { font-size: clamp(1.4rem, 2.5vw, 2rem); font-weight: 600; margin-bottom: 1.5rem; }
.slide h3 { font-size: .8rem; font-weight: 500; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); margin-bottom: 1rem; }

/* Title slide subtitle */
.subtitle { font-size: clamp(.9rem, 1.5vw, 1.1rem); color: var(--muted); max-width: 600px; line-height: 1.6; }

/* Inline stats on the title slide */
.stat-row { display: flex; gap: 3rem; margin-top: 2.5rem; flex-wrap: wrap; }
.stat-item .stat-value { font-size: clamp(1.5rem, 3vw, 2.5rem); font-weight: 700; color: var(--accent); }
.stat-item .stat-label { font-size: .75rem; color: var(--muted); text-transform: uppercase; letter-spacing: .06em; margin-top: .25rem; }

/* KPI cards grid */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--gap);
  width: 100%;
}
.kpi-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
}
.kpi-label { font-size: .7rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); margin-bottom: .5rem; }
.kpi-value { font-size: clamp(1.8rem, 3vw, 2.5rem); font-weight: 700; line-height: 1; margin-bottom: .4rem; }
.kpi-sub { font-size: .75rem; color: var(--muted); margin-bottom: .5rem; }
.kpi-delta { font-size: .8rem; font-weight: 600; }
.kpi-delta.ok   { color: var(--positive); }
.kpi-delta.warn { color: var(--warning); }
.kpi-delta.bad  { color: var(--negative); }

/* Badge */
.badge { display: inline-block; padding: 3px 10px; border-radius: 999px; font-size: .7rem; font-weight: 600; }
.badge.ok   { background: rgba(34,197,94,.15);  color: var(--positive); }
.badge.warn { background: rgba(245,158,11,.15); color: var(--warning); }
.badge.bad  { background: rgba(239,68,68,.15);  color: var(--negative); }

/* Charts grid */
.chart-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: var(--gap);
  width: 100%;
  flex: 1;
}
.chart-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem 1.5rem;
  display: flex;
  flex-direction: column;
}
.chart-wrap { position: relative; flex: 1; min-height: 180px; }

/* Table */
.table-wrap { width: 100%; overflow-x: auto; }
table { width: 100%; border-collapse: collapse; font-size: .85rem; }
thead th {
  text-align: left; padding: 8px 12px;
  border-bottom: 1px solid var(--border);
  color: var(--muted); font-size: .7rem;
  text-transform: uppercase; letter-spacing: .06em;
  white-space: nowrap;
}
tbody td { padding: 10px 12px; border-bottom: 1px solid var(--border); }
tbody tr:last-child td { border-bottom: none; }
tbody tr:hover { background: rgba(255,255,255,0.03); }

/* Alerts */
.alert-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: var(--gap); }
.alert-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 3px solid var(--warning);
  border-radius: var(--radius);
  padding: 1.25rem 1.5rem;
}
.alert-card.critical { border-left-color: var(--negative); }
.alert-title { font-size: .8rem; font-weight: 600; color: var(--warning); margin-bottom: .5rem; text-transform: uppercase; letter-spacing: .05em; }
.alert-card.critical .alert-title { color: var(--negative); }
.alert-text { font-size: .85rem; color: var(--muted); line-height: 1.6; }
.alert-action { font-size: .8rem; color: var(--text); margin-top: .75rem; }
.alert-action::before { content: '→ '; color: var(--accent); }

/* Navigation */
.nav {
  position: fixed; bottom: 1.5rem; left: 50%;
  transform: translateX(-50%);
  display: flex; align-items: center; gap: 1rem;
  background: rgba(255,255,255,0.06);
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: .5rem 1rem;
  backdrop-filter: blur(8px);
  z-index: 100;
}
.nav-btn {
  background: none; border: none; color: var(--text);
  font-size: 1rem; cursor: pointer; padding: .25rem .5rem;
  border-radius: 4px; transition: background .15s;
}
.nav-btn:hover { background: rgba(255,255,255,0.1); }
.nav-btn:disabled { opacity: .3; cursor: default; }
.progress-dots { display: flex; gap: 6px; align-items: center; }
.dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--muted); transition: all .2s;
  cursor: pointer;
}
.dot.active { background: var(--accent); width: 20px; border-radius: 3px; }

/* Toolbar */
.toolbar {
  position: fixed; top: 1rem; right: 1.5rem;
  display: flex; align-items: center; gap: .75rem;
  z-index: 100;
}
.slide-counter { font-size: .75rem; color: var(--muted); font-family: 'DM Mono', monospace; }
.toolbar-btn {
  background: rgba(255,255,255,0.06);
  border: 1px solid var(--border);
  color: var(--text); font-size: .85rem;
  padding: .35rem .6rem; border-radius: 6px;
  cursor: pointer; transition: background .15s;
}
.toolbar-btn:hover { background: rgba(255,255,255,0.12); }
.toolbar-btn.active { background: rgba(14,165,233,.2); border-color: var(--accent); color: var(--accent); }
```

---

## JS — navigation and controls

```javascript
// ── State ──────────────────────────────────────────────
const slides = document.querySelectorAll('.slide');
const total  = slides.length;
let current  = 0;
let autoTimer = null;
const AUTO_DELAY = 8000; // ms between slides in auto mode

// ── Navigation ─────────────────────────────────────────
function goTo(n) {
  slides[current].classList.remove('active');
  current = Math.max(0, Math.min(n, total - 1));
  slides[current].classList.add('active');
  updateUI();
  // Initialize the slide's charts if needed
  if (chartInits[current]) { chartInits[current](); chartInits[current] = null; }
}

function nextSlide() { if (current < total - 1) goTo(current + 1); }
function prevSlide() { if (current > 0) goTo(current - 1); }

// ── UI ─────────────────────────────────────────────────
function updateUI() {
  document.getElementById('counter').textContent = `${current + 1} / ${total}`;
  document.getElementById('btn-prev').disabled = current === 0;
  document.getElementById('btn-next').disabled = current === total - 1;

  // Dots
  const dotsEl = document.getElementById('dots');
  dotsEl.innerHTML = '';
  for (let i = 0; i < total; i++) {
    const d = document.createElement('div');
    d.className = 'dot' + (i === current ? ' active' : '');
    d.onclick = () => goTo(i);
    dotsEl.appendChild(d);
  }
}

// ── Keyboard ───────────────────────────────────────────
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') { e.preventDefault(); nextSlide(); }
  if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')  { e.preventDefault(); prevSlide(); }
  if (e.key === 'f' || e.key === 'F') toggleFullscreen();
  if (e.key === 'Escape' && autoTimer) toggleAuto();
});

// ── Fullscreen ─────────────────────────────────────────
function toggleFullscreen() {
  if (!document.fullscreenElement) document.documentElement.requestFullscreen();
  else document.exitFullscreen();
}

// ── Auto-advance ───────────────────────────────────────
function toggleAuto() {
  const btn = document.getElementById('btn-auto');
  if (autoTimer) {
    clearInterval(autoTimer);
    autoTimer = null;
    btn.classList.remove('active');
    btn.textContent = '▶';
  } else {
    autoTimer = setInterval(() => {
      if (current < total - 1) nextSlide();
      else { toggleAuto(); goTo(0); }
    }, AUTO_DELAY);
    btn.classList.add('active');
    btn.textContent = '⏸';
  }
}

// ── Lazy init charts ───────────────────────────────────
// Avoids initializing every Chart.js chart on load
// (invisible canvas = zero dimensions = broken chart)
const chartInits = {}; // { slideIndex: initFn }

// Example: chart on slide 2 (index 1)
chartInits[1] = function() {
  const ctx = document.getElementById('chart-trend').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: [/* extract from the source */],
      datasets: [{
        data: [/* extract from the source */],
        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--accent').trim(),
        backgroundColor: 'rgba(14,165,233,0.08)',
        fill: true, tension: 0.3, pointRadius: 3, borderWidth: 2
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: { color: '#94a3b8', font: { size: 11 } } },
        y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8', font: { size: 11 } } }
      }
    }
  });
};

// ── Init ───────────────────────────────────────────────
updateUI();
// Initialize the initial slide's chart if needed
if (chartInits[0]) { chartInits[0](); chartInits[0] = null; }
```

---

## Lazy init charts — why it is critical

Chart.js computes the canvas dimensions at init time. If the canvas is on a hidden slide (`opacity: 0`), its dimensions are 0 and the chart renders badly or not at all.

**Rule**: always register chart inits in `chartInits[slideIndex]` and trigger them in `goTo()` the first time the slide is shown.

---

## Value formatter

```javascript
function fmt(v, type = 'number') {
  if (v == null) return '—';
  if (type === 'currency') {
    if (v >= 1e6) return '$' + (v/1e6).toFixed(1) + 'M';
    if (v >= 1e3) return '$' + (v/1e3).toFixed(1) + 'K';
    return '$' + Math.round(v);
  }
  if (type === 'percent') return v.toFixed(1) + ' %';
  if (v >= 1e6) return (v/1e6).toFixed(1) + 'M';
  if (v >= 1e3) return (v/1e3).toFixed(1) + 'K';
  return v.toLocaleString('fr-FR');
}
```

---

## Cross-cutting rules

- **No scroll** — all of a slide's content must fit within `100vh`. Reduce the font size or split into two slides if it overflows.
- **Legible from a distance** — minimum font size `0.75rem` for labels, `1.8rem` for KPI values
- **Charts on hidden slides** → lazy init mandatory
- **Standalone file** — everything embedded, no local dependency
- **Rounded data** — every number goes through `fmt()`
- **Dark background by default** — better contrast in projection. Light background if the brief mentions "printed" or "shared by link"
- **Strict brand pack** — if injected, all visual variables must derive from it
- **Iconography** — HTML only, library/style from the `brand_pack`, no emoji

---

## Keyboard shortcuts to document on the title slide

```
→ / Space    Next slide
←            Previous slide
F            Fullscreen
▶ (toolbar)  Auto-advance (8s/slide)
```

---

## Final instruction for the LLM

1. **Read the source in full** — identify the relevant slides (remove those with no material)
2. **Choose a visual direction** — palette + font, dark background by default
3. **Structure the slides** — 4 to 6 max, each self-contained and legible from a distance
4. **Register the charts in `chartInits`** — never initialize directly on a hidden canvas
5. **Check**: does each slide fit within `100vh`? Do the charts initialize at the right time? Does keyboard navigation work?
6. **Output**: raw HTML only — no markdown, no ```html, no explanation

---

## Loop mode — infinite auto-advance on load

If the brief contains the keywords loop/tv/kiosk/automatic, replace the end of the JS with:

```javascript
// Loop mode — start auto-advance on load
const LOOP_DELAY = 20000; // 20s by default — adapt to the brief (10000 / 20000 / 30000)

function startLoop() {
  autoTimer = setInterval(() => {
    if (current < total - 1) nextSlide();
    else goTo(0); // back to the start — infinite loop
  }, LOOP_DELAY);
  const btn = document.getElementById('btn-auto');
  btn.classList.add('active');
  btn.textContent = '⏸';
}

// Start automatically
updateUI();
if (chartInits[0]) { chartInits[0](); chartInits[0] = null; }
startLoop(); // ← enable only if loop mode is detected in the brief
```

**Difference from toggleAuto**: in loop mode, instead of stopping at the last slide, the dashboard automatically restarts at slide 1 — infinite loop for TV/kiosk display.
