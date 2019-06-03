#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Author: Fenghao Tian
##Date: October 26,2018


import arcpy

def createlst(inputfeature,outworkspace):
    '''
    We verified the accuracy of the model using cross-validation by splitting the data into four groups containing training and test datasets.
    :param inputfeature: The random points feature.
    :param outworkspace: Output workspace.

    '''
    lstobj = []
    with arcpy.da.SearchCursor(inputfeature, "OBJ") as cursor:
        for row in cursor:
            lstobj.append(row[0])
    cnt = len(lstobj)
    n = cnt/10000
    sy = cnt - n*10000
    for i in range(n):
        arcpy.Select_analysis(inputfeature,outworkspace+'//'+'trdata_%s'%str(i),'OBJ<%d AND OBJ>%d'%(((i+1)*10000)+1,i*10000))
        arcpy.Select_analysis(inputfeature,outworkspace + '//' + 'yzdata_%s' % str(i),'Not(OBJ<%d AND OBJ>%d)' % (((i + 1) * 10000)+1, i * 10000))

        arcpy.AddMessage('Finnishing covert :'+str(i))

    arcpy.Select_analysis(inputfeature, outworkspace + '//' + 'trdata_%s' % str(sy),'OBJ>%d' % (n * 10000))
    arcpy.Select_analysis(inputfeature, outworkspace + '//' + 'yzdata_%s' % str(sy),'Not(OBJ>%d)' % (n * 10000))
    arcpy.AddMessage('Finishing covert :'+str(sy))


input = arcpy.GetParameterAsText(0)
outworkspace = arcpy.GetParameterAsText(1)
createlst(input,outworkspace)