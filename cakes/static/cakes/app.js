const burger = document.querySelector('.burger');
const LinkModal = document.querySelector('.nav-links');
const navLinks = document.querySelectorAll('.nav-link > a');

// Prevent animations triggering on window resizes
let resizeTimer;
window.addEventListener("resize", () => {
  document.body.classList.add("resize-animation-stopper");
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    document.body.classList.remove("resize-animation-stopper");
  }, 400);
});

// Trigger sidebar for mobile from burger icon
burger.addEventListener('click', () => {
  
  // Bring in sidebar
  LinkModal.classList.toggle('nav-active');

  // Trigger animation on individual links
  navLinks.forEach((link, index) => {
    if (link.style.animation) {
      link.style.animation = '';
    } else {
      link.style.animation = `nav-link-fade 0.5s ease forwards ${index / 9 + 0.1}s`
    }
  });

  // Trigger burger animation
  burger.classList.toggle('burger-state');
});




