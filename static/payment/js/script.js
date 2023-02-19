    checkoutButton.addEventListener("click", function ()  {
        fetch(api, {
            method: "GET",
            headers: {
                'X-CSRFToken': csrftoken
            }
        }).then(function (response){
                return response.json();
            }).then(function (session) {
                return stripe.redirectToCheckout({sessionId: session.id});
            }).then(function (result) {
                if (result.error){
                    alert(result.error.message)
                }
            }).catch(function (error) {
                console.error("ERROR:", error);
            });
    });