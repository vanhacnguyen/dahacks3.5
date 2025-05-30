import './App.css';
import React, { useState } from 'react';
import CurrencySelect from './CurrencySelect'; // Adjust path if needed

function App() {
  
  const [baseCurrency, setBaseCurrency] = useState(null);
  const [targetCurrency, setTargetCurrency] = useState(null);
  const [amount, setAmount] = useState('');
  const [converted, setConverted] = useState(null);
  const [error, setError] = useState('');

  const handleConvert = () => {
    console.log('baseCurrency:', baseCurrency);
    console.log('targetCurrency:', targetCurrency);
    console.log('amount:', amount);
    if (!baseCurrency || !targetCurrency || !amount) {
      setError('Please fill in all fields.');
      setConverted(null);
      return;
    }

    const base = baseCurrency.value;
    const target = targetCurrency.value;

    fetch(`http://localhost:5000/convert?base=${base}&target=${target}&amount=${amount}`)
      .then(res => res.json())
      .then(data => {
        if (data.converted_amount !== undefined) {
          setConverted(data.converted_amount);
          setError('');
        } else {
          setError(data.error || 'Conversion failed');
          setConverted(null);
        }
      })
      .catch(() => {
        setError('Server error');
        setConverted(null);
      });
  };

  // Clear results on any input change
  const handleAmountChange = (e) => {
    setAmount(e.target.value);
    setConverted(null);
    setError('');
  };

  const handleBaseCurrencyChange = (selectedOption) => {
    setBaseCurrency(selectedOption);
    setConverted(null);
    setError('');
  };

  const handleTargetCurrencyChange = (selectedOption) => {
    setTargetCurrency(selectedOption);
    setConverted(null);
    setError('');
  };  

  return (
    <div className="website">
      <img src="website-pic1.png" alt="input background" className="input-bg" />
      <header className="website-header">
        <h2>Currency Converter</h2>
      </header>
      <CurrencySelect
        baseCurrency={baseCurrency}
        setBaseCurrency={handleBaseCurrencyChange}
        targetCurrency={targetCurrency}
        setTargetCurrency={handleTargetCurrencyChange}
      />
      <div className="input-container">
        <input
          type="number"
          placeholder="Enter amount"
          value={amount}
          onChange={handleAmountChange}
        />
        <img src="arrow.png" alt="arrow"/>
        <button onClick={handleConvert}>Convert</button>
        {converted !== null && (
          <p>
            {amount} {baseCurrency?.value} = {converted.toFixed(2)} {targetCurrency?.value}
          </p>
        )}
        {error && <p style={{ color: 'red' }}>{error}</p>}
      </div>
    </div>
  );
}

export default App;
