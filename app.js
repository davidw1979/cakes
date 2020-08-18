const burger = document.querySelector('.burger');
const LinkModal = document.querySelector('.nav-links');
const navLinks = document.querySelectorAll('.nav-link > a')

burger.addEventListener('click', () => {
  console.log('clicked');
  LinkModal.classList.toggle('nav-active');

  navLinks.forEach((link, index) => {
    if (link.style.animation) {
      link.style.animation = '';
    } else {
      link.style.animation = `nav-link-fade 0.5s ease forwards ${index / 9 + 0.1}s`
    }
  });
});



