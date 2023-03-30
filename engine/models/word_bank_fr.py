from copy import deepcopy
datas = {
    "français": {
        "easy": [
            "Unité Travail Progrès",
            "La vie est belle",
            "Dieu est grand",
        ],

        "medium": [
            "Grandir est un choix",
            "Vivre est un droit",
            "La vie humaine est sacrée",
            "La terre tourne autour du soleil"
        ],

        "hard": [
            "Le système solaire compte 9 planètes",
            "Les hommes mentent pas les chiffres",
            "Être négrophobe c'est rédouter de voir de la neige noire à noël",
        ]
    },
    "english": {
        "easy": [
            "Charity begins at home",
            "The train was late",
            "He had a great army"
        ],

        "medium": [
            "I waited for the train",
            "I am buying a new pair of shoes",
            "The earth is spherical"
        ],

        "hard": [
            "I looked for mother and father at the bus station",
            "There were many others who wanted to become king",
            "My brother sometimes forgets his keys"

        ]
    }
}
datas_copy = deepcopy(datas)