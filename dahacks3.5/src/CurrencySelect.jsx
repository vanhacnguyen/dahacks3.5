import React, { useEffect, useState } from 'react';
import Select from 'react-select';

function CurrencySelect({ baseCurrency, setBaseCurrency, targetCurrency, setTargetCurrency }) {
  const [currencyOptions, setCurrencyOptions] = useState([]);
  const [loading, setLoading] = useState(true); // Renamed from isLoading to loading

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/currencies')
      .then(res => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then(data => {
        console.log("Fetched currencies:", data);
        // Ensure data is an array before mapping
        if (Array.isArray(data)) {
          const options = data.map(code => ({ value: code, label: code }));
          setCurrencyOptions(options);
          if (options.length > 1) {
            setBaseCurrency(options[0]);
            setTargetCurrency(options[1]);
          }
        } else {
          console.error("Expected array but got:", data);
        }
      })
      .catch(err => {
        console.error("Failed to load currencies:", err);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading currencies...</div>;
  }

  return (
    <div>
      <h3>Select Currencies</h3>
      <div style={{ display: 'flex', gap: '120px', justifyContent: 'center' }}>
        <div style={{ width: 250}}>
          <h4>Base Currency</h4>
          <Select
            options={currencyOptions}
            value={baseCurrency}
            onChange={setBaseCurrency}
            isDisabled={currencyOptions.length === 0}
          />
        </div>
        <img src="arrow.png" alt="arrow"/>
        <div style={{ width: 250}}>
          <h4>Target Currency</h4>
          <Select
            options={currencyOptions}
            value={targetCurrency}
            onChange={setTargetCurrency}
            isDisabled={currencyOptions.length === 0}
          />
        </div>
      </div>
    </div>
  );
}

export default CurrencySelect;