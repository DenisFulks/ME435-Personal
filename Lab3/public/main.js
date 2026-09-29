async function sendCommand(command) {
    console.log(command);
    let response = await fetch(`/api/${command}`);
    let replyText = await response.text();
    console.log(replyText);
    document.querySelector("#replyText").innerHTML = replyText;
    return replyText;
}

function main() {
    console.log("Hello, JavaScript!");

    document.querySelector("#resetButton").onclick = () => {
        sendCommand("RESET");
    };

    document.querySelector('#moveButton').onclick = () => {
        let startPos = document.querySelector("#moveFrom").value;
        let endPos = document.querySelector("#moveTo").value;
        sendCommand(`MOVE ${startPos} ${endPos}`);
    };
}

main();