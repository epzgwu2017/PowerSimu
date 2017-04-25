"""

"""
import system
from devices.base_device import base_device
from cvxopt.base import mul,matrix

class avr1(base_device):
    def __init__(self):
        base_device.__init__(self)
        self.u = mul(matrix(self.u), matrix(system.PV.u))
        self._data.update(
            {'bus': None, 'Type': 1, 'vrmax': 3.3, 'vrmin': -2.6, 'Ka': 0, 'Ta': 0, 'Kf': 0, 'Tf': 0,
             'Ke': 0, 'Te': 0, 'Tr': 0, 'Ae': 0, 'Be': 0})
        self._type = 'Avr1'
        self._name = 'Avr1'
        self._bus = {'bus': ['a', 'v']}
        self._algebs = ['vref']  # 后续得修改
        self._states = ['vm', 'vr1', 'vr2', 'vf']  # 后续得修改
        self._params.extend(['vrmax', 'vrmin', 'Ka', 'Ta', 'Kf', 'Tf', 'Ke', 'Te', 'Tr', 'Ae', 'Be'])
        self._voltages = ['V0']  # 后续得修改
        self._powers = ['Pg']  # 后续得修改


class avr2(base_device):
    def __init__(self):
        base_device.__init__(self)
        self.u = mul(matrix(self.u), matrix(system.PV.u))
        self._data.update(
            {'bus': None, 'Type': 2, 'vrmax': 5, 'vrmin': 0, 'Ka': 0, 'Ta': 0, 'Kf': 0, 'Tf': 0,
             'Ke': 0, 'Te': 0, 'Tr': 0, 'Ae': 0, 'Be': 0})
        self._type = 'Avr1'
        self._name = 'Avr1'
        self._bus = {'bus': ['a', 'v']}
        self._algebs = ['vref']  # 后续得修改
        self._states = ['vm', 'vr1', 'vr2', 'vf']  # 后续得修改
        self._params.extend(['vrmax', 'vrmin', 'Ka', 'Ta', 'Kf', 'Tf', 'Ke', 'Te', 'Tr', 'Ae', 'Be'])
        self._voltages = ['V0']  # 后续得修改
        self._powers = ['Pg']  # 后续得修改


class avr3():
    def __init__(self):
        return