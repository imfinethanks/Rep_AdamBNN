import torch
# from lib.models.networks.pose_dla_dcn import get_pose_net
# from lib.models.networks.pose_dla_dcn2cn import get_pose_net
# 增加可读性
import numpy as np
from tensorboardX import SummaryWriter
import torch
# from reactnet_full import reactnet
from reactnet_raw import reactnet
# from reactnet import reactnet
from ptflops import get_model_complexity_info


model = reactnet()

model_name = 'fairmot'
flops, params = get_model_complexity_info(model, (3,224,224),as_strings=False,print_per_layer_stat=True,ignore_modules=[torch.nn.BatchNorm1d,torch.nn.BatchNorm2d])#,torch.nn.AvgPool2d,torch.nn.AdaptiveAvgPool2d,torch.nn.PReLU])
print("%s |%f |%f" % (model_name,flops,params))