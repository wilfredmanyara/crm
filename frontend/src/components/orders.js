// orders.js
const API_URL = 'http://127.0.0.1:5000';

function loadOrders() {
    fetch(`${API_URL}/orders`)
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = `
                <h2>Orders</h2>
                <button onclick="showOrderForm()">Add Order</button>
                <div id="orders-list">${data.map(order => `<p>Order ID: ${order.id}</p>`).join('')}</div>
            `;
        });
}

function showOrderForm() {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h2>Add Order</h2>
        <form onsubmit="addOrder(event)">
            <input type="text" placeholder="Product ID" required>
            <input type="text" placeholder="Retailer ID" required>
            <input type="number" placeholder="Quantity" required>
            <button type="submit">Submit</button>
        </form>
    `;
}

function addOrder(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    fetch(`${API_URL}/orders`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadOrders(); // Refresh the list
    });
}

