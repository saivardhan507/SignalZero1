import re

file_path = 'app/page.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Colors replacement
color_map = {
    r'#0a0f1e': 'var(--bg-base)',
    r'#00f0ff': 'var(--accent-primary)',
    r'#00f5ff': 'var(--accent-primary)',
    r'#00ffcc': 'var(--accent-primary)',
    r'139, 92, 246': '123, 47, 255', # #8b5cf6 -> #7b2fff in rgba
    r'#8b5cf6': 'var(--accent-secondary)',
    r'#a855f7': 'var(--accent-secondary)',
    r'#00ff80': 'var(--accent-glow)',
    r'#36d6a5': 'var(--accent-glow)',
    r'#00e673': 'var(--accent-glow)',
    r'0, 240, 255': '0, 229, 255',
    r'0, 245, 255': '0, 229, 255',
    r'0, 255, 127': '0, 245, 196',
    r'border-[#00f5ff]/12': 'border-[var(--border-subtle)]',
    r'border-[#00ff80]/40': 'border-[var(--border-active)]',
    r'text-white font-bold text-lg tracking-widest': 'text-[var(--text-primary)] font-bold text-lg tracking-widest',
    r'neon-text text-\[var\(--accent-primary\)\] drop-shadow-\[0_0_30px_rgba\(0,255,204,0.4\)\]': 'neon-text text-[var(--accent-primary)] drop-shadow-[0_0_40px_rgba(0,229,255,0.4)]',
}

for old, new in color_map.items():
    content = re.sub(old, new, content)

# 2. Section Headings specific rules
# Replace "ZERO" hero
content = re.sub(
    r'className="neon-text text-\[\#00ffcc\] drop-shadow-\[0_0_30px_rgba\(0,255,204,0.4\)\]"',
    r'className="text-[var(--accent-primary)] [text-shadow:0_0_40px_rgba(0,229,255,0.4)]"',
    content
)

content = re.sub(
    r'className="neon-text-white text-white drop-shadow-\[0_0_20px_rgba\(255,255,255,0.15\)\]"',
    r'className="text-[var(--text-primary)]"',
    content
)

# Replace common card classes with glass
card_class_patterns = [
    r'bg-white/?\[?0\.03\]? backdrop-blur-xl rounded-2xl border border-white/5 shadow-2xl hover:bg-white/?\[?0\.05\]? hover:border-\[var\(--accent-glow\)\]/40 transition-all duration-500',
    r'bg-white/5 backdrop-blur-md rounded-xl border border-white/10 hover:border-white/20 transition-all duration-300',
    r'bg-\[\#0a0a0f\]/80 backdrop-blur-md rounded-2xl border border-white/5',
    r'bg-white/\[0\.02\] backdrop-blur-md rounded-2xl border border-white/5',
]
for pattern in card_class_patterns:
    content = re.sub(pattern, 'glass', content)

# Add tabular nums to stat values
content = re.sub(
    r'(className="text-[^"]+ font-extrabold text-white tracking-tight mb-1")',
    r'\1 tabular-nums',
    content
)

# Section Fades insertion (regex matching section endings and adding a div fade before the next section)
# We can do this manually for the major sections since they are finite, or let the script inject a Fade block.
# I will just write a function to replace </section> with </section><div className="w-full h-[100px] bg-gradient-to-b from-transparent via-[rgba(0,229,255,0.03)] to-transparent pointer-events-none" /> except the last one.

sections_split = content.split('</section>')
if len(sections_split) > 1:
    fade_div = '\n      {/* Section Fade */}\n      <div className="w-full h-[100px] bg-gradient-to-b from-transparent via-[rgba(0,229,255,0.03)] to-transparent pointer-events-none" />\n'
    content = ('</section>' + fade_div).join(sections_split[:-1]) + '</section>' + sections_split[-1]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Refactored page.js successfully.")
