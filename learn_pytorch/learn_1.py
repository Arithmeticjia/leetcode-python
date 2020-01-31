import torch
import numpy as np


np_data = np.arange(6).reshape((2,3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
torch_data_0 = torch.zeros(2,3)
torch_data_1 = torch.ones(2,3)
torch_data = torch.randn(2,3)
torch_data_from_list = torch.Tensor([[1,2,3],[4,5,6]])
torch_data_from_list_32 = torch.FloatTensor([[1,2,3],[4,5,6]])
print(
    '\nnumpy:', np_data,
    '\ntorch:', torch_data,
    '\ntensor2array', tensor2array,
    '\ntorch_data_0:', torch_data_0,
    '\ntorch_data_1:', torch_data_1,
    '\ntorch_data:', torch_data,
    '\ntorch_data_from_list:', torch_data_from_list,
    '\ntorch_data_from_list_32',torch_data_from_list_32
)
