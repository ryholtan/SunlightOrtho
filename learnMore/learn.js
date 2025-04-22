    // JavaScript for mobile menu toggle
document.addEventListener('DOMContentLoaded', function () {
        const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav-menu');
        toggle.addEventListener('click', () => {
    nav.classList.toggle('show');
        });
});
