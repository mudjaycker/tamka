function systemSayToUser(level, toSay) {

  let element = new Element()
  let conversation = element.select("conversation")
  let receivedMsg = element.create({
    classList: ["msg", "received-msg"],
  })
  let paragraph = element.create({
    type: "paragraph",
    text: toSay,
  })

  element.append(receivedMsg, paragraph)
  element.append(conversation, receivedMsg)
}

eel.expose(systemSayToUser)