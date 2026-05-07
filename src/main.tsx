import ReactDOM from 'react-dom/client'
import { Suspense } from 'react'
import './index.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { AnalyticsTracker } from './components/AnalyticsTracker';
import App from './App';

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