feather.replace();
const store = new InStore();
//store.set("language", {type: "english"})
const home = document.getElementById("home");
const stats = document.getElementById("stats");

function gotoStats() {
  setInCache();
  home.classList.add(["invisible"]);
  stats.classList.remove(["invisible"]);
}

function gotoHome() {
  stats.classList.add(["invisible"]);
  home.classList.remove(["invisible"]);
}

async function getSentences(level) {
  eel.start_speaker(getLanguage(), level);
  let totalPoint = document.getElementById("total-points");
  totalPoint.innerText = await eel.get_datas_length(getLanguage(), level)();
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

function getLanguage() {
  return store.get("language").type;
}
eel.expose(setSuccessPoints);
eel.expose(setFailedPoints);
eel.expose(getLanguage);

/*for stats.html*/
//Auto setting value in local storage
setTimeout(async () => {
  let storage = new InStore();
  let language = storage.get("language").type;

  let total_qty = await eel.get_tamka_qty(language)();
  let easy_qty = await eel.get_from_tamka(language, "easy", true, false)();
  let medium_qty = await eel.get_from_tamka(language, "medium", true, false)();
  let hard_qty = await eel.get_from_tamka(language, "hard", true, false)();

  let language_type = language + "_language";
  storage.set(language_type, { easy_qty, total_qty, medium_qty, hard_qty });
}, 500);
