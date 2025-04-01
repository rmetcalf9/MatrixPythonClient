 # MatrixPythonClient


TODO

- Finsih review of https://spec.matrix.org/v1.14/client-server-api/#standard-error-response
- Create a new user
- Add login endpoint for user providing access token in saas_club
- Endpoint creates a new user OR logs in as existing one


Design endpoint that login will need.
 - User ID (auth from token)
 - Room ID (Link to the room the user will want)
The endpoint is going to need to 
 - if user doesn't exist - create them (store password in cache)
 - log on the user using stored passwoed
 - if room does not exist create it
 - if user is not in room join them
 - return room id and access token to user

I need some kind of generic room user to be added to all rooms created this way.

Questions 
- can Admin see all the users on server
- can Admin see all the rooms on the server
- should I group rooms in any way? Spaces???
- e2e implications
