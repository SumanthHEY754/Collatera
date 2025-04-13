import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Home } from "./pages/Home";
import { LoanForm } from "./pages/LoanForm";
import { Result } from "./pages/Result";
import { AdminDashboard } from "./pages/AdminDashboard";
// export default function App() {
//   return (
//     <div className="bg-yellow-200 p-6 text-center">
//       <h1 className="text-2xl text-red-600 font-bold">Tailwind Test</h1>
//     </div>
//   );
// }

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/apply" element={<LoanForm />} />
        <Route path="/result" element={<Result />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </Router>
  );
}
