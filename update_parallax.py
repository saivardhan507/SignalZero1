import re

filepath = "app/page.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the <div className="hidden md:block absolute inset-0 pointer-events-none overflow-visible" style={{ zIndex: 0 }}> ... </div> chunk.

pattern = re.compile(r'<div className="hidden md:block absolute inset-0 pointer-events-none overflow-visible" style=\{\{ zIndex: 0 \}\}>.*?</svg>\s*</div>', re.DOTALL)

replacement = """<div className="hidden md:block absolute inset-0 pointer-events-none overflow-visible" style={{ zIndex: 0 }}>
            <svg className="w-full h-full overflow-visible pointer-events-none" viewBox="0 0 1080 600" preserveAspectRatio="none">
              <defs>
                <linearGradient id="g1-2"><stop offset="0%" stopColor={steps[0].color}/><stop offset="100%" stopColor={steps[1].color}/></linearGradient>
                <linearGradient id="g2-3"><stop offset="0%" stopColor={steps[1].color}/><stop offset="100%" stopColor={steps[2].color}/></linearGradient>
                <linearGradient id="g3-4"><stop offset="0%" stopColor={steps[2].color}/><stop offset="100%" stopColor={steps[3].color}/></linearGradient>
                <linearGradient id="g4-5"><stop offset="0%" stopColor={steps[3].color}/><stop offset="100%" stopColor={steps[4].color}/></linearGradient>
                <linearGradient id="g5-6"><stop offset="0%" stopColor={steps[4].color}/><stop offset="100%" stopColor={steps[5].color}/></linearGradient>

                {/* SVG Masks for "Drawing" the paths that contain natively scrolling CSS dashes */}
                <mask id="mask1">
                  <motion.path d="M 328 140 C 344 160, 360 120, 376 140" stroke="white" strokeWidth="8" fill="none"
                               initial={{ pathLength: 0 }} whileInView={{ pathLength: 1 }} viewport={{ once: false, margin: '-20%' }} transition={{ duration: 0.8, delay: 1 * 0.3 }} />
                </mask>
                <mask id="mask2">
                  <motion.path d="M 704 140 C 720 160, 736 120, 752 140" stroke="white" strokeWidth="8" fill="none"
                               initial={{ pathLength: 0 }} whileInView={{ pathLength: 1 }} viewport={{ once: false, margin: '-20%' }} transition={{ duration: 0.8, delay: 2 * 0.3 }} />
                </mask>
                <mask id="mask3">
                  <motion.path d="M 1080 140 C 1160 140, 1160 468, 1080 468" stroke="white" strokeWidth="8" fill="none"
                               initial={{ pathLength: 0 }} whileInView={{ pathLength: 1 }} viewport={{ once: false, margin: '-20%' }} transition={{ duration: 1.2, delay: 3 * 0.3 }} />
                </mask>
                <mask id="mask4">
                  <motion.path d="M 752 468 C 736 488, 720 448, 704 468" stroke="white" strokeWidth="8" fill="none"
                               initial={{ pathLength: 0 }} whileInView={{ pathLength: 1 }} viewport={{ once: false, margin: '-20%' }} transition={{ duration: 0.8, delay: 4 * 0.3 }} />
                </mask>
                <mask id="mask5">
                  <motion.path d="M 376 468 C 360 488, 344 448, 328 468" stroke="white" strokeWidth="8" fill="none"
                               initial={{ pathLength: 0 }} whileInView={{ pathLength: 1 }} viewport={{ once: false, margin: '-20%' }} transition={{ duration: 0.8, delay: 5 * 0.3 }} />
                </mask>
              </defs>

              {/* Infinitely Scrolling Dashed Paths tied to the expanding Masks */}
              <path d="M 328 140 C 344 160, 360 120, 376 140" stroke="url(#g1-2)" className="process-connector" mask="url(#mask1)" />
              <path d="M 704 140 C 720 160, 736 120, 752 140" stroke="url(#g2-3)" className="process-connector" mask="url(#mask2)" />
              <path d="M 1080 140 C 1160 140, 1160 468, 1080 468" stroke="url(#g3-4)" className="process-connector" mask="url(#mask3)" />
              <path d="M 752 468 C 736 488, 720 448, 704 468" stroke="url(#g4-5)" className="process-connector" mask="url(#mask4)" />
              <path d="M 376 468 C 360 488, 344 448, 328 468" stroke="url(#g5-6)" className="process-connector" mask="url(#mask5)" />
            </svg>
          </div>"""

new_content = pattern.sub(replacement, content)

# I will also update the Cards' viewport settings because '-50px' margin might be triggering inconsistently. Changing to '-20%'. 
card_pattern = re.compile(r'viewport=\{\{ once: false, margin: \'-50px\' \}\}')
new_content = card_pattern.sub(r"viewport={{ once: false, margin: '-20%' }}", new_content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Rewrite perfect.")
