setTimeout(() => {
  let storage = new InStore();
  let language = storage.get("language").type;

  const ctx = document.getElementById("myChart");

  let language_type = language + "_language";
  let { easy_qty, total_qty, medium_qty, hard_qty } =
    storage.get(language_type);

  let languageMap = {
    français: {
      easy: "facile",
      medium: "moyen",
      hard: "difficile",
      title: "Statistiques de Prononciation",
    },

    english: {
      easy: "easy",
      medium: "medium",
      hard: "hard",
      title: "Pronounciation Statistics",
    },
  };

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: [
        languageMap[language].easy,
        languageMap[language].medium,
        languageMap[language].hard,
      ],
      datasets: [
        {
          label: languageMap[language].title,
          data: [
            (easy_qty * 100) / total_qty,
            (medium_qty * 100) / total_qty,
            (hard_qty * 100) / total_qty,
          ],
          backgroundColor: [
            "rgba(75, 192, 192, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgb(255, 99, 132, 0.2)",
          ],
          borderColor: [
            "rgb(75, 192, 192)",
            "rgb(255, 159, 64)",
            "rgb(255, 99, 132)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          min: 0,
          max: 100,
          ticks: {
            callback: function (value, index, values) {
              return value + " %";
            },
          },
        },
      },
      elements: {
        line: {
          borderWidth: 3,
        },
      },
    },
  });
}, 1000);
