// retailers.js
const API_URL = 'http://127.0.0.1:5000';

function loadRetailers() {
    fetch(`${API_URL}/retailers`)
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = `
                <h2>Retailers</h2>
                <button onclick="showRetailerForm()">Add Retailer</button>
                <div id="retailers-list">${data.map(retailer => `<p>${retailer.name}</p>`).join('')}</div>
            `;
        });
}

function showRetailerForm() {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h2>Add Retailer</h2>
        <form onsubmit="addRetailer(event)">
            <input type="text" placeholder="Name" required>
            <input type="text" placeholder="Location" required>
            <button type="submit">Submit</button>
        </form>
    `;
}

function addRetailer(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    fetch(`${API_URL}/retailers`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadRetailers(); // Refresh the list
    });
}

