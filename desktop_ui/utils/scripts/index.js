feather.replace();

function page(option, id) {
  const page = document.getElementById(id);
  if (option === "show") {
    page.classList.remove(["invisible"]);
  } else {
    page.classList.add(["invisible"]);
  }
}

// document.addEventListener('keydown', (e) => {
// e.preventDefault()
// if (e.key.toLowerCase() === 'c' && e.ctrlKey && e.shiftKey) {
// alert('cannot show dev mode');
// }
// });
addEventListener("contextmenu", (event) => {
  event.preventDefault();
});


function gotoStats() {
  getCharts();
  page("hide", "home");
  page("show", "stats");
}

function login() {
  page("hide", "auth");
  page("show", "home");
}

function gotoHome() {
  page("hide", "stats");
  page("show", "home");
}


function translate(target, text) {
  let targetTo = document.getElementById(target)
  targetTo.innerText = text
  
}


function getLanguage() {
  return store.get("language").type;
}
//restart level function
async function restart() {
  await eel.restart(getLanguage(), currentLevel)();
}