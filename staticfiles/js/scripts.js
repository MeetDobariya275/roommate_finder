// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }

    // Form Validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const inputs = form.querySelectorAll('input[required], textarea[required]');
            let valid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    valid = false;
                    input.classList.add('error');
                    const error = document.createElement('span');
                    error.classList.add('error-message');
                    error.textContent = 'This field is required.';
                    input.parentElement.appendChild(error);
                } else {
                    input.classList.remove('error');
                    const error = input.parentElement.querySelector('.error-message');
                    if (error) error.remove();
                }
            });

            if (!valid) {
                event.preventDefault();
            }
        });
    });

    // Scroll-to-Top Button
    const scrollTopButton = document.createElement('button');
    scrollTopButton.textContent = 'Scroll to Top';
    scrollTopButton.classList.add('scroll-top');
    document.body.appendChild(scrollTopButton);

    scrollTopButton.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            scrollTopButton.classList.add('visible');
        } else {
            scrollTopButton.classList.remove('visible');
        }
    });
});
