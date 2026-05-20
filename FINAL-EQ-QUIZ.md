# FINAL EQ QUIZ — Brand & Technical Reference
**Empowered By Sofia · Version 3.0 · May 2026**
**File:** `eq-audit-v9.html` · GitHub Pages · No Netlify · No iframe

---

## 1. Overview

| Property | Value |
|---|---|
| Product | The EQ Audit — free quiz funnel |
| File | `eq-audit-v9.html` — single self-contained HTML file |
| Also serves as | **Homepage** — replaces `index.html` |
| Live URL | `https://empoweredbysofia.github.io/eqquiz/eq-audit-v9.html` |
| Screens | 13 screens, toggled via JS `show(id)` |
| Questions | 10 questions across 5 EQ domains |
| Completion time | ~2 minutes |
| Primary audience | Women navigating career, business, marriage, parenting or study |
| Contact capture | After quiz, before results — First Name + Email required, Phone optional |
| Email service | Formspree — endpoint `https://formspree.io/f/xykonwpj` |
| Confirmation email | Yes — auto-sent to user via Formspree `_autoresponse` field |
| Dependencies | Google Fonts CDN only |

---

## 2. Brand Colours

### Base Palette
| Name | Hex | Usage |
|---|---|---|
| Cream | `#FAF8F5` | Primary background — always hardcoded hex, never variable |
| Ink | `#1C140C` | Primary body text |
| Ink Mid | `#4A3A28` | Secondary text, descriptions |
| Ink Soft | `#8C7D65` | Tertiary text, labels, placeholders |
| Gold | `#C9943A` | CTAs, borders, highlights, progress bar |
| Gold Dark | `#9B6E2A` | Eyebrows, labels, Pinyon Script stage names |
| Gold Light | `#E8B85A` | Hover states, gradients |
| Gold Pale | `#F5E8C0` | Selected states, active stage background |
| Crimson | `#6B1020` | Tier quotes, gradient start |
| Plum | `#2E0D3A` | **Accent words only** — see Section 3 |
| Emerald | `#0D3D2E` | WhatsApp button |
| White | `#FFFFFF` | Card backgrounds |

### Line / Border
```css
--line: rgba(155,110,42,0.2);
```

---

## 3. Plum Accent Words

Plum (`#2E0D3A`) is used on **specific words only** — never as a background colour, never on entire paragraphs. Applied via `.plum` class: `color: var(--plum)`.

| Screen | Word / Phrase | Reason |
|---|---|---|
| S1 Landing | **"emotions"** in headline | Creates the OMG moment — she sees her pain point named |
| S1 Landing | **"rising"** in italic quote | Aspirational — the destination |
| S1 Landing | **IQ/EQ line** — "Emotional Intelligence (EQ)" in `<em>` | Defines the key term with emphasis |
| S2 Why EQ | **"Emotional Intelligence"** in h2 | Section heading emphasis |
| S2 Why EQ | **"emotions"** in Sofia quote | Her pain point named again |
| S2 Why EQ | **"emotions"** in EQ definition | Reinforces the term |
| S5 Interstitial | **"unguided"** in Sofia quote | The reframe moment — not broken, just unguided |
| S7 Testimonials | **"emotionally"** in Nadia quote | Connects the testimonial to the product |
| S7 Testimonials | **"unregulated"** in Zainab quote | The reframe in parenting context |
| S9 Pre-results | **"mirror"** in tease quote | The key metaphor — results as truth not judgement |
| S10 Form | **"rising"** in sub-heading | Reinforces the destination |
| S12 Profile | **"rising"** in sub-text | Consistent destination language |
| S13 Results | Growth Edge value in profile table | Highlights her area of growth in plum |

---

## 4. The IQ/EQ Statement

Placed on Screen 1 (Brand Landing), below the headline, with a plum left border:

> "Intelligence opens doors. *Emotional Intelligence (EQ)* decides what you do once you walk through them — how you love, lead and live."

CSS class: `.iq-eq-line` — left border in `var(--plum)`, italic `<em>` for the EQ term.

---

## 5. Typography

### Font Imports
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Crimson+Pro:ital,wght@0,300;0,400;1,300;1,400&family=Pinyon+Script&family=Cinzel:wght@400&display=swap" rel="stylesheet">
```

| Font | Usage |
|---|---|
| Cormorant Garamond | All headings, nav, eyebrows, labels, stage names |
| Crimson Pro | Body text, descriptions, testimonials |
| Pinyon Script | EQ stage names — profile card and results page |
| Cinzel | All `&` ampersand signs — Roman capitals, never italic |

---

## 6. The 13 Screens

| # | ID | Name | Key Change in v3 |
|---|---|---|---|
| 1 | `s1` | Brand Landing | IQ/EQ line added. Plum on "emotions" + "rising". Footer nav links. Now serves as homepage. |
| 2 | `s2` | Why EQ | Trimmed to Sofia quote + 3 stats only. Plum on "Emotional Intelligence" + "emotions". |
| 3 | `s3` | Life Areas | Career / Study / Business / Marriage / Parenting |
| 4 | `s4` | Quiz Block A | Q1–Q4. Auto-advances. |
| 5 | `s5` | Interstitial 1 | Plum on "unguided". |
| 6 | `s6` | Quiz Block B | Q5–Q8 personalised. |
| 7 | `s7` | Social Proof | Plum on "emotionally" (Nadia) and "unregulated" (Zainab). |
| 8 | `s8` | Quiz Block C | Q9–Q10. Pulse on Q10. |
| 9 | `s9` | Pre-Results Tease | Plum on "mirror". |
| 10 | `s10` | Contact Capture | Plum on "rising". Phone "clear" button — does NOT submit. |
| 11 | `s11` | Calculating | Personalised headline. Domain reveal animation. |
| 12 | `s12` | EQ Profile Card | Plum on growth edge value. Plum on "rising". |
| 13 | `s13` | Full Results | Stage name first. Score ring second. All 5 stages with next step chips. |

---

## 7. Formspree Integration

**Endpoint:** `https://formspree.io/f/xykonwpj`
**Method:** POST, JSON, non-blocking (results show regardless of submission status)

### Data submitted to Formspree:
| Field | Value |
|---|---|
| `name` | User's first name |
| `email` | User's email |
| `phone` | Phone or "Not provided" |
| `life_areas` | Comma-separated selected areas |
| `eq_stage` | Tier name e.g. "The Necessary Dark" |
| `eq_score` | Score percentage e.g. "62%" |
| `strongest_domain` | Highest scoring domain |
| `growth_edge` | Lowest scoring domain |
| `readiness` | Awakening / Opening Up / Ready to Rise |
| `recommended_next_step` | Highlighted product for their tier |
| `_subject` | Email subject: "EQ Audit Result: [Name] — [Stage]" |
| `_replyto` | User's email (so you can reply directly) |
| `_autoresponse` | Confirmation email sent to user with stage, arrived quote and next steps |

### Confirmation email to user includes:
1. Their EQ stage name
2. Their arrived quote
3. All 3 next step options — recommended marked with ★
4. Link back to the quiz

### You receive (in Formspree inbox):
- Every submission with full details
- Subject line includes name and stage for easy scanning

---

## 8. The 10 Questions

| Q | Block | Domain | Personalised |
|---|---|---|---|
| 1 | A | Nervous System Awareness | No |
| 2 | A | Emotional Processing | No |
| 3 | A | Trigger Identification | No |
| 4 | A | Recovery Speed | No |
| 5 | B | Regulated Relationships | No |
| 6 | B | Trigger Identification | No |
| 7 | B | Life Areas | **Yes** — `[areas]` replaced |
| 8 | B | Future Self | **Yes** — feeds readiness score |
| 9 | C | Nervous System Awareness | No |
| 10 | C | Emotional Processing | No — gold pulse animation |

**Scoring:** Never=1 · Rarely=2 · Sometimes=3 · Often=4 · Always=5 · Max=50
**Score %** = `Math.round((total/50)*100)`

---

## 9. The 5 EQ Tiers

| Tier | Range | Name | Meaning |
|---|---|---|---|
| 1 | 20–39% | The Still Beginning | Not yet connected to emotional patterns. Life feels heavy but hard to name. |
| 2 | 40–54% | The First Noticing | Beginning to observe patterns. Awareness is dawning. |
| 3 | 55–69% | The Necessary Dark | In the middle of transformation. Feels like breakdown but is breakthrough. |
| 4 | 70–84% | The Becoming | Actively transforming. Regulated responses forming. Wings in motion. |
| 5 | 85–100% | The Free Butterfly | Emerged. Regulated, grounded and free. Leading from wholeness. |

---

## 10. Next Step Guidance Per Tier

All 3 options always shown. Highlighted = recommended. Others remain clickable.

| Tier | Highlighted | Reason |
|---|---|---|
| 1 | The Emotional Reset £12 | Foundation needed first. |
| 2 | The Reset Room | Community and monthly guidance. |
| 3 | 1:1 with Sofia | Breakthrough moment — direct support. |
| 4 | The Reset Room | Sustain the transformation. |
| 5 | WhatsApp Community | Next stage is leading others. |

---

## 11. Results Page Order (Screen 13)

1. Stage name (Pinyon Script, large, gold) — emotional impact first
2. Tier description block — quote + description
3. Score ring — animated SVG, fills after stage name is read
4. Transformation block — 🐛 → 🦋 with arrived quote
5. All 5 stages breakdown — active stage highlighted
6. Social proof stat
7. Testimonial — auto-selected by primary life area
8. Footer nav links

---

## 12. All Internal Links

**Base:** `https://empoweredbysofia.github.io/eqquiz/`

| Page | URL |
|---|---|
| Homepage / EQ Audit | `...eq-audit-v9.html` |
| Ebook | `...ebook.html` |
| Membership | `...membership.html` |
| Apply | `...apply.html` |
| Organisations | `...organisations.html` |
| WhatsApp | `https://chat.whatsapp.com/D6qYf6tFUhMCrC1FkEu4Ce?mode=gi_t` |

---

## 13. Do Not

- ❌ Use dark backgrounds — parchment `#FAF8F5` always
- ❌ Use root-relative paths (`/filename.html`) — full GitHub Pages URL always
- ❌ Use any font other than Cinzel for `&` signs
- ❌ Make the phone "clear" button submit the form — clears only
- ❌ Place the score ring before the stage name on results — stage name first always
- ❌ Show only the recommended product — all 3 options must appear
- ❌ Use plum on entire paragraphs or backgrounds — accent words only
- ❌ Remove the `ED` coral colouring from EmpowerED Minds
- ❌ Change Formspree endpoint without updating `_autoresponse` content

---

*Empowered By Sofia · EQ Audit v3.0 · May 2026 · Confidential*
