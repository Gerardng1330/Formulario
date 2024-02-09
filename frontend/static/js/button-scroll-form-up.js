const scroll_up_button = document.querySelector("#scroll-up-button");

window.addEventListener("scroll", () => {
  if (window.pageYOffset > 100) {
    scroll_up_button.classList.remove("opacity-0");
  } else {
    scroll_up_button.classList.add("opacity-0");
  }
});
