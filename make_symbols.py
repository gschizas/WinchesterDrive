#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import itertools

im=Image.open('Winchester-Sprite.png')

colors = ['#{0[0]:02X}{0[1]:02X}{0[2]:02X}'.format(c[1]) for c in im.getcolors() if c[1] != (0,0,0)]

keys = list(itertools.product(colors, range(im.width//8), range(im.height//8)))
characters = dict(zip(keys, [[0]*8 for _ in keys]))

for cy in range(im.height//8):
    for cx in range(im.width//8):
        print(cx,cy)
        for y in range(8):
            for x in range(8):
                coord = (cx * 8 + x, cy * 8 + y)
                color = im.getpixel(coord)
                color_text = '#{0[0]:02X}{0[1]:02X}{0[2]:02X}'.format(color)
                if color_text != '#000000':
                    characters[color_text, cx, cy][y] |= 128 >> x

print('1000 SYMBOL AFTER 192')
print('\n'.join(["{} SYMBOL {},{}".format(10*i+1010, 192+i,','.join(map(str,characters[k]))) for i, k in enumerate(keys) if sum(characters[k])>=0]))
print('1330 RETURN')
