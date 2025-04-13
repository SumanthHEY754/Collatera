import React from "react";

export function Result() {
  const result = JSON.parse(localStorage.getItem("loanResult"));

  return (
    <div className="bg-gradient-to-br from-green-100 via-white to-green-100 min-h-screen flex items-center justify-center px-6">
      <div className="bg-white shadow-xl rounded-xl p-8 text-center max-w-md w-full">
        <h2 className="text-3xl font-bold text-green-700 mb-4">Loan Decision</h2>
        {result ? (
          <>
            <p className="mb-2 text-xl text-gray-800"><strong>Score:</strong> {result.score}</p>
            <p className="mb-2 text-xl text-blue-600 font-semibold"><strong>Tier:</strong> {result.tier}</p>
            <p className="mb-2 text-xl text-indigo-700 font-semibold"><strong>Decision:</strong> {result.decision}</p>
          </>
        ) : (
          <p className="text-red-600 text-lg">No result found</p>
        )}
      </div>
    </div>
  );
}