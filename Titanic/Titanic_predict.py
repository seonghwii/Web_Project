# Kaggle의 Titanic 데이터를 이용하여 예측하였습니다.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 1. 모델 학습 과정
df_train = pd.read_csv("./train.csv")

# 데이터 구성 확인
print(df_train.info())

#생존 결과 출력
gt_train = df_train["Survived"]

#axis=1 : 세로방향으로 지운다./관계가 없는 내용을 지우는 작업
df_train = df_train.drop(["Name", "PassengerId", "Ticket", "Fare", "Cabin", "Survived"], axis=1)

# df_train["Age"]의 비어있는 칸에 df_train["Age"]의 평균 값으로 채워준다.
df_train["Age"] = df_train["Age"].fillna(df_train["Age"].mean())
#************비어있는 칸을 채워주는 함수 : fillna/평균값을 구하는 함수 = column.mean()**************

#df_train["Embarked"]의 비어있는 칸에 "S"를 넣어준다.
df_train["Embarked"] = df_train["Embarked"].fillna("S")

# df_train["Sex"]의 male --> 0, female -->1 로 변경해준다.
# df_train["Embarked"]의 Q --> 0, C --> 1, S --> 2 로 변경해준다.
df_train["Sex"] = df_train["Sex"].map({"male":0, "female":1})
df_train["Embarked"] = df_train["Embarked"].map({"Q":0, "C":1, "S":2})

# 비어있는 컬럼 값의 갯수 확인
print(df_train.isnull().sum())

# Classifier = DecisionTreeClassifier()
Classifier = RandomForestClassifier()


# 학습
Classifier.fit(df_train, gt_train) #학습자료, 결과물로 나올 자료

# 예측의 정확도 확인
print(Classifier.score(df_train, gt_train))



# 2. test 시작
# test data 불러오기
df_test = pd.read_csv("test.csv")
pId = df_test["PassengerId"]

# 데이터 전처리 과정
# 데이터 정보 확인 후 예측에 필요 없는 컬럼 제거 및 가공
print(df_test.info())
df_test = df_test.drop(["Name", "PassengerId", "Ticket", "Fare", "Cabin"], axis=1)
df_test["Age"] = df_test["Age"].fillna(df_train["Age"].mean())
df_test["Embarked"] = df_test["Embarked"].fillna("S")
df_test["Sex"] = df_test["Sex"].map({"male":0, "female":1})
df_test["Embarked"] = df_test["Embarked"].map({"Q":0, "C":1, "S":2})

# 테스트 결과 == df_test데이터를 가지고 randomforest를 이용하여 결과 예측
test_result = Classifier.predict(df_test)

# PassengetId column, Survived column을 이용하여 제출할 Dataframe 생성
submit = pd.DataFrame({"PassengerId": pId, "Survived": test_result})

# ******답지 형식에 맞게 index는 False로 해주었습니다.******

# "submit.csv" 파일 저장
submit.to_csv("submit.csv", index=False)


# test set = 90%로 모델을 만들고 10%로 테스트
test_gt = pd.read_csv("groundtruth.csv")

hit = 0 #맞은 갯수
miss = 0 #틀린 갯수
for i in range(len(test_result)):
    if test_result[i] == test_gt["Survived"][i]:
        hit += 1

    else:
        miss += 1

# 맞은 갯수, 틀린 갯수 확인
print('hit: ', hit, 'miss: ',miss, "hit/(hit+miss) ", round(hit/(hit+miss), 2))

# 결과 : DecisionTreeClassifier보다 RandomForestClassifier의 정확도가 더 높게 나왔다.
