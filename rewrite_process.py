import re

filepath = "app/page.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacement = """// ===== OUR PROCESS SECTION - PREMIUM TIMELINE =====
function OurProcessSection() {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start end', 'end start']
  });

  const sectionScale = useTransform(scrollYProgress, [0, 0.5, 1], [0.82, 1, 0.92]);
  const sectionOpacity = useTransform(scrollYProgress, [0, 0.25, 0.75, 1], [0.35, 1, 1, 0.5]);
  const sectionY = useTransform(scrollYProgress, [0, 0.5, 1], [80, 0, -80]);

  const steps = [
    {
      id: 1, title: 'Ideation', description: 'We brainstorm and refine your concept.', color: '#00e5ff',
      icon: <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path strokeLinecap="round" strokeLinejoin="round" d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/><circle cx="12" cy="12" r="4"/></svg>
    },
    {
      id: 2, title: 'Scope', description: 'Defining clear requirements and roadmap.', color: '#a855f7',
      icon: <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
    },
    {
      id: 3, title: 'Design', description: 'Creating intuitive and beautiful interfaces.', color: '#f43f8e',
      icon: <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path strokeLinecap="round" strokeLinejoin="round" d="M12 20.94c1.88 0 3.05-1.04 3.05-2.08 0-1.1-1.12-1.48-1.57-2.67a5 5 0 0 1-4.14-7.58c.24-.4.8-1.3 1.14-1.63a7.41 7.41 0 0 0-1.52-5 9.87 9.87 0 0 0-4.43 2.5 10.4 10.4 0 0 0-2.45 4.5 10.13 10.13 0 0 0 3.23 9.4 14.52 14.52 0 0 0 6.69 2.56z"/><circle cx="6.5" cy="5.5" r=".5"/><circle cx="10" cy="4" r=".5"/><circle cx="13.5" cy="6.5" r=".5"/><circle cx="15.5" cy="10" r=".5"/><circle cx="16" cy="14" r=".5"/></svg>
    },
    {
      id: 4, title: 'Development', description: 'Clean coding with scalable architecture.', color: '#00d68f',
      icon: <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path strokeLinecap="round" strokeLinejoin="round" d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/><circle cx="12" cy="12" r="3"/></svg>
    },
    {
      id: 5, title: 'Delivery', description: 'Rigorous testing and smooth launch.', color: '#f59e0b',
      icon: <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path strokeLinecap="round" strokeLinejoin="round" d="M13.5 10.5 21 3M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.71-2.13.09-3.09a3 3 0 0 0-3.09.09zM12 15l9 3 3-3-3-9-15-3-3 3 3 9z"/></svg>
    },
    {
      id: 6, title: 'Support', description: 'Ongoing maintenance and improvements.', color: '#3b82f6',
      icon: <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path strokeLinecap="round" strokeLinejoin="round" d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg>
    }
  ];

  return (
    <motion.section
      ref={containerRef}
      style={{ scale: sectionScale, opacity: sectionOpacity, y: sectionY }}
      className="py-10 sm:py-20 px-[20px] md:px-[60px]"
    >
      <div className="glass rounded-[40px] px-5 py-10 md:p-[60px] border border-white/5 overflow-hidden mx-auto max-w-[1200px] w-full flex flex-col relative">
        
        {/* Header */}
        <div className="text-center mb-16 relative z-10 mx-auto max-w-2xl">
          <h3 className="text-[11px] font-mono font-bold text-[var(--accent-primary)] mb-4" style={{ letterSpacing: '0.2em', textShadow: "0 0 20px rgba(0,240,255,0.4)" }}>
            HOW WE WORK
          </h3>
          <h2 className="text-[28px] sm:text-[36px] md:text-[46px] font-extrabold text-[#f0f4ff] mb-6 tracking-tight">
            The Signal Zero Process
          </h2>
          <p className="text-[#8892a4] text-[16px] leading-[1.7]">Six orchestrated steps connecting your concept to a thriving product.</p>
        </div>

        <style dangerouslySetInnerHTML={{__html: `
          @keyframes dashMove {
            to { stroke-dashoffset: -100; }
          }
          .process-connector {
            stroke-dasharray: 8 6;
            animation: dashMove 2s linear infinite;
            stroke-width: 2;
            fill: none;
            opacity: 0.7;
          }
          .card-hover-effect {
            transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
          }
          .card-hover-effect:hover {
            transform: translateY(-4px);
            border-color: var(--hover-border) !important;
            box-shadow: var(--hover-shadow) !important;
          }
        `}} />

        {/* Global Wrapper for SVG and Grid */}
        <div className="relative w-full z-10">
          
          {/* Desktop SVG Overlay */}
          <div className="hidden md:block absolute inset-0 pointer-events-none overflow-visible" style={{ zIndex: 0 }}>
            <svg className="w-full h-full overflow-visible pointer-events-none" viewBox="0 0 1080 600" preserveAspectRatio="none">
              <defs>
                <linearGradient id="g1-2"><stop offset="0%" stopColor={steps[0].color}/><stop offset="100%" stopColor={steps[1].color}/></linearGradient>
                <linearGradient id="g2-3"><stop offset="0%" stopColor={steps[1].color}/><stop offset="100%" stopColor={steps[2].color}/></linearGradient>
                <linearGradient id="g3-4"><stop offset="0%" stopColor={steps[2].color}/><stop offset="100%" stopColor={steps[3].color}/></linearGradient>
                <linearGradient id="g4-5"><stop offset="0%" stopColor={steps[3].color}/><stop offset="100%" stopColor={steps[4].color}/></linearGradient>
                <linearGradient id="g5-6"><stop offset="0%" stopColor={steps[4].color}/><stop offset="100%" stopColor={steps[5].color}/></linearGradient>
              </defs>
              <path d="M 172 64 C 264 100, 448 20, 540 64" stroke="url(#g1-2)" className="process-connector" />
              <path d="M 540 64 C 632 100, 816 20, 908 64" stroke="url(#g2-3)" className="process-connector" />
              <path d="M 908 64 C 1050 150, 1050 300, 908 392" stroke="url(#g3-4)" className="process-connector" />
              <path d="M 908 392 C 816 430, 632 350, 540 392" stroke="url(#g4-5)" className="process-connector" />
              <path d="M 540 392 C 448 430, 264 350, 172 392" stroke="url(#g5-6)" className="process-connector" />
            </svg>
          </div>

          {/* Core Grid */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-y-[48px] md:gap-x-[24px] md:gap-y-[48px] w-full relative z-10">
            {steps.map((step) => {
              // Custom grid positions for snake flow
              const isCol3Row2 = step.id === 4;
              const isCol2Row2 = step.id === 5;
              const isCol1Row2 = step.id === 6;
              const gridPlaceClasses = isCol3Row2 ? "md:col-start-3 md:row-start-2" : 
                                       isCol2Row2 ? "md:col-start-2 md:row-start-2" : 
                                       isCol1Row2 ? "md:col-start-1 md:row-start-2" : "";
              
              const isActive = step.id === 1;

              return (
                <div key={step.id} className={`w-full ${gridPlaceClasses}`}
                     style={{ 
                       '--hover-border': `${step.color}66`,
                       '--hover-shadow': `0 0 40px ${step.color}66`
                     }}>
                  {/* Card */}
                  <div
                    className={`card-hover-effect relative flex flex-col items-start p-8 rounded-[20px] ${isActive ? 'bg-[rgba(255,255,255,0.06)] border-[rgba(255,255,255,0.7)] shadow-[0_0_40px_rgba(255,255,255,0.08)]' : 'bg-[rgba(255,255,255,0.03)] border-[rgba(255,255,255,0.08)]'}`}
                    style={{ minHeight: '280px', borderStyle: 'solid', borderWidth: '1px' }}
                  >
                    <div className="w-[64px] h-[64px] rounded-full flex items-center justify-center self-center mb-6 relative z-10"
                         style={{ 
                           border: `2px solid ${step.color}`,
                           background: `${step.color}1a`
                         }}>
                      <div style={{ color: step.color }}>
                        {step.icon}
                      </div>
                    </div>
                    
                    <div className="w-full relative z-10 text-center md:text-left">
                      <div className="font-mono font-bold uppercase mb-2"
                           style={{ letterSpacing: '0.2em', fontSize: '11px', color: step.color, opacity: 0.8 }}>
                        STEP {step.id}
                      </div>
                      <h4 className="text-[22px] font-bold text-[#f0f4ff] mb-2 leading-tight">
                        {step.title}
                      </h4>
                      <p className="text-[14px] leading-[1.7] text-[#8892a4]">
                        {step.description}
                      </p>
                    </div>

                    {/* Mobile Only Dashboard Dashed line */}
                    {step.id !== 6 && (
                      <div className="md:hidden absolute w-[2px] h-12 left-1/2 -bottom-[50px] -translate-x-1/2 border-l-2 border-dashed z-0"
                           style={{ borderColor: step.color, opacity: 0.5 }} />
                    )}
                  </div>
                </div>
              );
            })}
          </div>

        </div>
      </div>
    </motion.section>
  );
}"""

# Perform replacement utilizing regex to handle the chunk precisely
pattern = re.compile(r'// ===== OUR PROCESS SECTION - PREMIUM TIMELINE =====\nfunction OurProcessSection\(\) \{.*?\n\}\n', re.DOTALL)
new_content = pattern.sub(replacement + '\n', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replacement successful")
