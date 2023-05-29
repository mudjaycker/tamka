// Declarations ---------------------------
let store = new InStore();
store.set("page", { current: "auth" });
store.set("auth", { type: "login" });
let authType = () => store.get("auth").type;

let usernameTextField = () =>
  document.getElementById("username-text-field").value;

let passwordTextField = () =>
  document.getElementById("password-text-field").value;
// end Declarations ---------------------------

// Functions to set up the window -----------------
// document.addEventListener('keydown', (e) => {
// e.preventDefault()
// if (e.key.toLowerCase() === 'c' && e.ctrlKey && e.shiftKey) {
// alert('cannot show dev mode');
// }
// });
addEventListener("contextmenu", (event) => {
  event.preventDefault();
});

// end Functions to set up the window -----------------


// Navigation processes------------------
function page(id) {
  const current_page_id = store.get("page").current;
  const current_page = document.getElementById(current_page_id);
  const target_page = document.getElementById(id);

  current_page.classList.add(["invisible"]);
  target_page.classList.remove(["invisible"]);
  store.set("page", { current: id });
}

function gotoHome() {
  page("home");
}

function gotoStats() {
  getCharts();
  page("stats");
}
// end Navigation processes------------------

// Authentication processes --------------------------
function loginOrSignup() {
  eel.do_authentication(
    usernameTextField(),
    passwordTextField(),
    authType()
  )((res) => {
    if (res) {
      page("home");
    } else {
      alert(alertMessagesLang[getLanguage()][authType()]);
    }
  });
}

function gotoLogin() {
  store.set("auth", { type: "login" });
  authBtn.textContent = authBtnsLang[getLanguage()]["login"];
  gotoAuthBtn.textContent = gotoAuthLang[getLanguage()]["signup"];
  page("auth");
}

function gotoSignup() {
  store.set("auth", { type: "signup" });
  authBtn.textContent = authBtnsLang[getLanguage()]["signup"];
  gotoAuthBtn.textContent = gotoAuthLang[getLanguage()]["login"];
}

function gotoLoginOrToSignup() {
  let map = {
    signup: gotoLogin,
    login: gotoSignup,
  };
  map[authType()]();
}
// end Authentication processes --------------------------
