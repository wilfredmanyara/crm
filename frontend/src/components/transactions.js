// transactions.js
const API_URL = 'http://127.0.0.1:5000';

function loadTransactions() {
    fetch(`${API_URL}/transactions`)
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = `
                <h2>Transactions</h2>
                <button onclick="showTransactionForm()">Add Transaction</button>
                <div id="transactions-list">${data.map(transaction => `<p>Transaction ID: ${transaction.id}</p>`).join('')}</div>
            `;
        });
}

function showTransactionForm() {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h2>Add Transaction</h2>
        <form onsubmit="addTransaction(event)">
            <input type="text" placeholder="Order ID" required>
            <input type="number" placeholder="Amount" required>
            <button type="submit">Submit</button>
        </form>
    `;
}

function addTransaction(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    fetch(`${API_URL}/transactions`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadTransactions(); // Refresh the list
    });
}

