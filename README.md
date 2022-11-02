# **GusCosta_T2A2**

#### **R1 - Identification of the problem you are trying to solve by building this particular app. What the app is, what problem does it solve?**

- It takes a name of a type of wine and it returns food options that pair with it.
- It allows the user to acquire knowledge about the different types of wine and the foods that goes with it.


#### **R2 - Why it is a problem that needs solving?**

- Anyone that has an interest in foods and wines can access this API and use it to acquire more knowledge about it, not many options are available for this kind of market.
- It can be used on food apps, restaurant apps, bottleshop apps and other.
- To show that anyone over 18 can buy a bottle of wine, cook food that pairs with it and enjoy the little things in life.

#### **R3 - Why have you chosen this database system. What are the drawbacks compared to others? Why this DB system? using PosgreSQL, why Postgres? compare to others.**

- aoeifg

    [Why Postgresql](https://fulcrum.rocks/blog/why-use-postgresql-database#:~:text=Postgres%20allows%20you%20to%20store,lot%20of%20supporters%20and%20critics.)

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
* Planning - This tab focuses on general management of the project and things that need to be planned.
* In Progress - Tasks that are currently being worked on.
* Next-up - Tasks comming next.

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


    References
    [Reference](https://en.wikipedia.org/)