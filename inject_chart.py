import re

filepath = "app/page.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add useReducedMotion to framer-motion imports
content = content.replace(
    "import { motion, useInView, AnimatePresence, useScroll, useTransform, useSpring } from 'framer-motion';",
    "import { motion, useInView, AnimatePresence, useScroll, useTransform, useSpring, useReducedMotion } from 'framer-motion';"
)

injection = """
// ===== CUSTOM RECHARTS ANIMATED COMPONENTS =====
const CustomBarShape = (props) => {
  const { x, y, width, height, fill, index, isCyan } = props;
  const reducedMotion = useReducedMotion();
  const delay = reducedMotion ? 0 : index * 0.12 + (isCyan ? 0.15 : 0);
  const duration = reducedMotion ? 0 : (isCyan ? 1.2 : 1.0);
  
  if (width == null || height == null || x == null || y == null) return null;

  return (
    <motion.path
      d={`M${x},${y+height} L${x+width},${y+height} L${x+width},${y} L${x},${y} Z`}
      fill={fill}
      initial={{ scaleY: 0, originY: 1 }}
      animate={{ scaleY: 1 }}
      transition={{ duration, delay, ease: [0.16, 1, 0.3, 1] }}
      style={{
        filter: isCyan && !reducedMotion ? 'drop-shadow(0 0 12px rgba(0,229,255,0.4))' : 'none',
        transformOrigin: "bottom"
      }}
    />
  );
};

function AnimatedEfficiencyChart({ cs }) {
  const containerRef = useRef(null);
  const inView = useInView(containerRef, { amount: 0.2, margin: "0px 0px -10% 0px" });
  const reducedMotion = useReducedMotion();
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start end', 'end start']
  });
  
  // Subtle vertical parallax (max 30px offset) mapping scrolled state to Y
  const parallaxY = useTransform(scrollYProgress, [0, 1], [30, 0]);
  const yOffset = reducedMotion ? 0 : parallaxY;

  return (
    <motion.div
      ref={containerRef}
      style={{ y: yOffset, willChange: 'transform' }}
      className="w-full relative"
    >
      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={cs.data} key={inView ? 'active' : 'reset'}>
          <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
          <XAxis dataKey="source" stroke="#64748b" fontSize={11} />
          <YAxis stroke="#64748b" fontSize={12} label={{ value: 'Minutes', angle: -90, position: 'insideLeft', fill: '#64748b', fontSize: 11 }} />
          <Tooltip contentStyle={{ background: 'rgba(26, 26, 46, 0.8)', backdropFilter: 'blur(8px)', border: '1px solid rgba(0,240,255,0.5)', borderRadius: '12px', color: '#e2e8f0', boxShadow: '0 0 20px rgba(0,240,255,0.3), inset 0 0 20px rgba(0,240,255,0.1)' }} cursor={{ fill: 'rgba(255,255,255,0.05)' }} />
          <Bar dataKey="before" fill="#475569" radius={[4, 4, 0, 0]} name="Before" shape={(props) => <CustomBarShape {...props} isCyan={false} />} isAnimationActive={false} />
          <Bar dataKey="after" fill="var(--accent-primary)" radius={[4, 4, 0, 0]} name="After" shape={(props) => <CustomBarShape {...props} isCyan={true} />} isAnimationActive={false} />
        </BarChart>
      </ResponsiveContainer>
    </motion.div>
  );
}
"""

content = content.replace("// ===== CONSTANTS =====", injection + "\n// ===== CONSTANTS =====")

# Replace the previous BarChart render block targeting cs.chartType === 'bar' (lines ~1222-1243)
# We will use regex to capture the specific if (cs.chartType === 'bar') { ... } block

pattern = re.compile(r"if\s*\(cs\.chartType\s*===\s*'bar'\)\s*\{[\s\S]*?return\s*\([\s\S]*?<\/motion\.div>\s*\);\s*\}", re.DOTALL)
replacement = """if (cs.chartType === 'bar') {
      return <AnimatedEfficiencyChart cs={cs} />;
    }"""

content = pattern.sub(replacement, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected AnimatedEfficiencyChart.")
