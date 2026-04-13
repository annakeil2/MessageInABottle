window.addEventListener("load", () => {
    const box = document.querySelector(".message-box");
    if (box) {
        box.style.opacity = 0;
        box.style.transition = "opacity 1.5s";

        setTimeout(() => {
            box.style.opacity = 1;
        }, 200);
    }
});

// Countdown timer
let seconds = 3600;

setInterval(() => {
    const timer = document.getElementById("timer");
    if (!timer) return;

    seconds--;

    let min = Math.floor(seconds / 60);
    let sec = seconds % 60;

    timer.innerText = `Next bottle in: ${min}:${sec < 10 ? '0' : ''}${sec}`;

    if (seconds <= 0) seconds = 3600;

}, 1000);