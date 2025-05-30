import React, { useEffect, useState } from 'react';
import Select from 'react-select';

function CurrencySelect() {
  const [currencyOptions, setCurrencyOptions] = useState([]);
  const [baseCurrency, setBaseCurrency] = useState(null);
  const [targetCurrency, setTargetCurrency] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/currencies')
      .then(res => res.json())
      .then(data => {
        const options = data.map(code => ({ value: code, label: code }));
        setCurrencyOptions(options);
        setBaseCurrency(options[0]);
        setTargetCurrency(options[1]);
      })
      .catch(err => console.error("Failed to load currencies:", err));
  }, []);

  const handleSubmit = () => {
    if (!baseCurrency || !targetCurrency) return;

    const query = `http://localhost:5000/api/rates?base=${baseCurrency.value}&target=${targetCurrency.value}&year=2024&month=5`;

    fetch(query)
      .then(res => res.json())
      .then(data => {
        console.log("Exchange Data:", data); // You can visualize it
      });
  };

  return (
    <div>
      <h3>Select Currencies</h3>
      <div style={{ width: 300 }}>
        <label>Base Currency</label>
        <Select
          options={currencyOptions}
          value={baseCurrency}
          onChange={setBaseCurrency}
        />
        <label>Target Currency</label>
        <Select
          options={currencyOptions}
          value={targetCurrency}
          onChange={setTargetCurrency}
        />
      </div>
      <button onClick={handleSubmit} style={{ marginTop: "1rem" }}>
        Get Rates
      </button>
    </div>
  );
}

export default CurrencySelect;
