import re

filepath = "app/page.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

counter_injection = """
const AnimatedCounter = ({ value }) => {
  const [count, setCount] = useState(0);
  const ref = useRef(null);
  const inView = useInView(ref, { once: true, amount: 0.5 });
  const reducedMotion = useReducedMotion();

  // Extract number and suffix ("50+" -> num: 50, suffix: "+", "100%" -> num: 100, suffix: "%")
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
      let animationFrame;
      const duration = 1200; // 1.2s
      const startTime = performance.now();
      
      const step = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeProgress = 1 - Math.pow(1 - progress, 4); // easeOutQuart
        setCount(Math.floor(easeProgress * targetNum));
        
        if (progress < 1) {
          animationFrame = requestAnimationFrame(step);
        } else {
          setCount(targetNum);
        }
      };
      animationFrame = requestAnimationFrame(step);
      return () => cancelAnimationFrame(animationFrame);
    }
  }, [inView, targetNum, reducedMotion]);

  return <div ref={ref} className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight mb-1 tabular-nums">{count}{suffix}</div>;
};
"""

content = content.replace("const AnimatedYAxisTick = ({ x, y, payload, inView, reducedMotion }) => {", counter_injection + "\nconst AnimatedYAxisTick = ({ x, y, payload, inView, reducedMotion }) => {")

pattern = re.compile(r"<div className=\"text-3xl sm:text-4xl font-extrabold text-white tracking-tight mb-1 tabular-nums\">\{stat\.value\}<\/div>")
replacement = "<AnimatedCounter value={stat.value} />"
content = pattern.sub(replacement, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected AnimatedCounter.")
