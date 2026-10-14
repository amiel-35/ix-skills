# Reference: HTML deliverable (v2)

## Purpose of this reference

Applies when the `deliver` skill runs with `target_format: html`.
Produces a standalone, presentation-quality HTML deliverable — not markdown converted into tags.
This reference embeds the rules of the `frontend-design` skill, adapted to the deliverable context.

---

## Guiding principle

An HTML deliverable is a document designed to be **read in a browser, shared by link, presented in a meeting**.
It must be visually memorable, well structured, and immediately readable by someone who has not seen the source.

**This is not markdown with `<h2>` tags. It is a designed document.**

If a `Delivery branding` context is injected:

- it takes priority over any visual suggestion in this reference
- palette, typography, logo, footer, spacing and iconography must come from the `brand_pack`
- do not invent a contradictory visual direction
- use named CSS variables derived from the `brand_pack`, not hardcoded colors
- if icons are useful and the format is HTML, use only the library and style declared in `brand_pack.iconography`
- never use an emoji as a substitute for an icon

---

## Step 1 — Choose a visual direction

Before writing a single line of HTML:

- if a `brand_pack` is provided, follow it strictly
- otherwise only, decide on a local visual direction

When there is no `brand_pack`, decide:

- **Tone**: sober/corporate, editorial/magazine, data-dense/dashboard, minimal/clean
- **Palette**: one dominant color + one accent color + neutrals. Never a purple gradient on a white background.
- **Typography**: choose a distinctive Google font pairing if the branding imposes nothing. Examples that work well:
  - `DM Sans` + `DM Mono` → data/tech
  - `Fraunces` + `Inter` → premium editorial
  - `Syne` + `Epilogue` → modern/startup
  - `IBM Plex Sans` + `IBM Plex Mono` → corporate/precise
  - Avoid: Inter alone, Roboto, Arial, Space Grotesk

The direction must be **consistent from start to finish**. No mixing of styles.

---

## Step 2 — Detect the content type

| Source content | Template |
|---|---|
| KPIs, metrics, figures, dashboard | **Dashboard** |
| Analysis, report, strategic note, requirements document (CDC) | **Editorial document** |
| Option comparison, decision, offer comparison | **Decision sheet** |
| Personas, journey map | **Structured sheets** |
| Brief, short summary, one-pager | **One-pager** |

---

## Step 3 — Stack and technical constraints

**Allowed:**
- HTML5 + CSS embedded in `<style>`
- Chart.js: `https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js`
- Google Fonts: `https://fonts.googleapis.com/css2?family=...`
- Vanilla JS only — no React, Vue, or any framework

**Forbidden:**
- Local dependencies
- `position: fixed` (breaks rendering in some contexts) — except in the looping dashboard of `deliver_html_dashboard.md`, which defines its own fixed navigation
- Hardcoded text colors without a CSS variable
- Black or very dark background on `<body>`

**Mandatory:**
- **100% standalone** file — a single `.html`, everything embedded
- `<meta charset="UTF-8">` + `<meta name="viewport">`
- `<title>` consistent with the content
- Responsive: `minmax()` for grids, no fixed px widths on containers
- Every displayed number goes through `toFixed()` or `Math.round()`

---

## Template A — Dashboard

For KPIs, metrics, dashboards. This is the most visually rich template.

### Required structure

```
[Header] title + subtitle + period
[Metric cards] 3-5 key figures at the top — always visible first
[Charts] trend visualization — Chart.js mandatory if there is time-series data
[Detail table] all KPIs with target + status (traffic light badge)
[Alerts] problematic or off-target KPIs — amber background, at the bottom
```

### Chart.js rules

```html
<!-- Always wrap with an explicit height -->
<div style="position: relative; width: 100%; height: 260px;">
  <canvas id="chart1"></canvas>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script>
new Chart(document.getElementById('chart1'), {
  type: 'line', // or 'bar'
  data: {
    labels: ['D-9','D-8','D-7','D-6','D-5','D-4','D-3','D-2','D-1','Today'],
    datasets: [{
      label: 'Value',
      data: [/* data extracted from the source */],
      borderColor: '#accent-color',
      backgroundColor: 'rgba(r,g,b,0.08)',
      fill: true,
      tension: 0.3,
      pointRadius: 3
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      y: { ticks: { font: { size: 11 } }, grid: { color: 'rgba(128,128,128,0.1)' } },
      x: { ticks: { font: { size: 11 }, autoSkip: false }, grid: { display: false } }
    }
  }
});
</script>
```

### Traffic light badges

```html
<!-- Always these 3 states, never other colors -->
<span class="badge ok">OK</span>
<span class="badge warn">Watch</span>
<span class="badge bad">Off target</span>

<style>
.badge { display: inline-block; padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 600; }
.ok   { background: #dcfce7; color: #166534; }
.warn { background: #fef9c3; color: #854d0e; }
.bad  { background: #fee2e2; color: #991b1b; }
</style>
```

### Metric cards

```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 2rem;">
  <div class="metric-card">
    <div class="metric-label">Monthly churn</div>
    <div class="metric-value">1.8%</div>
    <div class="metric-delta ok-text">↓ below the 2% target</div>
  </div>
  <!-- repeat for each key KPI -->
</div>

<style>
.metric-card  { background: #f8f9fa; border-radius: 10px; padding: 1.25rem; border: 1px solid #e9ecef; }
.metric-label { font-size: 11px; text-transform: uppercase; letter-spacing: .06em; color: #6c757d; margin-bottom: 6px; }
.metric-value { font-size: 2rem; font-weight: 700; color: #111; line-height: 1; }
.metric-delta { font-size: 12px; margin-top: 6px; }
.ok-text   { color: #166534; }
.warn-text { color: #854d0e; }
.bad-text  { color: #991b1b; }
</style>
```

---

## Template B — Editorial document

For analyses, reports, strategic notes.

### Layout rules

- Max `760px` content width, centered on the page
- Page background: `#fafaf8` (slightly cream, not pure white)
- Typography: H1 title `2.2rem/700`, H2 `1.3rem/600` with `border-bottom: 2px solid accent`, body `1rem/400`, `line-height: 1.75`
- Quotes / key points: `border-left: 3px solid accent` + `padding-left: 1.5rem` + slightly muted `color`
- Sections separated by `margin: 3rem 0`
- No chart unless the source contains numerical data
- Alert / risk: callout box with `#fff3cd` background, `border-left: 4px solid #f59e0b`, `padding: 1rem 1.25rem`

---

## Template C — Decision sheet

For a decision, an offer comparison or a negotiation position.

### Specific rules

- Options in a side-by-side grid (`repeat(auto-fit, minmax(220px, 1fr))`)
- Recommended option: `border: 2px solid accent` + "Recommended" badge at the top of the card
- Comparison table with CSS symbols: `✓` in green, `✗` in red, `~` in amber
- "Next steps" section at the bottom: slightly tinted background, numbered list
- No chart — the visual comparison is enough

---

## Cross-cutting rules — always active

### Brand pack consumption

- declare the main tokens as CSS variables from `brand_pack.palette`, `brand_pack.typography`, `brand_pack.spacing` and `brand_pack.document_rules`
- use `brand_pack.format_rules.<format>` for format-specific choices (`rapport`, `fiche`, `slide`, `dashboard`)
- if `resolved_logo_assets` contains a preferred logo, use it as-is via its `data_uri`
- if `brand_pack.iconography` is present:
  - `icon_library` is strict
  - `icon_style` is strict
  - `icon_color` must remain `currentColor`
  - sizes to respect:
    - `sm/md/lg` for functional iconography
    - `xl/2xl` for illustrative iconography
    - `3xl` only as background decoration, low opacity

### Visual hierarchy (mandatory order on the page)
1. **Header** — title, context, period
2. **Summary / metric cards** — the 3-5 key figures or points, immediately visible
3. **Visualization** — charts or comparison grids
4. **Detail** — tables, lists, secondary sections
5. **Alerts / problems** — always at the bottom, never in the middle

### Animations (CSS only)
```css
/* Entrance on load — subtle, no distraction */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
.metric-card { animation: fadeUp .4s ease both; }
.metric-card:nth-child(2) { animation-delay: .08s; }
.metric-card:nth-child(3) { animation-delay: .16s; }
.metric-card:nth-child(4) { animation-delay: .24s; }
```

### What is forbidden in all templates
- Lorem ipsum or invented data if the source provides some
- Tables without `border-collapse: collapse`
- Charts without a `position: relative` wrapper + explicit height
- Two fonts from the same family (e.g. two generic sans-serifs)
- More than 3 colors in the main palette
- Empty sections or unfilled placeholders
- Explicitly contradicting an injected `Delivery branding`
- Hardcoding an icon library different from the one in the `brand_pack`
- Replacing HTML icons with emoji

---

## Final instruction for the LLM

When this reference is active:

1. **Read the source artifact in full** — skip nothing
2. **Choose a visual direction** (Step 1) — note it mentally and stick to it
3. **Detect the content type** → choose the right template (Step 2)
4. **Extract all the data from the source** — invent nothing, omit nothing
5. **Produce the complete, standalone HTML** — with Google fonts, embedded CSS, Chart.js if the Dashboard template
6. **Check**: does the file open in a browser without errors? Is all the source data present?
7. **Output**: raw HTML only — no markdown around it, no ```html, no explanation
