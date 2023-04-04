let currentLevel = null;

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

function english() {
  translate("choice-easy", "Easy");
  translate("choice-medium", "Medium");
  translate("choice-hard", "Hard");
  translate("show-statistics", "Show Statistics");
  translate("lang", "French language");
  translate("success", "Success");
  translate("failures", "Failures");
  translate("remaining-words", "Remaining Words");
  translate("reload-button", "Restart");
}
function français() {
  translate("choice-easy", "Facile");
  translate("choice-medium", "Moyen");
  translate("choice-hard", "Difficile");
  translate("show-statistics", "Voir les statistiques");
  translate("lang", "Langue anglaise");
  translate("success", "Réussites");
  translate("failures", "Failures");
  translate("remaining-words", "Mots Restants");
  translate("reload-button", "Recommencer");
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
