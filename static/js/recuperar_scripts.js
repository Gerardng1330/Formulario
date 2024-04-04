/* Referencias */
const input = document.getElementById("Correo");

function setupMessage(id, button) {
  const el = document.getElementById(id);
  const btn = document.querySelector(button);

  if (el && btn) {
    btn.addEventListener("click", () => {
      el.style.animation = "fadeOut 0.3s ease-in-out forwards";
      setTimeout(() => (el.style.display = "none"), 300);
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  ["info", "error", "succ"].forEach((prefix) => {
    setupMessage(`${prefix}-message`, `.${prefix === "succ" ? "ok" : "close"}-button`);
  });
});

const emailSend = () => {
  let countdownInterval;
  let email = document.getElementById("id_email");
  const regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  if (email.value != "" && regexEmail.test(email.value)) {
    setTimeout(function () {
      buttonDisabled(true);
      const expirationTime = new Date().getTime() + 5 * 60 * 1000;
      localStorage.setItem("buttonExpiration", expirationTime);
      countdownInterval = setInterval(updateCountdownLabel, 10);

      setTimeout(
        function () {
          clearInterval(countdownInterval);
          localStorage.removeItem("buttonExpiration");
          buttonDisabled(false);
        },
        5 * 60 * 1000,
      );
    }, 1000);
  }
};

function updateCountdownLabel() {
  const countdownLabel = document.getElementById("countdownLabel");
  const expirationTime = localStorage.getItem("buttonExpiration");
  let remainingTime = Math.max(0, parseInt(expirationTime) - new Date().getTime());
  let seconds = Math.floor((remainingTime % (60 * 1000)) / 1000);
  let minutes = Math.floor(remainingTime / (60 * 1000));
  let formattedTime = `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
  countdownLabel.textContent = formattedTime;

  if (minutes <= 0 && seconds <= 0) {
    buttonDisabled(false);
  }
}

function checkButtonState() {
  const expirationTime = localStorage.getItem("buttonExpiration");
  if (expirationTime && new Date().getTime() < parseInt(expirationTime)) {
    buttonDisabled(true);
    countdownInterval = setInterval(updateCountdownLabel, 10);
  }
}

function buttonDisabled(isDisabled) {
  const button = document.getElementById("sendEmail");
  const countdownLabel = document.getElementById("countdownLabel");
  if (isDisabled === true) {
    button.disabled = true;
    button.style.cursor = "not-allowed";
    button.style.opacity = 0.7;
  } else {
    button.disabled = false;
    button.style.cursor = "pointer";
    button.style.opacity = 1;
    countdownLabel.textContent = "";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  checkButtonState();
});
