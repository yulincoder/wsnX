# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:04:57 2016

@author: zhangte

@brief:
        wsnX功能简单,专用于无线传感网的网络连接算法仿真.
        wsnX基于pygame库开发.
"""

import pygame
from pygame.locals import *
import sys


def wsnX_init():
    pass

class wsnX:
    
    connector_color = (0, 0, 0) #全局连线颜色
    nodes_color = (255, 0, 0) #全局节点颜色
    
    others_color = (0,0,0) #其它部分颜色,现在懒得改,非重点!!
    
    def __init__(self, l=500, w=500, bg=(255, 255, 255)):
        pygame.init()
        self.length = l
        self.width = w
        
        # 第二个,第三个参数没查是什么作用
        # length与width是节点分布区域大小,乘以1.2后是实际窗口大小
        self.screen = pygame.display.set_mode((int(self.length*1.2), int(self.width*1.2)), 0, 32)
        self.screen.fill(bg)
        self.__creat_area()
        
        #所有节点集合
        self.nodes = []
        
    
    def __creat_area(self):
        pygame.draw.line(self.screen, wsnX.others_color, 
                         (int(self.length*0.1), int(self.width*0.1)), 
                         (int(self.length*1.1), int(self.width*0.1)))
                         
        pygame.draw.line(self.screen, wsnX.others_color, 
                         (int(self.length*0.1), int(self.width*0.1)), 
                         (int(self.length*0.1), int(self.width*1.1)))
                         
        pygame.draw.line(self.screen, wsnX.others_color, 
                         (int(self.length*0.1), int(self.width*1.1)), 
                         (int(self.length*1.1), int(self.width*1.1)))
                         
        pygame.draw.line(self.screen, wsnX.others_color, 
                         (int(self.length*1.1), int(self.width*0.1)), 
                         (int(self.length*1.1), int(self.width*1.1)))
                         
        self.__draw_update()
    
    
    # 添加一个节点
    def add_node(self, (x, y), color=nodes_color, radius=5):
        x, y = self.__coordinate_conver((x,y))
        self.nodes.append((x, y))
        
        pygame.draw.circle(self.screen, color, (x, y), radius)
        self.__draw_update()
       
    
    def __coordinate_conver(self,(x, y)):
        return int(x+self.length*0.1), int(y+self.width*0.1)
      
      
    # 添加多个节点
    def add_nodes(self, nodes, color=nodes_color, radius=5):
        
        for node in nodes:
            (x, y) = self.__coordinate_conver(node)
            self.nodes.append((x,y))
            
        for node in self.nodes:
            pygame.draw.circle(self.screen, color, node, radius)
            
        self.__draw_update()


    # 连接两个节点
    def link_double(self, node_1, node_2, color=connector_color):
        no_1, no_2 = self.__coordinate_conver(node_1), self.__coordinate_conver(node_2)
        
        pygame.draw.line(self.screen, color, no_1, no_2)
        self.__draw_update()
        
    
    # 放射状连接多个节点
    def link_radiant(self, central_node, nodes, color=connector_color):
        for node in nodes:
            self.link_double(central_node, node, color)

    # 刷新画布--将新画的内容添加到画布        
    def __draw_update(self):
        pygame.display.update()
        
    
    def EXIT(self):
        pass

    
        