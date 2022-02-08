- [Placeholder Title](#placeholder-title)
- [Project Introduction](#project-introduction)
- [User Experience](#user-experience)
  * [User Stories](#user-stories)
- [Site Design](#site-design)
  * [Composition](#composition)
  * [Colour Scheme](#colour-scheme)
  * [Wireframes](#wireframes)
    + [Balsamiq Wireframes](#balsamiq-wireframes)
    + [PC [2560 x 1440]](#pc--2560-x-1440-)
    + [Laptop [1366 x 768]](#laptop--1366-x-768-)
    + [Tablet](#tablet)
    + [Mobile](#mobile)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Coding Languages](#coding-languages)
  * [HTML5](https://en.wikipedia.org/wiki/HTML5). - Site structure.
  * [CSS3](https://en.wikipedia.org/wiki/CSS). - Site Design.
  * [Python3](https://en.wikipedia.org/wiki/Python_(programming_language)). - Used with Django.
- [Libraries and Frameworks](#libraries-and-tools)
  * [Django](https://www.djangoproject.com/) - Framework used to build the site and admin page.
  * [HerokuSQL](https://www.heroku.com/postgres) - Database used in the project.
  * [Python OS](https://docs.python.org/3/library/os.html). - Used for ```os.environ```.
  * [Markdown](https://en.wikipedia.org/wiki/Markdown). - Used for creating README.md document.
  * [Bootstrap](https://getbootstrap.com/). - Used for styling the site a framework addition to CSS3.
- [Testing](#testing)
  * [Validation](#validation)
  * [Bugs](#bugs)
- [Site Deployment](#site-deployment)
  * Deploying project to Heroku - [Live Link](https://project4-matt-ci.herokuapp.com/)
- [Cloning using Github](#cloning-using-Github)

    [Repository Link](https://github.com/Matex600/social-edit-matt)
    * Log in to Github.
    * Access my repository using above link.
    * In repository page select code next to Gitpod.
    * Button, make sure HTTPS is selected.
    * Click on the copy button on the right (Two overlapping squares)
    * Open a new workspace in Gitpod.
    * Once the workspace loads in the terminal type.
        ```
        git clone https://github.com/Matex600/social-edit-matt
        ```

- [Forking using Github](#Forking-using-Github)
    * You can contribute to this project without affecting the main branch with the following steps.
  1. Navigate to github repositores select this [repository](https://github.com/Matex600/social-edit-matt).
  2. On the right of the repository name you will find the fork button next to star and watch buttons.
  3. Pressing said button will create a copy for you to use.

- [Deployment using Heroku](#Deployment-usingHeroku)

    1. Create an account with [Heroku](https://signup.heroku.com/).
    2. Create a new app, with an appropriate region and name.
    3. In **Resources** add **Heroku Postgres**.
    4. Within your newly created app
    go to settings go to **Config Vars**
    use the **DATABASE_URL** Value and add it to your env.py file and connect it via settings.py.
    5. Create a **SECRET_KEY** Key and the Value as desired key.
    6. Next go to the **Deploy** tab next to **Deployment Method** click **GitHub** connect your account and repository.
    7. **Recommended** enable automatic deploys.
    8. At the Bottom of the page hit deploy branch making sure it is set to **main**

    #### **Note.**
    This project uses Python and has to be deployed with a hosting platform such as Heroku as it handles backend functionality.
- [Credits](#credits)
