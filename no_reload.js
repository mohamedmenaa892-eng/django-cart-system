console.log("JS loaded");

document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click',function(){
        let id = this.dataset.id;
        addToCart(id);
    })
})

function addToCart(id){
    fetch(`/cart/add/${id}`, {
        method : "POST",
        headers : {
            "X-CSRFToken" : getCookie("csrftoken")
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('cart-count').innerText=data.cart_count;
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = cookie.substring(name.length + 1);
                break;
            }
        }
    }
    return cookieValue;
}