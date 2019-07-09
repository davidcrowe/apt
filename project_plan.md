## CNN Semantic Segmentation
**Real Estate Image Recognition Search within 20 miles of Harvard**  

*Team 10: David Crowe, Nicolas Garza, Cynthia Gao*

## Project Description
The objective of the project is to leverage a combinatorial neural network (CNN), big data & cloud computing to create an image recognition system that detects specific apartment attributes from photos. The CNN will be deployed to the web via a Flask app integrating D3 vizualization, allowing users to easily view and interpret the results. The results of the CNN will also be combined with other apartment data to predict listing price and days on the market, thus combining deep learning networks and big data to create a powerful apartments analytic platform.  



## Project Approach
We will use an agile approach with weekly sprints. An outline of the objectives for each sprint can be found below:

### Sprint 1: Flask
Sprint owner: David  
Sprint timeline: *7/9 - 7/15*

| Area | Task | Task Owner | Notes |
| ---- | ---- | ---------- | ----- |
| Project Planning | Build Project Plan & push to Github | Team | (insert comments here) |
| Project Planning | Build Process Book & push to Github | Team |  |
| Project Planning | Write user stories for this week's tasks & post to process book by EOD 7/10 | Team |  |
| Web Application | Initialize Flask App, add base template / landing page / map page placeholder, add register & login functionality, & deploy to Heroku | David |  |
| Web Application | Design database, implement in Postgres & upload data | Cynthia | |
| Web Application | Leverage Bootstrap to develop template for apartment listing pages | Nicolas |  |
| Web Application | Ensure data is connected to & viewable in app  | David |  |



### Sprint 2: Neural Network 
Sprint owner: Nicolas  
Sprint timeline: *7/16 - 7/22*

| Area | Task | Task Owner | Notes |
| ---- | ---- | ---------- | ----- |
| Neural Network | Randomly deform, crop & brighten images to create new training inputs and improve results of CNN re-training | TBD | |
| Neural Network | Split images into training, validation & test sets | TBD | |
| Neural Network | Re-train a pre-trained CNN using labeled apartment photos | TBD | |
| Neural Network | Optimize the re-trained model by adjusting hyperparameters such as 'how many training steps', 'learning rate' & 'train batch size' | TBD | |
| Web Application | Integrate optimized CNN into web app, including building a page showing model performance (e.g. test perf. vs. training & val perf; optimized performance vs. re-trained model perf. vs. pre-trained model perf) | TBD | |



### Sprint 3: D3 Visualization 
Sprint owner: Cynthia  
Sprint timeline: *7/23 - 7/29*

| Area | Task | Task Owner | Notes |
| ---- | ---- | ---------- | ----- |
| Data Visualization | Develop map page including locations of available apartments based on location search with filters via D3 | TBD |  |
| Data Vizualization | Try to visualize layer by layer transformations to demonstrate how the NN identifies features within photos | TBD | |
| Data Vizualization | Build interesting D3 vizualizations based on data | TBD | |
| Web Application | Add necessary web server functions & refine UI & DB model as needed | TBD | |



### Sprint 4: Debugging 
Sprint timeline: *7/30 - 8/5*

| Area | Task | Task Owner | Notes |
| ---- | ---- | ---------- | ----- |
| Web Application | Complete any final debugging / tweaking of the Flask app | TBD | |
| Neural Network | Complete any final debugging / tweaking of the CNN | TBD | |
| Data Vizualization | Complete any final debugging / tweaking of the D3 vizualizations | TBD | |



