import torch
print(torch.cuda.is_available())  # Should return True
print(torch.cuda.device_count())  # Should return a number greater than 0
print(torch.cuda.get_device_name(0))  # Should return the name of your GPU
print(torch.zeros(1).cuda())