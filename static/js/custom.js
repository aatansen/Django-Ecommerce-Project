$(document).ready(function () {
    // increment button functionality
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        var inc_value=$(this).closest('.product_data').find('.qty-input').val();
        var value=parseInt(inc_value,10);
        value=isNaN(value)?0:value;
        if(value<10){
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    // decrement button functionality
    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        var dec_value=$(this).closest('.product_data').find('.qty-input').val();
        var value=parseInt(dec_value,10);
        value=isNaN(value)?0:value;
        if(value>1){
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    // add to cart button functionality
    $('.addToCartBtn').click(function (e) { 
        e.preventDefault();
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var product_qty=$(this).closest('.product_data').find('.qty-input').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-cart/",
            data: {
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                alertify.success(response.status)
            }
        });
    });

    // update and change the quantity of the product
    $('.changeQuantity').click(function (e) { 
        e.preventDefault();
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var product_qty=$(this).closest('.product_data').find('.qty-input').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-cart/",
            data: {
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                alertify.success(response.status)
            }
        });
    });

    // delete cart item
    $('.delete-cart-item').click(function (e) {
        e.preventDefault();

        // Cache the specific cart item row and CSRF token
        var $cartItem = $(this).closest('.product_data');
        var product_id = $cartItem.find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        // Send AJAX request to delete the item
        $.ajax({
            method: "POST",
            url: "/delete-cart-item/",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                // Show success message
                alertify.success(response.status);

                // Remove the specific cart item row from the DOM
                $cartItem.remove();

                // Check if the cart is now empty and display a message
                if ($('.product_data').length === 0) {
                    $('.card-data').html('<h4>Your cart is empty</h4>');
                }
            },
            error: function () {
                alertify.error("Failed to remove the item. Please try again.");
            }
        });
    });

    // add to wishlist button functionality
    $('.addToWishlistBtn').click(function (e) { 
        e.preventDefault();
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-wishlist/",
            data: {
                'product_id':product_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                alertify.success(response.status)
            }
        });
    });

    // delete wishlist item
    $('.delete-wishlist-item').click(function (e) {
        e.preventDefault();

        // Cache the specific wishlist item row and CSRF token
        var $wishlistItem = $(this).closest('.product_data');
        var product_id = $wishlistItem.find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        // Send AJAX request to delete the item
        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item/",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                // Show success message
                alertify.success(response.status);

                // Remove the specific wishlist item row from the DOM
                $wishlistItem.remove();

                // Check if the wishlist is now empty and display a message
                if ($('.product_data').length === 0) {
                    $('.card-data').html('<h4>Your wishlist is empty</h4>');
                }
            },
            error: function () {
                alertify.error("Failed to remove the item. Please try again.");
            }
        });
    });
});