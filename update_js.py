with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update renderSchemes to add click to apply
card_original = '<article class="scheme-card" data-index="${index}">'
card_new = '<article class="scheme-card" data-index="${index}" style="cursor:pointer;" onclick="applySchemeToAvatar(\'${mainHex}\', \'${secondaryHex}\', \'${accentHex}\')">'
content = content.replace(card_original, card_new)

# Stop event propagation for copy button so it doesn't trigger the card click
btn_original = '<button class="copy-btn" onclick="copyScheme(this, \'${mainHex}\', \'${secondaryHex}\', \'${accentHex}\')">'
btn_new = '<button class="copy-btn" onclick="event.stopPropagation(); copyScheme(this, \'${mainHex}\', \'${secondaryHex}\', \'${accentHex}\')">'
content = content.replace(btn_original, btn_new)

# 2. Add avatar JS logic
avatar_js = """
    // Avatar Logic
    const avatarState = {
      upper: 'tshirt',
      lower: 'skirt',
      hat: false,
      necklace: true,
      watch: false
    };

    function initAvatarControls() {
      // Upper
      document.querySelectorAll('#upperControls .btn-option').forEach(btn => {
        btn.addEventListener('click', (e) => {
          document.querySelectorAll('#upperControls .btn-option').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          avatarState.upper = btn.dataset.value;
          document.getElementById('cloth-tshirt').style.display = avatarState.upper === 'tshirt' ? 'block' : 'none';
          document.getElementById('cloth-sweater').style.display = avatarState.upper === 'sweater' ? 'block' : 'none';
        });
      });
      // Lower
      document.querySelectorAll('#lowerControls .btn-option').forEach(btn => {
        btn.addEventListener('click', (e) => {
          document.querySelectorAll('#lowerControls .btn-option').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          avatarState.lower = btn.dataset.value;
          document.getElementById('cloth-skirt').style.display = avatarState.lower === 'skirt' ? 'block' : 'none';
          document.getElementById('cloth-pants').style.display = avatarState.lower === 'pants' ? 'block' : 'none';
        });
      });
      // Accessories
      document.querySelectorAll('#accessoryControls .btn-option').forEach(btn => {
        btn.addEventListener('click', (e) => {
          btn.classList.toggle('active');
          const acc = btn.dataset.value;
          avatarState[acc] = btn.classList.contains('active');
          document.getElementById(`acc-${acc}`).style.display = avatarState[acc] ? 'block' : 'none';
        });
      });
    }

    function updateAvatarColors(mainHex, secondaryHex, accentHex) {
      document.querySelectorAll('.svg-upper path').forEach(el => el.setAttribute('fill', mainHex));
      document.querySelectorAll('.svg-lower').forEach(el => el.setAttribute('fill', secondaryHex));
      document.querySelectorAll('.svg-acc-fill').forEach(el => el.setAttribute('fill', accentHex));
      document.querySelectorAll('.svg-acc-stroke').forEach(el => el.setAttribute('stroke', accentHex));
    }

    function applySchemeToAvatar(mainHex, secondaryHex, accentHex) {
      updateAvatarColors(mainHex, secondaryHex, accentHex);
      
      // Highlight the selected scheme card
      document.querySelectorAll('.scheme-card').forEach(card => {
        card.style.borderColor = 'transparent';
        card.style.boxShadow = 'var(--shadow-md)';
      });
      const activeEvent = event;
      if (activeEvent && activeEvent.currentTarget && activeEvent.currentTarget.classList.contains('scheme-card')) {
        activeEvent.currentTarget.style.borderColor = 'var(--text-primary)';
        activeEvent.currentTarget.style.boxShadow = '0 0 0 2px var(--text-primary)';
      }
    }
"""

content = content.replace("    // Generate color schemes", avatar_js + "\n    // Generate color schemes")

# 3. Call initAvatarControls() in Initialize
content = content.replace("    initCopyComboBtn();\n    updateFromHSL();", "    initCopyComboBtn();\n    initAvatarControls();\n    updateFromHSL();")

# 4. Auto apply first scheme in generateSchemes() if mode is 'auto'
generate_schemes_end = """
      renderSchemes(schemes);
"""
generate_schemes_end_new = """
      renderSchemes(schemes);
      
      if (currentMode === 'auto') {
        const first = schemes[0].colors;
        updateAvatarColors(
          hslToHex(first.main.h, first.main.s, first.main.l),
          hslToHex(first.secondary.h, first.secondary.s, first.secondary.l),
          hslToHex(first.accent.h, first.accent.s, first.accent.l)
        );
      }
"""
content = content.replace(generate_schemes_end, generate_schemes_end_new)

# 5. Auto update avatar in updateStepPreview()
update_step_end = """
      if (selectedAccent) {
        selectedAccentSwatch.style.background = hslToHex(selectedAccent.h, selectedAccent.s, selectedAccent.l);
        selectedAccentHex.textContent = hslToHex(selectedAccent.h, selectedAccent.s, selectedAccent.l);
      } else {
        selectedAccentSwatch.style.background = '#e7e5e4';
        selectedAccentHex.textContent = '—';
      }
    }
"""
update_step_end_new = """
      if (selectedAccent) {
        selectedAccentSwatch.style.background = hslToHex(selectedAccent.h, selectedAccent.s, selectedAccent.l);
        selectedAccentHex.textContent = hslToHex(selectedAccent.h, selectedAccent.s, selectedAccent.l);
      } else {
        selectedAccentSwatch.style.background = '#e7e5e4';
        selectedAccentHex.textContent = '—';
      }
      
      if (currentMode === 'step') {
        updateAvatarColors(mainHex, secondaryHex, accentHex);
      }
    }
"""
content = content.replace(update_step_end, update_step_end_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("JS logic inserted successfully.")
