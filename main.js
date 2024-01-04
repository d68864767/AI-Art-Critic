```javascript
// Fetch API
const fetchAPI = async (url, options) => {
    const response = await fetch(url, options);
    const data = await response.json();
    return data;
};

// Upload Artwork
const uploadForm = document.getElementById('upload-form');
uploadForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(uploadForm);
    const options = {
        method: 'POST',
        body: formData,
    };
    const data = await fetchAPI('/upload', options);
    console.log(data);
});

// Compare Artworks
const compareForm = document.getElementById('compare-form');
compareForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(compareForm);
    const options = {
        method: 'POST',
        body: formData,
    };
    const data = await fetchAPI('/compare', options);
    console.log(data);
});

// User Profile
const userForm = document.getElementById('user-form');
const userProfile = document.getElementById('user-profile');
userForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(userForm);
    const options = {
        method: 'POST',
        body: formData,
    };
    const data = await fetchAPI('/user', options);
    userProfile.innerHTML = `<p>User: ${data.username}</p>`;
});
```
