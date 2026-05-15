"use client";

import dynamic from 'next/dynamic';
import { useRef, useEffect, useState } from 'react';
import { useInView } from 'framer-motion';
import { Skeleton } from '@/components/ui/skeleton';

const ModelViewerDynamic = dynamic(() => import('./ModelViewer'), {
  ssr: false,
  loading: () => <Skeleton className="w-full h-[400px]" />,
});

export default function LazyModelViewer(props) {
  const ref = useRef(null);
  const inView = useInView(ref, { once: true, amount: 0.25 });
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    if (inView) setMounted(true);
  }, [inView]);

  return (
    <div ref={ref} className="w-full h-full">
      {mounted ? <ModelViewerDynamic {...props} /> : <Skeleton className="w-full h-[400px]" />}
    </div>
  );
}
