#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Author: Fenghao Tian
##Date: October 22,2018
##Note:
#1、This file is order to inference the results with Bayesian-belief-networks according to the directed acyclic graph file(https://github.com/eBay/bayesian-belief-networks).

import arcpy
from numpy import *
from CreateFactors import *



class BNI:

    def __init__(self,path):
        '''
        Using the Bayesian network model to reason the final results.
        :param path:The path of DAG which write in the text.
        '''
        self.path = path

    def rtdic(self):
        '''
        Open the text and read the DAG data.
        '''
        f = open(self.path)
        dic = eval(f.read())
        f.close()
        return dic
    def build_JTP(self,dic):
        '''
        Building the junction tree according the BN model.
        :param dic:The reading data from the text.
        :return:Return the junction tree model.
        '''
        BN = BN_CreateFactors(dic)
        g = BN.addNodes()
        return g
    def get_JTP_data(self,g,dic):
        '''
        Return the inference results.
        :param g: The junction tree model.
        :param dic: The data of DAG.
        '''
        lst_JTP = []
        cnt = len(dic['A'])

        for i in xrange(cnt):
            joint_probability = g.query(A=dic['A'][i], G=dic['G'][i],
                                        DNR=dic['DNR'][i], R=dic['R'][i],
                                        DRD=dic['DRD'][i], DRW=dic['DRW'][i],
                                                    DT=dic['DT'][i], DW=dic['DW'][i], ES=dic['ES'][i], FO=dic['FO'][i], IE=dic['IE'][i], IW=dic['IW'][i],
                                                    UE=dic['UE'][i], LOP=dic['LOP'][i])
            data1 = joint_probability[('ELP', 1)]
            data2 = joint_probability[('ELP', 2)]

            if data1 == data2:
                lst_JTP.append(1)
            elif data1 > data2:
                lst_JTP.append(1)
            elif data1 < data2:
                lst_JTP.append(2)

        return lst_JTP

    def set_JTP_data(self, lst,VerificationFeature):
        '''
        Updating the field of random points with JTP value.
        :param lst: List of the inference results.
        :param VerificationFeature: Verification feature.
        '''
        arcpy.AddMessage('set_JTP_data....')
        n = 0
        with arcpy.da.UpdateCursor(VerificationFeature, ['JTP']) as cursor:
            for row in cursor:
                data = lst[n]
                arcpy.AddMessage('setting data :'+str(n))
                n += 1
                row[0] = data
                cursor.updateRow(row)


    def checkfield(self, VerificationFeature):
        '''
        Checking the field whether in source data or not.
        :param VerificationFeature: Verification feature.
        :return: True or false.
        '''
        fields = arcpy.ListFields(VerificationFeature)
        lstfields = []
        for i in fields:
            lstfields.append(i)
        if 'JTP' in lstfields:
            return True
        else:
            return False



if __name__ == "__main__":
    path = arcpy.GetParameterAsText(0)
    VerificationFeature = arcpy.GetParameterAsText(1)

    OBNI = BNI(path)
    dic = OBNI.rtdic()
    g = OBNI.build_JTP(dic)


    if OBNI.checkfield(VerificationFeature) is True:
        lst = OBNI.get_JTP_data(g,dic)
        OBNI.set_JTP_data(lst,VerificationFeature)
    else:
        arcpy.AddField_management(VerificationFeature, 'JTP', 'Float')
        lst = OBNI.get_JTP_data(g, dic)
        OBNI.set_JTP_data(lst, VerificationFeature)

