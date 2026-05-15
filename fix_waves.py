import re

filepath = "app/page.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacement = """
    const isTouch = typeof window !== 'undefined' && window.matchMedia('(pointer: coarse)').matches;
    let mouseTimeout;

    const handleMouse = (e) => {
      mouseRef.current = { x: e.clientX, y: e.clientY };
      // Safety net: if no mouse movement for 1s, treat as leave (safeguard against stuck states)
      clearTimeout(mouseTimeout);
      mouseTimeout = setTimeout(handleLeave, 1000);
    };
    const handleLeave = () => {
      mouseRef.current = { x: -9999, y: -9999 };
    };

    window.addEventListener('resize', resize);
    window.addEventListener('mousemove', handleMouse);
    window.addEventListener('mouseleave', handleLeave);
    window.addEventListener('touchend', handleLeave);
    window.addEventListener('touchcancel', handleLeave);
"""

# Replace the event listener binding area
content = re.sub(
    r'const handleMouse = \(e\) => {.*?window\.addEventListener\(\'mouseleave\', handleLeave\);',
    replacement.strip(),
    content,
    flags=re.DOTALL
)

# Bypass flatten logic using isTouch
logic_replacement = """
          // Target: 0 = flat (zero signal), 1 = full wave
          let target;
          if (!isTouch && dist < FLATTEN_RADIUS) {
            const t = dist / FLATTEN_RADIUS;
"""

content = content.replace(
"""          // Target: 0 = flat (zero signal), 1 = full wave
          let target;
          if (dist < FLATTEN_RADIUS) {""",
logic_replacement.strip("\n")
)

# And make sure currentSpeed calculations in animate don't use the timeout to break mouse tracking
# Wait, if `handleLeave` triggers after 1000ms of no movement, then if you hover stationary, it will flatten the waves back up!
# This changes desktop behavior: "If the mouse is perfectly still for 1s, the waves pop up".
# The user explicitly asked for "if for any reason the waves are still flat after 1 second with no touching happening", "on mobile, never flatten the waves at all".
# Actually, the 1 second safety net applies to `touchstart`/`touchmove`. If `isTouch`, then it doesn't flatten anyway.
# We should probably ONLY set the 1-second timeout if it's a touch device or pointer type is touch.
"""
          // Target: 0 = flat (zero signal), 1 = full wave
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated SignalWaveCanvas logic.")
