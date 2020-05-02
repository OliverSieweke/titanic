import pandas as pd
import feature_engineering_age as fe
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def estimate_age(df, cutoff=12, max_depth=3, n_estimators=1000):
    '''
    input: DataFrame

    Master function: estimates whether passenger is child or adult
    (for passengers with missing age values).
    Merges predictions with orginal df.

    output: DataFrame
    '''
    # split df in 2 (with/without age values); splits df with age values in X and y
    X, y, df_age_missing = create_X_y(df, cutoff)
    # feature-engineering of X
    X_fe = feature_engineer(X)
    # instantiate and fit model
    m = fit_model(X_fe, y, max_depth, n_estimators)
    # Calculate binary predictions for age
    age_predictions = calc_predictions(df_age_missing, m)
    # merge original df with predictions
    df_final = merge_df(df, age_predictions)

    return df_final

def create_X_y(df, cutoff=12):
    '''
    input: DataFrame

    1/ Splits df in 2 (with/without age values)
    2/ splits df with age values in X and y

    output: DataFrame
    '''
    # split df in 2 (with and without age values)
    df_complete, df_age_missing = df[df['Age'].notna()], df[df['Age'].isna()]
    # drop age column in df_age_missing (contains only NaNs anyway)
    X_test = df_age_missing.drop(['Age'], axis=1)
    # create binary child column
    df_complete = fe.children(df_complete, cutoff=cutoff)
    # define X
    X = df_complete.drop(['child'], axis=1)
    # define y
    y = df_complete['child']

    return X, y, X_test

def feature_engineer(df):
    '''
    input: DataFrame

    Feature-engineering for age estimation.

    output: DataFrame
    '''
    # set variables to keep
    df = df[['Name', 'SibSp', 'Parch']]
    # boolean (0, 1) on whether the passenger has more siblings/spouses than cutoff
    df = fe.many_sibsp(df, cutoff=2)
    # boolean (0, 1) on whether the passenger has more parents/children than cutoff
    df = fe.many_parch(df, cutoff=2)
    # create column indicating whether a certain string appears in the name column
    titles = ['Master', 'Miss']
    df = fe.name_titles(df, titles)

    return df

def fit_model(X_fe, y, max_depth=3, n_estimators=1000):
    '''
    input: DataFrame, series

    Feature-engineering for age estimation.

    output: fitted model
    '''
    # instantiate model
    m = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators)
    # train model
    m.fit(X_fe, y)

    return m

def calc_predictions(X_test, m):
    '''
    input: DataFrame, fitted model

    Calculate binary predictions for age (child/no child).

    output: DataFrame
    '''
    # feature engineering of df without age values
    X_test_fe = feature_engineer(X_test)
    # predict y (series)
    ypred = m.predict(X_test_fe)
    # create df to store predictions
    age_est = X_test[['PassengerId']]
    # store predictions in df
    age_est['child'] = ypred

    return age_est

def merge_df(df, age_predictions, cutoff=12):
    '''
    input: DataFrame

    Create binary child column in original df.
    Add predictions from model to original df.

    output: DataFrame
    '''
    # create binary column indicating whether the passenger was a child
    # in the original df
    df['child2'] = (df['Age'] <= cutoff).astype('int')
    # merge original df with age predictions on PassengerId
    df = pd.merge(df, age_predictions, how='left', on='PassengerId')
    # merge child columns
    df.loc[df['Age'].notna(), 'child'] = df['child2']
    # convert child column from float to integer
    df['child'] = df['child'].astype('int')
    # delete superfluous child2 column
    del df['child2']

    return df
