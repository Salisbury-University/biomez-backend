BIOME-Z Project Backend
Developed by Sam Blaxberg and Nick Lautieri
======================

Setting up MongoDB database:

1) Create remote MongoDB database hosted by MongoDB Atlas. Start by following link below:
  https://www.mongodb.com/basics/create-database-for-python-app?utm_campaign=python_inf_tim1&utm_source=youtube&utm_medium=influencers&utm_term=atlas
  
  a) Select free cloud database labeled "Shared"
  b) Select cloud provider and region (AWS and NAE)
  c) Rename cluster if you'd like (note: this cannot be changed later)
  d) Create a username and password to authenticate your connection, then create user
  e) Select connect from "My Local Environment" and add your current IP address
  f) Finish and close
  
2) Create virtual environment and install necessary dependencies (I used VS Code for this step which has a convenient extension MongoDB)

  a) Install pymongo:
  ~~~ pip install pymongo[srv] ~~~
  


Requirements: Flask
Installation Instructions:
