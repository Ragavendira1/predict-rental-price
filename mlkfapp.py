import kfp 
import json
from kfp import dsl
from kfp.compiler import compiler
from kfp.client import client

#Define the model development component
@dsl.component(packages_to_install=['numpy','pandas','joblib','scikit-learn','flask'])
def modeldevelopment(rooms: int,sqft: float) -> float:
    #Importing all required libraries
    import pandas as pd
    import numpy as np
    import joblib
    from flask import Flask, render_template, request 
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    
    # Load and Process the data
    rentalDF = pd.read_csv('https://raw.githubusercontent.com/Ragavendira1/predict-rental-price/d1ff8b034e32baf4ef77cbd9752f346e258f61c0/data/rental_1000.csv')
    
    # Data Transformation(Featurization  - Use Features for Model Development)
    X = rentalDF[['rooms','sqft']].values # Features
    y = rentalDF['price'].values          # Labels
    
    # Split Data into Training and Testing 
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20)
    
    # Model Training
    model = LinearRegression().fit(X_train,y_train)
    
    # Save the Model
    joblib.dump(model,'/tmp/rental_price_model.joblib')

    # compute RMSE (optional)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test,y_pred))
    print(f"RMSE: [rmse]")

    # Predict the rental price
    predict_rental_price = model.predict(np.array([[rooms,sqft]]))[0]
    #print(f"The Predicated Rental Price for Rooms  = {rooms} and Area in Sqft = {sqft} is={predict_rental_price}")
    return (predict_rental_price)

#Define the pipeline using the model development and prediction components       
@dsl.pipeline(
        name='Rental Prediction Pipeline',
        description='A pipeline to predict rental price using a trained model.'
)
def rental_prediction_pipeline(rooms_count: int, area_in_sqft: float) -> float:
    task = modeldevelopment(rooms=rooms_count,sqft=area_in_sqft)
    return task.output

if __name__ == "__main__":
    # Load pipeline arguments from a JSON file
    with open('pipeline_args.json','r') as f:
        arguments = json.load(f)
    # Compile and the pipeline
    # Connect to Kubeflow pipelines server
    kfp_endpoint=None # Replace with actual URL of the your kubeflow pipelines server
    client = kfp.Client(host=kfp_endpoint)
    
    # Create an Experiment
    experiment_name= 'Experiment for Model to predict Rental Price'
    experiment = client.create_experiment(name=experiment_name)
    print(f'Experiment created: {experiment}')

    # Run the pipeline using Create_run_from_pipeline_func
    run_name= 'Run of Rental Price Prediction Pipeline'
    run_result = client.create_run_from_pipeline_func(
        pipeline_func=rental_prediction_pipeline,
        run_name=run_name,
        experiment_name=experiment_name,
        arguments={
            'rooms_count': arguments.get('rooms_count'),
            'area_in_sqft': arguments.get('area_in_sqft')
        } # Provide the actual parametes here

    )
    
    print(f'Pipeline run submitted: {run_result}')