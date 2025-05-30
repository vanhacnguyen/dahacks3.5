import React, { useEffect, useState } from 'react';

function ExchangeRates() {
  const [rates, setRates] = useState([]);
  const [base, setBase] = useState("USD");
  const [target, setTarget] = useState("EUR");
  
  useEffect(() => {
    fetch(`http://localhost:5000/api/rates?base=${base}&target=${target}&year=2024&month=5`)
      .then(res => res.json())
      .then(data => setRates(data.data))
      .catch(err => console.error("API Error:", err));
  }, [base, target]);

    return (
    <div>
      <h2>Exchange Rate: {base} → {target} </h2>
      <div className="input-container">
        <input className="exchange-button" type="text" placeholder="USD to EUR" />
        <input className="exchange-button" type="text" placeholder="EUR to USD" />
      </div>
      <ul>
        {rates.map(([date, rate], index) => (
          <li key={index}>{date}: {rate}</li>
        ))}
      </ul>
    </div>
  );
}

export default ExchangeRates;