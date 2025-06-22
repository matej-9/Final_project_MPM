function updateQuantity(itemId, action) {
    // AJAX request
    const formData = new FormData();
    formData.append('item_id', itemId);
    formData.append('action', action);
    formData.append('csrfmiddlewaretoken', CSRF_TOKEN);

    fetch('/cart/update_cart/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.deleted) {
            // Hide item if deleted
            const itemElement = document.getElementById('item-' + itemId);
            if (itemElement) {
                itemElement.style.display = 'none';
            }
        } else {
            // Update quantity and price
            const quantityElement = document.getElementById('quantity-' + itemId);
            const totalElement = document.getElementById('total-' + itemId);

            if (quantityElement) {
                quantityElement.textContent = data.quantity;
            }
            if (totalElement) {
                totalElement.textContent = data.total + ' €';
            }
        }
    })
    .catch(error => {
        alert('Chyba pri aktualizácii košíka!');
        console.error('Error:', error);
    });
}

