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
    with arcpy.da.SearchCursor(inputfeature, "OID") as cursor:
        for row in cursor:
            lstobj.append(row[0])
    cnt = len(lstobj)
    n = cnt/5000

    for i in range(n):
        arcpy.Select_analysis(inputfeature,outworkspace+'//'+'trdata_%s'%str(i),'OID<%d AND OID>%d'%(((i+1)*5000)+1,i*5000))
        arcpy.Select_analysis(inputfeature,outworkspace + '//' + 'yzdata_%s' % str(i),'Not(OID<%d AND OID>%d)' % (((i + 1) * 5000)+1, i * 5000))

        arcpy.AddMessage('Finnishing covert :'+str(i))




input = arcpy.GetParameterAsText(0)
outworkspace = arcpy.GetParameterAsText(1)
createlst(input,outworkspace)