# Testing

## Contents 
   - [Automated Testing](#automated-testing)
      * [HTML validation](#w3c-markup-validator)
      * [CSS validation](#w3c-css-validator)
      * [JS validation](#jshint-javascript-validator)
      * [Pep8 validation](#pep8-validation)
      * [Lighthouse testing](#lighthouse-testing-in-devtools)
      * [Unit testing](#unit-testing)
   - [Testing User Stories](#testing-user-stories)
   - [Manual testing](#manual-testing)
   - [Bugs](#bugs)
      * [Found and Fixed](#found-and-fixed)
      * [Existing](#existing)


## Automated Testing

The W3C Markup Validator and W3C CSS Validator were used to validate every page of the project to ensure there were no syntax errors in the project.

-   ## [W3C Markup Validator](https://validator.w3.org/) 

    ### Initial testing
    - index.html

    - about.html

    - contact.html
  
    - edit-account.html

    - edit-user.html

    - manage-genres.html

    - manage-users.html

    - profile.html

    - profile-add.html

    - register.html

    - sign-in.html

    - edit-book.html

     ![Initial edit-book.html test](static/images/testing-images/validations/update-book-html.png)

     Same issue as contact.html, with the aria-checked attribute.

    - add-book.html

     ![Initial add-book.html test](static/images/testing-images/validations/add-book-html.png)

     Same issue as contact.html, with the aria-checked attribute.

    - 404.html

     ![Initial 404.html test](static/images/testing-images/validations/404-html.png)

    - 500.html

      Issues raised by inputting the 500.html code was due to the templating language and therefore raised errors of needing a head, doctype, language etc.
    
    ### Final testing (for those that needed fixed)

-   ## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    
    ### Initial testing

    ### Final testing

-   ## [JSHint JavaScript Validator](https://jshint.com/) 
    
    ### Initial/final testing

-   ## [Pep8 validation](http://pep8online.com/) 
    
    ### Initial/final testing

    
-   ## [Lighthouse testing in devtools](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) 
    
    
    ### index.html

     + 

    ### about.html

    ### profile.html

    ### contact.html

    ### register.html

    ### manage-genres.html

    ### manage-users.html

    ### edit-book.html

    ### sign-in.html

    ### profile-add.html

    ### edit-user.html

-   ## Unit Testing 

## Testing User Stories 

   - #### Unregistered Visitor
        1. As an unregistered visitor, I want to be able to add products to my cart
           On the landing page, the spinning vinyl, call to action button opens shop page, aswell as there being a 
           shop link in the nav menu.

             ![Image showing landing page call to action button](/docs/readme-assets/testing_images/shop_btn.png)
             ![Image showing Shop nav link](/docs/readme-assets/testing_images/nav.png)

        2. As an unregistered visitor, I want to be able to view my cart
           The basket is on the top right of the page. When there are items the number is in 
           brackets beside the basket. In addition when a product is added to the basket, success 
           message contains a link to view basket.

             ![Image showing basket in nav menu](/docs/readme-assets/testing_images/basket.png)
             ![Image showing Success message view basket link](/docs/readme-assets/testing_images/view_basket.png)

        3. As an unregistered visitor, I want to be able to edit my cart
           In view basket page there are Update and Delete links that open collapsibles.

             ![Image showing edit and delete links in basket](/docs/readme-assets/testing_images/edit_basket.png)

        4. As an unregistered visitor, I want to be able to checkout
           In view basket page and in success message upon adding a product there is a checkout 
           button that takes user to checkout page.

             ![Image showing checkout button in basket](/docs/readme-assets/testing_images/checkout_btn.png)
             ![Image showing Success message checkout button](/docs/readme-assets/testing_images/message_checkout.png)

        5. As an unregistered visitor, I want to see an order confirmation
           When an order is put through, the checkout success page renders and the user will recieve 
           a confirmation email.

             ![Image showing checkout success page](/docs/readme-assets/testing_images/order_confirm.png)
             ![Image showing order confirmation email](/docs/readme-assets/testing_images/order_email.png)

        6. As an unregistered visitor, I expect the site to look good on my mobile device.
           The site was designed with mobile first in mind

             ![Image showing mobile home page](/docs/readme-assets/testing_images/home.png)
             ![Image showing mobile nav menu page](/docs/readme-assets/testing_images/mobile_nav.png)
             ![Image showing mobile shop page](/docs/readme-assets/testing_images/shop.png)
             ![Image showing mobile product details page](/docs/readme-assets/testing_images/details.png)
             ![Image showing mobile basket page](/docs/readme-assets/testing_images/basket_mobile.png)
             ![Image showing checkout page](/docs/readme-assets/testing_images/checkout.png)
             ![Image showing mobile contact page](/docs/readme-assets/testing_images/contact.png)

        7. As an unregistered visitor, I want to easily search the vinyls.
           The Shop page has the products grouped in genres of which the user can use the arrows to browse through.
           The "Browse Genre" heading above each carousel is a link so that the user can see all products of a genre at once.
           There is also a view all products link and a search box.
           
             ![Image showing browse genre, see all and search box](/docs/readme-assets/testing_images/browse_products.png)

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
      
         
      
## Manual Testing

-  I generally test as I'm developing as well as at the end so some of the findings are from during development. The website was viewed with browsers: Google chrome, Safari, Microsoft Edge, Firefox and Opera. Viewed all pages on each and checked the following:
  - Nav links work from all three pages to all links.
  - Pocket Bookcase brand name takes user to home.
  - Book search bar works for genre, added_by, series, book title and author for logged in and non logged in users.
    * Got an error when I searched an empty input box for non-logged in user. Realised I hadn't put required attribute in the search box but now same thing happens when user searches for something that isn't there. Its when it redirects the user back to library the if session code is running and comes up with a KeyError at session["user"]. I thought only logged in users are in session but evidently not, so I have changed if session to if "user" in session and that seems to work.
  - Pagination links work.
  - All buttons take user to the correct page
  - Add book button should only show for logged in user.
  - Add book form doesn't allow user to add book without required fields being completed.
    * Removed required from review as it occurred to me if a user was adding a book to their 'Books to Read' bookshelf they won't have a review yet.
  - Add book form doesn't allow a book that already exists in library to be added.
    * Yes and no, if you spell it exactly the same then it won't let you, but if there is a letter different or you miss out "The" at the beginning for example it can get added when really its the same book.
  - Add book form doesn't allow a book with only spaces as a name to be added.
  - Book successfully added to library
  - If book url not supplied or broken, back up image shown.
  - Flash messages pop up where required, providing feedback to users actions.
    * Found that "Does not match our records" flash wasn't displaying full message. It was one of the flash messages that had to get split between two lines as the line was too long, put in a string concatenation.
  - Correct buttons appear for the correct users beside books. e.g all three for admin, two against book that a user added, one for logged in users, none for non logged in users.
  - Edit book form should prefill with current details, title should not be able to be edited except for admin.
  - Edit book form will not submit wihout required information.
  - Book information successfully edited.
  - Delete book, only allowed for admin, confirmation before deletion required, successfully deleted from library.
  - Registration form won't submit without required information.
  - Registration successfully adds a new user and their profile.
  - Add to profile switches put books on the correct profile bookshelves.
  - If user adds a book to profile that they have already added, duplicate book should not appear.
      * Found during development that addToSet would stop this from happening so changed from push which is what I initially had.
      * When testing, added a book to profile, then went back and added same book selecting the same options, this as expected didn’t give duplicate books in profile list. Then went back and added same book again, this time not selecting either switch. This resulted in the book being in the read and to read books. Added in a check to see if book is in profile already, if it is flash message will appear and user won't be taken to profile-add page. 
  - Using book buttons on profile should move books correctly. Remove button should remove book from that bookshelf only.
  - Edit account form should be pre-filled with existing information (not password)
  - Edit account should successfully update a users information.
  - Delete account should open confirmation and then successfully remove user if they proceed with deletion.
     * Link did not open confirmation, had missed a # in the href to target the collapsible.
  - If user tries to change their password, their existing password must be correct to proceed. And their new password must match the confirm password field.
    * Realised I hadn't put the tooltips in to help user with required format.
  - Manage genre page allows admin to successfully add a new genre.
    * When trying to add a genre that was already in the database an error occurred, realised that I had redirected to add_genre rather than manage_genre.
  - Manage genre page allows admin to update a genre.
    * Science fiction edit collapsible wouldn't open. Had missed a genre.name.replace(' ', '').
  - Manage genre page allows admin to successfully delete a genre after confirmation
    * Found that Action & Adventure buttons wouldn't do anything, realised similar to a previous issue that this was due to the id being generated from it having an "&". So in add genre input added a pattern and tooltip attributes so that this could be prevented from occurring. 
  - Manage users allows admin to search for admin users or a user by username.
  - Manage users page allows admin to open a users edit user page to successfully make them an admin.
  - Manage users page allows admin to open a users edit user page to successfully reset their password.
  - Manage users page allows admin to successfully delete a user after confirmation.
  - Cancel buttons take user off of the edit page/section they were on or close the delete confirmation.
     * Hadn't put a cancel button in edit_user and edit_book pages.
  - Clicking on social links work, opening in a new tab.
  - Footer links all go to the correct place, back to top link correct on each page.
     * Was having issued on mobile device clicking the correct link, put anchor into paragraph tags as that was the only way I could get them to space out.
  - Footer links appearing appropriately, logged in vs non logged in. 
  - Hover effects work on social icons and all links and buttons.
  - Contact form will not submit without all three required personal details and comment box being completed . 
  - Can type in contact form text area, star ratings work and on successful form submission, personalised modal appears
  - Both modal close buttons take user back to home page.
  - Upon successful submission, receive an email with details taken from the form by email.js and send button has changed to sent.
  - Upon contact form submission user also recieves a personalised acknowledgment email.
  - 404.html back to home button works.
  - 404 report issue link takes user to contact form.
  - About modal close buttons work.
  - Friends, family and slack peer review used. Devices and browsers were iphone 11: Safari (x3), iphone XS Max: Safari, iphone 6: Chrome, iphone XR: safari, iphone 11 Pro: Safari, iphone 10: Safari, Samsung S20 FE: Chrome, Samsung S10 and Sony Xperia I3: Chrome. 
  - Chrome devtools used to test responsiveness throughout the development process see bugs found below. Viewed all pages on all of the available devices at the end of the project to ensure everything still looked good.
  - Viewed physically on Macbook air 13", Huawei tablet, HP Chrome book, Dell 21" HD screen, iphone 11, Dell 17" laptop and Pixel 4XL phone to ensure that after all issues found and resolved that there was nothing else appearing
 

## Bugs

   ### Found and Fixed 

   In addition to those found in manual testing

   - On peer code review channel a user had got an error when trying to edit a book they had added. 


   ### Existing
     
   - 