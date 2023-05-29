feather.replace();
let store = new InStore();
store.set("page", { current: "auth" });
store.set("auth", { type: "login" });
let authType = () => store.get("auth").type;

let usernameTextField = () =>
  document.getElementById("username-text-field").value;

let passwordTextField = () =>
  document.getElementById("password-text-field").value;

let authBtn = document.getElementById("auth-btn");
let gotoLoginOrSignupButton = document.getElementById("login-or-signup");

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

function page(id) {
  const current_page_id = store.get("page").current;
  const current_page = document.getElementById(current_page_id);
  const target_page = document.getElementById(id);

  current_page.classList.add(["invisible"]);
  target_page.classList.remove(["invisible"]);
  store.set("page", { current: id });
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

// authentication proccesses --------------------------
function loginOrSignup() {
  eel.do_authentication(
    usernameTextField(),
    passwordTextField(),
    authType()
  )((res) => {
    if (res) {
      page("home");
    } else {
      if (authType === "login") alert("wrong username or password");
      else alert("username already exists");
    }
  });
}

function gotoLogin() {
  store.set("auth", { type: "login" });
  authBtn.textContent = "Login";
  gotoLoginOrSignupButton.textContent = "Create an account"
  page("auth");
}

function gotoSignup() {
  store.set("auth", { type: "signup" });
  authBtn.textContent = "Sign Up";
  gotoLoginOrSignupButton.textContent = "Go to login"
}

function gotoLoginOrToSignup() {
  let map = {
    signup: gotoLogin,
    login: gotoSignup,
  };
  console.log(authType());
  map[authType()]()
}

// end authentication proccesses ---------------------

function gotoHome() {
  page("home");
}

function gotoStats() {
  getCharts();
  // page("hide", "home");
  page("stats");
}
