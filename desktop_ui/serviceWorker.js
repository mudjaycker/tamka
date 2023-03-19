cacheName = "Tamka-v1";
const files = [
  "./index.html",
  "./assets/images/Hexagon.svg",
  "./assets/style/style.css",
  "./third_parts/chart.js",
  "./third_parts/feather_icons.min.js",
  "./utils/storage.js",
  "./utils/element.js",
  "./utils/say-to-system.js",
  "./utils/say-to-user.js",
];
function setInCache() {
  caches.open(cacheName).then((result) => {
    result.addAll(files);
  });
}

self.addEventListener("install", (e) => {
  caches.match(e.request).then((result) => result);
});
