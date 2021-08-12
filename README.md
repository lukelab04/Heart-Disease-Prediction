# Heart Disease Prediction
A script to predict whether or not an individual is at risk for heart disease based on certain symptoms. Based on the [Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci) dataset from Kaggle.

# Usage
This repo contains a trained model, so simply running the script will print out the results and accuracy of the predictions. However, by uncommenting lines 31-40, a model will be retrained.

This script depends on network.py, a custom built machine learning library. That is also included in this repo, but you can find more information on it [here](https://github.com/lukelab04/ML.PY).

This particular model takes 13 inputs and gives 1 output. You can input your own data by calling ```net.run(input)``` in the script (the input data should be an array of 13 items.)
