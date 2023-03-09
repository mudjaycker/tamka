setTimeout(() => {
  let storage = new InStore();
  const ctx = document.getElementById("myChart");
  let language_type = storage.get("language").type + "_language";
  let { easy_qty, total_qty, medium_qty, hard_qty } =
    storage.get(language_type);

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["easy", "medium", "hard"],
      datasets: [
        {
          label: "Pronounciation Statistics",
          data: [
            easy_qty / total_qty,
            medium_qty / total_qty,
            hard_qty / total_qty,
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
        },
      },
      elements: {
        line: {
          borderWidth: 3,
        },
      },
    },
  });
}, 1700);
