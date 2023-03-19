const print = console.log;
if ("serviceWorker" in navigator) {
  navigator.serviceWorker
    .register("/serviceWorker.js")
    .then(() => print("sw registered"))
    .catch((e) => print("got registration error =>", e));
}
