import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset_real = pd.read_csv('F:/data/edit/True_A1_done/csv/A1Master(test11again).csv')
dataset_fake = pd.read_csv('F:/data/edit/True_A1_done/csv/A1Master(attackwithrealfarnew).csv')

#importing dataset
print("The real data")
print(dataset_real.head())
print("The fake data")
print(dataset_fake.head())

#prepare

#balance dataset real
real_df_majority = dataset_real[dataset_real['label'] == 1]
real_df_minority = dataset_real[dataset_real['label'] == 0]

real_df_majority_downsampled = real_df_majority.sample(replace=False,    # sample without replacement
                                 n=real_df_minority['label'].count(),     # to match minority class
                                 random_state=123)

dataset_real = pd.concat([real_df_majority_downsampled, real_df_minority])

#balance dataset fake
fake_df_majority = dataset_fake[dataset_fake['label'] == 0]
fake_df_minority = dataset_fake[dataset_fake['label'] == 1]

fake_df_majority_downsampled = fake_df_majority.sample(replace=False,    # sample without replacement
                                 n=fake_df_minority['label'].count(),     # to match minority class
                                 random_state=123)

dataset_fake = pd.concat([fake_df_majority_downsampled, fake_df_minority])

#The real dataset
print("dataset real")
print(dataset_real.iloc[:, 0:22].values)
print("--------------------")
print(dataset_real.iloc[:, 22:23].values)

X_real = dataset_real.iloc[:, 0:22].values
y_real = dataset_real.iloc[:, 22:23].values

#The fake dataset
print("dataset fake")
print(dataset_fake.iloc[:, 0:22].values)
print("--------------------")
print(dataset_fake.iloc[:, 22:23].values)

X_fake = dataset_fake.iloc[:, 0:22].values
y_fake = dataset_fake.iloc[:, 22:23].values

from sklearn.model_selection import train_test_split

#real split
X_train_real, X_test_real, y_train_real, y_test_real = train_test_split(X_real, y_real, test_size=0.5, random_state=42)
#fake split
X_train_fake, X_test_fake, y_train_fake, y_test_fake = train_test_split(X_fake, y_fake, test_size=0.5, random_state=42)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
#real fit
X_train_real = sc.fit_transform(X_train_real)
X_test_real = sc.transform(X_test_real)
#fake fit
X_train_fake = sc.fit_transform(X_train_fake)
X_test_fake = sc.transform(X_test_fake)

# Train

from sklearn.ensemble import RandomForestClassifier

Classifier_real = RandomForestClassifier(n_estimators=100, random_state=42)
Classifier_fake = RandomForestClassifier(n_estimators=100, random_state=42)

#real train
Classifier_real.fit(X_train_real, y_train_real.ravel())
y_pred_real = Classifier_real.predict(X_test_real)
#fake train
Classifier_fake.fit(X_train_fake, y_train_fake.ravel())
y_pred_fake = Classifier_fake.predict(X_test_fake)

#evaluate

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score

#Accuracy real
print("Roc Auc Score real:", roc_auc_score(y_test_real,Classifier_real.predict(X_test_real)))

print(confusion_matrix(y_test_real,y_pred_real))
print(classification_report(y_test_real,y_pred_real))
print(accuracy_score(y_test_real, y_pred_real))

#Accuracy fake
print("Roc Auc Score fake:", roc_auc_score(y_test_fake,Classifier_real.predict(X_test_fake)))

print(confusion_matrix(y_test_fake,y_pred_fake))
print(classification_report(y_test_fake,y_pred_fake))
print(accuracy_score(y_test_fake, y_pred_fake))

#columns real
columns_real = dataset_real.iloc[:1, 0:22].columns
#columns fake
columns_fake = dataset_fake.iloc[:1, 0:22].columns

#real feature importance
real_feat_importances = pd.Series(Classifier_real.feature_importances_, index=columns_real)
#fake feature importance
fake_feat_importances = pd.Series(Classifier_fake.feature_importances_, index=columns_fake)

# print(pd.Series(Classifier_real.feature_importances_, index=columns_real))

#detection
# print("ranked true")
# print(sorted(Classifier_real.feature_importances_, reverse=True))
# print("ranked fake")
# print(sorted(Classifier_fake.feature_importances_, reverse=True))

#real result
# print(real_feat_importances.sort_values(ascending=False))
print(real_feat_importances.nlargest(3).sort_values(ascending=False).index.tolist())
real_feat_importances.nlargest(3).plot(kind='barh')
plt.show()
#fake result
print(fake_feat_importances.nlargest(3).sort_values(ascending=False).index.tolist())
fake_feat_importances.nlargest(3).plot(kind='barh')
plt.show()

if real_feat_importances.nlargest(3).sort_values(ascending=False).index.tolist() == fake_feat_importances.nlargest(3).sort_values(ascending=False).index.tolist():
    print("The network hasn't been spoofed")
else:
    print("The network has been spoofed")
