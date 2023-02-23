class InStore {
  get(dataname) {
    return JSON.parse(localStorage.getItem(dataname));
  }

  set(dataname, value) {
    localStorage.setItem(dataname, JSON.stringify(value));
  }

  remove(dataname) {
    localStorage.removeItem(dataname);
  }
}
