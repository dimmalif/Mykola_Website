import React from 'react';
import ReactDOM from 'react-dom/client';
import { App } from './App';
import './bundles/assets/css/styles.scss';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
    <App />
);