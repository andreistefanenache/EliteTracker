# EliteTracker

## Objective

* To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

Broken down this project has the following requirements:

-Create an app in Python that utilises CRUD functionality\
-Deploy front end using Flask\
-Track project progress using Scrum style board\
-Include use of external SQL database\
-Testing\
-Documentation\
-Repository of code base


## Project Initiation

I propose to create an app that allows the user to track Various player characters and the ships that they pilot in the popular video game Elite: Dangerous. Users will thus be able to input details for each player character they choose to track including their combat rank, create new ship models to track ship types, and then also add the individual ships that player characters regularly pilot, including an estimated armament rating and tags that briefly denote the appearance for quick reference. The User should be able to view a list of the individual ships owned by any one player character. \
\
The implicit CRUD functionality of this app will include:

* CREATE\
  -Add Pilots\
  -Add Ships\
  -Add Pilots Ships
  
* READ\
  -View Pilots\
  -View Pilots Ships arrayed by individual Pilot
  
* UPDATE\
  -Edit the details of all items in the database
  
* DELETE\
  -Remove any individual item from the database
  

## Planning, Design and Project Tracking

### ERD

I began with a basic entity relationship diagram designed around the relationships I expected these entities to have, with the assumption that these may change slightly in the development process. My initial design looked thus:
![Elite Dangerous Adversary Tracker(1)](https://user-images.githubusercontent.com/80707106/126901614-b1de3fdf-c96d-4e1a-9722-137cb8f24eac.png)

The following design is the updated model actually used in the project.\ 
The first change occurred when I realised that a composite key was an unneccessary complication. Instead I simply related the two main tables to the association table using the primary keys. Other changes were minimal changes to the desired attributes. Most notably to remove the fatuous attribute 'base engine rating' from the ship type table.
![Elite The Dangerous](https://user-images.githubusercontent.com/80707106/126901573-4fcfc3ba-4c1d-4d21-92a7-0bb147a128ef.png)

The main point of the relational data between these entities is the use of specific, already registered Pilots and Ship types when inputting data for individually named ships.

### Jira Board

I decided on using Jira as the provider for my project board as I wished a little experience in using software widely used in industry. My use of the software was basic but I was easily able to visualise the work I was doing and hed yet to complete so it certainly fulfilled it's function.
![JiraBoard](https://user-images.githubusercontent.com/80707106/126902122-492b2dc8-83ab-4a2c-8473-b09f5dfa8558.png)

### Risk Assessment

My risk assessment, though basic, attempted to percieve possible threats to the project. The entries with proposed Control Measures as opposed to implemented were considered and noted later on towards the end of the project.
![RiskAssessment](https://user-images.githubusercontent.com/80707106/126902336-9c4b2105-76c6-4373-89d3-64cd61696b2e.png)


## Front End

