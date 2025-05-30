import './App.css';

function App() {
  return (
    <div className="website">
      <header className="website-header"></header>

      <img src="website-pic1.png" alt="input background" className="input-bg" />

      <div className="input-container">
        <input className="exchange-button" type="text" placeholder="USD to EUR" />
        <img src="arrow.png" alt="arrow"/>
        <input className="exchange-button" type="text" placeholder="EUR to USD" />
      </div>
    </div>
  );
}

export default App;


