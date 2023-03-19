<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="background.css" />
    <link rel="stylesheet" href="./assets/style/style.css" />
    <script type="text/javascript" src="/eel.js"></script>
    <script src="./third_parts/chart.js"></script>
    <script src="./utils/storage.js"></script>
    <script src="./utils/element.js"></script>

    <title>Tamka</title>
  </head>

  <body>
    <div id="home">{% include "./components/conversations.html" %}</div>
    <div id="stats" class="stats invisible">
      {% include "./components/statiscs.html" %}
    </div>

    <script src="./utils/say-to-system.js"></script>
    <script src="./utils/say-to-user.js"></script>
    <script src="src/index.js"></script>
    <script src="./third_parts/feather_icons.min.js"></script>
    <script src="./serviceWorker.js"></script>

    <script>
      {% include "./utils/scripts.js" %}
      {% include "./utils/makeChart.js" %}
    </script>
    <script src="./setServiceWorker.js"></script>
  </body>
</html>
