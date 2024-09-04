// products.js
const API_URL = 'http://127.0.0.1:5000';

function loadProducts() {
    fetch(`${API_URL}/products`)
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = `
                <h2>Products</h2>
                <button onclick="showProductForm()">Add Product</button>
                <div id="products-list">${data.map(product => `<p>${product.name}</p>`).join('')}</div>
            `;
        });
}

function showProductForm() {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h2>Add Product</h2>
        <form onsubmit="addProduct(event)">
            <input type="text" placeholder="Name" required>
            <input type="text" placeholder="Description" required>
            <input type="number" placeholder="Price" required>
            <input type="text" placeholder="Image URL" required>
            <button type="submit">Submit</button>
        </form>
    `;
}

function addProduct(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    fetch(`${API_URL}/products`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadProducts(); // Refresh the list
    });
}

