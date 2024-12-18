import React, { useState } from "react";

function App() {
    const [text, setText] = useState("");
    const [result, setResult] = useState(null);

    const analyzeText = async () => {
        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ text }),
        });
        const data = await response.json();
        setResult(data.analysis);
    };

    return (
        <div style={{ padding: "20px" }}>
            <h1>Sentiment Analysis</h1>
            <textarea
                value={text}
                onChange={(e) => setText(e.target.value)}
                rows={4}
                cols={50}
                placeholder="Enter text here..."
            />
            <br />
            <button onClick={analyzeText}>Analyze</button>
            {result && (
                <div>
                    <h2>Result:</h2>
                    {/* Exibindo os resultados de forma mais legível */}
                    <p><strong>Label:</strong> {result[0].label}</p>
                    <p><strong>Score:</strong> {result[0].score.toFixed(4)}</p>
                </div>
            )}
        </div>
    );
}

export default App;
