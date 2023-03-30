const store = new InStore();
function getLanguage() {
  return store.get("language").type;
}
feather.replace();

// document.addEventListener('keydown', (e) => {
// e.preventDefault()
// if (e.key.toLowerCase() === 'c' && e.ctrlKey && e.shiftKey) {
// alert('cannot show dev mode');
// }
// });
addEventListener("contextmenu", (event) => {
  event.preventDefault();
});
//store.set("language", {type: "english"})
const home = document.getElementById("home");
const stats = document.getElementById("stats");

currentLevel = null
//restart level function
async function restart() {
  await eel.restart(getLanguage(), currentLevel)()
  console.log(currentLevel)
}

function gotoStats() {
  getCharts();
  home.classList.add(["invisible"]);
  stats.classList.remove(["invisible"]);
}

function gotoHome() {
  stats.classList.add(["invisible"]);
  home.classList.remove(["invisible"]);
}
// total points state

function getSentences(level) {
  let lang = getLanguage();
  let totalPoint = document.getElementById("total-points");
  eel.get_datas_length(
    getLanguage(),
    level
  )((len) => {
    totalPoint.innerText = len;
  });
  currentLevel = level;
  eel.start_speaker(lang, level);
}

function setSuccessPoints() {
  let successPoints = document.getElementById("success-points");
  successPoints.innerText = Number(successPoints.textContent) + 1;
}
function setFailedPoints() {
  let failedPoints = document.getElementById("failed-points");
  failedPoints.innerText = Number(failedPoints.textContent) + 1;
}

let choiceEasy = document.getElementById("choice-easy");
let choiceMedium = document.getElementById("choice-medium");
let choiceHard = document.getElementById("choice-hard");
let showStatistics = document.getElementById("show-statistics");
let lang = document.getElementById("lang");
let success = document.getElementById("success");
let failures = document.getElementById("failures");
let remainingWords = document.getElementById("remaining-words");
let reloadButton = document.getElementById("reload-button");

function english() {
  choiceEasy.innerText = "Easy";
  choiceMedium.innerText = "Medium";
  choiceHard.innerText = "Hard";
  showStatistics.innerText = "Show Statistics";
  lang.innerText = "French language";
  success.innerText = "Success";
  failures.innerText = "Failures";
  remainingWords.innerText = "Remaing Words";
  reloadButton.innerText = "Restart";
}
function français() {
  choiceEasy.innerText = "Facile";
  choiceMedium.innerText = "Moyen";
  choiceHard.innerText = "Difficile";
  showStatistics.innerText = "Voir les statistiques";
  lang.innerText = "Langue anglaise";
  success.innerText = "Réussites";
  failures.innerText = "Échecs";
  remainingWords.innerText = "Mots Restants";
  reloadButton.innerText = "Recommencer";
}

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

eel.expose(setSuccessPoints);
eel.expose(setFailedPoints);
eel.expose(getLanguage);
