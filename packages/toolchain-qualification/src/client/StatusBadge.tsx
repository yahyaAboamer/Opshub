import { useState } from 'react';

export interface StatusBadgeProps {
  label: string;
}

export function StatusBadge({ label }: StatusBadgeProps) {
  const [checked, setChecked] = useState(false);
  return (
    <button type="button" aria-pressed={checked} onClick={() => setChecked(true)}>
      {`${label}: ${checked ? 'checked' : 'idle'}`}
    </button>
  );
}
