# Heroku Tutorial

Heroku is a hosting service that is popular for its ease of use and free tier.

## Quickstart

With reference from [Getting Started with Python](https://devcenter.heroku.com/articles/getting-started-with-python).

1. Install Heroku.
2. Login to Heroku Dashboard.
3. Login on command line interface (CLI) with `heroku login`.
4. Create an app on either Heroku Dashboard or CLI with `heroku create`.
5. In your git repository, run `heroku git:remote -a <project name>`
6. Create a procfile `Procfile`:
   1. There are various process types, e.g. `web`, `worker`.
   2. `web` is the only process type that can receive external HTTP traffic.
    ```
    web: python main.py
    ```
7. Create a `requirements.txt`.
8. Deploy with `git add .`, `git commit -m "<message>"`, `git push heroku master`.
9. Ensure running of 1 instance with `heroku ps:scale web=1`. This scales the number of web dynos to 1.
10. Open app with `heroku open`.
11. View logs with `heroku logs --tail`.
12. Check how many dynos are running using `heroku ps`.

## Deploy to Heroku Button
1. Create `app.json` in the **root** directory.
   ```
   {
     "name": "Node.js Sample",
     "description": "A barebones Node.js app using Express",
     "repository": "https://github.com/heroku/node-js-getting-started",
     "logo": "https://node-js-sample.herokuapp.com/node.png",
     "keywords": ["node", "express", "static"],
     "addons": ["runtime-dyno-metadata"]
   }
   ```
2. Heroku add-ons, custom environment variables or post-deploy scripts can be specified in `app.json` [too](https://devcenter.heroku.com/articles/app-json-schema).
3. Validate the `app.json` works by checking with:
   
   `https://heroku.com/deploy?template=https://github.com/heroku/node-js-getting-started/tree/master`
4. Add the button to markdown using:

   `[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/heroku/node-js-getting-started)`

5. Or add the button to HTML using:

   ```
   <a href="https://heroku.com/deploy?template=https://github.com/heroku/node-js-getting-started">
      <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
   </a>
   ```
6. This is how it looks: [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/heroku/node-js-getting-started)