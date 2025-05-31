import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import CurrencySelect from './CurrencySelect';


const limitedCurrencyOptions = [
  { value: 'USD', label: 'USD - US Dollar' },
  { value: 'EUR', label: 'EUR - Euro' },
  { value: 'AUD', label: 'AUD - Australian Dollar' }
];


function Chart() {
  const [baseCurrency, setBaseCurrency] = useState(null);
  const [targetCurrency, setTargetCurrency] = useState(null);
  const [rates, setRates] = useState([]);
  const [noDataMessage, setNoDataMessage] = useState(null);

  useEffect(() => {
    if (baseCurrency && targetCurrency) {
      fetch(`http://localhost:5000/historical-rates?base=${baseCurrency.value}&target=${targetCurrency.value}`)
        .then(res => res.json())
        .then(data => {
          console.log("API data:", data);
          if (data.success) {
            if (data.dates.length === 0) {
              setRates([]);  // clear rates
              setNoDataMessage(`No historical data available for ${baseCurrency.value} to ${targetCurrency.value} in selected month.`);
            } else {
              const combined = data.dates.map((date, i) => ({
                date,
                rate: data.rates[i]
              }));
              setRates(combined);
              setNoDataMessage(null);
            }
        } else {
          setRates([]);
          console.error("API Error:", data.error);
        }
      })
      .catch(err => {
        setRates([]);
        console.error("Fetch error:", err);
      });
  }
}, [baseCurrency, targetCurrency]);

  return (
    <div>
      <h2>Currency Rate Chart</h2>

      <CurrencySelect
        baseCurrency={baseCurrency}
        setBaseCurrency={setBaseCurrency}
        targetCurrency={targetCurrency}
        setTargetCurrency={setTargetCurrency}
        options={limitedCurrencyOptions}
      />

      {noDataMessage ? (
      <p>{noDataMessage}</p>
      ) : rates.length > 0 ? (
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={rates}>
            <XAxis dataKey="date" />
            <YAxis />s
            <Tooltip />
            <Line type="monotone" dataKey="rate" stroke="#007bff" />
          </LineChart>
        </ResponsiveContainer>
      ) : (
        baseCurrency && targetCurrency && <p>Loading chart data...</p>
      )}
    </div>
  );
}

export default Chart;
