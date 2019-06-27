#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Author: Fenghao Tian
##Date: October 5,2018

import arcpy
from numpy import *

class basicfunction:
    def __init__(self,InputField,InputFeature):
        '''
        The basic function for the BNP.
        '''
        self.InputField = InputField
        self.InputFeature = InputFeature
    def getfields(self):
        '''
           ##obtain fields
        '''

        lstfield = self.InputField.split(";")
        formatfield = []
        for i in range(len(lstfield)):
            formatfield.append(str(lstfield[i]))
        return formatfield

    def getdata(self):
        '''
           ##the data set of input table in ArcGIS
        '''

        dic = {}
        lstfield = self.InputField.split(";")

        num = len(lstfield)

        for i in range(num):
            cnt = 1
            locals()['data' + str(i)] = []
            with arcpy.da.SearchCursor(self.InputFeature, lstfield) as cursor:
                for row in cursor:
                    # arcpy.AddMessage(str("Collecting %s Data :" % lstfield[i] + str(cnt)))
                    locals()['data' + str(i)].append(row[i])
                    cnt += 1
            # data.append(locals()['data'+str(i)])
            dic.update({str(lstfield[i]): locals()['data' + str(i)]})

        return dic

    def formatmodel(self, String):
        '''
            ##formate input model
        '''
        formatdata = String.split(";")
        formatfield = []
        for i in range(len(formatdata)):
            formatfield.append(str(formatdata[i]))

        data2 = []
        for i in formatfield:
            k = i.split("=>")
            data2.append(tuple(k))
        return data2

    def formatoutvalues(self, lst):
        num = len(lst)
        if num == 1:
            return list(round(lst[0], 2))
        else:
            return 0

    def getlstdata(self, dic):
        lst = []
        for key in dic:
            lst.append(dic[key])
        return lst


