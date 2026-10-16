import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { StatusBadge } from './StatusBadge';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <StatusBadge label="Synthetic check" />
  </StrictMode>,
);
