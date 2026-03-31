# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`color-combo` is a static, single-page web application for clothing color matching. It helps users generate harmonious color palettes based on the 60-30-10 color rule. The app is entirely contained in `index.html` (HTML, CSS, and JS all in one file).

## Development Workflow

- **Run/View:** Open `index.html` directly in any modern web browser. Babylon.js is loaded from CDN (`https://cdn.babylonjs.com/babylon.js`) — an internet connection is required for the 3D avatar.
  - *Optional:* Serve locally using Python: `python3 -m http.server 8000`
- **Build/Lint/Test:** There is no build step (no bundlers or compilers), and no automated linting or testing frameworks are configured. Changes are made directly to `index.html` and tested manually in the browser.

## High-Level Architecture & Structure

The application's logic is conceptually divided into UI panels, state management, and color algorithms.

### UI Structure
The user interface is split into three main vertical panels:
1. **Left Panel (Color Picker & Modes):**
   - Supports two modes: "Auto Generation" (5 schemes) and "Step-by-Step" (manual secondary/accent selection).
   - Contains a Canvas-based interactive color wheel, saturation/lightness sliders, and HEX input fields.
2. **Middle Panel (3D Avatar Preview):**
   - A Babylon.js 3D avatar representing a person with configurable clothing.
   - Allows users to toggle clothing items (T-shirt vs sweater, skirt vs pants) and accessories.
   - Instantly previews the applied 60-30-10 color scheme on a modeled outfit.
3. **Right Panel (Color Schemes):**
   - Displays a scrollable list of 5 generated color scheme cards (visible in "Auto Generation" mode).
   - Clicking a scheme card applies the colors to the 3D Avatar in the Middle Panel.

### Core Logic & Data Flow
- **Global State** (lines ~1076):
  - `currentHue`, `currentSaturation`, `currentLightness` — the main color in HSL
  - `currentMode` — `'auto'` or `'step'`
  - `selectedSecondary`, `selectedAccent` — `{ h, s, l }` for step-by-step mode
  - `secondaryLightness`, `accentLightness` — lightness overrides per slot
- **Rendering:** DOM events (sliders, canvas clicks, mode toggles, avatar control buttons) trigger direct DOM/canvas/WebGL updates — no virtual DOM or framework.
- **Color Representation:** HSL is the internal canonical format for all color math.
- **Color Conversion Utilities:** `hexToRgb`, `rgbToHsl`, `hslToHex`, `hslToRgb`, `rgbToHex`
- **Palette Generation Algorithms** — each scheme computes hue offsets from the main color's hue:
  - **Complementary:** +180°
  - **Analogous:** ±30°
  - **Triadic:** +120°, +240°
  - **Split-Complementary:** +150°, +210°
  - **Double Analogous:** ±60°

  These map into the 60-30-10 distribution: Main (60%), Secondary (30%), Accent (10%).

### Avatar (Babylon.js)
- Single `initBabylonScene()` function creates the scene, camera, lighting, and avatar mesh hierarchy.
- Avatar materials are PBRMaterial (`upperMaterial`, `lowerMaterial`, `accMaterial`, etc.) — clothing colors are updated by setting `diffuseColor` on these materials.
- Avatar has swappable meshes for top (T-shirt/sweater), bottom (skirt/pants), and accessories (hat, bag, glasses, watch, necklace, earrings).
