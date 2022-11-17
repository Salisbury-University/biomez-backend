BIOME-Z Project Backend
======================
Developed by Sam Blaxberg and Nick Lautieri

## Setting up MongoDB database:

##### 1) Create remote MongoDB database hosted by MongoDB Atlas. [Start here](https://www.mongodb.com/basics/create-database-for-python-app?utm_campaign=python_inf_tim1&utm_source=youtube&utm_medium=influencers&utm_term=atlas)

    a) Create account and select free cloud database labeled "Shared"
    b) Select cloud provider and region (AWS and NAE)
    c) Rename cluster if you'd like (note: this cannot be changed later)
    d) Create a username and password to authenticate your connection, then "Create User"
    e) Select connect from "My Local Environment" and add your current IP address
    f) Finish and close
   
##### 2) Create virtual environment and install necessary dependencies (using VS Code and Unix commands)
    a) Navigate to your desired project folder and setup virtual environment
`python venv [venv_name]`
    
    b) Install pymongo 
`pip install pymongo[srv]`

    c) Install python-dotenv for accessing an environment variable file that contains user credentials
`pip install python-dotenv`
    
    d) Add MongoDB extension for VS Code
    
  
Requirements: Flask
Installation Instructions:
