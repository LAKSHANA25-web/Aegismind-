import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async () => {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();
    setResult(data.prediction);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>AegisMind</h1>
      <input
        type="text"
        placeholder="Enter your text"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br /><br />
      <button onClick={handleSubmit}>Predict</button>
      <h2>Result: {result}</h2>
    </div>
  );
}

export default App;
