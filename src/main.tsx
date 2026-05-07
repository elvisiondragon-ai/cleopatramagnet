import ReactDOM from 'react-dom/client'
import React, { Suspense } from 'react'
import './index.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { AnalyticsTracker } from './components/AnalyticsTracker';

// ==========================================
// Single source of truth: var V in index.html — only change there
export const APP_VERSION = (window as any).__APP_VERSION__ as string;
// ==========================================

if (localStorage.getItem('v_cache') !== APP_VERSION) {
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.getRegistrations().then(regs => regs.forEach(r => r.unregister()));
  }
  if ('caches' in window) {
    caches.keys().then(names => names.forEach(n => caches.delete(n)));
  }
  localStorage.setItem('v_cache', APP_VERSION);
  setTimeout(() => window.location.reload(), 500);
}

const App = React.lazy(() => import('./App'));

const LoadingFallback = () => {
  return (
    <div style={{ minHeight: '100vh', background: '#0D0A14', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ width: 24, height: 24, border: '2px solid #D4A84B', borderTopColor: 'transparent', borderRadius: '50%', animation: 'spin 0.7s linear infinite' }} />
      <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById('root')!).render(
  <BrowserRouter>
    <AnalyticsTracker />
    <Suspense fallback={<LoadingFallback />}>
      <Routes>
        <Route path="/" element={<App />} />
      </Routes>
    </Suspense>
  </BrowserRouter>,
)