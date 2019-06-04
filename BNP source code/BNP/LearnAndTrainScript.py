#!/usr/bin/env python
# -*- coding: utf-8 -*-


##Author: Fenghao Tian
##Date: December 2,2018
##Note:
#1、This file is order to create a Bayesian Network(BN) model with Pgmpy(https://github.com/pgmpy) and get a directed acyclic graph(DAG) for junction tree algorithm.
#2、We have modified the source code according to the requirements of our research. You can download the source code in my GitHub site(https://github.com/drtianfenghao/BNP).

import arcpy
from bayesian.bbn import *
import pandas as pd
from numpy import *
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from basicfunction import *

class LearnAndTrain:
    def __init__(self,Bayesdata,Bayesfields):
        '''
        Creating a BN model for JTA reasoning engine.
        :param Bayesdata:Containing each geo-information of resource data as the input feature.
        :param Bayesfields:The fields of building model (Fig3).
        '''
        self.Bayesdata = Bayesdata
        self.Bayesfields = Bayesfields

    def build_BN(self):
        '''
        The BayesianModel present a method to create a BN.
        Note:A-Altitude; C-Cropland; DNR-Distance to nature reserve; DRD-Distance to road; DRW-Distance to railway; DT-Distance to township; DW-Distance to water body; ES-Eco-environmental sensitivity; G-Gradient; IE-Importance of ecosystem services; IW-Importance of water conservation; R-Relief amplitude; SD-Soil erosion degree; LC-Urban encroachment; ELP-ERA potential
        :return:The result for JTA.
        '''
        data = pd.DataFrame(data=self.Bayesdata)
        model = BayesianModel([('A', 'ES'), ('R', 'ES'), ('DW', 'ES'),('SD','ES'),
                               ('IW', 'IE'), ('DNR', 'IE'),('G','IE'),
                               ('DRW', 'LC'), ('DT', 'LC'), ('DRD', 'LC'),
                               ('G', 'C'), ('DW', 'C'),
                               ('ES', 'ELP'), ('IE', 'ELP'), ('LC', 'ELP'),('C','ELP'),
                               ])
        mle_model = MaximumLikelihoodEstimator(model, data)

        alldict = {}
        for i in range(len(self.Bayesfields)):
            locals()['cpd_' + str(self.Bayesfields[i])] = mle_model.estimate_cpd(self.Bayesfields[i])
            arcpy.AddMessage(str(locals()['cpd_' + str(self.Bayesfields[i])]))
            values = locals()['cpd_' + str(self.Bayesfields[i])].get_values().tolist()
            dic = locals()['cpd_' + str(self.Bayesfields[i])].returndic()
            model.add_cpds(locals()['cpd_' + str(self.Bayesfields[i])])
            alldict[str(self.Bayesfields[i])] = dic

        return alldict

if __name__ == "__main__":
    InputFeature = arcpy.GetParameterAsText(0)
    InputField = arcpy.GetParameterAsText(1)
    outpath = arcpy.GetParameterAsText(2)

    obf = basicfunction(InputField,InputFeature)

    Bayesdata = obf.getdata()
    ## Get the fields of input feature.
    Bayesfields = obf.getfields()

    obj = LearnAndTrain(Bayesdata,Bayesfields)
    ## Create a BN model.
    BNdic =  obj.build_BN()
    #Write to the text file.
    f = open(outpath,'w+')
    f.write(str(BNdic))
    f.close()

