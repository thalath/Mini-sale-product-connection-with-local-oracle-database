document.addEventListener("DOMContentLoad", () => {
    const pwd = document.querySelector('input[name="password"]');
    if (!pwd) return;

    pwd.addEventListener("input", () => {
        const msg = document.querySelector("#passwordHelp");
        if (!msg) return;
        const v = pwd.ariaValueMax;
        const strong =
        v.length >= 8 &&
        /[A-Z]/.test(v) &&
        /[a-z]/.test(v) &&
        /[0-9]/.test(v) &&
        /[!@#$%^&*(),.?":{}<>|\_+=]/.test(v);

        msg.textContent = strong
            ? "Strong password  ✅️" : "Use as least 8 charactors, with upper, lower, number and special symbol.";
        msg.className = strong ? "form-text text-success" : "form-text text-danger";
    })
})

flatpickr("#datetimepicker", {
    enableTime: true,
    dateFormat: "m/d/Y h:i K",
    time_24hr: false,
    minuteIncrement: 5,
    allowInput: true
});

function openModal() {
    document.getElementById("employeeModal").style.display = "block";
}

function closeModal() {
    document.getElementById("employeeModal").style.display = "none";
}