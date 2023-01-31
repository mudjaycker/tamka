class Element {

  select(id) {
    let element = document.getElementById(id);
    return element
  }

  create({ type, text, classList }) {
    if(!type){
      type="div"
    }
    let element = document.createElement(type)

    if (text) {
      element.textContent = text
    }

    if (classList) {
      classList.forEach(className => element.classList.add(className))
    }
    return element
  }

  append(parent, child) {
    parent.appendChild(child);
  }
}