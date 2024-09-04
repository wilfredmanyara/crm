// app.js
const API_URL = 'http://127.0.0.1:5000'; 
function loadFarmers() {
    import('./components/farmers.js').then(module => module.loadFarmers());
}

function loadRetailers() {
    import('./components/retailers.js').then(module => module.loadRetailers());
}

function loadProducts() {
    import('./components/products.js').then(module => module.loadProducts());
}

function loadOrders() {
    import('./components/orders.js').then(module => module.loadOrders());
}

function loadTransactions() {
    import('./components/transactions.js').then(module => module.loadTransactions());
}

