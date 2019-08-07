**Team 10 Process Book**

### 7/6

| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| Project Planning | Met with Fred to understand project requirements & best practice for approach. To do: fill in project plan | David |  
| Project Planning | Filled in majority of project plan. To do: fill in vizualization section of project plan | David |  


### 7/7

| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| Web Development | Met as a team for detailed introductions and to agree on and fill in the project plan | Team |
| Web Development | Added initial routes.py file; layout.html, register.html, & login.html templates; added Boston March 2018 data set to repo | David |


### 7/8

| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| Web Development | Added initial landing.html file to serve as site landing page; updated routes.py file to add /landing route; removed Boston March 2018 data set to repo | David |


### 7/12

| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| Organization | Added .gitignore file for env and requirements.txt | David |


### 7/14
| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| Database | Added db to routes.py and began models.py; To-do: link local db with zona's db => heroku db | Cynthia |


### 7/17
| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| UI | Improved landing/login pages and updated css file | Nicholas |

### 7/22
| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| CNN | Made the basic layout for the model implementation. | Nicholas |
| UI | Updated the Html Templates with additional bootstrap components and a draft for a D3 Visualization. | Nicholas |
| DB | Replaced initial, overly simple database design with a design that included all fields in the dataset. The data is broken out over multiple tables to optimize design and linked via foreign key relationships | David |
| Heroku | Deployed app and database to Heroku for the 1st time | David |


### 7/28
| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| UI | Continued to fix some errors regarding jinja templates and their DB connectivity. | Nicolas |
| CNN | Worked on the CNN regarding what we commented with our team lead, Fred. | David |
| Debug | Continued to Debug CNN. | David & Nicolas |
| DB | Based on multiple conversations with Fred, moved to a simpler DB design. While we agreed that the initial approach (shown in screenshots in the root/screenshot folder) is optimal, it proved very difficult to import the data given the complexities of having multiple tables and associated foreign key relationships (not included in the source data, which is a single flat csv file). If there is time we can return to a DB model similar to the initial model in order to improve the richness of data included in the app and optimize the performance of the database. | David |
| DB | Added additional database table named images to capture the image features output from the Neural Network | David |
| DB | Created .ipynb and began writing the script to run images through VGG16 to extract features | David |


### 7/31
| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| NN | Ran all 219k images through the NN and extracted the features | David |
| UI | Added photo upload functionality | Nicolas |


### 8/1
| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| NN | Added functionality to run uploaded photos through VGG16 in routes.py, and uploaded csv of feature values from the image dataset | David |
| UI | Significant imporvements to the front end including the begin-search, property-detail and view-properties views. Corresponding improvements to routes.py | Nicolas |


### 8/4

| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| UI | Partly Implemented Mapbox Visualization. | Nicolas |
| UI | Implemented dynamic Feed of properties to view-properties page. | Nicolas |
| DB | Added additional fields to the properties database (specifically address, city, state, remarks & style fields) | David |


### 8/5

| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| NN | Improved .ipynb to split code into multiple cells and export image features in the correct format | David |
| NN | Built functionality to run uploaded images through NN and use norm() function to find the most similar photos in the image database | David |


### 8/6

| Area | Task, To-do, Design, Idea, Question etc. | Name |
| ---- | ---- | ---------- |
| UI | Finalized all front end views, including view-properties & property details. Linked NN output to corresponding similar property image urls to display similar property photos within the property-detail view | Nicolas |
| UI | Finalized 3D map, including importing property address data to display the exact property location on the map | Nicolas |
| NN | Finalized NN & functionality to identify similar photos on the property-detail view | David & Nicolas |
| NN | Troubleshooting to enable upload image feature to work on Heroku. This required removing a line of code which saved the uploaded image, which will also help in terms of the app scalability | David & Nicolas |



