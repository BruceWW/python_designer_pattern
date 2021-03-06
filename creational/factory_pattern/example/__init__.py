#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/10
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import ABCMeta, abstractmethod

from creational import Phone


class PhoneFactory(metaclass=ABCMeta):
    """
    手机类，里面提供了所需的抽象方法
    这是个抽象工厂，我们使用工厂模式来实现抽象工厂的创建
    """

    @staticmethod
    def phone():
        return Phone()

    @abstractmethod
    def os(self) -> str:
        """
        操作系统
        :return:
        """
        pass

    @abstractmethod
    def cpu(self) -> str:
        """
        手机cpu
        :return:
        """
        pass

    @abstractmethod
    def name(self) -> str:
        """
        手机名称
        :return:
        """
        pass


class iPhoneKit(PhoneFactory):
    """
    具体的iphone抽象工厂
    """

    def os(self) -> str:
        """
        返回操作系统实例
        :return:
        """
        return 'ios'

    def cpu(self) -> str:
        """
        返回cpu实例
        :return:
        """
        return 'a13'

    def name(self) -> str:
        """
        返回手机信息实例
        :return:
        """
        return 'iphone 11'


class SamsungS20Kit(PhoneFactory):
    def os(self) -> str:
        return 'android'

    def cpu(self) -> str:
        return 'adreno650'

    def name(self) -> str:
        return 'samsung s20'


class HuaweiMate30Kit(PhoneFactory):
    def os(self) -> str:
        return 'android'

    def cpu(self) -> str:
        return 'kirin990'

    def name(self) -> str:
        return 'huawei mate30'
