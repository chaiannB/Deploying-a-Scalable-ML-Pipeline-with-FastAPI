# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was created for a Udacity project for the class Machine Learning DevOps.
We used a Random Forest model for this project and it was created in December 2024.
## Intended Use
Based on the data from census.csv, this model is intended to be able to identify the likelihood of someone making a specific amount of income based on a variety of features in the dataset.
## Training Data
For this project, I used 80% of the data to train the Random Forest model.
## Evaluation Data
To ensure that the model is not overfitted, we have held back 20% of the data to test our model on.
## Metrics
We looked at 3 different metrics in this model: recall, precision, and fbeta. This modeled received the following scores for these metrics:
recall: 0.6277
precision: 0.7226
fbeta: 0.67
As we can see, the model performed relatively well in each area but there is definitely room for improvement if the model were to be adjusted. 

Then, we sliced the data to see how the model would perform on these metrics for different features. The performance on these metrics is held in the txt document slice_output.text.

## Ethical Considerations
There are some areas that this model performed particularly poorly at predicting based on the slices in sice_output.txt. 
Areas where workclass is unknown, the areas of HS-grad, 10th, 11th 12th, 1st-4th, 5th-6th, 9th, and 7th-8th grade level education, marital status had varied levels or accuracy and precision, unknown occupation, Handlers and Cleaners occupation, Other-service occupations. The relationship metrics also have quite low scores. 

When it comes to race, white and asian races were categorized much more accurately than black or other races. 

Please be aware of biases, such as the ones above,  that may be present in this model before use. 

## Caveats and Recommendations
This data was collected quite a long time ago so it may be better to look for more recent data if trying to predict income in 2024. Als0, this model did not perform extremely well on the metrics so it may be best to adjust the Random Forest parameters to attempt to get a better performance on the metrics before implementing the model.