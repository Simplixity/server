"""Database population script

This is going to jam some sweet sweet data into your mongo.
"""

from pymongo import MongoClient
import json


sample_users = json.loads("""
[
  {
    "last_name": "Doyle",
    "first_name": "Haley",
    "address": [
      {
        "street": "979 Jodie Court",
        "unit": "Apartment #450",
        "city": "Iola",
        "state": "Maine",
        "zip_code": 25619,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "ZENSOR",
      "address": [
        {
          "street": "506 Anna Court",
          "unit": "Apartment #484",
          "city": "Emory",
          "state": "Palau",
          "zip_code": 23091,
          "country": "USA"
        }
      ],
      "phones": [
        "(973) 433-2576",
        "(834) 484-2842"
      ],
      "emails": [
        "haleydoyle@zensor.com"
      ]
    },
    "social_security": 637380140,
    "race": "other",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1963-05-13",
    "emails": [
      "haleydoyle@zensor.com"
    ],
    "phones": [
      "(832) 551-2805",
      "(841) 438-2997"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Delaney",
    "first_name": "Hubbard",
    "address": [
      {
        "street": "566 Bouck Court",
        "unit": "Apartment #604",
        "city": "Kingstowne",
        "state": "Oregon",
        "zip_code": 93844,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "BIOHAB",
      "address": [
        {
          "street": "269 Columbus Place",
          "unit": "Apartment #734",
          "city": "Summertown",
          "state": "Utah",
          "zip_code": 24128,
          "country": "USA"
        }
      ],
      "phones": [
        "(947) 449-3864",
        "(810) 425-3647"
      ],
      "emails": [
        "hubbarddelaney@biohab.com"
      ]
    },
    "social_security": 812129806,
    "race": "white",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1968-08-04",
    "emails": [
      "hubbarddelaney@biohab.com"
    ],
    "phones": [
      "(943) 421-3661",
      "(836) 540-2719"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Bradley",
    "first_name": "Hannah",
    "address": [
      {
        "street": "503 Farragut Road",
        "unit": "Apartment #634",
        "city": "Waverly",
        "state": "Michigan",
        "zip_code": 52238,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "ENTHAZE",
      "address": [
        {
          "street": "955 President Street",
          "unit": "Apartment #723",
          "city": "Skyland",
          "state": "Louisiana",
          "zip_code": 51695,
          "country": "USA"
        }
      ],
      "phones": [
        "(912) 519-3717",
        "(932) 568-2585"
      ],
      "emails": [
        "hannahbradley@enthaze.com"
      ]
    },
    "social_security": 912269631,
    "race": "other",
    "sex": "female",
    "maritalStatus": "divorced",
    "birthdate": "1965-01-22",
    "emails": [
      "hannahbradley@enthaze.com"
    ],
    "phones": [
      "(847) 493-3902",
      "(817) 400-2404"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Roman",
    "first_name": "Olson",
    "address": [
      {
        "street": "823 Emmons Avenue",
        "unit": "Apartment #815",
        "city": "Salvo",
        "state": "Illinois",
        "zip_code": 51075,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "VIAGREAT",
      "address": [
        {
          "street": "607 Hendrickson Place",
          "unit": "Apartment #631",
          "city": "Wilmington",
          "state": "Kentucky",
          "zip_code": 75368,
          "country": "USA"
        }
      ],
      "phones": [
        "(836) 600-3456",
        "(867) 459-3562"
      ],
      "emails": [
        "olsonroman@viagreat.com"
      ]
    },
    "social_security": 777236175,
    "race": "asian",
    "sex": "male",
    "maritalStatus": "single",
    "birthdate": "1958-10-13",
    "emails": [
      "olsonroman@viagreat.com"
    ],
    "phones": [
      "(838) 403-3074",
      "(832) 442-3667"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Herring",
    "first_name": "Mathis",
    "address": [
      {
        "street": "107 Canton Court",
        "unit": "Apartment #305",
        "city": "Cobbtown",
        "state": "South Dakota",
        "zip_code": 24305,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "MITROC",
      "address": [
        {
          "street": "363 Chestnut Avenue",
          "unit": "Apartment #663",
          "city": "Longbranch",
          "state": "Oklahoma",
          "zip_code": 53590,
          "country": "USA"
        }
      ],
      "phones": [
        "(864) 425-2929",
        "(873) 488-3301"
      ],
      "emails": [
        "mathisherring@mitroc.com"
      ]
    },
    "social_security": 86062455,
    "race": "indian",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1986-08-29",
    "emails": [
      "mathisherring@mitroc.com"
    ],
    "phones": [
      "(964) 555-2929",
      "(955) 404-3618"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Banks",
    "first_name": "Mathews",
    "address": [
      {
        "street": "492 Kosciusko Street",
        "unit": "Apartment #757",
        "city": "Hondah",
        "state": "Virgin Islands",
        "zip_code": 11334,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "EXPOSA",
      "address": [
        {
          "street": "947 Ellery Street",
          "unit": "Apartment #362",
          "city": "Hoehne",
          "state": "Guam",
          "zip_code": 94858,
          "country": "USA"
        }
      ],
      "phones": [
        "(832) 410-3096",
        "(952) 489-3780"
      ],
      "emails": [
        "mathewsbanks@exposa.com"
      ]
    },
    "social_security": 573288757,
    "race": "other",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1976-07-27",
    "emails": [
      "mathewsbanks@exposa.com"
    ],
    "phones": [
      "(971) 501-2285",
      "(894) 437-2176"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "allergy",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Farley",
    "first_name": "Becky",
    "address": [
      {
        "street": "352 Royce Place",
        "unit": "Apartment #347",
        "city": "Harold",
        "state": "Wisconsin",
        "zip_code": 69983,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "COMVOY",
      "address": [
        {
          "street": "590 Wythe Avenue",
          "unit": "Apartment #190",
          "city": "Robinette",
          "state": "Delaware",
          "zip_code": 76174,
          "country": "USA"
        }
      ],
      "phones": [
        "(886) 562-2949",
        "(942) 518-2951"
      ],
      "emails": [
        "beckyfarley@comvoy.com"
      ]
    },
    "social_security": 247997564,
    "race": "latino",
    "sex": "female",
    "maritalStatus": "divorced",
    "birthdate": "1953-09-26",
    "emails": [
      "beckyfarley@comvoy.com"
    ],
    "phones": [
      "(937) 458-2801",
      "(877) 478-2448"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Grimes",
    "first_name": "Rosanne",
    "address": [
      {
        "street": "310 Manhattan Court",
        "unit": "Apartment #337",
        "city": "Sunnyside",
        "state": "Nevada",
        "zip_code": 61587,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "KOG",
      "address": [
        {
          "street": "831 Union Street",
          "unit": "Apartment #948",
          "city": "Beaulieu",
          "state": "Indiana",
          "zip_code": 88100,
          "country": "USA"
        }
      ],
      "phones": [
        "(850) 489-2699",
        "(865) 432-3461"
      ],
      "emails": [
        "rosannegrimes@kog.com"
      ]
    },
    "social_security": 736792352,
    "race": "asian",
    "sex": "female",
    "maritalStatus": "single",
    "birthdate": "2000-06-10",
    "emails": [
      "rosannegrimes@kog.com"
    ],
    "phones": [
      "(906) 566-2562",
      "(921) 513-2424"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Hahn",
    "first_name": "Evangelina",
    "address": [
      {
        "street": "945 Newport Street",
        "unit": "Apartment #206",
        "city": "Osage",
        "state": "Pennsylvania",
        "zip_code": 36223,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "KINDALOO",
      "address": [
        {
          "street": "256 Wakeman Place",
          "unit": "Apartment #930",
          "city": "Hanover",
          "state": "Virginia",
          "zip_code": 36673,
          "country": "USA"
        }
      ],
      "phones": [
        "(970) 500-3631",
        "(952) 576-2704"
      ],
      "emails": [
        "evangelinahahn@kindaloo.com"
      ]
    },
    "social_security": 365438588,
    "race": "latino",
    "sex": "female",
    "maritalStatus": "single",
    "birthdate": "2005-12-05",
    "emails": [
      "evangelinahahn@kindaloo.com"
    ],
    "phones": [
      "(914) 490-3388",
      "(964) 462-2326"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "disease",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Cross",
    "first_name": "Willa",
    "address": [
      {
        "street": "461 Wyckoff Street",
        "unit": "Apartment #552",
        "city": "Brownsville",
        "state": "Florida",
        "zip_code": 14483,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "STRALUM",
      "address": [
        {
          "street": "299 Stockholm Street",
          "unit": "Apartment #669",
          "city": "Spokane",
          "state": "Northern Mariana Islands",
          "zip_code": 29254,
          "country": "USA"
        }
      ],
      "phones": [
        "(857) 422-2795",
        "(980) 454-3223"
      ],
      "emails": [
        "willacross@stralum.com"
      ]
    },
    "social_security": 711554551,
    "race": "black",
    "sex": "female",
    "maritalStatus": "married",
    "birthdate": "1940-07-20",
    "emails": [
      "willacross@stralum.com"
    ],
    "phones": [
      "(900) 573-2713",
      "(880) 456-3908"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "disease",
        "code": "herpes"
      }
    ]
  },
  {
    "last_name": "Carter",
    "first_name": "Clark",
    "address": [
      {
        "street": "325 Bergen Avenue",
        "unit": "Apartment #117",
        "city": "Heil",
        "state": "South Carolina",
        "zip_code": 23212,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "INCUBUS",
      "address": [
        {
          "street": "361 Greenwood Avenue",
          "unit": "Apartment #939",
          "city": "Yonah",
          "state": "Alabama",
          "zip_code": 28714,
          "country": "USA"
        }
      ],
      "phones": [
        "(958) 470-2377",
        "(826) 484-3884"
      ],
      "emails": [
        "clarkcarter@incubus.com"
      ]
    },
    "social_security": 894683878,
    "race": "indian",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1994-07-03",
    "emails": [
      "clarkcarter@incubus.com"
    ],
    "phones": [
      "(940) 584-3174",
      "(866) 484-3165"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Guerra",
    "first_name": "Sanchez",
    "address": [
      {
        "street": "179 Melrose Street",
        "unit": "Apartment #935",
        "city": "Dexter",
        "state": "Ohio",
        "zip_code": 25958,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "SOFTMICRO",
      "address": [
        {
          "street": "272 Bainbridge Street",
          "unit": "Apartment #393",
          "city": "Boykin",
          "state": "Alaska",
          "zip_code": 28994,
          "country": "USA"
        }
      ],
      "phones": [
        "(900) 518-2320",
        "(893) 570-2069"
      ],
      "emails": [
        "sanchezguerra@softmicro.com"
      ]
    },
    "social_security": 676204947,
    "race": "white",
    "sex": "male",
    "maritalStatus": "married",
    "birthdate": "1958-11-23",
    "emails": [
      "sanchezguerra@softmicro.com"
    ],
    "phones": [
      "(813) 453-2722",
      "(851) 439-3788"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "herpes"
      }
    ]
  },
  {
    "last_name": "Larsen",
    "first_name": "Peggy",
    "address": [
      {
        "street": "390 Ludlam Place",
        "unit": "Apartment #128",
        "city": "Wescosville",
        "state": "American Samoa",
        "zip_code": 60734,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "GLOBOIL",
      "address": [
        {
          "street": "638 Manor Court",
          "unit": "Apartment #605",
          "city": "Snyderville",
          "state": "Iowa",
          "zip_code": 35084,
          "country": "USA"
        }
      ],
      "phones": [
        "(974) 458-2850",
        "(957) 484-3285"
      ],
      "emails": [
        "peggylarsen@globoil.com"
      ]
    },
    "social_security": 928650094,
    "race": "asian",
    "sex": "female",
    "maritalStatus": "single",
    "birthdate": "1958-07-12",
    "emails": [
      "peggylarsen@globoil.com"
    ],
    "phones": [
      "(988) 474-2281",
      "(818) 414-3729"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "herpes"
      }
    ]
  },
  {
    "last_name": "Sandoval",
    "first_name": "Stokes",
    "address": [
      {
        "street": "405 Danforth Street",
        "unit": "Apartment #917",
        "city": "Fostoria",
        "state": "North Dakota",
        "zip_code": 49669,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "ZENTURY",
      "address": [
        {
          "street": "423 Imlay Street",
          "unit": "Apartment #655",
          "city": "Carlos",
          "state": "Arizona",
          "zip_code": 69313,
          "country": "USA"
        }
      ],
      "phones": [
        "(914) 534-2127",
        "(878) 512-3139"
      ],
      "emails": [
        "stokessandoval@zentury.com"
      ]
    },
    "social_security": 747073531,
    "race": "asian",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1942-12-07",
    "emails": [
      "stokessandoval@zentury.com"
    ],
    "phones": [
      "(858) 460-2980",
      "(967) 525-3610"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Merrill",
    "first_name": "Kimberly",
    "address": [
      {
        "street": "629 Montana Place",
        "unit": "Apartment #845",
        "city": "Masthope",
        "state": "Idaho",
        "zip_code": 26564,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "ISOLOGIA",
      "address": [
        {
          "street": "463 Commercial Street",
          "unit": "Apartment #142",
          "city": "Fruitdale",
          "state": "New York",
          "zip_code": 79742,
          "country": "USA"
        }
      ],
      "phones": [
        "(960) 495-2138",
        "(844) 597-2062"
      ],
      "emails": [
        "kimberlymerrill@isologia.com"
      ]
    },
    "social_security": 747339979,
    "race": "other",
    "sex": "female",
    "maritalStatus": "divorced",
    "birthdate": "2007-02-06",
    "emails": [
      "kimberlymerrill@isologia.com"
    ],
    "phones": [
      "(975) 416-2637",
      "(940) 540-3117"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Buckner",
    "first_name": "Natalia",
    "address": [
      {
        "street": "736 Scholes Street",
        "unit": "Apartment #231",
        "city": "Washington",
        "state": "New Jersey",
        "zip_code": 87203,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "KINETICUT",
      "address": [
        {
          "street": "964 Lawn Court",
          "unit": "Apartment #159",
          "city": "Cavalero",
          "state": "West Virginia",
          "zip_code": 54764,
          "country": "USA"
        }
      ],
      "phones": [
        "(912) 518-2516",
        "(995) 436-2751"
      ],
      "emails": [
        "nataliabuckner@kineticut.com"
      ]
    },
    "social_security": 741618508,
    "race": "latino",
    "sex": "female",
    "maritalStatus": "divorced",
    "birthdate": "1980-11-20",
    "emails": [
      "nataliabuckner@kineticut.com"
    ],
    "phones": [
      "(963) 479-3285",
      "(941) 596-3496"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "allergy",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Maldonado",
    "first_name": "Paulette",
    "address": [
      {
        "street": "946 Berriman Street",
        "unit": "Apartment #827",
        "city": "Joes",
        "state": "Marshall Islands",
        "zip_code": 69224,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "ZUVY",
      "address": [
        {
          "street": "553 Ridge Boulevard",
          "unit": "Apartment #658",
          "city": "Sexton",
          "state": "North Carolina",
          "zip_code": 88204,
          "country": "USA"
        }
      ],
      "phones": [
        "(815) 501-3120",
        "(897) 572-2105"
      ],
      "emails": [
        "paulettemaldonado@zuvy.com"
      ]
    },
    "social_security": 672513969,
    "race": "latino",
    "sex": "female",
    "maritalStatus": "married",
    "birthdate": "1993-09-04",
    "emails": [
      "paulettemaldonado@zuvy.com"
    ],
    "phones": [
      "(868) 536-2410",
      "(870) 449-3289"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Mullins",
    "first_name": "Foley",
    "address": [
      {
        "street": "737 Maple Street",
        "unit": "Apartment #745",
        "city": "Coventry",
        "state": "Montana",
        "zip_code": 15690,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "COSMOSIS",
      "address": [
        {
          "street": "430 Chester Avenue",
          "unit": "Apartment #965",
          "city": "Orviston",
          "state": "Nebraska",
          "zip_code": 38939,
          "country": "USA"
        }
      ],
      "phones": [
        "(928) 476-2156",
        "(894) 497-3112"
      ],
      "emails": [
        "foleymullins@cosmosis.com"
      ]
    },
    "social_security": 640203541,
    "race": "asian",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1936-03-03",
    "emails": [
      "foleymullins@cosmosis.com"
    ],
    "phones": [
      "(956) 597-2117",
      "(837) 577-3903"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Evans",
    "first_name": "Shari",
    "address": [
      {
        "street": "523 Quay Street",
        "unit": "Apartment #507",
        "city": "Johnsonburg",
        "state": "Mississippi",
        "zip_code": 93810,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "ENTROFLEX",
      "address": [
        {
          "street": "520 Prince Street",
          "unit": "Apartment #801",
          "city": "Day",
          "state": "Colorado",
          "zip_code": 82816,
          "country": "USA"
        }
      ],
      "phones": [
        "(858) 436-2407",
        "(800) 449-3266"
      ],
      "emails": [
        "sharievans@entroflex.com"
      ]
    },
    "social_security": 75837073,
    "race": "other",
    "sex": "female",
    "maritalStatus": "married",
    "birthdate": "1951-08-16",
    "emails": [
      "sharievans@entroflex.com"
    ],
    "phones": [
      "(978) 566-3485",
      "(880) 494-2676"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "English",
    "first_name": "Latasha",
    "address": [
      {
        "street": "328 Canal Avenue",
        "unit": "Apartment #628",
        "city": "Otranto",
        "state": "Vermont",
        "zip_code": 54236,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "CAPSCREEN",
      "address": [
        {
          "street": "673 Gelston Avenue",
          "unit": "Apartment #916",
          "city": "Cade",
          "state": "California",
          "zip_code": 12270,
          "country": "USA"
        }
      ],
      "phones": [
        "(829) 541-2489",
        "(892) 403-2405"
      ],
      "emails": [
        "latashaenglish@capscreen.com"
      ]
    },
    "social_security": 833359678,
    "race": "white",
    "sex": "female",
    "maritalStatus": "divorced",
    "birthdate": "1944-04-14",
    "emails": [
      "latashaenglish@capscreen.com"
    ],
    "phones": [
      "(998) 554-3575",
      "(891) 549-2009"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Webb",
    "first_name": "Kristi",
    "address": [
      {
        "street": "320 Box Street",
        "unit": "Apartment #885",
        "city": "Manitou",
        "state": "Arkansas",
        "zip_code": 62291,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "UNQ",
      "address": [
        {
          "street": "117 Friel Place",
          "unit": "Apartment #532",
          "city": "Lithium",
          "state": "Wyoming",
          "zip_code": 17433,
          "country": "USA"
        }
      ],
      "phones": [
        "(825) 567-3804",
        "(977) 455-3579"
      ],
      "emails": [
        "kristiwebb@unq.com"
      ]
    },
    "social_security": 355389887,
    "race": "white",
    "sex": "female",
    "maritalStatus": "single",
    "birthdate": "1937-06-01",
    "emails": [
      "kristiwebb@unq.com"
    ],
    "phones": [
      "(838) 423-2874",
      "(923) 417-3279"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "herpes"
      }
    ]
  },
  {
    "last_name": "Dalton",
    "first_name": "Livingston",
    "address": [
      {
        "street": "479 Vernon Avenue",
        "unit": "Apartment #560",
        "city": "Succasunna",
        "state": "New Hampshire",
        "zip_code": 69194,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "TYPHONICA",
      "address": [
        {
          "street": "609 Rose Street",
          "unit": "Apartment #991",
          "city": "Herlong",
          "state": "Washington",
          "zip_code": 56587,
          "country": "USA"
        }
      ],
      "phones": [
        "(963) 430-2610",
        "(861) 454-2477"
      ],
      "emails": [
        "livingstondalton@typhonica.com"
      ]
    },
    "social_security": 92237468,
    "race": "black",
    "sex": "male",
    "maritalStatus": "single",
    "birthdate": "1986-03-27",
    "emails": [
      "livingstondalton@typhonica.com"
    ],
    "phones": [
      "(990) 459-3593",
      "(822) 441-2079"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Petersen",
    "first_name": "Medina",
    "address": [
      {
        "street": "588 Fairview Place",
        "unit": "Apartment #932",
        "city": "Suitland",
        "state": "Missouri",
        "zip_code": 10975,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "MAROPTIC",
      "address": [
        {
          "street": "300 Newkirk Placez",
          "unit": "Apartment #302",
          "city": "Imperial",
          "state": "Maryland",
          "zip_code": 61234,
          "country": "USA"
        }
      ],
      "phones": [
        "(828) 600-2073",
        "(835) 584-2843"
      ],
      "emails": [
        "medinapetersen@maroptic.com"
      ]
    },
    "social_security": 91472103,
    "race": "asian",
    "sex": "male",
    "maritalStatus": "married",
    "birthdate": "1963-11-12",
    "emails": [
      "medinapetersen@maroptic.com"
    ],
    "phones": [
      "(908) 414-3498",
      "(981) 479-3393"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Medina",
    "first_name": "Pruitt",
    "address": [
      {
        "street": "869 Conduit Boulevard",
        "unit": "Apartment #453",
        "city": "Robbins",
        "state": "Federated States Of Micronesia",
        "zip_code": 60250,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "OPTICALL",
      "address": [
        {
          "street": "597 Boynton Place",
          "unit": "Apartment #317",
          "city": "Berlin",
          "state": "Tennessee",
          "zip_code": 18941,
          "country": "USA"
        }
      ],
      "phones": [
        "(842) 527-3844",
        "(892) 574-3437"
      ],
      "emails": [
        "pruittmedina@opticall.com"
      ]
    },
    "social_security": 547481718,
    "race": "white",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1932-11-28",
    "emails": [
      "pruittmedina@opticall.com"
    ],
    "phones": [
      "(915) 429-2297",
      "(970) 583-2311"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "disease",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Collins",
    "first_name": "Burke",
    "address": [
      {
        "street": "121 Bushwick Avenue",
        "unit": "Apartment #652",
        "city": "Newry",
        "state": "New Mexico",
        "zip_code": 19807,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "INTERFIND",
      "address": [
        {
          "street": "327 Hinckley Place",
          "unit": "Apartment #548",
          "city": "Belvoir",
          "state": "Hawaii",
          "zip_code": 49470,
          "country": "USA"
        }
      ],
      "phones": [
        "(963) 513-2090",
        "(839) 543-3176"
      ],
      "emails": [
        "burkecollins@interfind.com"
      ]
    },
    "social_security": 330459621,
    "race": "latino",
    "sex": "male",
    "maritalStatus": "single",
    "birthdate": "1976-12-06",
    "emails": [
      "burkecollins@interfind.com"
    ],
    "phones": [
      "(848) 433-2409",
      "(870) 574-3837"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Carey",
    "first_name": "Bonnie",
    "address": [
      {
        "street": "512 Woodbine Street",
        "unit": "Apartment #178",
        "city": "Malott",
        "state": "Connecticut",
        "zip_code": 77559,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "EMPIRICA",
      "address": [
        {
          "street": "787 Clifton Place",
          "unit": "Apartment #305",
          "city": "Healy",
          "state": "Minnesota",
          "zip_code": 14774,
          "country": "USA"
        }
      ],
      "phones": [
        "(851) 581-3508",
        "(974) 482-3176"
      ],
      "emails": [
        "bonniecarey@empirica.com"
      ]
    },
    "social_security": 196974749,
    "race": "black",
    "sex": "female",
    "maritalStatus": "single",
    "birthdate": "1931-11-18",
    "emails": [
      "bonniecarey@empirica.com"
    ],
    "phones": [
      "(913) 599-2759",
      "(879) 490-2672"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "herpes"
      }
    ]
  },
  {
    "last_name": "Walsh",
    "first_name": "Cooley",
    "address": [
      {
        "street": "707 Jackson Place",
        "unit": "Apartment #119",
        "city": "Eastvale",
        "state": "Georgia",
        "zip_code": 97613,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "AQUASURE",
      "address": [
        {
          "street": "469 Metrotech Courtr",
          "unit": "Apartment #107",
          "city": "Delwood",
          "state": "Texas",
          "zip_code": 66793,
          "country": "USA"
        }
      ],
      "phones": [
        "(808) 539-2365",
        "(965) 554-2267"
      ],
      "emails": [
        "cooleywalsh@aquasure.com"
      ]
    },
    "social_security": 760125291,
    "race": "latino",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1953-06-11",
    "emails": [
      "cooleywalsh@aquasure.com"
    ],
    "phones": [
      "(893) 506-3290",
      "(927) 469-2619"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Gardner",
    "first_name": "Wilkinson",
    "address": [
      {
        "street": "840 Bergen Place",
        "unit": "Apartment #257",
        "city": "Murillo",
        "state": "Massachusetts",
        "zip_code": 56916,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "BEDLAM",
      "address": [
        {
          "street": "557 Amboy Street",
          "unit": "Apartment #332",
          "city": "Datil",
          "state": "Kansas",
          "zip_code": 87409,
          "country": "USA"
        }
      ],
      "phones": [
        "(907) 454-2134",
        "(845) 444-3109"
      ],
      "emails": [
        "wilkinsongardner@bedlam.com"
      ]
    },
    "social_security": 59951642,
    "race": "asian",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1932-10-30",
    "emails": [
      "wilkinsongardner@bedlam.com"
    ],
    "phones": [
      "(852) 591-3128",
      "(938) 452-3873"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "disease",
        "code": "herpes"
      }
    ]
  },
  {
    "last_name": "Payne",
    "first_name": "Bush",
    "address": [
      {
        "street": "869 Cedar Street",
        "unit": "Apartment #308",
        "city": "Tolu",
        "state": "Puerto Rico",
        "zip_code": 73608,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "XINWARE",
      "address": [
        {
          "street": "665 Seton Place",
          "unit": "Apartment #169",
          "city": "Caroline",
          "state": "District Of Columbia",
          "zip_code": 68364,
          "country": "USA"
        }
      ],
      "phones": [
        "(951) 486-3509",
        "(997) 459-3136"
      ],
      "emails": [
        "bushpayne@xinware.com"
      ]
    },
    "social_security": 790345881,
    "race": "white",
    "sex": "male",
    "maritalStatus": "married",
    "birthdate": "1986-04-04",
    "emails": [
      "bushpayne@xinware.com"
    ],
    "phones": [
      "(928) 561-2537",
      "(835) 546-2409"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "herpes"
      }
    ]
  },
  {
    "last_name": "Estrada",
    "first_name": "Bette",
    "address": [
      {
        "street": "743 Portland Avenue",
        "unit": "Apartment #328",
        "city": "Unionville",
        "state": "Maine",
        "zip_code": 12638,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "PRISMATIC",
      "address": [
        {
          "street": "722 Montgomery Street",
          "unit": "Apartment #876",
          "city": "Alafaya",
          "state": "Palau",
          "zip_code": 35879,
          "country": "USA"
        }
      ],
      "phones": [
        "(935) 586-3143",
        "(934) 531-2766"
      ],
      "emails": [
        "betteestrada@prismatic.com"
      ]
    },
    "social_security": 315720673,
    "race": "black",
    "sex": "female",
    "maritalStatus": "divorced",
    "birthdate": "1949-09-22",
    "emails": [
      "betteestrada@prismatic.com"
    ],
    "phones": [
      "(906) 453-2209",
      "(918) 565-4000"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "gonorrhea"
      }
    ]
  },
  {
    "last_name": "Malone",
    "first_name": "Cooke",
    "address": [
      {
        "street": "904 Times Placez",
        "unit": "Apartment #222",
        "city": "Southmont",
        "state": "Oregon",
        "zip_code": 52596,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "MULTRON",
      "address": [
        {
          "street": "385 Liberty Avenue",
          "unit": "Apartment #952",
          "city": "Barstow",
          "state": "Utah",
          "zip_code": 15427,
          "country": "USA"
        }
      ],
      "phones": [
        "(835) 403-3753",
        "(896) 484-3422"
      ],
      "emails": [
        "cookemalone@multron.com"
      ]
    },
    "social_security": 799690374,
    "race": "indian",
    "sex": "male",
    "maritalStatus": "single",
    "birthdate": "1937-06-18",
    "emails": [
      "cookemalone@multron.com"
    ],
    "phones": [
      "(897) 528-3314",
      "(974) 520-3747"
    ],
    "orgonDonor": true,
    "conditions": [
      {
        "type": "allergy",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Atkins",
    "first_name": "Johanna",
    "address": [
      {
        "street": "312 Post Court",
        "unit": "Apartment #206",
        "city": "Lafferty",
        "state": "Michigan",
        "zip_code": 55761,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "ENORMO",
      "address": [
        {
          "street": "101 Dakota Place",
          "unit": "Apartment #563",
          "city": "Indio",
          "state": "Louisiana",
          "zip_code": 85981,
          "country": "USA"
        }
      ],
      "phones": [
        "(926) 563-2551",
        "(910) 492-2990"
      ],
      "emails": [
        "johannaatkins@enormo.com"
      ]
    },
    "social_security": 731116896,
    "race": "indian",
    "sex": "female",
    "maritalStatus": "divorced",
    "birthdate": "1967-11-30",
    "emails": [
      "johannaatkins@enormo.com"
    ],
    "phones": [
      "(867) 464-3188",
      "(875) 525-3782"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "allergy",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Chandler",
    "first_name": "Carolina",
    "address": [
      {
        "street": "971 Cleveland Street",
        "unit": "Apartment #624",
        "city": "Waterford",
        "state": "Illinois",
        "zip_code": 95245,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "MUSANPOLY",
      "address": [
        {
          "street": "635 Riverdale Avenue",
          "unit": "Apartment #679",
          "city": "Boyd",
          "state": "Kentucky",
          "zip_code": 51899,
          "country": "USA"
        }
      ],
      "phones": [
        "(819) 454-2111",
        "(891) 555-3743"
      ],
      "emails": [
        "carolinachandler@musanpoly.com"
      ]
    },
    "social_security": 239984940,
    "race": "black",
    "sex": "female",
    "maritalStatus": "single",
    "birthdate": "1931-03-11",
    "emails": [
      "carolinachandler@musanpoly.com"
    ],
    "phones": [
      "(880) 559-3427",
      "(902) 454-3431"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "allergy",
        "code": "crabs"
      }
    ]
  },
  {
    "last_name": "Pennington",
    "first_name": "Frye",
    "address": [
      {
        "street": "483 Ditmars Street",
        "unit": "Apartment #987",
        "city": "Onton",
        "state": "South Dakota",
        "zip_code": 72760,
        "country": "USA"
      }
    ],
    "employer": {
      "name": "DIGIRANG",
      "address": [
        {
          "street": "572 Pierrepont Place",
          "unit": "Apartment #761",
          "city": "Waiohinu",
          "state": "Oklahoma",
          "zip_code": 97843,
          "country": "USA"
        }
      ],
      "phones": [
        "(834) 577-2913",
        "(983) 569-2097"
      ],
      "emails": [
        "fryepennington@digirang.com"
      ]
    },
    "social_security": 520302004,
    "race": "asian",
    "sex": "male",
    "maritalStatus": "divorced",
    "birthdate": "1962-08-21",
    "emails": [
      "fryepennington@digirang.com"
    ],
    "phones": [
      "(836) 478-3808",
      "(899) 468-2980"
    ],
    "orgonDonor": false,
    "conditions": [
      {
        "type": "disease",
        "code": "herpes"
      }
    ]
  }
]
""")



if __name__ == '__main__':
    print 'Simplixity Data Insertion'

    client = MongoClient()
    db = client['simplixity']

    user = db.user
    user.remove(None)
    result = user.insert(sample_users)
    print 'Inserted %s users' % len(result)



