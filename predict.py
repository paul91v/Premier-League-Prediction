import os
import settings
import pandas as pd
from sklearn import metrics, cross_validation
from sklearn.linear_model import LogisticRegression

def cross_validate(train):
    footy_LR = LogisticRegression(random_state = 1 )
    predictions = cross_validation.cross_val_predict(footy_LR, train[settings.PREDICTORS], train[settings.TARGET], cv = settings.CV_FOLDS)
    return predictions

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath('__file__'))
    train = pd.read_csv(os.path.join(current_dir, settings.PROCESSED_DIR, 'train.csv'))
    predictions = cross_validate(train)
    error = metrics.accuracy_score(train[settings.TARGET], predictions)
    print('CV Accuracy Score: {}'.format(round(error,4)))