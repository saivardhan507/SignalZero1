export default function manifest() {
  return {
    name: 'Signal Zero | Integrated AI & Systems Engineering Agency',
    short_name: 'Signal Zero',
    description:
      'We architect custom AI agents, enterprise RAG pipelines, real-time data, and fintech platforms.',
    start_url: '/',
    display: 'standalone',
    background_color: '#030712',
    theme_color: '#00e5ff',
    icons: [
      {
        src: '/signal-zero-logo-300x300.png',
        sizes: '300x300',
        type: 'image/png',
      },
      {
        src: '/signal-zero-logo-800x800.png',
        sizes: '800x800',
        type: 'image/png',
      },
    ],
  };
}
