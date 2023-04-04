feather.replace();
let store = new InStore();

let langMap = { english, français };
langMap[store.get("language").type]();

let setLangMap = {
  english: () => {
    store.set("language", { type: "français" });
    langMap[store.get("language").type]();
    console.log("french language is set");
  },
  français: () => {
    store.set("language", { type: "english" });
    langMap[store.get("language").type]();
    console.log("english language is set");
  },
};

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

function translate(target, text) {
  let targetTo = document.getElementById(target);
  targetTo.innerText = text;
}

function getLanguage() {
  return store.get("language").type;
}

function login() {
  page("hide", "auth");
  page("show", "home");
}

function gotoHome() {
  page("hide", "stats");
  page("show", "home");
}

function gotoStats() {
  getCharts();
  page("hide", "home");
  page("show", "stats");
}

