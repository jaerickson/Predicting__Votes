import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder

# Read the data
data = pd.read_csv('condensed_cvr.csv', dtype=str).sample(n=20000, random_state=42)

# Set aside some data for testing
# TODO You have to do this, using train_test_split. Put 20% of the data into the test set.
# Use 42 as the random number seed.
# Splits data into a training set and a test set.
# Test set = 20%
# Train Set = 80%
train_set, test_set = train_test_split(data,test_size=0.2,train_size=0.8,random_state=42)

# Separate the target column as the label for supervised learning
# Uncomment one of the two lines below to predict a specific race (CURRENTLY SET TO MAYORAL RACE)
TARGET_COLUMN = 'City of Portland, Mayor'
# TARGET_COLUMN = 'President and Vice President'

train_X = train_set.drop(TARGET_COLUMN, axis=1)
train_y = train_set[TARGET_COLUMN].copy()

# Use one-hot encoding for the input attributes, as sklearn needs these
# TODO You have to do this. When creating your OneHotEncoder, specify handle_unknown='ignore', as there
# may be votes that appear in the test set but not in the training set. Call the augmented train_X
# "train_X_1hot".
#Simplifies the input data into a format that can be more easily read categorically by the computer
vote_encoder = OneHotEncoder(handle_unknown='ignore')
train_X_1hot = vote_encoder.fit_transform(train_X)

# Train a decision tree
# TODO You have to do this. Use a max depth of 6. Call your tree "tree".
tree = DecisionTreeClassifier(max_depth = 6) #Use DecisionTreeClassifier
tree.fit(train_X_1hot,train_y) #Fit data to tree

# Below line needs to be uncommented to run training set
#print(f'Accuracy on training set: {tree.score(train_X_1hot, train_y)}')

# Test it on the test set
# TODO You have to create test_X_1hot and test_y. Don't re-fit the OneHotEncoder, just use it to transform the
# test data.
test_y = test_set[TARGET_COLUMN].copy()
test_X = test_set.drop(TARGET_COLUMN, axis=1)
test_X_1hot = vote_encoder.transform(test_X)

# Below line needs to be uncommented to run test set
#print(f'Accuracy on test set: {tree.score(test_X_1hot, test_y)}')
