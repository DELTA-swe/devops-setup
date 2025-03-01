import React, { useState } from 'react';
import axios from 'axios';
const apiURL = import.meta.env.VITE_BACKEND_URL;

const CalculatorComponent = () => {
  const [operation, setOperation] = useState("add"); // Default operation
  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const [result, setResult] = useState('');

  const handleOperationChange = (event) => {
    setOperation(event.target.value);
  };

  const handleAChange = (event) => {
    setA(event.target.value);
  };

  const handleBChange = (event) => {
    setB(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!operation || !a || !b) {
      console.error("Operation or numbers are not set correctly.");
      return; // Don't proceed if any value is missing
    }
    
    try {
      console.log(`${apiURL}/operations/${operation}/${a}/${b}`);
      const response = await axios.get(`${apiURL}/operations/${operation}/${a}/${b}`);
      console.log(response.data);
      setResult(response.data.result);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Operation:
          <select value={operation} onChange={handleOperationChange}>
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
          </select>
        </label>
        <br />
        <label>
          A:
          <input type="number" value={a} onChange={handleAChange} />
        </label>
        <br />
        <label>
          B:
          <input type="number" value={b} onChange={handleBChange} />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
      <br />
      {result && <p>Result: {result}</p>}
    </div>
  );
};

export default CalculatorComponent;