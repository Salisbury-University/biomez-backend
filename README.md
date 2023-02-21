BIOME-Z Project Backend
======================
Developed by Nick Lautieri

## Setting up MongoDB database:

##### Create remote MongoDB database hosted by MongoDB Atlas. [Start here](https://www.mongodb.com/basics/create-database-for-python-app?utm_campaign=python_inf_tim1&utm_source=youtube&utm_medium=influencers&utm_term=atlas)

    a) Create account and select free cloud database labeled "Shared"
    b) Select cloud provider and region (AWS and NAE)
    c) Rename cluster if you'd like (note: this cannot be changed later)
    d) Create a username and password to authenticate your connection, then "Create User"
    e) Select connect from "My Local Environment" and add your current IP address. (Also includes a setting to allow access from any device)
    f) Finish and close
   
## Installing back-end libraries:
   
##### Create virtual environment and install necessary dependencies (using VS Code and Unix commands)
    a) Navigate to your desired project folder and setup virtual environment:
`python venv [venv_name]`

    b) Install flask:
`pip install Flask`

    c) Install CORS:
`pip install -U flask-cors`
    
    d) Install pymongo:
`pip install pymongo[srv]`

    e) Install yaml for accessing URI key:
`pip install pyyaml`
    
    f) Add MongoDB extension for VS Code
    
## Importing files from Zotero library into MongoDB

    a) After being added to Dr. Maier's Zotero library, use the control key to select up to 100 files at once
    b) Click the export button and then export as a CSV file
    c) Open MongoDB Compass and sign into database
    d) Select your collection and then click 'Add Data' then 'Import File'
    e) Insert the Zotero CSV file and choose CSV file type
    f) Keep the delimiter as comma, deselect ignore empty strings, and select the following fields:
        - Item Type, Pub Year, Author, Title, Pub Title, ISSN, DOI, URL, Abstract Title, Date, Issue, Volume, Library Catalog, Manual and Automatic Tags
    g) Finish my clicking import



