// Funkcia na zmenu množstva produktu v košíku
function updateQuantity(itemId, action) {
    // Pripravíme dáta na odoslanie
    const data = new FormData();
    data.append('item_id', itemId);
    data.append('action', action);
    data.append('csrfmiddlewaretoken', CSRF_TOKEN);

    // Pošleme požiadavku na server
    fetch('/cart/update_cart/', {
        method: 'POST',
        body: data
    })
    .then(response => response.json()) // Konvertujeme odpoveď na JSON
    .then(result => {
        // Ak bol produkt vymazaný, skryjeme ho
        if (result.deleted) {
            hideProduct(itemId);
        } else {
            // Inak aktualizujeme množstvo a cenu
            updateProductDisplay(itemId, result.quantity, result.total);
        }

        // Prepočítame celkovú sumu
        calculateTotal();
    })
    .catch(error => {
        alert('Chyba pri aktualizácii košíka!');
        console.log('Chyba:', error);
    });
}

// Skryje produkt z košíka
function hideProduct(itemId) {
    const product = document.getElementById('item-' + itemId);
    if (product) {
        product.style.display = 'none';
    }
}

// Aktualizuje zobrazenie produktu (množstvo a cenu)
function updateProductDisplay(itemId, quantity, total) {
    const quantityElement = document.getElementById('quantity-' + itemId);
    const totalElement = document.getElementById('total-' + itemId);

    if (quantityElement) {
        quantityElement.textContent = quantity;
    }
    if (totalElement) {
        totalElement.textContent = total + ' €';
    }
}

// Vypočíta celkovú sumu všetkých produktov v košíku
function calculateTotal() {
    let totalSum = 0;

    // Nájdeme všetky viditeľné produkty
    const visibleProducts = document.querySelectorAll('li.product:not([style*="display: none"])');

    // Pre každý produkt prirátame jeho cenu
    visibleProducts.forEach(product => {
        const priceElement = product.querySelector('[id^="total-"]');
        if (priceElement) {
            const priceText = priceElement.textContent.replace(' €', '');
            const price = parseFloat(priceText);

            if (!isNaN(price)) {
                totalSum += price;
            }
        }
    });

    // Zobrazíme celkovú sumu
    const totalElement = document.getElementById('total-sum');
    if (totalElement) {
        totalElement.textContent = totalSum.toFixed(2);
    }
}

// Spustíme výpočet celkovej sumy keď sa stránka načíta
document.addEventListener('DOMContentLoaded', calculateTotal);