 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 18:14:53 2017

@author: jacob
"""
from UsbControl import LightCrafter6500Device as lc
import UsbControl.PatternCreation as pc
#import numpy as np
from scipy.misc import imread
import time

def load_N_pictures():
        #Prepare Pattern
        lc_dmd = lc.LC6500Device()
        list_of_patterns = []
        pattern_list = [('PatternRepository/LCR6500_Images/All_Block.bmp', 10000000),
                        ('PatternRepository/LCR6500_Images/678_Block.bmp', 500000),
                        ('PatternRepository/LCR6500_Images/All_Block.bmp', 5000000),
                        ]
        for lines in pattern_list:
            path = lines[0]
            exposure = int(lines[1])
            settings = {
                        'compression':'rle',
                        'exposure_time':exposure # in us
                        }
            
            dmd_pattern = pc.DMDPattern(**settings)
            picture = imread(path)
            picture_change = picture.astype('bool')
            dmd_pattern.pattern = picture_change
            list_of_patterns.append(dmd_pattern)
            
    
        
        dmd_patterns = {'patterns': list_of_patterns}
        start_time = time.clock()
        lc_dmd.upload_image_sequence(dmd_patterns)
        end_time = time.clock()
        elapsed_time = end_time - start_time
        print "Time it took to send images:" , elapsed_time
                    
    
#def load_by_user_input():
#        lc_dmd = lc.LC6500Device()
#        exposure = int(raw_input('Input exposure time in us:'))
#        image = raw_input('What is the name of the picture:') #678_Block.bmp'
#        path = 'PatternRepository/LCR6500_Images/' + image 
#        print path
#        settings = {
#                    'compression':'rle',
#                    'exposure_time':exposure # in us
#                    }
#        dmd_pattern = pc.DMDPattern(**settings)
#        picture = imread(path)
#        picture_change = picture.astype('bool')
        
#        dmd_pattern.pattern = picture_change
        
#        dmd_patterns = {'patterns':[dmd_pattern]}
#        lc_dmd.upload_image_sequence(dmd_patterns)

load_N_pictures()
