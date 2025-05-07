## BENTOML BASIC ##
- BentoML is a framework for serving and deploying machine learning models. It provides a simple way to package, ship, and run ML models in production.
- It allows you to create a REST API for your model, which can be used to make predictions from anywhere.
- BentoML supports multiple deployment options, including Docker, Kubernetes, and AWS Lambda.
- It is stored in your local machine (user/bentoml) and can be used to create a local server for testing and development.
## BENTOML INSTALLATION ##
1. run `pip install -r requirements.txt` to install the required packages.
1. run `python train.py` to get the model and save it to a file.
2. bentofile.yaml to define the BentoML service and its dependencies.
3. run `bentoml serve service.py:svc --reaload` to start the server. (localhost:3000)
4. run `bentoml build` to build the BentoML service.