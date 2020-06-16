#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:32:10 2020

@author: Sharad
"""
import ps3
width, height, dirt_amount = (5, 10, 1)
room = ps3.EmptyRoom(width, height, dirt_amount)
freq_buckets = {}
for i in range(10000):
    pos = room.get_random_position()
    x, y = pos.get_x(), pos.get_y()
    x0, y0 = int(x), int(y)
    freq_buckets[(x0, y0)] = freq_buckets.get((x0, y0), 0) + 1
    if x0 > 4 or y0 >4:
        print('haha')