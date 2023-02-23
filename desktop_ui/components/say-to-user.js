function systemSayToUser(msg) {
  let element = new Element()
  let conversation = element.select("conversation")
  let receivedMsg = element.create({
    classList: ["msg", "received-msg"],
  })
  let paragraph = element.create({
    type: "paragraph",
    text: msg,
  })

  element.append(receivedMsg, paragraph)
  element.append(conversation, receivedMsg)
}

eel.expose(systemSayToUser)