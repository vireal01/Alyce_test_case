# Alyce_test_case
automated testing with selenium (python)

Underlying business rules:
* Business logic rule 1 - basket never can give more than 1 apple per minute
* Business logic rule 2 - user never can have apples with both odd and even ids  (use local app or http://hrtest.alycedev.com/users endpoint to check ids)

### Tests:
* Test one: "Free Apples" -> 5 sec pause -> Jonathan grabs apple1 -> 5 sec pause -> Adrian grabs apple2 -> 5 sec pause  -> Julie grabs apple3 -> 5 sec pause -> Jonathan grabs apple5 -> 5 sec pause -> Adrian grabs apple4 .

* Test two: "Free Apples" -> 5 sec pause -> Jonathan grabs apple1 -> 5 sec pause -> Jonathan grabs apple3 -> 5 sec pause  -> Jonathan grabs apple5 -> 5 sec pause -> Julie grabs apple2 -> 5 sec pause -> Julie grabs apple4.

* Test three: Check the pop-up message, if "Grab apple" was clicked without a 5-second pause.

* Test four: Check the pop-up message, if you're trying to take an apple from the empty basket.
