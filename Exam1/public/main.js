async function sendLED(state) {
    let response = await fetch(`/api/led/${state}`);
    let replyText = await response.text();
    document.querySelector("#replyText").innerHTML = replyText;
    return replyText;
}

async function sendFlash(count, period) {
    let response = await fetch(`/api/flash/${count}/${period}`);
    let replyText = await response.text();
    document.querySelector("#replyText").innerHTML = replyText;
    return replyText;
}

function main() {
    document.querySelector("#ledOn").onclick = () => {
        sendLED("ON");
    };

    document.querySelector("#ledOff").onclick = () => {
        sendLED("OFF");
    };

    document.querySelector('#flash').onclick = () => {
        let count = document.querySelector("#count").value;
        let period = document.querySelector("#period").value;
        sendFlash(count, period);
    };
}

main();