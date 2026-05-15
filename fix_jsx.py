file_path = 'app/page.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The exact fade string injected
fade_str = '\n      {/* Section Fade */}\n      <div className="w-full h-[100px] bg-gradient-to-b from-transparent via-[rgba(0,229,255,0.03)] to-transparent pointer-events-none" />\n'
content = content.replace(fade_str, '')

# Add fade safely inside main return block instead (after each section, except last), wait I'll just remove them to get the site running perfectly now. Fades can be added later if needed.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed bad JSX")
