import React, { useEffect, useState } from 'react';
import Select from 'react-select';

function CurrencySelect({ baseCurrency, setBaseCurrency, targetCurrency, setTargetCurrency, options}) {
  const [currencyOptions, setCurrencyOptions] = useState([]);
  const [loading, setLoading] = useState(true); // Renamed from isLoading to loading

  useEffect(() => {
    // If custom options are passed in, use them and skip API fetch
    if (options && Array.isArray(options)) {
      setCurrencyOptions(options);
        if (options.length > 1) {
            setBaseCurrency(options[0]);
            setTargetCurrency(options[1]);
        }
        setLoading(false);
        } else {
        // Otherwise fetch from API
        fetch('http://127.0.0.1:5000/api/currencies')
            .then(res => {
            if (!res.ok) throw new Error('Network response was not ok');
            return res.json();
            })
            .then(data => {
            if (Array.isArray(data)) {
                const fetchedOptions = data.map(code => ({ value: code, label: code }));
                setCurrencyOptions(fetchedOptions);
                if (fetchedOptions.length > 1) {
                setBaseCurrency(fetchedOptions[0]);
                setTargetCurrency(fetchedOptions[1]);
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
        }
    }, [options]);

  if (loading) {
    return <div>Loading currencies...</div>;
  }

  return (
    <div>
      <h3>Select Currencies</h3>
      <div style={{ display: 'flex', gap: '40px', justifyContent: 'center' }}>
        <div style={{ width: 250 }}>
          <h4>Base Currency</h4>
          <Select
            options={currencyOptions}
            value={baseCurrency}
            onChange={setBaseCurrency}
            isDisabled={currencyOptions.length === 0}
          />
        </div>
        <img src="arrow.png" alt="arrow" className="arrow-img" />
        <div style={{ width: 250 }}>
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