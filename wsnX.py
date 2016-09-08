# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:04:57 2016

@author: zhangte

@brief:
        wsnX功能简单,专用于无线传感网的网络连接算法仿真.
        wsnX基于pygame库开发.
        
        
@todo:  1.增加设置连线粗细的参数
        2.增加设置全局节点与连线的颜色功能
        3.增加删除连线功能
        4.增加英文说明与注释
        5.参数达到简洁明了
        6.将网络画在一个矩形框里,矩形框可以显示网格,矩形框的定点为节点坐标原点
"""

import pygame
from pygame.locals import *

class wsnX:
    
    
    def __init__(self, l=500, w=500, bg=(255, 255, 255)):
        pygame.init()
        
        # 第二个,第三个参数没查是什么作用
        self.screen = pygame.display.set_mode((l, w), 0, 32)
        self.screen.fill(bg)
        
        #以下两个属性对应的功能并未实现,一会实现        
        self.connector_color = (0, 0, 0) #全局连线颜色
        self.nodes_color = (0, 0, 0) #全局节点颜色
    
    
    # 添加一个节点
    def add_node(self, (x, y), color=(251,2,3), radius=5):
        pygame.draw.circle(self.screen, color, (x, y), radius)
        self.draw_update()
        
    
    # 添加多个节点
    def add_nodes(self, nodes, color=(251,2,3), radius=5):
        for node in nodes:
            pygame.draw.circle(self.screen, color, node, radius)
            
        self.draw_update()


    # 连接两个节点
    def link_double(self, node_1, node_2, color=(1,2,3)):
        pygame.draw.line(self.screen, color, node_1, node_2)
        self.draw_update()
        
    
    # 放射状连接多个节点
    def link_radiant(self, central_node, nodes, color=(1,2,3)):
        for node in nodes:
            self.link_double(central_node, node, color)


    # 刷新画布--将新画的内容添加到画布        
    def draw_update(self):
        pygame.display.update()
    
        