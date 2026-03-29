# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`color-combo` is a clothing color matching web application. It helps users generate harmonious color palettes based on the 60-30-10 color rule.

## Architecture

Single-page application with two main panels:
- **Left Panel**: Color picker with hue wheel, saturation slider, and HEX input
- **Right Panel**: Scrollable list of 5 generated color scheme cards

Color algorithms (HSL-based):
- Complementary: hue +180°
- Analogous: hue ±30°
- Triadic: hue +120°, +240°
- Split-Complementary: hue +150°, +210°
- Double Analogous: hue ±60°

## Running

Open `index.html` directly in any modern browser. No build step required.

## Color Conversion Utilities

All color math lives in standalone functions using HSL as the canonical internal format:
- `hexToRgb(hex)` → `{r, g, b}`
- `rgbToHex(r, g, b)` → `#RRGGBB`
- `rgbToHsl(r, g, b)` → `{h (0-360), s (0-100), l (0-100)}`
- `hslToRgb(h, s, l)` → `{r, g, b}`
- `hslToHex(h, s, l)` → `#RRGGBB`

These are used by both the color wheel picker and the scheme generators.

## Color Scheme Generators

Five algorithms (all HSL-based, hue rotation in degrees):
- **Complementary**: `hue + 180°`
- **Analogous**: `hue ± 30°`
- **Triadic**: `hue + 120°, + 240°`
- **Split-Complementary**: `hue + 150°, + 210°`
- **Double Analogous**: `hue ± 60°`

Each returns `{ main, secondary, accent }` using the 60-30-10 distribution (main=60%, secondary=30%, accent=10%).
