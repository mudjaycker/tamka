cacheName = "Tamka-v1";
const files = ["./index.html"];
function setInCache() {
  caches.open(cacheName).then((result) => {
    result.addAll(files)
  });
}