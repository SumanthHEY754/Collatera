import React from "react";
import { Link } from "react-router-dom";

export function Home() {
  return (
    <div className="bg-gradient-to-br from-indigo-900 via-purple-800 to-indigo-900 text-white min-h-screen flex flex-col justify-center items-center px-6">
      <h1 className="text-5xl font-extrabold mb-4 text-center">Welcome to Collatera</h1>
      <p className="text-lg text-gray-200 mb-6 text-center max-w-lg">
        Unlock smarter lending with AI-powered credit decisions & secure collateral management.
      </p>
      <div className="flex gap-4">
        <Link to="/apply" className="bg-blue-600 hover:bg-blue-500 px-6 py-3 rounded-full text-lg font-semibold transition">
          Apply Now
        </Link>
        <Link to="/admin" className="bg-white text-indigo-800 hover:bg-gray-200 px-6 py-3 rounded-full text-lg font-semibold transition">
          Admin Portal
        </Link>
      </div>
    </div>
  );
}