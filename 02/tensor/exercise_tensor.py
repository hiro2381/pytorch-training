import numpy as np
import torch

if __name__=="__main__":
    data = np.array([
        [[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
        [[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
        [[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]
    ])

# 問題1
t = torch.tensor(data, dtype=float)
print("=====problem 1=====")
print(t.shape)

# 問題2
t = t.permute(2, 0, 1)
print("=====problem 2=====")
print(t.shape)

# 問題3
total_student = t.sum(dim=0)

print("=====problem 3=====")
print(total_student)

# 問題4
average_per_class = total_student / t.shape[0]
print("=====problem 4=====")
print(average_per_class)