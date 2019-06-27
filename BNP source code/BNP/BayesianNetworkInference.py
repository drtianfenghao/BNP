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
    def set_JTP_data(self,g,VerificationFeature):
        '''
        Return the inference results.
        :param g: The junction tree model.
        :param VerificationFeature: Verification feature.
        '''
        num = 1
        fields = arcpy.ListFields(VerificationFeature)
        lstfield = []
        scores = []
        for i in fields:
            lstfield.append(i.name)
        with arcpy.da.UpdateCursor(VerificationFeature, lstfield) as cursor:
            for row in cursor:

                valueA = row[lstfield.index('A')]
                valueG = row[lstfield.index('G')]
                valueDNR = row[lstfield.index('DNR')]
                valueR = row[lstfield.index('R')]
                valueDRD = row[lstfield.index('DRD')]
                valueDRW = row[lstfield.index('DRW')]
                valueDT = row[lstfield.index('DT')]
                valueDW = row[lstfield.index('DW')]
                valueES = row[lstfield.index('ES')]
                valueC = row[lstfield.index('C')]
                valueIE = row[lstfield.index('IE')]
                valueIW = row[lstfield.index('IW')]
                valueLC = row[lstfield.index('LC')]
                valueSD = row[lstfield.index('SD')]
                valueELP = row[lstfield.index('ELP')]
                # scores.append(valueELP)
                # value_DRW * value_DT * value_DRD * value_R * value_ES * value_A * value_SD * value_DW * value_G * value_C * value_IE * value_IW * value_DNR * value_LC * value_ELP
                # BNP = self.return_BN_P(valueDRW , valueDT , valueDRD , valueR , valueES , valueA , valueSD , valueDW , valueG , valueC , valueIE , valueIW , valueDNR , valueLC , valueELP)
                # set BNP
                # row[lstfield.index('BNP')] = BNP

                # set JTP
                joint_probability = g.query(A=valueA, G=valueG, DNR=valueDNR, R=valueR, DRD=valueDRD, DRW=valueDRW,
                                            DT=valueDT, DW=valueDW, ES=valueES, C=valueC, IE=valueIE, IW=valueIW,
                                            LC=valueLC, SD=valueSD)

                data1 = joint_probability[('ELP', 1)]
                data2 = joint_probability[('ELP', 2)]

                if data1 == data2:
                    row[lstfield.index('JTP')] = 1
                elif data1 > data2:
                    row[lstfield.index('JTP')] = 1
                elif data1 < data2:
                    row[lstfield.index('JTP')] = 2

                cursor.updateRow(row)
                # arcpy.AddMessage(str(BNP))
                arcpy.AddMessage("Setting data %s in process"%str(num))

                num += 1

    # def set_JTP_data(self, lst,VerificationFeature):
    #     '''
    #     Updating the field of random points with JTP value.
    #     :param lst: List of the inference results.
    #     :param VerificationFeature: Verification feature.
    #     '''
    #     arcpy.AddMessage('set_JTP_data....')
    #     n = 0
    #     with arcpy.da.UpdateCursor(VerificationFeature, ['JTP']) as cursor:
    #         for row in cursor:
    #             data = lst[n]
    #             arcpy.AddMessage('setting data :'+str(n))
    #             n += 1
    #             row[0] = data
    #             cursor.updateRow(row)


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
        OBNI.set_JTP_data(g,VerificationFeature)

    else:
        arcpy.AddField_management(VerificationFeature, 'JTP', 'Float')
        OBNI.set_JTP_data(g, VerificationFeature)

