function systemSayToUser(message) {
  let element = new Element();
  let conversation = element.select("conversation");

  let userMsg = element.create({
    classList: ["msg", "sent-msg"]
  })

  let paragraph = element.create({
    type: "p",
    text: message
  })

  element.append(userMsg, paragraph)
  element.append(conversation, userMsg)
  let centerSide = document.getElementById('center')
  centerSide.scrollTop = centerSide.scrollHeight
}

eel.expose(systemSayToUser)


// L´ancienne méthode:
/*
function sendMessage(msg) {
let conversation = document.getElementById('conversation')
let userMsg = document.createElement("div")
let classeNames = ["msg", "sent-msg"]
classeNames.forEach(classeName => userMsg.classList.add(classeName))

let paragraph = document.createElement("p")
paragraph.textContent = msg
userMsg.appendChild(paragraph)
conversation.appendChild(userMsg)
}
*/