import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load
import numpy as np

#오프라인에 다운로드(데이터셋 로딩)
def load_dataset(online=False):
    if online:
        (tr_data, tr_label), (te_data, te_label) = tf.keras.datasets.mnist.load_data()


    else:
        # path = "파일 경로"
        path = "CNN/mnist.npz"
        (tr_data, tr_label), (te_data, te_label) = tf.keras.datasets.mnist.load_data(path)

    return (tr_data, tr_label), (te_data, te_label)

#이미지로 보고 싶을 때(이미지 한 장 show)
#dataset = train_data, test_data
def show_image(dataset, index):
    # figure 정해줌
    # #0에 가까울수록 어두워짐
    plt.imshow(255-dataset[index], cmap="gray")
    plt.show()

#모든 이미지를 보고 싶을 때
def show_all_image(dataset):
    for i in range(len(dataset)):
        show_image(dataset, i)


#데이터 분포를 시각화
def show_data_values(label):
    # bincount = 각각의 빈도수를 체크하는 것이다. ex_(1, 2, 1, 1, 1, 3, 4, 4, 4, 6)
    # => [0, 4, 1, 1, 0, 0, 1, ...]
    count_value = np.bincount(label)
    print(count_value)

    plt.bar(np.arange(0, 10), count_value)
    plt.xticks(np.arange(0, 10))
    plt.grid()
    plt.show()

#학습
def train(x, y): #x = data, y = label // feature : 픽셀의 밝기(0~255:1byte)
    clf = RandomForestClassifier()
    clf.fit(x, y)
    print(clf.score(x, y)) #모델이 학습 데이타 셋에 대한 score(결과치)
    dump(clf, "rf_mnist.pkl")

#테스트
def test(x, y): #x = data, y = 정답
    model = load("rf_mnist.pkl")
    result = model.predict(x)

    hit = 0
    miss = 0
    wrong_list = []
    for i in range(len(x)):
        if result[i] == y[i]:
            hit += 1

        else:
            miss += 1
            wrong_list.append(i)

    print(hit, miss)
    return wrong_list, result


if __name__ == "__main__":
    (train_data, train_lable), (test_data, test_lable) = load_dataset()

    # 데이터 분포 시각화
    # show_data_values(train_lable)
    # show_data_values(test_lable)

    #학습
    test_data = test_data.reshape(10000, 784)
    train_data = train_data.reshape(60000, 784) #숫자를 표현해주기 위해서 784라는 숫자의 값을 사용했다. (값이 많을수록 더 정교하게 값을 정의할 수 있다.)
    #train(train_data, train_lable)


    #모델 로드
    model = load("rf_mnist.pkl")
    result = model.predict(test_data[:10000])
    print(result)
    print(test_lable[:10])


    show_image(train_data, 0)
    show_image(test_data, 100)
    show_image(train_data, 50000)
    # show_all_image(test_data) #그림 보고 싶을 때만 호출
    # print(test_lable[:10])
    # show_image(test_data, 2)
    #



# print(train_data[0].shape)
# print(train_data.shape)
# print(train_lable.shape)
# print(train_lable[0:10])
# print(train_data[0])






