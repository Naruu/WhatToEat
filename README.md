# WhatToEat
#### Menu/reciepe recommendation website based on seasonal ingredients & sale product.

#### Goal : Build a website that recommends menu/food based on the seasonal ingredients, and sale information.
ex) Apple is fresh in Autummn -> recommend apple pie  
ex) Cream cheese is on sale -> recommend cream cheese apple tart

  
# Steps
## 1. Build DB for food, ingredient.
1) ingredient - month/season (http://foodsafetykorea.go.kr/portal/sensuousmenu/recipeNtrtList.do)
2) menu - ingredient

## 2. get sale inforamtion
1) garakprice - http://www.garakprice.com/ : price at garak marekt
- get the list of ingredients that is cheaper than yesterday
2) several supermarkets : homeplus(/emart/lotte mart. default : homeplus -> but later let user select the supermarket)
- get the list of items that are on sale
=> once get the result, save it on the database

## 3. Make an website.
1) click "get seasonal ingredient" -> show list of recommended seasonal ingredient(with photo/later add nutritional information)
2) show ingredients that are on sale
3) suggest menu/food based on the combination of seasonal ingredient and on sale product.

#### +)
4) show recipe/related restaurant(nearby)
5) include/exclude this ingredient option
6) filter option : pick one ingredient : only show menus with selected ingredients

  
# Additionals
1) recipe/suggestion of restaurants nearby.
2) recommendation with consideration on the weather/temperature.
3) archive recipe/restaurant function
