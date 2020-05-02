import pandas as pd
import numpy as np

def name_titles(df, title_list):
    '''
    input: df, cutoff=12

    Creates a binary column indicating whether passenger's name contains
    a certain string (one column per string provided).
    Based on Name column, removes said column.

    output: df
    '''

    for title in title_list:
        df[title]=(df['Name'].str.contains(title)).astype('int')
    del df['Name']
    return df

def children(df, cutoff=12):
    '''
    input: df, cutoff=12

    Creates a binary column indicating whether the passenger was a child.
    Based on the age column, removes said column.

    output: df
    '''
    df['child'] = (df['Age'] <= cutoff).astype('int')
    del df['Age']
    return df


def many_parch(df, cutoff=2):
    '''
    input: df, cutoff=2

    Creates a binary column indicating whether a passenger had many
    parents or children.
    Based on Parch column, removes said column.

    output: df
    '''
    df['many_parch'] = (df['Parch'] > cutoff).astype('int')
    del df['Parch']
    return df

def many_sibsp(df, cutoff=1):
    '''
    input: df, cutoff=1

    Creates a binary column indicating whether a passenger had many
    siblings or spouses.
    Based on SibSp column, removes said column.

    output: df
    '''
    df['many_sibsp'] = (df['SibSp'] > cutoff).astype('int')
    del df['SibSp']
    return df

def fill_fare_na(df):
    '''
    input: df

    Fills missing values for Fare with median fare

    output: df
    '''
    median_fare = df['Fare'].median()
    df = df.fillna({'Fare': median_fare})
    return df

def log_fare(df):
    '''
    input: df

    Converts fare values into log.

    output: df
    '''
    df['log_fare'] = 0
    df.loc[(df['Fare']>0), 'log_fare'] = np.log(df['Fare'])
    del df['Fare']
    return df

def female_class3(df):
    '''
    input: df

    Creates column with interaction term for women in 3rd class.
    (1 for women in 3rd class, otherwise 0).

    output: df
    '''
    df['female_class3'] = 0
    df.loc[(df['Sex']=='female')&(df['Pclass']==3),'female_class3'] = 1
    return df

def male_class1(df):
    '''
    input: df

    Creates column with interaction term for men in 1st class.
    (1 for men in 1st class, otherwise 0).

    output: df
    '''
    df['male_class1'] = 0
    df.loc[(df['Sex']=='male')&(df['Pclass']==1),'male_class1'] = 1
    return df
