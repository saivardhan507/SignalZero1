import re

filepath = "app/page.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

tick_injection = """
const AnimatedYAxisTick = ({ x, y, payload, inView, reducedMotion }) => {
  const [val, setVal] = useState(0);
  useEffect(() => {
    if (reducedMotion) {
      setVal(payload.value);
      return;
    }
    if (inView) {
      let animationFrame;
      const end = payload.value;
      const duration = 1200;
      const startTime = performance.now();
      
      const step = (currentTime) => {
        const elapsed = currentTime - startTime;
        // EaseOutQuart approximation
        const progress = Math.min(elapsed / duration, 1);
        const easeProgress = 1 - Math.pow(1 - progress, 4);
        setVal(Math.floor(easeProgress * end));
        if (progress < 1) {
          animationFrame = requestAnimationFrame(step);
        }
      };
      animationFrame = requestAnimationFrame(step);
      return () => cancelAnimationFrame(animationFrame);
    } else {
      setVal(0);
    }
  }, [inView, payload.value, reducedMotion]);

  return <text x={x} y={y} dy={4} textAnchor="end" fill="#64748b" fontSize={11}>{val}</text>;
};
"""

content = content.replace("const CustomBarShape = (props) => {", tick_injection + "\nconst CustomBarShape = (props) => {")

# Update AnimatedEfficiencyChart YAxis to use tick
yAxisPattern = re.compile(r"<YAxis stroke=\"#64748b\" fontSize=\{12\}.*?\/>")
replacement = "<YAxis stroke=\"#64748b\" fontSize={12} tick={(props) => <AnimatedYAxisTick {...props} inView={inView} reducedMotion={reducedMotion} />} label={{ value: 'Minutes', angle: -90, position: 'insideLeft', fill: '#64748b', fontSize: 11 }} />"
content = yAxisPattern.sub(replacement, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected AnimatedYAxisTick.")
