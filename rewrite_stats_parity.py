import re

filepath = "app/page.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update AnimatedCounter
counter_injection = """
const AnimatedCounter = ({ value, delay }) => {
  const [count, setCount] = useState(0);
  const [glow, setGlow] = useState(false);
  const ref = useRef(null);
  const inView = useInView(ref, { once: false, amount: 0.3 });
  const reducedMotion = useReducedMotion();

  const numMatch = value.match(/\\d+/);
  const suffixMatch = value.match(/\\D+$/);
  const targetNum = numMatch ? parseInt(numMatch[0]) : 0;
  const suffix = suffixMatch ? suffixMatch[0] : '';

  useEffect(() => {
    if (reducedMotion) {
      setCount(targetNum);
      return;
    }
    if (inView) {
      setGlow(false);
      let animationFrame;
      const duration = 1800;
      const startTime = performance.now() + delay * 1000;
      
      const step = (currentTime) => {
        if (currentTime < startTime) {
          animationFrame = requestAnimationFrame(step);
          return;
        }
        
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeProgress = 1 - Math.pow(2, -10 * progress);
        setCount(Math.floor(easeProgress * targetNum));
        
        if (progress < 1) {
          animationFrame = requestAnimationFrame(step);
        } else {
          setCount(targetNum);
          setGlow(true);
          setTimeout(() => setGlow(false), 600);
        }
      };
      animationFrame = requestAnimationFrame(step);
      return () => cancelAnimationFrame(animationFrame);
    } else {
      setCount(0);
    }
  }, [inView, targetNum, reducedMotion, delay]);

  return (
    <div 
      ref={ref} 
      className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight mb-1 tabular-nums transition-shadow duration-300"
      style={{ textShadow: glow ? '0 0 20px rgba(0,229,255,0.8)' : '0 0 0px transparent' }}
    >
      {count}{suffix}
    </div>
  );
};
"""

content = re.sub(r'const AnimatedCounter\s*=\s*\(\{\s*value\s*\}\)\s*=>\s*\{.*?\n\s*return\s*<div[^>]*>\{count\}\{suffix\}<\/div>;\n};', counter_injection.strip(), content, flags=re.DOTALL)


# 2. Update HeroSection grid loop to use whileInView and parallax
grid_replacement = """
        {/* Bento Grid Stats */}
        <motion.div 
          className="mt-16 lg:mt-24 grid grid-cols-2 lg:grid-cols-4 gap-4 max-w-5xl w-full mx-auto pointer-events-auto relative z-10 px-2 lg:px-0"
          style={{ y: useTransform(scrollY, [0, 800], [0, -40]), willChange: 'transform' }}
        >
          {statsData.map((stat, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: false, amount: 0.3 }}
              transition={{ duration: 0.6, delay: i * 0.1, ease: [0.25, 0.46, 0.45, 0.94] }}
              className="glass p-6 sm:p-7 transition-all duration-500 group relative overflow-hidden text-left"
            >
              <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-b from-[var(--accent-glow)]/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none" />
              <div className="flex items-center gap-3 mb-4">
                <motion.div 
                  initial={{ scale: 0.6 }}
                  whileInView={{ scale: 1 }}
                  viewport={{ once: false, amount: 0.5 }}
                  transition={{ duration: 0.4, delay: i * 0.1, ease: [0.34, 1.56, 0.64, 1] }}
                  className="p-2.5 rounded-xl bg-white/5 border border-white/10 group-hover:border-[var(--accent-glow)]/30 transition-colors duration-300"
                >
                  <stat.icon className="w-5 h-5 text-[var(--accent-glow)]" />
                </motion.div>
              </div>
              <AnimatedCounter value={stat.value} delay={i * 0.15} />
              <div className="text-[10px] sm:text-[11px] text-zinc-400 tracking-[0.2em] font-medium uppercase">{stat.label}</div>
            </motion.div>
          ))}
        </motion.div>
"""

content = re.sub(
    r'\{\/\*\s*Bento Grid Stats\s*\*\/\}\s*<div className="mt-16 lg:mt-24 grid.*?(?=\{\/\*\s*Scroll indicator\s*\*\/\})',
    grid_replacement,
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated AnimatedCounter and Hero grid interactions.")
