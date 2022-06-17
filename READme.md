# ORIGINAL PLAN:
The original plan for this project was to use terraform to spin-up
a k8s cluster with Jenkins-X running.  Considering the many deprecation issues and bugs I was running into, I scrap the idea and simply used Github Actions.

# THE PIPELINE
- The pipeline is automated to build, and to deploy a docker image
based on a commit to master.  It will then push this docker image to 
google artifact registry.  From there it is deployed to the cluster.  Considering the time crunch, I was not able to finish the deploy portion of the pipeline.  Because of this, I must deploy .yaml files locally.  Close enough? 

# HOW TO RUN PYTHON APP LOCALLY: 

- Start python environment 
source env/bin/activate 

- change base app for flask
FLASK_APP="APP"

- CHANGE FLASK ENVIRONMENT
FLASK_ENV="DEVELOPEMNT"

