from kfp import dsl
from kfp import compiler
import kfp 
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
    
    
    # Data Processing
    # Load and Process the Data 
    #rentalDF = pd.read_csv('data/rental_1000.csv')
    rentalDF = pd.read_csv('https://raw.githubusercontent.com/Ragavendira1/predict-rental-price/d1ff8b034e32baf4ef77cbd9752f346e258f61c0/data/rental_1000.csv')
    # Data Transformation(Featurization  - Use Features for Model Development)
    X = rentalDF[['rooms','sqft']].values # Features
    y = rentalDF['price'].values          # Labels
    
    # Split Data into Training and Testing 
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20)
    
    # Model Training
    model = LinearRegression().fit(X_train,y_train)

    #sample_index = 0 # change ths index to test different samples
    #predict_rental_price = model.predict([X_test[sample_index]])[0]
    #print(f"The Actual Rental Price for Rooms with count = {X_test[sample_index][0]} and Area in Sqft ={X_test[sample_index][1]} is={y_test[sample_index]}")
    #print(f"The Predicated Rental Price for Rooms with count = {X_test[sample_index][0]} and Area in Sqft = {X_test[sample_index][1]} is={predict_rental_price}")
    #return (predict_rental_price)
       
    predict_rental_price = model.predict(np.array([[rooms,sqft]]))[0]
    print(f"The Predicated Rental Price for Rooms is={predict_rental_price}")
    
    return (predict_rental_price)

    # Save the Model
    #joblib.dump(model,'rental_price_model.joblib')
 
    #Load the Model
    #model = joblib.load('rental_price_model.joblib')
    
    # initialize Flask Application
    #app = Flask(__name__)
    
    #@app.route('/')
    #def home():
        #return render_template('index.html')
    
    #@app.route('/predict',methods=['POST'])
    #def predict():
        #rooms = int(request.form['rooms'])
        #sqft = int(request.form['sqft'])
    
        #Make the Prediction
        #prediction = model.predict(np.array([[rooms,sqft]]))
        #return render_template('result.html',prediction=prediction[0])
@dsl.pipeline
def rental_prediction_pipeline(rooms_count: int, area_in_sqft: float) -> float:
    task = modeldevelopment(rooms=rooms_count,sqft=area_in_sqft)
    return task.output

if __name__ == "__main__":
    #    app.run(debug=True,host="0.0.0.0")    
    # Example Prediction for a specific test sample
    #compiler.Compiler().compile(rental_prediction_pipeline,'rental_prediction.yaml') 
    # Connect to Kubeflow Pipelines Server
    kfp_endpoint = None # Replace with the actual URL of your Kubeflow Pipelines server
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
        arguments={'rooms_count':3,'area_in_sqft':1500} # Provide the actual parametes here

    )
    
    print(f'Pipeline run submitted: {run_result}')