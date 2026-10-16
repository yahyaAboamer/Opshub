// @vitest-environment jsdom
// T0002 client test contract: a React component rendered into jsdom and driven through act().
import { act } from 'react';
import { createRoot, type Root } from 'react-dom/client';
import { afterEach, describe, expect, it } from 'vitest';
import { StatusBadge } from './StatusBadge';

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let root: Root | undefined;
afterEach(() => {
  act(() => root?.unmount());
  root = undefined;
  document.body.replaceChildren();
});

function render(label: string): HTMLButtonElement {
  const container = document.body.appendChild(document.createElement('div'));
  root = createRoot(container);
  act(() => root!.render(<StatusBadge label={label} />));
  return container.querySelector('button')!;
}

describe('T0002 React client contract', () => {
  it('renders typed props and updates state on click', () => {
    const button = render('Synthetic check');
    expect(button.textContent).toBe('Synthetic check: idle');
    expect(button.getAttribute('aria-pressed')).toBe('false');
    act(() => button.click());
    expect(button.textContent).toBe('Synthetic check: checked');
    expect(button.getAttribute('aria-pressed')).toBe('true');
  });
});
