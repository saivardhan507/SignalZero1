import './globals.css';
import { ThemeProvider } from '@/components/theme-provider';

export const metadata = {
  metadataBase: new URL('https://wearesignalzero.tech'),
  title: {
    default: 'Signal Zero | Integrated AI & Systems Engineering Agency',
    template: '%s | Signal Zero',
  },
  description:
    'Signal Zero is an integrated AI & systems engineering agency. We architect custom AI agents, enterprise RAG pipelines, real-time data, and fintech platforms.',
  keywords: [
    'AI engineering agency',
    'custom AI agents',
    'RAG pipeline development',
    'systems engineering',
    'enterprise data engineering',
    'ETL pipeline automation',
    'real-time analytics',
    'fintech dashboards',
    'cognitive workflow automation',
    'full-stack web platform',
    'WebGL 3D visualization',
    'machine learning consulting',
    'Apache Kafka streaming',
    'Signal Zero',
    'wearesignalzero.tech',
  ],
  authors: [{ name: 'Eppa Sai Vardhan Reddy', url: 'https://www.linkedin.com/in/eppa-sai-vardhan-reddy-5b71213a4' }],
  creator: 'Signal Zero',
  publisher: 'Signal Zero',
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  alternates: {
    canonical: 'https://wearesignalzero.tech',
  },
  openGraph: {
    title: 'Signal Zero | Integrated AI & Systems Engineering Agency',
    description:
      'We engineer intelligent systems that transform raw data into competitive advantage. Production-grade AI agents, real-time data pipelines, and high-performance platforms.',
    url: 'https://wearesignalzero.tech',
    siteName: 'Signal Zero',
    images: [
      {
        url: '/founder.png',
        width: 1200,
        height: 630,
        alt: 'Signal Zero - Integrated AI & Systems Engineering Agency',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Signal Zero | Integrated AI & Systems Engineering Agency',
    description:
      'Production-grade AI agents, automated data pipelines, and real-time systems that drive competitive advantage.',
    images: ['/founder.png'],
    creator: '@SignalZero',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  verification: {
    google: 'wTTahPudOh-Z405wtC4NuMnGLQgMoXni9z2cY9f0dgo',
  },
};

export const viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 5,
};

const jsonLd = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'WebSite',
      '@id': 'https://wearesignalzero.tech/#website',
      url: 'https://wearesignalzero.tech',
      name: 'Signal Zero',
      description: 'Integrated AI & Systems Engineering Agency',
      publisher: {
        '@id': 'https://wearesignalzero.tech/#organization',
      },
      inLanguage: 'en-US',
    },
    {
      '@type': ['Organization', 'ProfessionalService'],
      '@id': 'https://wearesignalzero.tech/#organization',
      name: 'Signal Zero',
      alternateName: 'Signal Zero Technologies',
      url: 'https://wearesignalzero.tech',
      logo: 'https://wearesignalzero.tech/signal-zero-logo.svg',
      image: 'https://wearesignalzero.tech/founder.png',
      description:
        'Signal Zero is an integrated AI and systems engineering agency specializing in custom RAG AI agents, real-time data engineering, algorithmic fintech platforms, and scalable full-stack software.',
      email: 'contact@wearesignalzero.tech',
      telephone: '+91-9347302648',
      priceRange: '$$',
      currenciesAccepted: 'USD, INR, EUR',
      founder: {
        '@id': 'https://wearesignalzero.tech/#founder',
      },
      address: {
        '@type': 'PostalAddress',
        streetAddress: 'HITEC City, Madhapur',
        addressLocality: 'Hyderabad',
        addressRegion: 'Telangana',
        postalCode: '500081',
        addressCountry: 'IN',
      },
      sameAs: [
        'https://www.linkedin.com/in/eppa-sai-vardhan-reddy-5b71213a4',
      ],
      knowsAbout: [
        'Artificial Intelligence',
        'Generative AI',
        'Custom AI Agents',
        'Retrieval-Augmented Generation (RAG)',
        'Enterprise Data Engineering',
        'ETL Automation',
        'Apache Kafka',
        'Apache Spark',
        'FinTech Analytics',
        'Machine Learning',
        'Predictive Modeling',
        'WebGL and 3D Visualizations',
      ],
    },
    {
      '@type': 'Person',
      '@id': 'https://wearesignalzero.tech/#founder',
      name: 'Eppa Sai Vardhan Reddy',
      jobTitle: 'Founder & Chief Architect',
      worksFor: {
        '@id': 'https://wearesignalzero.tech/#organization',
      },
      url: 'https://www.linkedin.com/in/eppa-sai-vardhan-reddy-5b71213a4',
      award: 'NASA Space Settlement Design Contest (World 2nd Prize, 2018)',
      sameAs: [
        'https://www.linkedin.com/in/eppa-sai-vardhan-reddy-5b71213a4',
      ],
      knowsAbout: [
        'Machine Learning',
        'Deep Learning',
        'Natural Language Processing',
        'TensorFlow',
        'Predictive Modeling',
        'Systems Engineering',
      ],
    },
    {
      '@type': 'WebPage',
      '@id': 'https://wearesignalzero.tech/#webpage',
      url: 'https://wearesignalzero.tech',
      name: 'Signal Zero | Integrated AI & Systems Engineering Agency',
      description:
        'We engineer intelligent systems that transform raw data into competitive advantage. Production-grade AI agents, real-time data pipelines, and high-performance platforms.',
      isPartOf: {
        '@id': 'https://wearesignalzero.tech/#website',
      },
      about: {
        '@id': 'https://wearesignalzero.tech/#organization',
      },
      inLanguage: 'en-US',
      speakable: {
        '@type': 'SpeakableSpecification',
        cssSelector: ['h1', 'h2', 'p', '.faq-answer'],
      },
    },
    {
      '@type': 'FAQPage',
      '@id': 'https://wearesignalzero.tech/#faq',
      mainEntity: [
        {
          '@type': 'Question',
          name: 'What is Signal Zero?',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Signal Zero is an integrated AI and systems engineering agency that architects and deploys production-grade custom AI agents, automated ETL pipelines, real-time analytics platforms, and full-stack software for high-growth businesses and startups.',
          },
        },
        {
          '@type': 'Question',
          name: 'What engineering services does Signal Zero offer?',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Signal Zero provides 6 core engineering capabilities: (1) Custom AI Agents & RAG Pipelines with vector databases, (2) Enterprise Data Engineering & ETL Automation with Apache Spark and Kafka, (3) FinTech & Algorithmic Dashboards with sub-second latency, (4) Cognitive Workflow Automation (OCR/NLP), (5) Full-Stack Web Platforms (Next.js/React), and (6) Interactive 3D WebGL Visualizations.',
          },
        },
        {
          '@type': 'Question',
          name: 'What performance benchmarks and results has Signal Zero delivered?',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Across 50+ delivered projects with a 100% delivery rate, Signal Zero has achieved an 84% directional accuracy on real-time stock prediction (<200ms latency), a 70% reduction in ETL data processing time unifying 12 disparate data sources with 99.8% data accuracy, and a 96% answer relevance rate indexing 10,000+ medical documents with HIPAA compliance.',
          },
        },
        {
          '@type': 'Question',
          name: 'Who leads engineering at Signal Zero?',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Signal Zero is led by Founder & Chief Architect Eppa Sai Vardhan Reddy, a NASA Space Settlement World 2nd Prize awardee and published IEEE researcher (IEEE ICOECA 2024, IRJMETS 2025) specializing in machine learning, deep learning, NLP, and scalable data architecture.',
          },
        },
        {
          '@type': 'Question',
          name: 'How do I start a project with Signal Zero?',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'You can start a project by submitting an inquiry through the interactive Project Discovery form at https://wearesignalzero.tech/#discovery or emailing contact@wearesignalzero.tech. Our technical team evaluates requirements and responds within 24 hours with architectural recommendations.',
          },
        },
      ],
    },
  ],
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <meta name="google-site-verification" content="wTTahPudOh-Z405wtC4NuMnGLQgMoXni9z2cY9f0dgo" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap"
          rel="stylesheet"
        />
        <script
          type="module"
          src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"
        ></script>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body className="antialiased relative min-h-screen bg-[var(--bg-base)] text-[var(--text-primary)] transition-colors duration-300">
        <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false}>
          {/* Layer 1: Aurora Mesh Gradient */}
          <div className="fixed inset-0 z-0 pointer-events-none overflow-hidden">
            <div className="absolute top-[-10%] left-[-10%] w-[50vw] h-[50vh] rounded-full bg-[#3b82f6] dark:bg-[#00e5ff] opacity-[0.05] dark:opacity-[0.18] blur-[120px] animate-aurora-1 transition-opacity duration-500" />
            <div className="absolute top-[-5%] right-[-10%] w-[45vw] h-[50vh] rounded-full bg-[#60a5fa] dark:bg-[#00e5ff] opacity-[0.05] dark:opacity-[0.18] blur-[120px] animate-aurora-2 transition-opacity duration-500" />
            <div className="absolute top-[30%] left-[20%] w-[60vw] h-[60vh] rounded-full bg-[#8b5cf6] dark:bg-[#7b2fff] opacity-[0.04] dark:opacity-[0.18] blur-[120px] animate-aurora-3 transition-opacity duration-500" />
            <div className="absolute bottom-[-10%] right-[-10%] w-[50vw] h-[50vh] rounded-full bg-[#2563eb] dark:bg-[#084298] opacity-[0.04] dark:opacity-[0.18] blur-[120px] animate-aurora-4 transition-opacity duration-500" />
          </div>

          {/* Layer 2: Dot Grid Overlay */}
          <div
            className="fixed inset-0 z-0 pointer-events-none opacity-50 dark:opacity-40 select-none bg-[radial-gradient(circle,_rgba(100,116,139,0.14)_1px,_transparent_1px)] dark:bg-[radial-gradient(circle,_rgba(0,229,255,0.07)_1px,_transparent_1px)] transition-all duration-500"
            style={{ backgroundSize: '32px 32px' }}
          />

          {/* Layer 3: Noise Texture Overlay */}
          <div
            className="fixed inset-0 z-0 pointer-events-none opacity-[0.015] dark:opacity-[0.025] mix-blend-overlay select-none"
            style={{
              backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E")`,
            }}
          />

          <div className="relative z-10 w-full flex flex-col">{children}</div>
        </ThemeProvider>
      </body>
    </html>
  );
}
