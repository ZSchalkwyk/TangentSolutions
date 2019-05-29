# Tangent Solutions

Hi guys, here's the final documentation thingy for the assessment.

## Technology used

- Docker + Docker-Compose

  - Docker because you asked, docker-compose because YAML is pretty

- Postman + Newman

  - For testing the api and running the test using the command line.

  - <https://www.getpostman.com/>

  - <https://learning.getpostman.com/docs/postman/collection_runs/command_line_integration_with_newman/>

  - I didn't include the running this in the container, the collection should be run after running "docker-compose up"

  - The command to run is:

    - ```bash
      newman run Demo.postman_collection.json
      ```

- I used Hug to make the api because I like it as well as it's one of the faster python based APIs (Based off of falcon)
- As for creating documentation, I'm doing it using markdown haha
- Swagger docs for 2 calls seems a little pointless
- I used Sqlite to make the app more contained
- For serving the app, I'll be using ngrok.
  - <https://ngrok.com/>
  - I'll be serving it from my local machine so please let me know if you guys want to test it and I'll serve the app to an accessible URL for you guys.

## Api calls

### /

The root call is used to init the db and to test if the project is "working".

It's a get call with no required paramaters.

### /leave

Is a post call which creates a leave entity in the database.

Parameters:

- start_date
- end_date
- employee_pk

All are required.

If the system returns a 400, something went wrong...

I added handling for all cases I could think of.

If it returns 200 leave was submitted with days of leave calculated and set to status of "New"



## Final

Sorry for the long wait, this were exploding at work. If anything else is need please feel free to call or mail.



xxx

Z