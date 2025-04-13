import React, { useEffect, useState } from "react";
import axios from "axios";

export function AdminDashboard() {
  const [applications, setApplications] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/applications").then((res) => {
      setApplications(res.data);
    });
  }, []);

  return (
    <div className="p-6 min-h-screen bg-gray-100">
      <h2 className="text-3xl font-bold mb-6 text-center text-indigo-800">Admin Dashboard</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full border-collapse shadow-lg bg-white rounded-xl overflow-hidden">
          <thead className="bg-indigo-50 text-indigo-700 text-sm">
            <tr>
              <th className="p-3">User</th>
              <th className="p-3">Loan</th>
              <th className="p-3">Score</th>
              <th className="p-3">Tier</th>
              <th className="p-3">Decision</th>
              <th className="p-3">Income</th>
              <th className="p-3">Term</th>
              <th className="p-3">Collateral</th>
              <th className="p-3">Employment</th>
            </tr>
          </thead>
          <tbody>
            {applications.map((app) => (
              <tr key={app.id} className="border-t hover:bg-indigo-50 text-sm text-gray-800">
                <td className="p-3">{app.user_id}</td>
                <td className="p-3 font-medium text-green-600">${app.loan_amount}</td>
                <td className="p-3">{app.score}</td>
                <td className="p-3 text-blue-600 font-semibold">{app.tier}</td>
                <td className="p-3 text-indigo-600 font-semibold">{app.decision}</td>
                <td className="p-3">${app.income}</td>
                <td className="p-3">{app.term_months}</td>
                <td className="p-3">${app.collateral_value}</td>
                <td className="p-3">{app.employment_status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}