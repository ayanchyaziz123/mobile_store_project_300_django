var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product id :', productId, 'action : ', action)

        if (user == 'AnonymousUser') {
            console.log("Not Loggged in")
        }
        else {
            console.log("Log in")
        }
    })

}

function updateUserOrder(productId, action) {
    console.log("User is logged in, sendin data..")

    var url = '/user_update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data', data)
        })
}