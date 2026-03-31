import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert CSS for .avatar-panel before /* Right Panel - Color Schemes */
css_to_insert = """
    /* Avatar Panel (Middle) */
    .avatar-panel {
      width: 420px;
      min-width: 420px;
      background: var(--bg-primary);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .avatar-header {
      padding: 48px 32px 24px;
    }

    .avatar-header h2 {
      font-size: 20px;
      font-weight: 600;
      margin-bottom: 8px;
    }
    
    .avatar-header p {
      font-size: 14px;
      color: var(--text-secondary);
    }

    .avatar-preview-container {
      flex: 1;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      padding: 0 20px;
    }

    .avatar-svg {
      max-height: 100%;
      width: 100%;
    }

    .avatar-controls {
      background: var(--bg-secondary);
      border-top: 1px solid var(--border-color);
      padding: 24px 32px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .control-group {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .control-label {
      font-size: 13px;
      font-weight: 500;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .control-options {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .btn-option {
      padding: 8px 16px;
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      border-radius: 100px;
      font-size: 13px;
      font-weight: 500;
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .btn-option:hover {
      border-color: var(--text-primary);
      color: var(--text-primary);
    }

    .btn-option.active {
      background: var(--text-primary);
      border-color: var(--text-primary);
      color: white;
    }
"""
content = content.replace("    /* Right Panel - Color Schemes */", css_to_insert + "\n    /* Right Panel - Color Schemes */")

# 2. Update media queries
mq1200 = """
    @media (max-width: 1200px) {
      .avatar-panel {
        width: 360px;
        min-width: 360px;
      }
    }
"""
content = content.replace("    /* Responsive */\n    @media (max-width: 900px) {", "    /* Responsive */\n" + mq1200 + "\n    @media (max-width: 900px) {")

mq900_insert = """
      .avatar-panel {
        width: 100%;
        min-width: unset;
        border-right: none;
        border-bottom: 1px solid var(--border-color);
      }
      .avatar-preview-container {
        height: 400px;
        padding: 20px;
      }
"""
content = content.replace("      .picker-panel {\n        width: 100%;", "      .picker-panel {\n        width: 100%;" + mq900_insert)

mq480_insert = """
      .avatar-header, .avatar-controls {
        padding: 24px 16px;
      }
"""
content = content.replace("      .picker-panel {\n        padding: 24px 16px;\n      }", "      .picker-panel {\n        padding: 24px 16px;\n      }\n" + mq480_insert)

# 3. Insert HTML between </aside> and <main>
html_to_insert = """
    <!-- Middle Panel: Avatar Dress Up -->
    <section class="avatar-panel">
      <header class="avatar-header">
        <h2>模特换装预览</h2>
        <p>直观查看色彩搭配在人物身上的效果</p>
      </header>
      
      <div class="avatar-preview-container">
        <!-- SVG Avatar will be defined here -->
        <svg class="avatar-svg" viewBox="0 0 300 500" xmlns="http://www.w3.org/2000/svg">
          <!-- SVG content goes here (to be filled in task 2) -->
        </svg>
      </div>

      <div class="avatar-controls">
        <div class="control-group">
          <div class="control-label">上衣款式</div>
          <div class="control-options" id="upperControls">
            <button class="btn-option active" data-type="upper" data-value="tshirt">T恤</button>
            <button class="btn-option" data-type="upper" data-value="sweater">毛衣</button>
          </div>
        </div>
        <div class="control-group">
          <div class="control-label">下装款式</div>
          <div class="control-options" id="lowerControls">
            <button class="btn-option active" data-type="lower" data-value="skirt">裙子</button>
            <button class="btn-option" data-type="lower" data-value="pants">长裤</button>
          </div>
        </div>
        <div class="control-group">
          <div class="control-label">配饰 (点缀色)</div>
          <div class="control-options" id="accessoryControls">
            <button class="btn-option" data-type="acc" data-value="hat">帽子</button>
            <button class="btn-option active" data-type="acc" data-value="necklace">项链</button>
            <button class="btn-option" data-type="acc" data-value="watch">手表</button>
          </div>
        </div>
      </div>
    </section>
"""

content = content.replace("    </aside>\n\n    <!-- Right Panel: Color Schemes -->", "    </aside>\n\n" + html_to_insert + "\n    <!-- Right Panel: Color Schemes -->")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML and CSS structure updated successfully.")
