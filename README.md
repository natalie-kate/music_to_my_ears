# Music To My Ears

Here is a link to the live project. ()

This website was created for Milestone 4 

![Image showing the website displayed on different screen sizes]()

## Contents 

- [User Experience (UX)](#user-experience-ux)
   * [Strategy](#strategy)
   * [User Stories](#user-stories) 
   * [Scope](#scope)
      + [Current Features](#current-features)
      + [Features to implement in the future](#features-to-implement-in-the-future)
   * [Structure](#structure)
   * [Skeleton](#skeleton)
   * [Surface](#surface)
     + [Colour Scheme](#colour-scheme)
     + [Typography](#typography)
     + [Imagery](#imagery)
- [Technologies](#technologies)
   * [Languages used](#languages-used)
   * [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

- [Challenges](#challenges)

- [Testing](#testing)
   
- [Deployment](#deployment)
   * [Creation](#creation)
   * [Forking](#forking)
   * [Clone](#clone)
   * [Setting up AWS](#setting-up-aws)
   * [Setting Up Stripe](#setting-up-stripe)
   * [Setting Up App](#setting-up-app)
   * [Heroku Deployment](#heroku-deployment)

- [Credits](#credits)
   * [Code](#code)
   * [Content](#content)
   * [Media](#media)
   * [Acknowledgements](#acknowledgements)


## User Experience (UX)

   ### Strategy 
   - User goals 
     * As a user I want help keeping track of my books.
     * As a user I want to save my money and time by not buying books I already own or have read. 

   - Site owner/ business goals
     * As the site owner I want my site to be responsive to different screen sizes.
     * As the site owner I want my site to be accessible to my visitors.
     * As the site owner I want to build up media presence, to ultimately build up users so that I can earn money from affiliate links.
     * Ultimately though I want to use the application to track my own books.

   ### User Stories

   - #### Unregistered Visitor
        1. As an unregistered visitor, I want to be able to add products to my cart
        2. As an unregistered visitor, I want to be able to view my cart
        3. As an unregistered visitor, I want to be able to edit my cart
        4. As an unregistered visitor, I want to be able to checkout
        5. As an unregistered visitor, I want to see an order confirmation
        6. As an unregistered visitor, I expect the site to look good on my mobile device.
        7. As an unregistered visitor, I want to easily search the vinyls.

   - #### First Time Visitor (in addition to above)
        1. As a first time visitor, I want to easily understand the main purpose of the site.
        2. As a first time visitor, I want to be able to intuitively use the site.
        3. As a first time visitor, I expect to see an attractive, visually appealing site.
        4. As a first time visitor, I expect an accessible site.
        5. As a first time visitor, I expect the site to look good on my mobile device.
        6. As a first time visitor, I want to easily register.

   - #### Registered Returning Visitor Goals
        1. As a returning visitor, I want to be able to view and add to the event board.
        2. As a returning visitor, I want to follow on social media so I can hear of any new products.
        3. As a returning visitor, I want to be able to change my password.
        4. As a returning visitor, I want to be able to save my details
        5. As a returning visitor, I want to get feedback so I know that something has went through.
      
   - #### Registered Frequent Visitor Goals
        1. As a frequent visitor, I want to be able to edit an event I’ve added to the event board.
        2. As a frequent visitor, I want to be able to contact the owner.
        3. As a frequent visitor, I want to be able to edit my profile information.
        4. As a frequent visitor, I want to be able to delete my account
        5. As a frequent visitor, I want to be able to see my order history
        6. As a frequent visitor, I don't want to have never ending scrolling up or down.

   - #### Admin goals
        1. As admin, I want to be able to add, delete or edit a product.
        2. As admin, I want to be able to add a genre.
        3. As admin, I want to be able to delete or edit an event on the event board
        4. As admin, I want to be able to delete a user.
        5. As admin, I want to be able to make another user an admin.
        6. As admin, I don’t want users to be able to order product if there is none left in stock.

   ### Scope

   Within project conception, a list of features were compiled, these were the scored 
   between 1 & 5 for importance and feasibility/ viability which then decided which features 
   could be included for initial launch.    

   #### Current features 

-   Responsive on all device sizes

-   Accessible 

-   Easy to navigate (Single use learning)

-   Interactive elements

-   Social Links 

-   Ability to contact owner via contact page.

-   Contact form prefills the personal information for logged in users.

-   Changing nav menu and footer links and buttons in depending on the users log in status, admin status and what event if any they have added.

-   Search bar for products and events.

-   'Back to top' footer link on each page, saves users from having to scroll up to Nav bar especially on mobile devices.

-   Logged in users can add events to event board.

-   Logged in user can save their payment information and delivery address.

-   User can edit events on event board that they themselves added. 

-   User can edit their own profile information

-   Admin users can add, edit and delete any products.

-   Admin user can add, edit and delete any event.

-   When product stock quantity is 0, add to cart buttons are not available and will display 'Out of Stock'.

-   Before anything is deleted a confirmation is required preventing accidental deletion.

-   Cancel buttons on edit pages in case user changed their mind or got there accidentally.


   #### Features to implement in the future



### Structure


- Created a database schema using [dbdiagram](https://dbdiagram.io/home), see below. 
![database schema]()

### Skeleton 

Wireframes were created on Balsamiq (see links below)

* [Mobile](/static/readme_assets/wireframes/ms4-mobile.pdf)
* [Tablet](/static/readme_assets/wireframes/ms4-tablet.pdf)
* [Desktop](/static/readme_assets/wireframes/ms4-desktop.pdf)

### Surface

 -   #### Colour Scheme
        

-   #### Typography
         
      Used [Google Fonts](https://fonts.google.com/) to import the fonts used for this site.
      
-   #### Imagery

## Technologies 

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

1. [Bootstrap v4.6.0](https://getbootstrap.com/docs/4.6.0/getting-started/introduction/)
    - Bootstrap was used for the initial layout and styling before customising it.
2. [Google Fonts](https://fonts.google.com/)
    - Google fonts were used to import the Tangerine and Gentium Book Basic. 
3. [Font Awesome](https://fontawesome.com/)
    - The icons used throughout.
4. [Git](https://git-scm.com/)
    - Version control.
5. [GitHub](https://github.com/)
    - For storing project.
6. [Gitpod](https://www.gitpod.io/)
    - Used for editing my code.
7. [Balsamiq](https://balsamiq.com/)
    - Wireframe creation
8. [TinyJPG](https://tinyjpg.com/)
    - TinyJPG was used to optimise the images I used on my site to minimise loading time.
9. [Am I responsive](http://ami.responsivedesign.is/)
    - This was used to generate the image at the top of this README.
10. [Chrome devtools](https://developer.chrome.com/docs/devtools/)
    - This was used massively throughout development to troubleshoot, try out changes before 
   changing code, to test responsiveness and for testing performance of the final site with lighthouse. 
11. [jQuery](https://jquery.com/)
    - Required for some of the bootstrap elements such as collapsibles, modal and tooltips.
12. [Heroku](https://dashboard.heroku.com/apps)
    - For deploying the application
13. [MongoDB](https://www.mongodb.com/)
    - Database used for our data
14. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Micro framework for building applications.
15. [Emailjs](https://www.emailjs.com/)
    - Used to link the contact form to my emails
16. [RandomKeygen](https://randomkeygen.com/)
    - Used to generate secret key
17. [dbdiagram](https://dbdiagram.io/home)
    - Used to create the database schema.
18. [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
    - Dependency of Flask and used security helpers.
19. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - Dependency of Flask, templating language used in all my pages.
20. [convertingcolors.com](https://convertingcolors.com/color-bucket.html)
    - For making my colour palette picture

## Challenges 
   These are aspects of the development that took me a while to figure out due to inexperience.
   - <br> 
       + <span style="color: grey;">Solution: </span>      

## Testing

Testing and results can be found [here](TESTING.md)

## Deployment

 - ### Creation 

    I created this repository by:<br>
    (a) Logging into Github and clicked the green new button.<br>
    (b) This took me to the page below. I selected the code institute template, input a repository name and clicked the green create repository button.<br>

    ![image showing green new button](static/images/readme-images/deployment/new.png)
    ![Image showing the create repository page](static/images/readme-images/deployment/new-repo.png)

    (c) Opened new repository and clicked green Gitpod button to create a workspace in Gitpod for editing.

  - ### Forking
    (a) To fork my project sign in to Github and go to my [repository]()<br>
    (b) Above and to the right of the settings there are three options and the far right one says Fork, select this.<br>
    (c) The fork is now in your repositories.

    ![Image showing fork button](static/images/readme-images/deployment/fork.png)

  - ### Clone
    To clone my project sign in to Github and go to my [repository]()<br>
    See [Setting up MongoDB](#setting-up-mongodb), [Setting Up App](#setting-up-app), [Connecting to MongoDB](#connecting-to-mongodb) and [Heroku Deployment](#heroku-deploment) for more information about what will be required to run Pocket Bookcase.

    *  Clone using command line 
        +  Next to the green Gitpod button is a button that says code, select this. There is a few options as to how you 
        would like to clone, if you choose https, SSH or Github CLI, select the clipboard icon to copy the URL.
        +  In your workspace that you've created, in the terminal , type git clone, paste the URL and enter.

        ![Image showing the cloning options](static/images/readme-images/deployment/clone.png)

    *  Desktop Github
        + If you choose to clone by selecting open with desktop Github, it will guide you through the clone with prompts.<br>

    For more information or troubleshooting see the Github documentation 
    [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository)

- ### Setting up AWS

- ### Setting up Stripe

- ### Setting Up app
   
    - Install requirements in terminal using pip3 install, see requirements below. 
    
      ![Image showing the requirements](static/images/readme-images/deployment/requirements.png)

    - Create requirements.txt file and Procfile by typing below into the console. These are required by Heroku so ensure these are pushed to github prior to deployment.

      ![Image showing the commands in console](static/images/readme-images/deployment/pip3-freeze.png)


- ### Heroku deployment
    - Log in to Heroku, click 'New' and select 'Create New App'. In window give the app a name and choose region closest to you and then click 'Create App'.
    - In new app page select settings from menu, click reveal config vars and complete the following
      
      ![Image showing the config vars required](static/images/readme-images/deployment/input-config.png)

    - Next select 'Deploy' from menu, three options of deployment are available. If you select Heroku Git, it gives you step by step of what you need to do.

      ![Image showing the Heroku deployment methods](static/images/readme-images/deployment/deployment-methods.png)

    - I chose to use Github, so you have to search and connect to your github repository. 

      ![Image showing connect to github](static/images/readme-images/deployment/github-connect.png)
    
    - Click enable automatic deployment, below that in manual deploy section, you can pick and deploy a branch to ensure everything is et up correctly. 

      ![Image showing automatic and manual deploy](static/images/readme-images/deployment/deploy.png)

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/): Bootstrap Library used for the layout and styling and modals.


### Content

-   Content was created by Natalie Alexander.
    
-   README and TESTING layout and content from my MS1 which took inspirations and ideas from these excellent examples
    * [Code institute](https://github.com/Code-Institute-Solutions/SampleREADME)
    * [Daisy McGirr](https://github.com/Daisy-McG/MilestoneProject-1/blob/master/README.md)
    * [Richard Henyash](https://github.com/richardhenyash/artofnht/blob/darktheme/README.md)
    * [byllsa](https://github.com/byIlsa/Aloy-from-outcast-to-heroine)

### Media

 
### Acknowledgements

-   Code Institute and Tim Nelson for task manager walk through project. Used the videos a fair bit to get me started.
-   My mentor Spencer Barriball for his time and feedback.
-   My mini feb 2021 team on slack for their feedback and support.
-   The slack community.
-   My partner for taking the lions share of raising our baby and the cooking so that I can study.