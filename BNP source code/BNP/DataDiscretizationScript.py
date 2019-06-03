#!/usr/bin/env python
# -*- coding: utf-8 -*-


##Author: Fenghao Tian
##Date: October 10,2018

##Note: The discrete method based on Table 1 in the manuscript.

import arcpy
from arcpy.sa import *
from arcpy import env

class Data_Discretization_Scipt:
    def __init__(self, Inputworkspace,OutputFeaturePath,OutputFeatureName,InputConstraingFeature,Numbersofpoints):
        '''
        The script can be dispersed from the original data.
        :param Inputworkspace: The original data
        :param OutputFeature:  Defining the results after dispersing.
        :param InputConstraingFeature:  The range of generating random points.
        '''
        self.Inputworkspace = Inputworkspace
        self.OutputFeaturePath = OutputFeaturePath
        self.OutputFeatureName = OutputFeatureName
        self.InputConstraingFeature = InputConstraingFeature
        self.Numbersofpoints = Numbersofpoints
    def setworkspace(self):
        '''
        Setting the workspace in ArcGIS environment.
        '''
        env.workspace = self.Inputworkspace
    def Add_Field(self,Inputfeature,Field_Name,Filed_Type):
        '''
        Add field from input feature customize.
        :param Inputfeature:The feature to add field.
        :param Field_Name: The field name to add.
        :param Filed_Type: The filed type to set.
        '''
        arcpy.AddField_management(Inputfeature,Field_Name,Filed_Type)
    def Create_random_points(self):
        '''
        Creating random points from the range of constraining feature.
        :param outpath: The geo-database to output.
        :param outname: The output feature name.
        :param constrainingfeatureclass: The range of generating random points.
        :param numberofpoints: The numbers for creating random points.
        :return:
        '''
        arcpy.AddMessage("Creating random points")
        # env.outputCoordinateSystem = arcpy.SpatialReference("Xian 1980 3 Degree GK Zone 43")
        arcpy.CreateRandomPoints_management(self.OutputFeaturePath, self.OutputFeatureName, self.InputConstraingFeature,'',self.Numbersofpoints)
        # arcpy.CreateFishnet_management(self.OutputFeature,'1397827.035600 4660075.233999999', '1397827.035599999 4660085.233999999 ', 1000,1000, 600, 700, '1694007.492800001 4940949.5798', "LABELS", '#', "POLYGON")
        arcpy.AddMessage("Finishing creating random points from %s"%str(self.OutputFeaturePath+'\\'+self.OutputFeatureName))

    def getraster(self):
        '''
        Getting each raster from the workspace.
        '''
        lstraster = arcpy.ListRasters()
        return lstraster
    def exdataraster(self,pointfeature,lstraster):
        '''
        Discrete data.
        :param pointfeature: The points to load raster geo-information.
        :param lstraster: Each raster of geo-information will loaded to the random points.
        '''
        ExtractMultiValuesToPoints(pointfeature,lstraster,"NONE")
    def getboundary(self):
        '''
        Getting boundary from the random points feature.
        '''
        features = arcpy.ListFeatureClasses()
        return features



if __name__ == "__main__":

    Inputworkspace = arcpy.GetParameterAsText(0)
    InputConstraingFeature = arcpy.GetParameterAsText(1)
    Numbersofpoints = arcpy.GetParameterAsText(2)
    OutputFeatureName = arcpy.GetParameterAsText(3)
    OutputFeaturePath = arcpy.GetParameterAsText(4)

    obj = Data_Discretization_Scipt(Inputworkspace,OutputFeaturePath,OutputFeatureName,InputConstraingFeature,Numbersofpoints)
    obj.setworkspace()
    lstraster = obj.getraster()
    count = len(lstraster)
    clipfeature = obj.getboundary()
    obj.Create_random_points()

    for i in range(count):
        arcpy.AddMessage(str(lstraster[i])+"  filed  is loading!")
        obj.exdataraster(OutputFeaturePath+'\\'+OutputFeatureName,Inputworkspace+'//'+str(lstraster[i]))
    arcpy.AddMessage("DataDiscretizationScript has finished!")
