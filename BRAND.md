# Spark ✦ & Spectrum CIC — Brand Guidelines
**Version 1.0 · May 2026**

> This document is the single source of truth for replicating the Spark & Spectrum CIC logo and all sub-brand visual identities. Any deviation must be approved before implementation.

---

## 1. Brand Architecture

```
Spark ✦ & Spectrum CIC  (umbrella / parent)
├── School of Autism        (founded by Selina Afzal)
└── EmpowerED Minds         (founded by Sofia Iqbal · sub-brand of Empowered By Sofia)
        └── Empowered By Sofia  (parent personal brand · Reset Internally · Rise Externally)
```

---

## 2. Spark & Spectrum CIC Logo

### 2.1 Logo Construction

The logo is composed of four elements in this exact order:

```
[SPARK in Gold]  [✦ diamond]  [& in Cinzel]  [SPECTRUM in rainbow gradient]
```

### 2.2 Typography

| Element    | Font                  | Weight | Style  |
|------------|-----------------------|--------|--------|
| Spark      | Playfair Display      | 700    | Normal |
| &          | Cinzel                | 400    | Normal |
| Spectrum   | Playfair Display      | 700    | Normal |
| CIC badge  | DM Sans               | 500    | Normal |
| Tagline    | Playfair Display      | 400    | Italic |

Google Fonts import:
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Cinzel:wght@400&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
```

### 2.3 Colours

| Element        | Colour        | Hex       |
|----------------|---------------|-----------|
| Spark          | Gold          | `#C9943A` |
| Diamond ✦      | Gold          | `#C9943A` |
| & (ampersand)  | Warm grey     | `#8C7D65` |
| S (Spectrum)   | Purple        | `#7B6BB5` |
| pe (Spectrum)  | Blue          | `#5B9EC8` |
| ct (Spectrum)  | Teal          | `#3BADB5` |
| rum (Spectrum) | Green         | `#6BAD5B` |
| Background     | Cream         | `#FAF8F5` |
| Tagline        | Warm grey     | `#8C7D65` |

Spectrum gradient formula (left to right):
```css
background: linear-gradient(90deg, #7B6BB5, #5B9EC8, #3BADB5, #6BAD5B);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

### 2.4 The Concave Diamond ✦

- **Character:** `✦` (U+2736 SIX POINTED BLACK STAR / four-pointed star)
- **Position:** Absolute, placed **above the k and to the right** — this is the defining mark of the logo
- **Sizing:** Approximately 22–23% of the Spark font size
- **Top offset:** Always `top: 10px` — fixed across all sizes, places the diamond in the upper-right area of the k, clearly above its midpoint
- **Right offset:** Negative value = ~14% of font size, pushing the diamond outside the k's right edge
- **Colour:** Always gold `#C9943A` — never the Spectrum gradient

> ★ **The hero h1 on the organisations page is the master reference. All other instances must replicate this placement proportionally.**

Scale reference table:

| Context          | Spark font size | Diamond size | top  | right  |
|------------------|-----------------|--------------|------|--------|
| Hero h1 ★        | ~88px           | 20px         | 10px | -12px  |
| Section heading  | ~45px           | 10px         | 10px | -6px   |
| Brand card       | ~24px           | 6px          | 10px | -3px   |
| Programme header | ~22px           | 5px          | 10px | -3px   |
| Nav              | ~18px           | 4px          | 10px | -2px   |

HTML pattern:
```html
<span style="position:relative;">
  k
  <span style="position:absolute; top:10px; right:-12px; font-size:20px; color:#C9943A;">✦</span>
</span>
```

## 2.5 The Ampersand &

**Every single `&` sign on the page — without exception — uses Cinzel.**

This is a non-negotiable brand rule. Cinzel's Roman-inspired capitals give the `&` an architectural, ceremonial quality that balances the flowing serif of Playfair Display and the gradient energy of Spectrum.

- **Font:** Cinzel, weight 400
- **Size:** Smaller than surrounding text — approximately `0.75em–0.85em` of the context font size
- **Colour:** `#8C7D65` (warm grey) via `color: var(--text-light)`
- **Opacity:** `0.65–0.75` — always slightly receded, never dominant
- **Style:** `font-style: normal` — Cinzel is Roman capitals, **never italic**
- **Vertical alignment:** `vertical-align: middle`

### CSS class (used on `.amp` and `.nav-amp`):
```css
.amp, .nav-amp {
  font-family: 'Cinzel', serif;
  font-style: normal;
  font-size: 0.75em;
  color: var(--text-light); /* #8C7D65 */
  opacity: 0.65;
  vertical-align: middle;
}
```

### Inline span (used everywhere else):
```html
<span style="font-family:'Cinzel',serif;font-style:normal;font-size:0.8em;color:var(--text-light);opacity:0.65;vertical-align:middle;">&amp;</span>
```

### Google Fonts import (required):
```html
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400&display=swap" rel="stylesheet">
```

### Applies to ALL instances including:
- Spark `&` Spectrum logo (all sizes: hero, nav, card, heading, block header)
- Section labels: "Psychology `&` modalities", "All programmes `&` ..."
- Modality names: "Strengths-Based `&` Narrative", "Mindfulness `&` Somatic", etc.
- Programme tags: "Schools `&` SEND", "NQTs `&` PGCE", "NHS `&` public sector"
- Stats: "Programmes `&` workshops", "In-person `&` online"
- Footer: "Spark `&` Spectrum CIC"
- Co-founders line: "Sofia Iqbal `&` Selina Afzal"
- Any new `&` added to the page in future

### 2.6 Full HTML Logo (Hero Size)

```html
<h1 style="font-family:'Playfair Display',serif; font-weight:700; font-size:clamp(2.8rem,8vw,5.5rem); line-height:1.05;">
  <span style="color:#C9943A;">
    Spar<span style="position:relative;">k<span style="position:absolute;top:10px;right:-12px;font-size:20px;color:#C9943A;">✦</span></span>
  </span>
  <span style="font-family:'Cinzel',serif;font-style:normal;font-size:0.55em;color:#8C7D65;opacity:0.6;vertical-align:middle;"> &amp; </span>
  <span style="background:linear-gradient(90deg,#7B6BB5,#5B9EC8,#3BADB5,#6BAD5B);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Spectrum</span>
</h1>
```

### 2.7 Tagline

```
reset internally  ·  rise externally
```

- Font: Playfair Display Italic, weight 400
- Size: ~0.35em of the logo size
- Colour: `#8C7D65`
- Separator: `·` (middle dot), spaced with two spaces either side

### 2.8 CIC Badge

- Text: `CIC`
- Font: DM Sans, weight 500, letter-spacing 0.12em, uppercase
- Background: Transparent with gold border `#C9943A`, border-radius 8px
- Colour: `#C9943A`

---

## 3. School of Autism — Sub-Brand

**Founded by Selina Afzal · Part of Spark & Spectrum CIC**

### 3.1 Colours

| Colour  | Hex       | Usage                          |
|---------|-----------|--------------------------------|
| Blue    | `#2B5FA5` | S, o, o, s letters · eye label |
| Red     | `#D42B2B` | c, l, A, u, m letters          |
| Green   | `#2E7D32` | h, t letters                   |
| Yellow  | `#F5A623` | o (first), i letters           |

### 3.2 Logo Name Letter Colouring

Applied character by character:

| Letter | Colour        |
|--------|---------------|
| S      | Blue `#2B5FA5`|
| c      | Red `#D42B2B` |
| h      | Green `#2E7D32`|
| o      | Yellow `#F5A623`|
| o      | Blue `#2B5FA5`|
| l      | Red `#D42B2B` |
| (of)   | Ink `#0E0A0F` |
| A      | Red `#D42B2B` |
| u      | Yellow `#F5A623`|
| t      | Green `#2E7D32`|
| i      | Yellow `#F5A623`|
| s      | Blue `#2B5FA5`|
| m      | Red `#D42B2B` |

### 3.3 HTML Pattern

```html
<span style="color:#2B5FA5;">S</span><span style="color:#D42B2B;">c</span><span style="color:#2E7D32;">h</span><span style="color:#F5A623;">o</span><span style="color:#2B5FA5;">o</span><span style="color:#D42B2B;">l</span>
<span style="color:#0E0A0F;"> of </span>
<span style="color:#D42B2B;">A</span><span style="color:#F5A623;">u</span><span style="color:#2E7D32;">t</span><span style="color:#F5A623;">i</span><span style="color:#2B5FA5;">s</span><span style="color:#D42B2B;">m</span>
```

### 3.4 Border / Accent Gradient

```css
border-image: linear-gradient(135deg, #2B5FA5, #D42B2B, #2E7D32, #F5A623) 1;
```

Top accent bar:
```css
background: linear-gradient(90deg, #2B5FA5, #D42B2B, #2E7D32, #F5A623, #2B5FA5);
```

### 3.5 Voice & Positioning

- Specialist autism education, therapeutic support and family programmes
- Neurodiversity-affirming, strengths-based approach
- Founded by Selina Afzal
- Part of Spark & Spectrum CIC umbrella

---

## 4. EmpowerED Minds — Sub-Brand

**Founded by Sofia Iqbal · Sub-brand of Empowered By Sofia · Part of Spark & Spectrum CIC**

### 4.1 Colours

| Colour      | Hex       | Usage                        |
|-------------|-----------|------------------------------|
| Navy        | `#1C2B4A` | "Empower" and "Minds" text   |
| Coral/Amber | `#D85A30` | "ED" — the emphasis          |
| Light coral | `#F0997B` | "ED" on dark backgrounds     |

### 4.2 Logo Name HTML Pattern

On light backgrounds:
```html
<span style="color:#1C2B4A;">Empower</span><span style="color:#D85A30;font-style:normal;">ED</span><span style="color:#1C2B4A;"> Minds</span>
```

On dark backgrounds (programme header):
```html
<span style="color:#FFFFFF;">Empower</span><span style="color:#F0997B;font-style:normal;">ED</span><span style="color:#FFFFFF;"> Minds</span>
```

### 4.3 Programme Header Background

```css
background: #2A3850; /* dark navy */
```

Eyebrow text on dark bg: `color: rgba(255,255,255,0.85)`

### 4.4 CTA / Button Colours

```css
background: #D85A30; /* coral button */
```
Hover:
```css
background: #993C1D;
```

### 4.5 Specialisms

- Emotional intelligence (EQ) — Salovey–Mayer and Goleman models
- NLP (Neuro-Linguistic Programming)
- Trauma-informed practice
- Vision loss and complex medical needs
- CPD-certified delivery

### 4.6 Audience

Teachers · Women · Parents · Young girls · Children · Schools · Employers · Community organisations

### 4.7 Parent Brand — Empowered By Sofia

| Element   | Value                              |
|-----------|------------------------------------|
| Tagline   | Reset Internally · Rise Externally |
| Gold      | `#C9943A`                          |
| Crimson   | `#6B1020`                          |
| Plum      | `#2E0D3A`                          |
| Cream     | `#FAF8F5`                          |
| Font      | Cormorant Garamond + Crimson Pro   |

---

## 5. Shared Design System

### 5.1 Background & Base

```css
background: linear-gradient(135deg,
  #FAF8F5 0%,
  rgba(232,184,90,0.08) 25%,
  rgba(107,16,32,0.06) 50%,
  rgba(46,13,58,0.08) 75%,
  #F5EFE7 100%);
background-attachment: fixed;
```

### 5.2 Glass Card

```css
background: rgba(255,255,255,0.85);
backdrop-filter: blur(20px);
border: 2px solid;
border-image: linear-gradient(135deg, #C9943A, #6B1020, #2E0D3A, #0D3D2E, #C9943A) 1;
box-shadow: 0 20px 60px rgba(0,0,0,0.08), 0 2px 8px rgba(0,0,0,0.04);
```

Top accent bar (3px, inside glass card):
```css
background: linear-gradient(90deg, #2E0D3A, #6B1020, #C9943A, #0D3D2E, #C9943A);
opacity: 0.6;
```

### 5.3 Primary CTA Button

```css
background: linear-gradient(135deg, #2E0D3A 0%, #6B1020 50%, #C9943A 100%);
color: white;
border-radius: 50px;
box-shadow: 0 6px 25px rgba(107,16,32,0.35);
font-family: 'Cormorant Garamond', serif;
font-weight: 600;
letter-spacing: 0.1em;
text-transform: uppercase;
```

### 5.4 Section Label (eyebrow)

```css
font-family: 'Cormorant Garamond', serif;
font-size: 0.75rem;
font-weight: 600;
letter-spacing: 0.3em;
text-transform: uppercase;
background: linear-gradient(135deg, #C9943A, #E8B85A);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

### 5.5 Heading Gradient (h2)

```css
background: linear-gradient(135deg, #6B1020, #2E0D3A);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

### 5.6 Floating Orbs

```css
/* Primary orb */
background: radial-gradient(circle, rgba(46,13,58,0.18) 0%, rgba(107,16,32,0.1) 50%, transparent 70%);
filter: blur(60px);
animation: float 9s ease-in-out infinite;

/* Secondary orb */
background: radial-gradient(circle, rgba(232,184,90,0.22) 0%, rgba(13,61,46,0.1) 50%, transparent 70%);
animation: float 12s ease-in-out infinite reverse;
```

```css
@keyframes float {
  0%, 100% { transform: translate(0,0) scale(1); }
  50%       { transform: translate(25px,-25px) scale(1.08); }
}
```

---

## 6. File Checklist

| File                     | Purpose                                      |
|--------------------------|----------------------------------------------|
| `index.html`             | Empowered By Sofia homepage                  |
| `eq-audit-v9.html`       | EQ Audit quiz wrapper                        |
| `organisations.html`     | Spark & Spectrum CIC organisations page      |
| `ebook.html`             | The Emotional Reset ebook page               |
| `membership.html`        | The Reset Room membership page               |
| `apply.html`             | 1:1 Coaching application page                |
| `spark-spectrum-logo.jpg`| Master logo JPEG for sharing / print         |
| `BRAND.md`               | This file — single source of truth           |

---

## 7. Do Not

- ❌ Use the Spectrum rainbow gradient on "Spark" — Spark is always gold only
- ❌ Move the diamond — it always sits **above the k and to the right**. The hero h1 is the master reference. Never place it below the k or centred on it
- ❌ Use any font other than Cinzel for ANY `&` sign anywhere on the page — this is absolute
- ❌ Use italic style on the Cinzel `&` — Cinzel is Roman capitals, never italic
- ❌ Write a bare `&amp;` without wrapping it in the Cinzel span (except inside CSS or HTML attributes)
- ❌ Place "EmpowerED Minds" before "School of Autism" in the hero/header — SoA always leads on the organisations page
- ❌ Remove the `ED` coral colouring from EmpowerED Minds in any context
- ❌ Use dark backgrounds on the main page body — cream `#FAF8F5` always

---

*Empowered By Sofia · EmpowerED Minds · Spark & Spectrum CIC · School of Autism*
*© 2026 All rights reserved*
