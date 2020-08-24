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
 
 ## EDA  
 
 
 
