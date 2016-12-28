# Premier League Prediction

------------------------------------

Predict the Result of a Premier League Football match as Home Win, Away Win or Draw. Premier League matches are played between England's top 20 Football matches. All Teams have to play every other team in their Home and the opponent's home. Every Team play a total of 38 matches per season. We have used the cost of the Football squad assembled as the predictor for the results.

##Installation
###Download the Data
- Clone this Repo to your Computer.
- Get into the Folder using `cd Premier-League-Prediction`.
- Note that the Required data will be downloaded along with the Repo in `Data` Folder.

###Install the Requirements
- Ensure that Python-3 and Pip are installed in the Computer.
- Install the required Libraries using `pip install -r requirements.txt`.

##Usage
- Run `mkdir processed' to create a directory for our processed data sets.
- Run `python assemble.py' to create the datasets for our Program. 
  * This will create `FullSquadData.csv`, `PL1617.csv` and `train.csv`.
- Run `python predict.py` 
  * This will run a Logistic regression algorithm with Cross validation on the training data and print the Accuracy score.

##Extend this
This project can be extended in the following ways:
- Trying to predict the result with different algorithms
- Predict the results of Future fixtures Weekly
- Including Value of the Starting XI instead of Average squad value
  * This would need Starting line up of the teams
 
