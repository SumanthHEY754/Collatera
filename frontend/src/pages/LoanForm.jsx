import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export function LoanForm() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    user_id: "demo-user",
    income: "",
    loan_amount: "",
    term_months: "",
    credit_score: "",
    collateral_value: "",
    employment_status: "Full-Time"
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/apply-loan", formData);
      localStorage.setItem("loanResult", JSON.stringify(res.data));
      navigate("/result");
    } catch (err) {
      console.error("❌ Submission failed:", err.response?.data || err.message);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <form onSubmit={handleSubmit} className="bg-white shadow-lg rounded-xl p-8 max-w-xl w-full space-y-4">
        <h2 className="text-2xl font-bold text-center text-indigo-700">Loan Application</h2>
        {["income", "loan_amount", "term_months", "credit_score", "collateral_value"].map((field) => (
          <input
            key={field}
            type="number"
            name={field}
            placeholder={field.replace("_", " ")}
            value={formData[field]}
            onChange={handleChange}
            className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-400"
            required
          />
        ))}
        <select
          name="employment_status"
          value={formData.employment_status}
          onChange={handleChange}
          className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-400"
        >
          <option value="Full-Time">Full-Time</option>
          <option value="Part-Time">Part-Time</option>
          <option value="Unemployed">Unemployed</option>
        </select>
        <button
          type="submit"
          className="w-full bg-indigo-700 hover:bg-indigo-800 text-white font-semibold py-3 px-6 rounded-lg transition"
        >
          Submit Application
        </button>
      </form>
    </div>
  );
}