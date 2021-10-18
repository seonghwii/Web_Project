import torch
import torch.nn as nn #nn.Linear 라이브러리를 사용하기 위해 import

# F.mse(mean squared error) <--linear regression, 다양한 LOSS Function 존재
# Classification problem에서 사용하는 loss function: Cross-Entropy (집합체 : torch.nn.functional에 존재한다.)

import torch.nn.functional as F
import torch.optim as optim #SGD, Adam, etc. 최적화 라이브러리


def read_file(file_name):

    rtn_list = []
    cnt = 0

    #file을 열면 꼭 닫아주어야 한다. | open, close
    try:
        f = open(file_name, mode="rt")

        while True:
            line = f.readline()
            if not line: break

            #map : 리스트의 요소를 지정된 함수, 내장함수 (float으로 형변환)
            line = list(map(float, (line.rstrip('\n').split("\t"))))
            rtn_list.append(line)
            cnt += 1


        f.close()

        return rtn_list, cnt

    except FileNotFoundError as e:
            print(e)


# test = 5개, train = 23개
# 파일 불러오기
house_info, cnt = read_file("sell_house.txt")

A = torch.FloatTensor(house_info)

x_train = A[:-5, 1:-1] # (23, 11)
y_train = A[:-5, -1:] #결과치(23, 1)

x_test = A[-5:, 1:-1] #(5, 11)
y_test = A[-5:, -1:] #결과치 (5, 1)

# input : 11, output : 1
model = nn.Linear(11, 1)

# lr : learning rate(조절하기 위해서는 lr을 낮춰주는 것이 좋다._보폭_)
optimizer = optim.SGD(model.parameters(), lr=0.000002)

nb_epochs = 7500
for epoch in range(nb_epochs+1):
    # weight * x_train(입력 데이터) 를 계산해서  H(x)값 도출
    #x_train이라는 데이터를 가지고 Linear regression 모델을 사용해 최적해 예측
    pred = model(x_train)
    # cost 계산
    # mse = torch.mean((x_train - prediction).pow(2).sum())
    # 최적의 w, b 값을 도출하기 위한 부분
    cost = F.mse_loss(pred, y_train)

    # 누적이 발생하기 때문에 zero_grad() 로 초기화
    optimizer.zero_grad()

    # 미분(loss, cost function 함수를 미분하여 gradient 계산(w, b 값 도출))
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f'Epoch: {epoch:4d}/{nb_epochs} Cost: {cost.item():.6f}')

print(list(model.parameters()))

new_var = torch.FloatTensor(x_test)
pred_y = model(new_var) # model.forward(new_var)
f = open("result.txt", "w")
# f.write(f'{str(pred_y)}\n')
f.close()







