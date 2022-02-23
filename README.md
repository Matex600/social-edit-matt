# Meddit - Blog

![AmIresponsive](documentation/readme_images/amiresponsive.PNG)

[Site Live link](https://project4-matt-ci.herokuapp.com/)

I recommend clicking any links found in this README with Ctrl + Left mouse click for (Windows) and Control + click (Mac) 
# Project Introduction

This website is a fullstack application Using mainly the Django fullstack web framework.

My Goal is to create a functioning, responsive Blog that users can make blog posts, up vote and down vote as well as make comments.

The Sites purpose is to allow users to connect with each other and share things they find interesting like hobbies or news!

Project 4 for [CodeInstitute](https://codeinstitute.net/) Full stack course (5P)


 * This project is created using
  1. Django 3.2
  2. Heroku (Deployment)
  3. Heroku PostgresSQL
  4. Bootstrap 5
  5. Github (Repository Hosting)
  6. Gitpod (Development environment)

  * Blog site allowing users to
  1. Create | Edit | Delete Posts
  2. Create | Categories
  3. Create | Comments
  4. Login | Register | Logout
  5. Create | Update | User Profile

- [User Experience](#user-experience)
  * [User Stories](#user-stories)
  # Site Design

  ## Composition

  ### Fonts 
    * [Roboto](https://fonts.google.com/specimen/Roboto). - Font used for Body text.
    * [Roboto - Slab](https://fonts.google.com/specimen/Roboto+Slab?query=roboto+slab). - Font used for Header text.

    * I have chosen these two fonts as they compliment themselves together and compliment my blog.

    * sans-serif is used as a backup font incase one or both fail for any reason.
  ### Font Size
    
    * I have kept font size as default as I feel that it looks good and what I wanted for the blog hence I have no need to change it.

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
   * ```
      DETAIL:  Key (slug)=() already exists.
     ``` 
     solution add null=True to slug model
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
  * Development Environment
    1. Create requirements.txt ```pip3 freeze --local > requirements.txt```
    2. Create Procfile containing application name ensure proper formatting or deploymentw will fail.
    3. Commit and push changes to Github.
    4. Move to Heroku part of deployment.

  * Heroku
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
https://mdbootstrap.com/docs/standard/extended/login/