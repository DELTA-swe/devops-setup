import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Calc from '/pages/Calc.jsx';

/**
 * The App component sets up the main application router using BrowserRouter.
 * It defines the application routes using Routes and Route components.
 * Currently, it includes a single route that renders the Calc component at the root path ("/").
 */

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Calc />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;