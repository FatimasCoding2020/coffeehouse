<p align="center">
<img src="assets/coffeehouse-banner.gif" alt=" ">
</p>

<div align="center">
 
<p>Welcome to the big, bold flavours of <strong>coffee house.</strong>We’ll help you wake up first thing in the morning and unwind at the end of the day with our very own fresh blends, sourced from around the globe.</p>
 
<p><strong>coffee house.</strong> offers the world’s best expertly curated artisan coffee - seasonally sourced and carefully roasted - delivered to your doorstep.
Sip your way to a memorable cup!</p>

<p>This is the fourth milestone project in the Full Stack Web Development Program I am attending at The Code Institute.</p>

[View the live project here](https://ms4-coffeehouse.herokuapp.com/)
<hr>
</div>


## Index 

- <a href="#ux">1. User experience (UX)</a>
    - <a href="#ux-goals">1.1. Project Goals</a>
    - <a href="#business-goals">1.2 Business Goals</a>
    - <a href="#visitor-goals">1.3 Visitor Goals</a>
    - <a href="#target-audience">1.4 Target Audience</a>
    - <a href="#ux-stories">1.5 User Stories</a>
    - <a href="#ux-design">1.6 Design</a>
    - <a href="#ux-mockup">1.7 Mockup designs</a>
- <a href="#information-architecture">2. Information Architecture</a>
    - <a href="#database">2.1 Database</a> 
    - <a href="#er-diagram">2.2 ER Diagram </a>  
    - <a href="#data-modelling">2.3 Data Modelling</a>
- <a href="#features">3. Features</a>
    - <a href="#features-existing">3.1 Existing features</a>
    - <a href="#features-future">3.2 Features left to implement in the future</a>
- <a href="#technologies">4. Technologies used</a>
- <a href="#testing">5. Testing</a>
- <a href="#deployment">6. Deployment</a>
- <a href="#credits">7. Credits</a>
- <a href="#Acknowledge">8. Acknowledge</a>
- <a href="#Acknowledge">9. Disclaimer</a>

---
## Responsive displays

![coffee house responsive displays](assets/readme-files/responsive.png)

---

<span id="ux"></span>

<h1>1. User experience (UX)</h1>

<span id="ux-goals"></span>

### 1.1 Project goals 

- Making a full-stack site based around business logic used to control a centrally-owned database. 
- The site provides an authentication mechanism and provides paid access to the site’s data based on the dataset. 
- Making a full-stack site that uses HTML, CSS, JavaScript, Python + Django.
- Creating a website that uses a relational database 
- Creating a website that uses Stripe payments 
- Building a full-stack website that serves as a webshop for a collection of fresh blended coffees. 

<span id="business-goals"></span>

### 1.2 Business goals

- Creating a secure and professional e-commerce website. 
- Provide users collection of coffees from around the globe. 
- Make profit selling collection of coffees. 
- Make fresh blends of coffee delivered to customers doorstep.

<span id="visitor-goals"></span>

### 1.3 Visitor goals

- Explore and choose from the collection of coffees. 
- Safely purchase coffee on the webshop. 

<span id="target-audience"></span>

### 1.4 Target audience

- Coffee lovers.
- People who want to try different flavours of coffee.  

<span id="ux-stories"></span>

### 1.5 User stories 

**Visitor goals:**
1. As a visitor, I want to access the website from any device, so that I can go to the website on desktop, mobile and tablet. 
2. As a visitor, I want to be able to navigate easily through the website, so I can find everything easily. 
3. As a visitor, I want to access the social media accounts of the company, so I can follow them and see the latest trends and news. 
4. As a visitor, I want to sign up for the newsletter, so I can be up to date about the latest news and trends. 
5. As a visitor, I want to know more about the company, so I know what the company's story is about.
6. As a visitor, I want to be able to contact the owners of the website, so I can easily ask a question. 
7. As a visitor, I want to see an overview of all the coffee collection, so I can see what the website is offering. 
8. As a visitor, I want to be able to search coffees, so I can find specific coffee quick and easy.
9. As a visitor, I want to be able to read more information about different blends of coffee (flavours, price, image, description), so I can see if the product suits my taste preferences. 


**Consumer goals:** 

10. As a consumer, I want to add products to my basket, so I can buy products. 
11. As a consumer, I want to modify my order, so I can make last changes before I order the products. 
12. As a consumer, I want to be able to delete products in my order, so I can remove products that I no longer wish to purchase. 
13. As a consumer, I want to see the total price and shipping costs of my order, so I can see how much I have spent in total. 
14. As a consumer, I want to pay with a card in a safe and secure way, so I know that my payment goes well. 
15. As a consumer, I want to receive a confirmation email of the order, so I know that the order is successfully received. 
16. As a consumer, I want to create an account, so I can see my profile details and order history. 
17. As a consumer, I want to know more about shipping, delivery, etc., so I know more about when and how my package arrives. 
18. As a consumer, I want to know how I can return my package, so I know how I can return my packages if I want to. 

**Returning consumer goals:** 

19. As a returning consumer, I want to login and logout at my account anytime, so I can make an order quickly and so I can see my order history. 
20. As a returning consumer, I want to reset/change my password, so I can get access to my profile.  

**Admin goals:** 

21. As admin, I want to add, modify and delete products, so I manage the collection of coffees on the website. 

<span id="ux-design"></span>

### 1.6 Design 

- #### Frameworks

[The Bootstrap front-end framework](https://getbootstrap.com/) is used through the project. Bootstrap provides a quick design, responsive grid system, extensive prebuilt components and a modern interface for the project.  

- #### Colour Scheme 
The colours that are used for the website have a dark background that shows light colours. These colours give a feast for the eyes, to make it look tempting. 
The products stand out of the dark and sleep appearance of the colours.

![Colour Palette](assets/readme-files/colour-scheme.png "General Colour Palette")


- #### Fonts
The **Spartan** font is used throughout the whole website. The sans serif font serves as fallback in case the main font isn’t being imported to the site correctly. The Spartan font is used for all the text on the website. This font is used because the font is clear and is easy to read. The font is used in lowercase letters for all titles and for paragraphs. 

- #### Icons
The icons in the project are provided by [Font Awesome](https://fontawesome.com/). All icons that are used have functional purposes such as the hamburger menu for the mobile version and social media icons.

- #### Images
The images that are used for the project are from [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/). The images are used for background images, the video on the homepage is from [Pexels](https://www.pexels.com/).The logo is made on [Canva](https://www.canva.com/).

<span id="ux-mockup"></span>

### 1.5 Mockup designs
Mockup designs are made with [Balsamiq](https://balsamiq.com/)

Click on the links below to see the mockups in Balsamiq.
|    Desktop   |    Mobile    |   Tablet   |
|    :----:    |     :----:   |     :----:    | 
|[coffee house.](assets/readme-files/wireframes/desktop.pdf)|[coffee house.](assets/readme-files/wireframes/mobile.pdf) |[coffee house.](assets/readme-files/wireframes/tablet.pdf) | 

<div align="right">
    <a href="#coffeehouse">↥ Back to top!</a>
</div>

<span id="information-architecture"></span>

<h1>2. Information Architecture</h1>

<span id="database"></span>

### 2.1 Database
- During the development phase I have worked with the **sqlite3** database, which was set by default by Django. 
- For deployment, I used the **PostgreSQL** database whcih is provided by Heroku. 

<span id="er-diagram"></span>

### 2.2 ER Diagram

![ER Diagram](assets/readme-files/erd.png)


<span id="data-modelling"></span>

### 2.2 Data Modelling


#### 1. Profile app 
#### UserProfile model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | ForeignKey |  User, on_delete=models.CASCADE
 Full Name | full_name | CharField | max_length=50, null=True, blank=True
 Phone number | phone_number | CharField | max_length=20, null=True, blank=True
 Country | country | CharField | blank_label='Country', null=True, blank=True
 Postcode | postcode | CharField | max_length=20, null=True, blank=True
 Town/City | town_or_city | Charfield | max_length=40, null=True, blank=True
 Street address 1 | street_address1 | CharField | max_length=80, null=True, blank=True
 Street address 2 | street_address2 | CharField | max_length=80, null=True, blank=True

#### 2. Products app 
#### Product model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Sku number | sku | CharField | max_length=40, null=True, blank=True
 Name| name | CharField | max_length=250
 Description| description | TextField | null=True, blank=True
 Price | price | DecimalField | max_digits=5, decimal_places=2, null=False, default=0
 Image | image | ImageField | null=True, blank=True
 Image url | image_url | URLField | max_length=1024, null=True, blank=True
 In stock | in_stock | BooleanField | default=True

#### 3. Checkout app 
#### Order model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order number | order_number | CharField | max_length=32, null=False, editable=False
 User | user | ForeignKey | User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full name | full_name | CharField | max_length=50, null=False, blank=False
 Email| email| EmailField | max_length=254, null=False, blank=False
 Phone number | phone_number | Charfield | max_length=20, null=True, blank=True
 Country| country | CountryField | blank_label='Country *', null=False, blank=False
 Postcode | postcode| CharField | max_length=20, null=True, blank=True
 Town/City | town_or_city | CharField | max_length=40, null=True, blank=True
 Street address 1 | street_address1 | CharField | max_length=80, null=True, blank=True
 Street address 2 | street_address2 | CharField | max_length=80, null=True, blank=True
 Date | date | DateTimeField | auto_now_add=True
 Delivery cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
 Order total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Grand total | frand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Original bag | original_bag | TextField | null=False, blank=False, default=''
 Stipe pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''


#### 5. Newsletter app 
#### Subscribe model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Email | email| EmailField | max_length=255
 Timestamp | timestamp | DateTimeField | auto_now_add=True

<div align="right">
    <a href="#coffee house.">↥ Back to top!</a>
</div>


<span id="features"></span>

<h1>3. Features</h1>

<span id="features-existing"></span>

### 3.1 Existing features 

The website is classified by the following applications: home, our collection, Our story, blog, checkout, profile page, newsletter and contact.

#### 1. Navbar
- **The name** (which also serves as logo) is clearly visible in the left side of the navbar. The name is also a redirect to the home page. 
- The navbar contains the **search functionality**, where the user can search for products. The search term would match with the product name or the product description. 
    - The search functionality allows users to enter keywords associated with the name or the description of the product. 
    - The search results are displayed on the products page. 
    - On the product page, a message will appear with ‘no results’ if there are no search results.
- The navbar contains the **profile icon**, where people can login, register and go to their profile.
- The navbar contains the **shopping bag**, where users can see the items they have put in order. The bag redirects to the order summary. 
- The navbar is visible as a **hamburger menu** on mobile devices. 

#### 2. Footer
- **Relevant links** such as the collection, the account, FAQ and contact are placed at the bottom of the footer.
- The **social media links** are placed at the bottom of the footer. 


#### 3. Home page 
- The home page serves as an introduction to the webshop with relevant information and inspiration.
- The **video** is on top of the page. 
- There is a section with **our collection** that are in store. 
- There is a section with **our story** in general.
- There is a separate section with four **unique selling points**  (best quality, free shipping, sustainability and quick safe payments.) displays with icons. 
- There is a separate section where people can **sign up for the newsletter**. The newsletter is linked to Mailchimp to automatically send emails to the mailing list. 

#### 4. Product detail page 
There are 4 product pages under Our collection
- **The product detail page shows information about that specific item**, the information includes; name, image, if the item is in stock, the price and the product description.  
- A user can **choose the quantity** of the product.
- There is a button where the user can **add the item to the shopping bag**.
    - When the user  puts the item in the bag there will be a toast success message.
    - When the user puts the item in the bag, the shopping bag will show the number of items that are in the shopping bag.
- There is a **‘back to our collection’** link that redirects to the product page. 

#### 5. The shopping bag page
- **The shopping bag page is available for logged in users and guests.** Purchases can be made by both.
- Gives **an overview of all items** that are in the shopping bag, the overview information includes; image, name, quantity, price and subtotal.
- users  can **update the quantity** of the items they have.
- users  can **delete items** from their order.
- There is an **overview of the total price, the delivery costs and the grant total** of the order.
- There is a button with **‘keep shopping’** that links to the product page. 
- There is a button with **‘go to checkout’** to continue the purchase.

#### 6. Checkout page 
- The **order summary** gives information about the item, this information includes; name, price, total, delivery costs and grand total. 
- There is an option to **login with an account**, where the personal and delivery information already exists to continue the payment process quickly. 
- **The checkout form** to continue the payment. The form asks for the following information: full name, email, phone number, country, postal code, town or city and  street address 1 - all these input fields must be valid. The country field is an input where users can scroll to a list to choose the country.
- At the end of the checkout form there is an option to **save** the delivery information to an account. This function only shows when the user is authenticated.
- The user has to fill in their information about the card number. The Stripe functionality is in testing mode, the credit card number **4242424242424242** will lead to a successful payment. expiration date, CVC can be made up yourself.
- A **webhook** is used for security when the order is processed, even in the case when the payment process is interrupted.
- There is a **button to go back to the shopping bag page.** The user can go back to the shopping bag page to adjust items in the bag.
- There is a send button to **complete the order**.
- When the user clicks on the complete the order button, there is a little **loading overlay**. The user is directed to the checkout success page after the overlay. 
- **When the order is completed:**
    - There is a redirect to the checkout success page.
    - A confirmation email is sent to the user’s mail.
    - A toast message ‘completed’ shows to ensure the user that the order is successfully completed.

#### 7. Checkout success page
- Contains a **thank you message**.
- Includes information about the **order summary**. The order summary consists of information about the date, order number, products, delivery information and billing information. 

#### 9. Profile page 
- The account page is only accessible for users who have an account. 
- The page contains a **personal info section** (username, email). The user can change the password. 
- There is a shipping **info section** (country, postal code, town/city, street address 1 and street address 2. Users can **edit this information** also. 
- There is an **order history** section (order number, date of order, items and total) 

#### 10. FAQ page 
- This page contains all relevant questions users divided in two main sections; delivery, returns. 

#### 11. Contact page 
- Users can reach out to the company with the **contact form**. The user has to fill in the name, email and message. The form will be sent to the admin. 
- **Contact details** (phone number, email) are displayed on this page. 
- There is a separate section with four **unique selling points** (best quality, free shipping, sustainability and quick safe payments.) displays with icons. 

#### 12. Django-Allauth features 
- **Sign up**
    - Users can create a new account by filling in a from where the user have to filling an email, username, password and password confirmation. If the info already exists there will be a message that he/she already has an account. The user can submit the form when the data is new. A verification email is sent to the user.
- **Login**
    - Users can login with their username ans password. There is also a link to change the password, if the user has forgotten. 
- **Forgot password**
    - A user can reset their password. 
- **Logout** 
    - The user can logout by clicking the logout link. After clicking the link there wil a confirmation if the user is sure to logout. 

#### 13. Error pages 
- The custom error handling page with short information about the error. The error is displayed in the style of the website. 
- The 500 errors is included.

<span id="features-future"></span>

### 3.2 Features left to implement in the future 
- Adding a favorite and review section. Users can favorite their product, review and see them on their favorite page if they are logged in. 
- Creating a interactive and flexible subscriptions, where users can save points for discounts.
- Expand the collection where people can choose between different flavours. In addition, they can also can buy equipment like cups, mugs and other accessories and coffee machines for the products.
- Adding an address finder where the address finder can check if the address is valid and exists.

<div align="right">
    <a href="#coffee house.">↥ Back to top!</a>
</div>

<span id="technologies"></span>

<h1>4. Technologies used</h1>

#### Languages used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML5 provides the structure and the content for my project. 
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - CSS3 provides the style of the HTML5 elements.
- [JavaScript](https://nl.wikipedia.org/wiki/JavaScript)
    - JavaScript provides the interactive elements on the website. 
- [jQuery](https://jquery.com/)
    - jQuery is used for implementation of Bootstrap.
- [Python](https://www.python.org/)
    - Python provides the backend of the project.
- [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))
    - Jinja provides the templating language for Python.

#### Frameworks, libraries & other
- [Django](https://www.djangoproject.com/) 
    - The GitPod is used as Python framework for the project.
- [Gitpod](https://www.gitpod.io/) 
    - The GitPod is used to develop the project.
- [Git](https://git-scm.com/)
    - The Git was used for version control to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
    - The GitHub is used to host the project.
- [Pip3](https://pip.pypa.io/en/stable/)
    - Pip3 is used for installing the necessary tools, libraries and frameworks.
- [Heroku](https://heroku.com/)
    - Heroku is a cloud platform used to host the project and deploy the app.
- [AWS Amazon](https://aws.amazon.com/)
    - AWS Amazon is used to store static and media files.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - Boto3 is used for compatibility in AWS.
- [Gunicorn](https://pypi.org/project/gunicorn/)
    - Gunicorn is used to enable deployment to Heroku.
- [Spycopg2](https://pypi.org/project/gunicorn/)
    - Spycopg2 is used to enable the PostGreSQL database to connect with Django.
- [Google Fonts](https://fonts.google.com/)
    - Google Fonts is used to provide the font roboto for all the text that is used in the project. 
- [Balsamiq](https://www.balsamiq.com/)
    - Balsamiq is used to create the mockup designs for the project.
- [Bootstrap](https://getbootstrap.com/)
    - Bootstrap is used for the design framework.
- [Django Crispy Forms ](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Django Crispy Forms is used to style the Django forms
- [Stripe](https://stripe.com/en-nl)
    - Stripe is used for the secure payments. 

#### Databases 
- [SQlite3](https://www.sqlite.org/index.html)
    - SQlite3 is used as the development database.
- [PostgreSQL](https://www.postgresql.org/)
    - PostgreSQL is used as the production database.

#### Testing tools used 
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/open) is used to detect problems and test responsiveness.
- [Autoprefixer](https://autoprefixer.github.io/)
    - Autoprefixer is used to parse the CSS and to add vendor prefixes to CSS rules. 
- [W3C Markup Validation Service](https://validator.w3.org/)
    - The W3C Markup Validation Service is used to check whether there were any errors in the HTML5 code. 
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
    - The W3C CSS validator is used to check whether there were any errors in the CSS3 code.
- [JShint](https://jshint.com/)
    - JShint is a JavaScript validator that is used to check whether there were any errors in the JavaScript code. 
- [PEP8](http://pep8online.com/)
    - The PEP8 validator is used to check whether there were any errors in the Python code.

<div align="right">
    <a href="#coffee house.">↥ Back to top!</a>
</div>

<span id="testing"></span>

<h1>5. Testing</h1>

The testing process can be found [here](TESTING.md).

<div align="right">
    <a href="#coffee house.">↥ Back to top!</a>
</div>

<span id="deployment"></span>

<h1>6. Deployment</h1>

#### Requirements 
- Python3 
- Github account 
- Heroku account
- An IDE of choice 
- Stripe account
- AWS Amazon account
- Gmail account

#### Clone the project 
To make a local clone, follow the following steps. 
1. Log in to GitHub and go to the repository. 
2. Click on the green button with the text **“Code”.**
3. Click on **“Open with GitHub Desktop”** and follow the prompts in the GitHub Desktop Application or follow the instructions from **[this link](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)** to see how to clone the repository in other ways. 

#### Working with the local copy
1. Install all the requirements: Go to the workspace of your local copy. In the terminal window of your IDE type: **pip3 install -r requirements.txt**.
2. Set up the environment variables: 
    - Create a `.gitignore` file in the root directory of the project. 
    - Create a `.env` file. This will contain the following environment variables:

    ```
    Import os
    os.environ("SECRET_KEY", "Added by developer")
    os.environ("STRIPE_PUBLIC_KEY", "Added by developer")
    os.environ("STRIPE_SECRET_KEY", "Added by developer")
    os.environ("STRIPE_WH_SECRET", "Added by developer")
    ```

    - Add the `.env` file to the `.gitignore` file.
    **NOTE:** See more in the [Stripe Documentation](https://stripe.com/docs/keys) to read more about setting the API key.
3. Migrate the models to create the database by the following commands:
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
4. Load the data fixtures for categories and product in this exact order:
    - `python3 manage.py loaddata categories`
    - `python3 manage.py loaddata products`
5. Create a superuser. The superuser has acces to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter your username, email and password.
6. Run the app: Open your terminal window in your IDE. Type: `python3 manage.py runserver` and run the app.
7. To acces the admin environment, you can add `/admin` at the end of your url and login with the superuser.


#### Heroku Deployment  
1. Set up local workspace for Heroku 
    - In terminal window of your IDE type: `pip3 freeze -- local > requirements.txt.` (The file is needed for Heroku to know which filed to install.)
    - Create a Procfile with the following text: `web: gunicorn <name app>.wsgi:application` (The file is needed for Heroku to know which file is needed as entry point.)
    - Push all these files to your GitHub reposity.
2. Set up Heroku
    - Create a Heroku account and create a new app and select your region. 
    - Go to resources in Heroku and search for **postgess**. Select **Hobby dev - Free** and click on the provision button to add it to the project.
    - Go to the settings app in Heroku and go to **Config Vars**. Click on **Reveal Config Vars** and add the following config variables:

    | KEY            | VALUE         |
    |----------------|---------------|
    | AWS_ACCESS_KEY_ID | `<aws access key>`  |
    | AWS_SECRET_ACCESS_KEY | `<aws secret access key>`  |
    | DATABASE_URL| `<postgres database url>`  |
    | EMAIL_HOST_PASS | `<email password(generated by Gmail)>` |
    | EMAIL_HOST_USER| `<email address>`  |
    | SECRET_KEY | `<your secret key>`  |
    | STRIPE_PUBLIC_KEY| `<your stripe public key>`  |
    | STRIPE_SECRET_KEY| `<your stripe secret key>`  |
    | STRIPE_WH_SECRET| `<your stripe wh key>`  |
    | USE_AWS | `True`  |

3. Set up Database
    - Copy the **DATABASE_URL** (Postgres URL) from the config variables of Heroku and past it into the default database in `setting.py`

    ```
    DATABASES = {
        'default': dj_database_url.parse("<DATABASE_URL here>")
    }
    ```
    **NOTE:** This setup for the databases is temporary for deployment to Heroku.
    - Migrate the models to create the database by the following commands:
        - `python3 manage.py makemigrations`
        - `python3 manage.py migrate`
    - Load the data fixtures for categories and product in this exact order:
        - `python3 manage.py loaddata categories`
        - `python3 manage.py loaddata products`
    - Create a superuser. The superuser has acces to the admin environment.
        - `python3 manage.py createsuperuser`
        - Enter your username, email and password.
    - Now you can remove the DATABASE_URL from `settings.py` and set the 'old' default DATABASE settings.
    - Adjust the ALLOWED_HOSTS in you settings.py with the following:
    
    ```
    ALLOWED_HOSTS = ['<your Heroku app URL>', 'localhost]
    ```
    - Push the code to Github.
4. Connect with Heroku 
    - Click on the **Connect to GitHub** section in the deploy tab in Heroku. 
        - Search your repository to connect with it.
        - When your repository appears click on **connect** to connect your repository with the Heroku. 
    - Set automatic deploment: Go to the deploy tab in Heroku and scroll down to **Automatic deployments**. Click on **Enable Automatic Deploys**. By **Manual deploy** click on **Deploy Branch**.
Heroku will receive the code from Github and host the app using the required packages. 
Click on **Open app** in the right corner of your Heroku account. The app wil open and the live link is available from the address bar. 

#### Hosting static and media files with AWS
The static and media files are hosted in the AWS S3 Bucket. To host them you will need an account and create an S3 bucket and set a group, policy and user in the IAM environment. 
Read more about the the S3 Bucket storage [here](https://aws.amazon.com/s3/). For more information about the storage in your project [click here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).

<div align="right">
    <a href="#coffee house.">↥ Back to top!</a>
</div>

<span id="credits"></span>

<h1>7. Credits</h1>

#### Content
- The idea of this project is from [Frontend mentor challenge](https://www.frontendmentor.io/challenges/coffeeroasters-subscription-site-5Fc26HVY6) and [The Barn](https://thebarn.de/).

#### Media 
- All images are from [Pexels](https://www.pexels.com) and [Unsplash](https://unsplash.com/).The video on homepage is from [Pexels](https://www.pexels.com).The logo is made on [Canva](https://www.canva.com/).


#### Code
- The code for the project is partly from the video lessons of the Boutique Ado project of [Code Institute](https://codeinstitute.net/). 
- [Stack Overflow](https://stackoverflow.com/) was helpful for little bugs or troubles in the code. 

<div align="right">
    <a href="#coffee house.">↥ Back to top!</a>
</div>

<span id="Acknowledge"></span>

<h1>8. Acknowledge</h1>

I would like to thank:

-The support and guidance of my mentor Precious Ijege.

-The lessons and knowledge-walkthrough videos on the Code Institute platform [Code Institute.](https://codeinstitute.net/)

<div align="right">
    <a href="#coffee house.">↥ Back to top!</a>
</div> 
<span id="Disclaimer"></span>

<h1>9. Disclaimer</h1>

Please contact me: fatimasmails@gmail.com if there is any issue with copyright or the content. 

This project is for educational purpose only.

Thank you for visiting!

<div align="right">
    <a href="#coffee house.">↥ Back to top!</a>
</div>


