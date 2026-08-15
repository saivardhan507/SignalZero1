export default function robots() {
  return {
    rules: [
      {
        userAgent: '*',
        allow: '/',
        disallow: ['/api/'],
      },
      // Explicit permissions for AI Search Crawlers & Generative Engines (GEO)
      {
        userAgent: [
          'GPTBot',
          'ChatGPT-User',
          'PerplexityBot',
          'ClaudeBot',
          'anthropic-ai',
          'Google-Extended',
          'Googlebot',
          'Bingbot',
          'cohere-ai',
          'Bytespider',
          'Applebot',
        ],
        allow: '/',
      },
    ],
    sitemap: 'https://wearesignalzero.tech/sitemap.xml',
    host: 'https://wearesignalzero.tech',
  };
}
