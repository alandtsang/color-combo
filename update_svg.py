with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

svg_content = """
          <g transform="translate(150, 420)">
            <!-- 背景发型 (Back Hair) -->
            <path d="M -40,-270 Q -50,-180 -20,-120 Q 0,-140 20,-120 Q 50,-180 40,-270 Q 50,-350 0,-350 Q -50,-350 -40,-270 Z" fill="#2d2d2d" />
            
            <!-- 身体肤色层 (Skin) -->
            <g id="avatar-skin" fill="#fcdbb5">
              <!-- 腿部 (Legs) -->
              <path d="M -15,0 L -25,-180 L -5,-180 L 0,-10 L 10,-10 L 5,-180 L 25,-180 L 15,0 Z" />
              <!-- 身体/躯干 (Torso) -->
              <path d="M -25,-180 Q -30,-250 -15,-300 L 15,-300 Q 30,-250 25,-180 Z" />
              <!-- 手臂 (Arms) -->
              <path d="M -15,-300 L -55,-160 L -45,-155 L -10,-280 Z" />
              <path d="M 15,-300 L 55,-160 L 45,-155 L 10,-280 Z" />
              <!-- 手 (Hands) -->
              <circle cx="-50" cy="-150" r="8" />
              <circle cx="50" cy="-150" r="8" />
              <!-- 脖子 (Neck) -->
              <rect x="-8" y="-320" width="16" height="20" />
            </g>
            
            <!-- 下装层 (Lower Body) -->
            <g id="layer-lower">
              <path id="cloth-skirt" class="svg-lower" d="M -25,-180 Q 0,-175 25,-180 L 35,-90 Q 0,-80 -35,-90 Z" fill="#e7e5e4" />
              <path id="cloth-pants" class="svg-lower" style="display:none;" d="M -25,-180 L 25,-180 L 35,-30 L 10,-30 L 0,-120 L -10,-30 L -35,-30 Z" fill="#e7e5e4" />
            </g>

            <!-- 上装层 (Upper Body) -->
            <g id="layer-upper">
              <!-- T恤 -->
              <g id="cloth-tshirt" class="svg-upper">
                <path d="M -25,-180 Q 0,-175 25,-180 L 20,-300 Q 0,-280 -20,-300 Z" fill="#6366f1" />
                <path d="M -15,-300 L -45,-240 L -35,-230 L -10,-280 Z" fill="#6366f1" />
                <path d="M 15,-300 L 45,-240 L 35,-230 L 10,-280 Z" fill="#6366f1" />
              </g>
              <!-- 毛衣 -->
              <g id="cloth-sweater" class="svg-upper" style="display:none;">
                <path d="M -30,-185 Q 0,-175 30,-185 Q 35,-240 25,-305 Q 0,-290 -25,-305 Q -35,-240 -30,-185 Z" fill="#6366f1" />
                <path d="M -25,-305 L -65,-180 L -50,-170 L -15,-270 Z" fill="#6366f1" />
                <path d="M 25,-305 L 65,-180 L 50,-170 L 15,-270 Z" fill="#6366f1" />
                <path d="M -12,-305 Q 0,-295 12,-305 L 10,-315 Q 0,-305 -10,-315 Z" fill="#6366f1" />
              </g>
            </g>

            <!-- 脸部 (Face) -->
            <ellipse cx="0" cy="-345" rx="30" ry="38" fill="#fcdbb5" />
            <!-- 眼睛 -->
            <circle cx="-12" cy="-350" r="2.5" fill="#3a3a3a" />
            <circle cx="12" cy="-350" r="2.5" fill="#3a3a3a" />
            <!-- 嘴巴 -->
            <path d="M -6,-335 Q 0,-325 6,-335" fill="none" stroke="#d49a89" stroke-width="2" stroke-linecap="round" />
            <!-- 腮红 -->
            <ellipse cx="-20" cy="-340" rx="5" ry="3" fill="#ffb6c1" opacity="0.6" />
            <ellipse cx="20" cy="-340" rx="5" ry="3" fill="#ffb6c1" opacity="0.6" />

            <!-- 前发刘海 (Front Bangs) -->
            <path d="M -35,-350 Q -25,-390 0,-390 Q 25,-390 35,-350 Q 20,-365 0,-360 Q -20,-365 -35,-350 Z" fill="#2d2d2d" />

            <!-- 配饰层 (Accessories) -->
            <g id="layer-acc">
              <!-- 项链 -->
              <g id="acc-necklace">
                <path d="M -12,-300 Q 0,-275 12,-300" fill="none" stroke="#e7e5e4" stroke-width="2" class="svg-acc-stroke" />
                <circle cx="0" cy="-286" r="4" fill="#e7e5e4" class="svg-acc-fill" />
              </g>
              <!-- 手表 -->
              <g id="acc-watch" style="display:none;">
                <path d="M -52,-175 L -45,-170 L -48,-165 L -55,-170 Z" fill="#3a3a3a" />
                <circle cx="-50" cy="-170" r="3.5" fill="#e7e5e4" class="svg-acc-fill" />
              </g>
              <!-- 帽子 -->
              <g id="acc-hat" style="display:none;">
                <path d="M -45,-370 Q 0,-400 45,-370 L 40,-380 Q 0,-420 -40,-380 Z" fill="#e7e5e4" class="svg-acc-fill" />
                <path d="M -30,-380 Q 0,-440 30,-380 Z" fill="#e7e5e4" class="svg-acc-fill" />
                <path d="M -28,-380 Q 0,-370 28,-380 L 25,-390 Q 0,-380 -25,-390 Z" fill="rgba(0,0,0,0.2)" />
              </g>
            </g>
          </g>
"""

content = content.replace("<!-- SVG content goes here (to be filled in task 2) -->", svg_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SVG content inserted successfully.")
