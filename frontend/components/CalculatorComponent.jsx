import React, { useState } from 'react';
import axios from 'axios';

const apiURL = import.meta.env.VITE_BACKEND_URL;

  /**
   * The CalculatorComponent is a React component that renders a simple calculator
   * interface. It allows the user to select an operation (add, subtract, multiply,
   * or divide) and enter two numbers, A and B. When the user submits the form,
   * the component makes a GET request to the backend, passing the selected operation
   * and the two numbers. The response from the backend is then displayed as the
   * result of the calculation.
   */
const CalculatorComponent = () => {
  const [operation, setOperation] = useState('');
  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const [result, setResult] = useState('');

  /**
   * Handles changes to the selected operation. Updates the state with the new
   * value.
   *
   * @param {React.ChangeEvent<HTMLSelectElement>} event - The change event.
   */
  const handleOperationChange = (event) => {
    setOperation(event.target.value);
  };

  /**
   * Handles changes to the input field for the first number, A. Updates the state
   * with the new value.
   *
   * @param {React.ChangeEvent<HTMLInputElement>} event - The change event.
   */

  /**
   * Handles changes to the input field for the first number, A. Updates the state
   * with the new value.
   *
   * @param {React.ChangeEvent<HTMLInputElement>} event - The change event.
   */
  const handleAChange = (event) => {
    setA(event.target.value);
  };

  /**
   * Handles changes to the input field for the second number, B. Updates the state
   * with the new value.
   *
   * @param {React.ChangeEvent<HTMLInputElement>} event - The change event.
   */
  const handleBChange = (event) => {
    setB(event.target.value);
  };

  /**
   * Handles the form submission. Makes a GET request to the backend with the
   * selected operation and the two numbers, A and B. The response from the backend
   * is then displayed as the result of the calculation.
   *
   * @param {React.FormEvent<HTMLFormElement>} event - The form submission event.
   */
  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
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