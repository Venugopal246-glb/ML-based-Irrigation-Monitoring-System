# ML BASED IRRIGATION MONITORING SYSTEM

## Project Overview

Efficiently automate irrigation by predecting soil moistures levels using environmental and soil data , reducing water wastage and optimizing crop growth
## Key Features

- *Real-time Monitoring:* Remotely monitor your fields for crucial properties such as temperature, humidity, and soil moisture levels.
- *Predictive Insights:* Utilize machine learning algorithms to forecast future soil moisture levels and optimize watering schedules.
- *Water Conservation:* Efficiently use water resources, reducing waste and environmental impact.
- *Improved Crop Yield:* Achieve higher yields and healthier crops by providing optimal irrigation conditions.
- *Data-Driven Decisions:* Make informed decisions based on accurate sensor data and reliable machine learning models.

## Requirements
Make sure you have the following installed before running the project
- Python 3.x
- Jupyter Notebook
- Required Python libraries:
  You can install these by running the command
 ``` bash
  pip install -r requirements.txt
```
## The required libraries are :
- numpy
- pandas
- scikit-learn
- matplotlib
  
## Installition
1. Clone the repository to your local machine;
   ``` bash
   git clone https://github.com/Venugopal246-glb/ML-based-Irrigation-Monitoring-System.git
2. Navigate to the project directory:
``` bash
cd modefied_Crop_recommendation
```
3. Install the required dependencies:
``` bash
pip install -r requirements.txt
```
4. Run the Jupyter Notebook by executing :
``` bash
jupyter notebook
```
5. Open the  main (2).ipynb files in your browser and run the code cells to execute the model.
 ## Usage
 1. Prepare Input Data: The model requires several inputs such as :
    - Temperature(°C)
    - Humidity (%)
    - Rainfall (mm)
    - Soil Moisture (%)
    - Average Temperature (°C)
    
  2. Running the model :
     Open the notebook ( main (2).ipynb ), enter your environmental data, and run the notebook cells. The model will compute the predicted soil moisture level.
3. Results:
The predicted soil moisture levels will be displayed at the end of the notebook, which can be used for decision-making in irrigation systems
4. Optional - Customize the Model:
  You can tweak the model's parameters (e.g., weights, biases, number of hidden layers) inside the notebook to better fit your local environmental conditions or crops.
## File Descriptions
- main (2).ipynb : Contains the soil moisture prediction model using input data to predict the optimal soil moisture levels. This notebook includes pre-trained weights and biases.
- requirements.txt :List all the dependencies needed to run the project
## Model Explanation
The model is based on a neural network approach using a multi-layer perceptron (MLP). It takes in environmental inputs (e.g., temperature, humidity, etc.) and processes them through a hidden layer with a ReLU activation function. The final output is the predicted soil moisture level, which can be directly used in irrigation systems to optimize water usage.
Key Parameters:
- Input Features:Temperarture ,Humidity,Rainfall,Soil Moisture, Average temperature
- Activation Function: ReLU for the hidden layer
- Output: Predicted soil moisture level.
## Contributing
Contributions are always welcome! If you'd like to improve or extend this project:

1. Fork the repository.
2. Create a new feature branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request and describe the changes.
6. 


