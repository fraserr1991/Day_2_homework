users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jonathans_twitter_handle = users["Jonathan"]["twitter"]
print(jonathans_twitter_handle)

# 2. Get Erik's hometown
eriks_hometown = users["Erik"]["home_town"]
print(eriks_hometown)
# 3. Get the list of Erik's lottery numbers
eriks_lottery_numbers = users["Erik"]["lottery_numbers"]
print(eriks_lottery_numbers)

# 4. Get the species of Avril's pet Monty
avrils_pet = users["Avril"]["pets"][0]["species"]
print(avrils_pet)

# 5. Get the smallest of Erik's lottery numbers
eriks_lottery_numbers.sort()
print(eriks_lottery_numbers[0])

# 6. Return an list of Avril's lottery numbers that are even
even_numbers = 0

avrils_lottery_numbers = users["Avril"]["lottery_numbers"]
for lottery_number in avrils_lottery_numbers:
  even_numbers += lottery_number % 2

print(even_numbers)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# eriks_lottery_numbers2 = users["Erik"]["lottery_numbers"]
# eriks_lottery_numbers2.append(7)
# print(eriks_lottery_numbers2)
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh 
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"

eriks_dog = {
  "name" : "fluffy", "species" : "dog"
  }

users["Erik"]["pets"].append(eriks_dog)
print(users["Erik"]["pets"])

# # 10. Add another person to the users dictionary
users["John"] = {
"twitter" : "twitter name",
"lottery_numbers" : [4,5,6,7,8],
"home_town" : "Edinburgh",
"pets" : [ 
    {
    "name" : "Dave",
    "species" : "dog"
    }
  ]
}
print(users["John"])
