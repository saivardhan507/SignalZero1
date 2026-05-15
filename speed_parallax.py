import re

filepath = "app/page.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace transition speeds for SVG Paths
content = content.replace("transition={{ duration: 0.8, delay: 1 * 0.3 }}", "transition={{ duration: 0.4, delay: 1 * 0.15 }}")
content = content.replace("transition={{ duration: 0.8, delay: 2 * 0.3 }}", "transition={{ duration: 0.4, delay: 2 * 0.15 }}")
content = content.replace("transition={{ duration: 1.2, delay: 3 * 0.3 }}", "transition={{ duration: 0.6, delay: 3 * 0.15 }}")
content = content.replace("transition={{ duration: 0.8, delay: 4 * 0.3 }}", "transition={{ duration: 0.4, delay: 4 * 0.15 }}")
content = content.replace("transition={{ duration: 0.8, delay: 5 * 0.3 }}", "transition={{ duration: 0.4, delay: 5 * 0.15 }}")

# Replace transition speed for Cards
content = content.replace("transition={{ duration: 0.6, delay: step.id * 0.3 }}", "transition={{ duration: 0.4, delay: step.id * 0.15 }}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Timing updated.")
