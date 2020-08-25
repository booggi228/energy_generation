# Energy Generation: Project Overview
  * Created a tool that estimates renewable energy generation from all renewable types of sources.   
  * Got the inside data from  Ministry of Energy of Ukraine.   
  * Optimized Linear, Lasso, Ridge, Random Forest Regressors and XGBoost using GridsearchCV to reach the best model.    
  * Built a web application using flask.  
  * Link to my application: https://energy-generation.herokuapp.com/  
    
## Code and Tools used
  * **Python version:** 3.7  
  * **Packages:** pandas, numpy, sklearn, matplotlib, seaborn, flask, pickle  
  * **Tools:** Power BI Desktop  
  
 ## Data Cleaning  
 Before building a model, I needed to clean up the data so that it was usable for a model. I made the following changes:  
 * First of all I had to understand nature of the data .info() .describe()
 * Dealt with missing data and null values.  
 * Built heatmap to check the correlation between features that helped to understand feature importance.   
 * Dropped some of extreme outliers.  
 * Dealt with categorical variables using label encoder technique.  
 
 ## Exploratory Data Analysis  
 I looked at the distributions of the data and the value counts for the various categorical variables. After I removed highly correlated features.  
 ![alt text](https://github.com/booggi228/energy_generation/blob/master/images/cor.png "Correlations")
 ![alt text](https://github.com/booggi228/energy_generation/blob/master/images/dashboard-1.png)
 
 ## Model Building  
 First, I transformed the categorical variables into numeric using Label encoder. I also split the data into train and tests sets with a test size of 20%.  
 
 I tried five different models:  
  * Linear regression (77%)
  * Ridge and Lasso regression gave me 77.1% of accuracy.  
  * XGBoost (94%)  
  * Random Forest regressor (98%)  
 I didn't start to apply model tuning techniques because I was pretty satisfied with results I've got from Random Forest with accuracy score 98%.  
 
 ## Productionization  
 In this step, I built a flask web application that was hosted on `heroku` platform. The app takes in a request with a list of values from the data and returns a planned yearly electricity generation.  
 



 
