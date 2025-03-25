document.addEventListener('DOMContentLoaded', function () {
    // Arrays to store the properties for requests, favorites, and wishlist
    let requests = [];
    let favorites = [];
    let wishlist = [];

    // Success message container
    const successMessage = document.createElement('div');
    successMessage.classList.add('success-message');

    // Request More Info for a property
    function requestInfo(propertyId) {
        if (!requests.includes(propertyId)) {
            requests.push(propertyId);
            displayRequests();
            successMessage.textContent = 'Request for more information submitted!';
            document.body.appendChild(successMessage);  // Append success message to the body or somewhere appropriate
        } else {
            alert('You have already requested more info for this property!');
        }
    }

    // Add property to Favorites
    function addToFavorites(propertyId) {
        if (!favorites.includes(propertyId)) {
            favorites.push(propertyId);
            successMessage.textContent = 'Property added to Favorites!';
            document.body.appendChild(successMessage); // Show the success message
            displayFavorites();
        } else {
            alert('Property is already in Favorites!');
        }
    }

    // Add property to Wishlist
    function addToWishlist(propertyId) {
        if (!wishlist.includes(propertyId)) {
            wishlist.push(propertyId);
            successMessage.textContent = 'Property added to Wishlist!';
            document.body.appendChild(successMessage); // Show the success message
            displayWishlist();
        } else {
            alert('Property is already in Wishlist!');
        }
    }

    // Display Requested Properties
    function displayRequests() {
        const requestsList = document.getElementById('requests');
        requestsList.innerHTML = ''; // Clear previous list
        requests.forEach(function(property) {
            const listItem = document.createElement('li');
            listItem.className = 'list-group-item';
            listItem.textContent = 'Property ID: ' + property;
            requestsList.appendChild(listItem);
        });
    }

    // Display Favorite Properties
    function displayFavorites() {
        const favoritesList = document.getElementById('favorites');
        favoritesList.innerHTML = ''; // Clear previous list
        favorites.forEach(function(property) {
            const listItem = document.createElement('li');
            listItem.className = 'list-group-item';
            listItem.textContent = 'Property ID: ' + property;
            favoritesList.appendChild(listItem);
        });
    }

    // Display Wishlist Properties
    function displayWishlist() {
        const wishlistList = document.getElementById('wishlist');
        wishlistList.innerHTML = ''; // Clear previous list
        wishlist.forEach(function(property) {
            const listItem = document.createElement('li');
            listItem.className = 'list-group-item';
            listItem.textContent = 'Property ID: ' + property;
            wishlistList.appendChild(listItem);
        });
    }

    // Add event listener for the "Request More Info" buttons
    const infoButtons = document.querySelectorAll('.btn-info');
    infoButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Using data-property-id to get the unique ID
            const propertyId = button.closest('.card').dataset.propertyId;
            requestInfo(propertyId);
        });
    });

    // Add event listener for the "Add to Favorites" buttons
    const favoriteButtons = document.querySelectorAll('.btn-favorites');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const propertyId = button.closest('.card').dataset.propertyId;
            addToFavorites(propertyId);
        });
    });

    // Add event listener for the "Add to Wishlist" buttons
    const wishlistButtons = document.querySelectorAll('.btn-wishlist');
    wishlistButtons.forEach(button => {
        button.addEventListener('click', function () {
            const propertyId = button.closest('.card').dataset.propertyId;
            addToWishlist(propertyId);
        });
    });
});
