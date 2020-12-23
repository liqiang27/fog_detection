import torch
import torch.nn as nn
from my_model.FeatureModule import g_exactor, d_exactor
from my_model.TaskModule import VisDistance_Estimation

class DisEstimation_Single(nn.Module):
    def __init__(self):
        super(DisEstimation_Single, self).__init__()
        self.g_feature = g_exactor()
        self.d_feature = d_exactor()
        self.task = VisDistance_Estimation()

    def forward(self, x1, x2):
        g_x = self.g_feature(x1)
        d_x = self.d_feature(x2)

        g_x = torch.reshape(g_x, (g_x.size(0), 1, 32, 32))
        d_x = torch.reshape(d_x, (d_x.size(0), 1, 32, 32))
        m_x = torch.cat((d_x, g_x), dim=1)

        distance = self.task(m_x)
        return distance