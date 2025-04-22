// Add scroll event listener to change navbar style on scroll
window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar-glass');
    if (window.scrollY > 150) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

function changeImageAndNavbar() {
    const imageHeight = document.querySelector('.background-image').offsetHeight;
    document.querySelector('#tagline').style.top = `${imageHeight * 0.4}px`;
    document.querySelector('#comment').style.top = `${imageHeight * 0.675}px`
    document.querySelector('#learnMore').style.top = `${imageHeight * 0.85}px`

    const navbar = document.querySelector("#navbarNav")
    if (window.innerWidth < 768) {
        navbar.classList.add('navCollapsed')
    } else {
        navbar.classList.remove('navCollapsed')
    }

    if (window.innerWidth < 500) {
        document.querySelector('#tagline').style.top = `${imageHeight * 0.3}px`;
    }
}

window.addEventListener('resize', () => {
    changeImageAndNavbar();
})

window.addEventListener('DOMContentLoaded', () => {
    changeImageAndNavbar();
})

document.getElementById('learnMore').addEventListener('click', function () {
    // Get the target element
    const targetElement = document.getElementById('cardQuestions');

    // Get the element's position
    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;

    // Calculate the offset (3% of viewport height)
    const viewportHeight = window.innerHeight;
    const offset = viewportHeight * 0.03;

    // Scroll to the adjusted position
    window.scrollTo({
        top: targetPosition - offset,
        behavior: 'smooth'
    });
});

document.getElementById('nextSolutions').addEventListener('click', () => {
    // Get the target element
    const targetElement = document.getElementById('solutions');

    // Get the element's position
    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;

    // Calculate the offset (3% of viewport height)
    const viewportHeight = window.innerHeight;
    const offset = viewportHeight * 0.03;

    // Scroll to the adjusted position
    window.scrollTo({
        top: targetPosition - offset,
        behavior: 'smooth'
    });
})

document.getElementById('nextSolutions').addEventListener('click', () => {
    // Get the target element
    const targetElement = document.getElementById('solutions');

    // Get the element's position
    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;

    // Calculate the offset (3% of viewport height)
    const viewportHeight = window.innerHeight;
    const offset = viewportHeight * 0.03;

    // Scroll to the adjusted position
    window.scrollTo({
        top: targetPosition - offset,
        behavior: 'smooth'
    });
})

document.getElementById('nextSustainability').addEventListener('click', () => {
    // Get the target element
    const targetElement = document.getElementById('sustainability');

    // Get the element's position
    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;

    // Calculate the offset (3% of viewport height)
    const viewportHeight = window.innerHeight;
    const offset = viewportHeight * 0.03;

    // Scroll to the adjusted position
    window.scrollTo({
        top: targetPosition - offset,
        behavior: 'smooth'
    });
})

document.getElementById('nextFAQ').addEventListener('click', () => {
    // Get the target element
    const targetElement = document.getElementById('faq');

    // Get the element's position
    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;

    // Calculate the offset (3% of viewport height)
    const viewportHeight = window.innerHeight;
    const offset = viewportHeight * 0.03;

    // Scroll to the adjusted position
    window.scrollTo({
        top: targetPosition - offset,
        behavior: 'smooth'
    });
})







// Add scroll event listener to change navbar style on scroll
window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar-glass');
    if (window.scrollY > 150) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

function changeImageAndNavbar() {
    const imageHeight = document.querySelector('.background-image').offsetHeight;
    document.querySelector('#tagline').style.top = `${imageHeight * 0.4}px`;
    document.querySelector('#comment').style.top = `${imageHeight * 0.675}px`
    document.querySelector('#learnMore').style.top = `${imageHeight * 0.85}px`

    const navbar = document.querySelector("#navbarNav")
    if (window.innerWidth < 768) {
        navbar.classList.add('navCollapsed')
    } else {
        navbar.classList.remove('navCollapsed')
    }

    if (window.innerWidth < 500) {
        document.querySelector('#tagline').style.top = `${imageHeight * 0.3}px`;
    }
}

window.addEventListener('resize', () => {
    changeImageAndNavbar();
})

window.addEventListener('DOMContentLoaded', () => {
    changeImageAndNavbar();
})

document.getElementById('learnMore').addEventListener('click', function () {
    // Get the target element
    const targetElement = document.getElementById('cardQuestions');

    // Get the element's position
    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;

    // Calculate the offset (3% of viewport height)
    const viewportHeight = window.innerHeight;
    const offset = viewportHeight * 0.03;

    // Scroll to the adjusted position
    window.scrollTo({
        top: targetPosition - offset,
        behavior: 'smooth'
    });
});

document.getElementById('nextSolutions').addEventListener('click', () => {
    // Get the target element
    const targetElement = document.getElementById('solutions');

    // Get the element's position
    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;

    // Calculate the offset (3% of viewport height)
    const viewportHeight = window.innerHeight;
    const offset = viewportHeight * 0.03;

    // Scroll to the adjusted position
    window.scrollTo({
        top: targetPosition - offset,
        behavior: 'smooth'
    });
})

document.getElementById('nextSustainability').addEventListener('click', () => {
    // Get the target element
    const targetElement = document.getElementById('sustainability');

    // Get the element's position
    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;

    // Calculate the offset (3% of viewport height)
    const viewportHeight = window.innerHeight;
    const offset = viewportHeight * 0.03;

    // Scroll to the adjusted position
    window.scrollTo({
        top: targetPosition - offset,
        behavior: 'smooth'
    });
})

document.getElementById('nextFAQ').addEventListener('click', () => {
    // Get the target element
    const targetElement = document.getElementById('faq');

    // Get the element's position
    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;

    // Calculate the offset (3% of viewport height)
    const viewportHeight = window.innerHeight;
    const offset = viewportHeight * 0.03;

    // Scroll to the adjusted position
    window.scrollTo({
        top: targetPosition - offset,
        behavior: 'smooth'
    });
})

// FAQ Accordion Logic
document.querySelectorAll('.accordion-button').forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;

        // Toggle open class for animation
        content.classList.toggle('open');

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + 'px';
        }
    });
});

// FAQ Animation with Intersection Observer
const faqItems = document.querySelectorAll('.faq-item');

const faqObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.1
});

faqItems.forEach(item => faqObserver.observe(item));

