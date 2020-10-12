# Accelerated Underwriting Model Deployment
Testing the deployment of applications that serve machine learning models. This focus of this project is more on the technology to put models into production rather than the complexity of the models themselves. Future enchancements include implementing a more sophisiticated model and better looking frontend.

The project is split into a frontend and backend. They are containerized and hosted using docker, docker-compose, and AWS EC2.

The app can be viewed here: http://54.200.227.226:80

# Backend
Using FastAPI to serve the model.
 - Model: Simple decision tree

 
# Frontend
Created using Streamlit.
 - Inputs: Gender, Issue age, BMI
