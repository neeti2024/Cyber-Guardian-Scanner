async function startScan() {
    const url = document.getElementById('targetUrl').value;
    if (!url) return alert('Please enter a valid URL');

    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    
    loading.style.display = 'block';
    results.innerHTML = '';

    try {
        const response = await fetch('http://localhost:5000/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
        });

        if (!response.ok) {
            throw new Error(`Scan failed: ${response.status}`);
        }

        const data = await response.json();
        displayResults(data.vulnerabilities);
    } catch (error) {
        alert(error.message);
    } finally {
        loading.style.display = 'none';
    }
}

function displayResults(vulnerabilities) {
    const results = document.getElementById('results');
    results.innerHTML = vulnerabilities.map(vuln => `
        <div class="vulnerability-card">
            <h3>${vuln.name}</h3>
            <div class="severity ${vuln.severity}">
                ${vuln.severity.toUpperCase()}
            </div>
            <p>${vuln.description}</p>
            <div class="solution">
                ${vuln.solution}
            </div>
        </div>
    `).join('');
}