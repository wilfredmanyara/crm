// farmers.js
const API_URL = 'http://127.0.0.1:5000';

function loadFarmers() {
    fetch(`${API_URL}/farmers`)
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = `
                <h2>Farmers</h2>
                <button onclick="showFarmerForm()">Add Farmer</button>
                <div id="farmers-list">${data.map(farmer => `<p>${farmer.name}</p>`).join('')}</div>
            `;
        });
}

function showFarmerForm() {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h2>Add Farmer</h2>
        <form onsubmit="addFarmer(event)">
            <input type="text" placeholder="Name" required>
            <input type="text" placeholder="Location" required>
            <button type="submit">Submit</button>
        </form>
    `;
}

function addFarmer(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    fetch(`${API_URL}/farmers`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadFarmers(); // Refresh the list
    });
}

