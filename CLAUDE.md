# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`color-combo` is a static, single-page web application for clothing color matching. It helps users generate harmonious color palettes based on the 60-30-10 color rule. The app is entirely contained in `index.html` (HTML, CSS, and JS all in one file) with no external dependencies.

## Development Workflow

- **Run/View:** Open `index.html` directly in any modern web browser.
  - *Optional:* Serve locally using Python: `python3 -m http.server 8000`
- **Build/Lint/Test:** There is no build step (no bundlers or compilers), and no automated linting or testing frameworks are configured. Changes are made directly to `index.html` and tested manually in the browser.

## High-Level Architecture & Structure

The application's logic is conceptually divided into UI panels, state management, and color algorithms.

### UI Structure
The user interface is split into three main vertical panels:
1. **Left Panel (Color Picker & Modes):**
   - Supports two modes: "Auto Generation" and "Step-by-Step".
   - Contains a Canvas-based interactive color wheel, saturation/lightness sliders, and HEX input fields.
2. **Middle Panel (Avatar Preview):**
   - An interactive SVG avatar representing a person with configurable clothing.
   - Allows users to toggle clothing items (T-shirt vs sweater, skirt vs pants) and accessories.
   - Instantly previews the applied 60-30-10 color scheme on a modeled outfit.
3. **Right Panel (Color Schemes):**
   - Displays a scrollable list of 5 generated color scheme cards (visible in "Auto Generation" mode).
   - Clicking a scheme card automatically applies the colors to the SVG Avatar in the Middle Panel.

### Core Logic & Data Flow
- **State & Event Handling:** DOM events (sliders, canvas clicks, mode toggles, and avatar control buttons) trigger updates to a global state, which immediately re-renders the UI components without page reloads.
- **Color Representation:** HSL (Hue, Saturation, Lightness) is the internal canonical format for all color math.
- **Color Conversion Utilities:** Custom functions (`hexToRgb`, `rgbToHsl`, `hslToHex`, etc.) convert between HEX, RGB, and HSL.
- **Palette Generation Algorithms:**
  Automatically calculates 5 schemes based on the Main Color's hue (hue rotation in degrees):
  - **Complementary:** +180°
  - **Analogous:** ±30°
  - **Triadic:** +120°, +240°
  - **Split-Complementary:** +150°, +210°
  - **Double Analogous:** ±60°

  The generated output maps these colors into the 60-30-10 distribution pattern (Main = 60%, Secondary = 30%, Accent = 10%).