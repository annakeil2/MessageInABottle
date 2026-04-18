// Countdown timer
let seconds = 900;

setInterval(() => {
    const timer = document.getElementById("timer");
    if (!timer) return;

    seconds--;

    let min = Math.floor(seconds / 60);
    let sec = seconds % 60;

    timer.innerText = `Next bottle in: ${min}:${sec < 10 ? '0' : ''}${sec}`;

    if (seconds <= 0) seconds = 900;

}, 1000);