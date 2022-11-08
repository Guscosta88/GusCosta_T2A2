# **GusCosta_T2A2**

#### **R1 - Identification of the problem you are trying to solve by building this particular app. What the app is, what problem does it solve?**

- It takes a name of a type of wine and it returns food options that pair with it.
- It allows the user to acquire knowledge about the different types of wine and the foods that goes with it.


#### **R2 - Why it is a problem that needs solving?**

- Anyone that has an interest in foods and wines can access this API and use it to acquire more knowledge about it, not many options are available for this kind of market.
- It can be used on food apps, restaurant apps, bottleshop apps and other.
- To show that the person accessing the app, can cook food that pairs with it and enjoy the little things in life.

#### **R3 - Why have you chosen this database system. What are the drawbacks compared to others? Why this DB system? using PosgreSQL, why Postgres? compare to others.**

- aoeifg

    [Why Postgresql](https://fulcrum.rocks/blog/why-use-postgresql-database#:~:text=Postgres%20allows%20you%20to%20store,lot%20of%20supporters%20and%20critics.)

#### **R5 - Document all endpoints for your API.**

----------------------------------------------------------------

#### **1. auth/register/**

- Method: Post
- Identifier: None
- Authentication: Password Hashed with the use of Bcrypt
- Token: None
- Description: Adds new user information to the Database.

![Post auth/register/](./images/endpoints/001.jpg)

----------------------------------------------------------------

#### **2. auth/login/**

- Method: Post
- Identifier: Email
- Authentication: email and Password
- Token: Generated with JWT
- Description: Allows the registered user to Login and it generates a JWT Token required to access the other routes.

![Post auth/login/](./images/endpoints/002-A.jpg)

----------------------------------------------------------------

#### **3. auth/users/**

- Method: Get
- Identifier: None
- Authentication: None
- Token: None
- Description: It displays a list with all users, including which wine and which food the user entered.

![Get auth/users/](./images/endpoints/002-B.jpg)

----------------------------------------------------------------

#### **4. auth/users/id**

- Method: Get
- Identifier: user_id
- Authentication: None
- Token: None
- Description: It displays information of the user with the selected id, including which wine and which food the user entered.

![Get auth/users/id](./images/endpoints/002-C.jpg)

----------------------------------------------------------------

#### **5. wines/**

- Method: Post
- Identifier: user_id
- Authentication: @jwt_required()
- Token: JWT Access bearer Token Generated when login is successful.
- Description: It allows the user to add a new wine to the database and it returns the new entered wine and user information. It also adds the date created with the use of datetime Python Module.

![Post wines/](./images/endpoints/003.jpg)

----------------------------------------------------------------

#### **6. wines/**

- Method: Get
- Identifier: None
- Authentication: None
- Token: None
- Description: It Displays all wines in the database.

![Get wines/](./images/endpoints/004.jpg)

----------------------------------------------------------------

#### **7. wines/id**

- Method: Get
- Identifier: wine_id
- Authentication: None
- Token: None
- Description: It Displays id selected wine information.

![Get wines/id](./images/endpoints/005.jpg)

----------------------------------------------------------------

#### **8. wines/id**

- Method: Delete
- Identifier: wine_id
- Authentication: @jwt_required()
- Token: JWT Access bearer Token Generated when login is successful.
- Description: It Deletes id selected wine information and returns a delete successfully message.

![Delete wines/id](./images/endpoints/006.jpg)

----------------------------------------------------------------

#### **9. wines/id**

- Method: Put / Patch
- Identifier: wine_id
- Authentication: @jwt_required()
- Token: JWT Access bearer Token Generated when login is successful.
- Description: It Updates id selected wine information and returns Updated wine Information.

![Update wines/id](./images/endpoints/008.jpg)

----------------------------------------------------------------

#### **10. foods/**

- Method: Post
- Identifier: user_id
- Foreign key: wine_id
- Authentication: @jwt_required()
- Token: JWT Access bearer Token Generated when login is successful.
- Description: It allows the user to add a new food to the database and it returns the new entered food, user and wine information. It also adds the date created with the use of datetime Python Module.

![Post foods/](./images/endpoints/009.jpg)

----------------------------------------------------------------

#### **11. foods/**

- Method: Get
- Identifier: None
- Authentication: None
- Token: None
- Description: It Displays all foods in the database.

![Get foods/](./images/endpoints/010.jpg)

----------------------------------------------------------------

#### **12. foods/id**

- Method: Get
- Identifier: food_id
- Authentication: None
- Token: None
- Description: It Displays id selected food information. It also returns user information and information about the wine that pairs with it.

![Get foods/id](./images/endpoints/011-A.jpg)

----------------------------------------------------------------

#### **13. foods/id**

- Method: Delete
- Identifier: food_id
- Authentication: @jwt_required()
- Token: JWT Access bearer Token Generated when login is successful.
- Description: It Deletes id selected food information and returns a delete successfully message.

![Delete foods/id](./images/endpoints/011.jpg)

----------------------------------------------------------------

#### **14. foods/id**

- Method: Put / Patch
- Identifier: food_id
- Authentication: @jwt_required()
- Token: JWT Access bearer Token Generated when login is successful.
- Description: It Updates id selected food information and returns Updated food Information.

![Update foods/id](./images/endpoints/013.jpg)

----------------------------------------------------------------

#### **Error Handling Endpoints and code snippets:**

----------------------------------------------------------------

#### **1. auth/login/**

- Method: Post
- Identifier: None
- Authentication: email and password
- Token: None
- Description: Tried login in without required information.
- Error: 400 Bad Request

![Error 400](./images/endpoints/014-400.jpg)

![Error 400](./images/endpoints/015-400.jpg)

----------------------------------------------------------------

#### **2. wines/**

- Method: Post
- Identifier: user_id
- Authentication: @jwt_required()
- Token: JWT Access bearer Token Generated when login is successful.
- Description: Tried adding new wine but had a field typo. Returns an Unknown field message.
- Error: 400 Bad Request

![Error 400](./images/endpoints/016-400.jpg)

----------------------------------------------------------------

#### **3. wines/**

- Method: Post
- Identifier: user_id
- Authentication: @jwt_required()
- Token: JWT Access bearer Token Generated when login is successful.
- Description: Tried adding new wine without token. returns a missing authorization message.
- Error: 401 Unauthorized

![Error 401](./images/endpoints/017-401.jpg)

![Error 401](./images/endpoints/018-401.jpg)

----------------------------------------------------------------

#### **4. auth/login/**

- Method: Post
- Identifier: email
- Authentication: email and password
- Token: None
- Description: Tried login in with wrong password. Returns a invalid email or password message.
- Error: 401 Unauthorized

![Error 401](./images/endpoints/019-401.jpg)

----------------------------------------------------------------

#### **5. 404**

- Method: Get
- Identifier: None
- Authentication: None
- Token: None
- Description: Tried accessing non existing route. Returns a not found message.
- Error: 404 Not Found

![Error 404](./images/endpoints/020-404.jpg)

![Error 404](./images/endpoints/021-404.jpg)

----------------------------------------------------------------

#### **6. auth/register/**

- Method: Post
- Identifier: None
- Authentication: None
- Token: None
- Description: Tried Registering with email already entered in the database. Returns a email already exists message.
- Error: 409 Conflict

![Error 409](./images/endpoints/022-409.jpg)

![Error 409](./images/endpoints/023-409.jpg)

----------------------------------------------------------------

#### **7. foods/**

- Method: Post
- Identifier: user_id
- Foreign Key: wine_id
- Authentication: @jwt_required()
- Token: JWT Access bearer Token Generated when login is successful.
- Description: Tried adding new food and entered non existing wine_id foreign key. return a wine_id not present in the table message.
- Error: 500 IntegrityError

![Error 500](./images/endpoints/024-500.jpg)

![Error 500](./images/endpoints/025-500.jpg)

----------------------------------------------------------------


#### **R6 - An ERD for your app.**

![ERD](./images/wine_and_food_ERD.svg)

#### **R9 - Discuss the database relations to be implemented in your application.**

- User = id primary_key, first_name, last_name, email NOT NULL UNIQUE, password NOT NULL, dob.
- Wine = id primary_key, name, description, region, type, date, user_id foreign_key.
- Food = id primary_key, name, description, type, date, wine_id foreign_key, user_id foreign_key.

#### **R10 - Describe the way tasks are allocated and tracked in your project**

- The managing system tool I have decided to use is Trello board, I started my board with an Agile template and made some adjustments to suit my project which is divided into 5 tabs:
* Completed - This is where I archive the tasks that are completed.
* Design - on this session I alocated tasks that are related to Design such as, Code requirements, Conventions, etc.
* Planning - This tab focuses on general management of the project and things that need to be planned and that can guide the direction of the project such as User Stories.
* In Progress - Tasks that are currently being worked on.
* Next-up - Tasks comming next.

#### **User Stories:**

- Taking into consideration the main three types of target audience the API is created for, I have decided to create three user stories to understand what would be the way these three distinct users would approach its usability and with what end, to also understand the priority of each and what features should be available.
    Any user can Register and login, access and alter foods and wines.

![User Story One](./images/user_story_one.svg)

#### **User Story One:**

- Analysing the first user story which is from a Professional Sommelier, I was able to identify Three features that the app needs to support to attend his needs. He needs to be able to acess a list or one specific wine, he needs to be able to add a wine if not in the list and he needs to be able to delete any wine he thinks is not in accordance with his standards.

![User Story Two](./images/user_story_two.svg)

#### **User Story Two:**

- Analysing the second user story which is from a Chef, I was able to identify Three features that the app needs to support to attend his needs. He needs to be able to acess a list or one specific food, he needs to be able to add foods if not in the list and he needs to be able to delete any foods he thinks are not in accordance with his standards.

![User Story Three](./images/user_story_three.svg)

#### **User Story Three:**

- Analysing the third user story which is from an Wine Enthusiast, I was able to identify Two features that the app needs to support to attend his needs. He needs to be able to acess a list or one specific food, He needs to be able to acess a list or one specific wine.

#### **Day one:**

- Following the same Idea from my Terminal App I have decided to now build an API for foods and wines.
- On the First day of planning I basically allocated all I can think about in terms of tasks to an Agile Trello Board, the more time I spend in this project, the more I will be able to refine my Trello board to be efficient.
- Initial Commits.

#### **Stand-up Day one:**

1. Trello Board Structure, App idea defined.
2. Deciding the best way to approach planning
3. Complete Trello Board, App's purpose, ERD Diagram.
4. Don't think to much, just start.

![Day One](./images/001.jpg)


#### **Day two:**

- Focus on Setting up Schemas, Controllers, app structure and environment configuration in general.


#### **Stand-up Day two:**

1. R1, R2, R6 ERD, R9, server and environment setup, Models.
2. Not blockers just getting everything sorted slowly.
3. Setup Schemas and controllers.
4. If you make a bit the next step opens up and gets clearer.

![Day Two](./images/002.jpg)


#### **Day three:**

#### **Stand-up Day three:**

1. Set-up wine Schemas, wine Controllers defined app structure.
2. translate my ERD to the actual application.
3. Go back to my Trello board and refine it adding User stories, work on the other schemas and controllers.
4. When everything is strategically structured and organized from the beggining it makes the process easier down the road.

![Day Three](./images/003.jpg)

#### **Day Four:**

#### **Stand-up Day Four:**

1. Set-up Table relations.
2. Thinking of best way to Retrieve Wine ID to use it on foods controller.
3. Add tasks to Trello Board that will help refine the code.
4. To have a better idea on how to approach table relations.

![Day Four](./images/004.jpg)


#### **Day Five:**

#### **Stand-up Day Five:**

1. Organized what to be returned on the Schema.
2. Complicating what is simple.
3. Finish the code, Add error handlers, Testing.
4. Most real life API's only need id's to interconnect.

![Day Five](./images/005.jpg)

[T2A2 - Trello Board Link](https://trello.com/invite/b/PFdD3j01/ATTI3c1f6177a4fcfb1c8ad7cb418e806189CE4181F9/t2a2-agile-board)




    References
    [Reference](https://en.wikipedia.org/)