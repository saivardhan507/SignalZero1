import re

filepath = "app/page.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

mobile_menu_replacement = """
      {/* Mobile Menu */}
      <AnimatePresence>
        {menuOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: '100vh' }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden absolute top-full left-0 w-full bg-[#050810] shadow-[0_10px_30px_rgba(0,0,0,0.5)] overflow-y-auto z-[9999] pointer-events-auto"
          >
            <div className="px-6 py-8 flex flex-col gap-2">
              {links.map((link) => (
                <a 
                  key={link.href} 
                  href={link.href} 
                  onClick={() => setMenuOpen(false)}
                  onTouchEnd={() => setMenuOpen(false)}
                  className="block w-full py-4 text-gray-300 hover:text-[var(--accent-primary)] text-lg font-bold tracking-widest uppercase transition-colors cursor-pointer"
                  style={{ minHeight: '48px', WebkitTapHighlightColor: 'rgba(0,229,255,0.2)' }}
                >
                  {link.label}
                </a>
              ))}
              <a 
                href="#discovery" 
                onClick={() => setMenuOpen(false)} 
                onTouchEnd={() => setMenuOpen(false)}
                className="mt-6 block w-full cursor-pointer"
                style={{ WebkitTapHighlightColor: 'rgba(0,229,255,0.2)' }}
              >
                <Button className="w-full bg-[var(--accent-primary)] text-[var(--bg-base)] hover:bg-[var(--accent-primary)] font-bold py-6 rounded-full text-lg transition-all duration-300 hover:shadow-[0_0_18px_rgba(0,245,255,0.5)] pointer-events-none">
                  Start a Project <ArrowRight className="w-5 h-5 ml-2" />
                </Button>
              </a>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
"""

# Find and replace the Mobile Menu block
content = re.sub(
    r'\{\/\*\s*Mobile Menu\s*\*\/\}\s*<AnimatePresence>.*?</AnimatePresence>',
    mobile_menu_replacement.strip(),
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Mobile Menu layout and interactions.")
