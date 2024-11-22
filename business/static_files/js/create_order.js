    document.addEventListener("DOMContentLoaded", function () {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const productsListContainer = document.getElementById("products-list");
    const addProductButton = document.getElementById("add-product-button");

    let userProducts = []; // Список товаров пользователя

    // Загружаем товары пользователя из API
    function fetchUserProducts() {
        fetch(api_url)
            .then(response => response.json())
            .then(data => {
                userProducts = data;
            })
            .catch(error => {
                console.error("Ошибка при загрузке товаров пользователя:", error);
            });
    }
    // Функция для добавления нового блока товара
    function addProductRow() {
        const row = document.createElement("div");
        row.classList.add("product-row");

        // Создаём выпадающий список для выбора товара
        const select = document.createElement("select");
        select.classList.add("product-select");
        select.innerHTML = `<option value="">Выберите товар</option>`;
        userProducts.forEach(product => {
            select.innerHTML += `<option value="${product.id}" data-price="${product.selling_price}" data-amount="${product.amount}">
                ${product.title}
            </option>`;
        });

        // Поле для отображения цены
        const priceInput = document.createElement("input");
        priceInput.type = "number";
        priceInput.classList.add("product-price");
        priceInput.placeholder = "Цена";

        // Поле для отображения остатка
        const amountSpan = document.createElement("span");
        amountSpan.classList.add("product-amount");
        amountSpan.textContent = "Остаток: выберите товар";

        // Поле для ввода количества
        const quantityInput = document.createElement("input");
        quantityInput.type = "number";
        quantityInput.classList.add("product-quantity");
        quantityInput.placeholder = "Количество";
        quantityInput.min = "0.001";
        quantityInput.step = "0.001";

        // Удалить товар
        const removeButton = document.createElement("button");
        removeButton.textContent = "Удалить";
        removeButton.type = "button";
        removeButton.classList.add("remove-product-button");

        removeButton.addEventListener("click", () => {
            row.remove();
        });

        // Обновление цены и остатка при выборе товара
        select.addEventListener("change", function () {
            const selectedOption = select.options[select.selectedIndex];
            const price = selectedOption.getAttribute("data-price");
            const amount = selectedOption.getAttribute("data-amount");

            priceInput.value = price || "";
            amountSpan.textContent = `Остаток: ${amount || 0}`;
            quantityInput.max = amount || 0; // Устанавливаем максимальное количество
        });

        // Добавляем элементы в строку
        row.appendChild(select);
        row.appendChild(priceInput);
        row.appendChild(amountSpan);
        row.appendChild(quantityInput);
        row.appendChild(removeButton);

        // Добавляем строку в контейнер
        productsListContainer.appendChild(row);
    }

    // Обработчик для добавления нового товара
    addProductButton.addEventListener("click", addProductRow);

    // Загружаем список товаров при загрузке страницы
    fetchUserProducts();

    // Отправка данных формы
    const orderForm = document.getElementById("order-form");
    orderForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Предотвращаем стандартную отправку формы

        const products = [];
        const productRows = document.querySelectorAll(".product-row");
        productRows.forEach(row => {
            const select = row.querySelector(".product-select");
            const priceInput = row.querySelector(".product-price");
            const quantityInput = row.querySelector(".product-quantity");

            const productId = select.value;
            const price = priceInput.value;
            const quantity = quantityInput.value;

            if (productId && quantity > 0) {
                products.push({
                    product_id: productId,
                    price: parseFloat(price),
                    quantity: parseFloat(quantity)
                });
            }
        });
        const buyer = document.getElementById("id_buyer").value;
        fetch(send_data, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ products, buyer })
        })
        .then(response => {
            if (response.ok) {
                window.location.href = redirect_url;
            } else {
                return response.json();  // Возвращаем данные ошибки
            }
        })
        .then(data => {
            if (data?.error) {
                alert(`Ошибка: ${data.error}`);
            }
        })
        .catch(error => {
            console.error("Ошибка при создании заказа:", error);
        });
    });
});