// Declarations -----------------------
let authBtn = document.getElementById("auth-btn");
let gotoAuthBtn = document.getElementById("login-or-signup");
let currentLevel = null;
let changeLangBtn = document.getElementById("lang");
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

let alertMessagesLang = {
  english: {
    signup: "username already exists",
    login: "wrong username or password",
  },

  français: {
    signup: "Ce nom d'utilisateur est déjà utilisé",
    login: "Le nom d'utilisateur ou le mot de passe est incorrect",
  },
};

let authBtnsLang = {
  english: {
    signup: "Sign up",
    login: "Log in",
  },

  français: {
    signup: "Créer un compte",
    login: "Se connecter",
  },
};

let gotoAuthLang = {
  english: {
    signup: "Go to Sign up",
    login: "Go to Log in",
  },

  français: {
    signup: "Vous avez déjà un compte",
    login: "Vous n'avez pas de compte",
  },
};
// end Declarations -----------------------

function getLanguage() {
  return store.get("language").type;
}

changeLangBtn.addEventListener("click", (e) => {
  setLangMap[getLanguage()]();
});

function translate(target, text) {
  let targetTo = document.getElementById(target);
  targetTo.innerText = text;
}

authBtn.textContent = authBtnsLang[getLanguage()]["login"];
gotoAuthBtn.textContent = gotoAuthLang[getLanguage()]["signup"];

function getSentences(level) {
  let lang = getLanguage();
  currentLevel = level;
  // eel.start_speaker(lang, level);
  eel.do_recognition(lang);
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
  translate("go-to-login", "Go To Login");
}
function français() {
  translate("choice-easy", "Facile");
  translate("choice-medium", "Moyen");
  translate("choice-hard", "Difficile");
  translate("show-statistics", "Voir les statistiques");
  translate("lang", "Langue anglaise");
  translate("success", "Réussites");
  translate("failures", "Echecs");
  translate("remaining-words", "Mots Restants");
  translate("go-to-login", "Aller à la page de connexion");
}

eel.expose(setSuccessPoints);
eel.expose(setFailedPoints);
eel.expose(getLanguage);
