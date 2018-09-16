# Influenze Vaccine Prediction
This repo explores tweets trends such as:
* flu_vaccine_received 
* flu_vaccine_received_relevant_intent_to_receive	
* flu_vaccine_received_relevant_positive_sentiment
* flu_vaccine_relevant
* flu_vaccine_relevant_intent_to_receive

This repo also juxtaposes them with vaccination trends provided by HHS.



## Things to do:
 * Benchmark Prediction based on linear models just based on the HHS data 
 * Variations of the linear model to try:
    * Combing last seasons data to predict this seasons data
    * Normalizing data by state poppulation
    * Add google trends data to prediction features 
    * Add twitter data to prediction features
    
## Completed:
 * Download state wise /national data and try doing weekly predictions
 * Benchmarked Prediction  based on this years data for p weeks forward using data from the previous k weeks
 * Just using previous k weeks of HHS data to predict n weeks forward in time
