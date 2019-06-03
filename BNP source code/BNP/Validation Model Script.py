#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Author: Fenghao Tian
##Date: November 1,2018

import numpy as np
from sklearn.metrics import auc
from sklearn import metrics
import matplotlib.pyplot as plt
import itertools
import arcpy
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from BNP.basicfunction import basicfunction

def printRoc(y_test, scores,group):
    '''
    Verifying the accuracy of the model using cross-validation.
    Evaluating the classification accuracy with the area under the curve (AUC) and the receiver operating characteristic (ROC).
    :param y_test:Standard value.
    :param scores:Positive probability corresponding to predicted value.
    :param group:Group name for figure title.
    '''
    fpr, tpr, thresholds = metrics.roc_curve(y_test, scores, pos_label=2)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, lw=5, alpha=0.8, color='r', label='AUC = %0.2f' % (roc_auc))
    plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', alpha=.8)#label='Luck'

    plt.grid()
    plt.xlabel('1 - specificity', fontsize=30)
    plt.ylabel('sensitivity', fontsize=30)
    # plt.title('%s   ROC_auc ( AUC = %0.2f )' % (group,roc_auc), fontsize=25)
    plt.title('%s' % (group), fontsize=30)
    plt.legend(loc="lower right", fontsize=25)
    plt.show()
# def newpaintConfusion_float(true_label,pred_label,pred_y,classes):
#     lmr_matrix=confusion_matrix(true_label,pred_label)
#     acc_score=accuracy_score(true_label,pred_label)
#     roc_auc_score= metrics.roc_auc_score(true_label, pred_y)
#     plt.imshow(lmr_matrix,interpolation='nearest',cmap=plt.cm.Blues)
#     plt.title('confusion matrix')
#     plt.colorbar()
#     tick_marks=np.arange(len(classes))
#     plt.xticks(tick_marks,classes,rotation=45)
#     plt.yticks(tick_marks,classes)
#     plt.xlabel('Pre label')
#     plt.ylabel('True label')
#     lmr_matrix=lmr_matrix.astype('float')/lmr_matrix.sum(axis=1)[:,np.newaxis]
#     fmt='.2f'
#     thresh=lmr_matrix.max()/2.
#     for i,j in itertools.product(range(lmr_matrix.shape[0]),range(lmr_matrix.shape[1])):
#         plt.text(j, i, format(lmr_matrix[i, j], fmt),
#                  horizontalalignment="center",
#                  color="black" if lmr_matrix[i, j] > thresh else "red")
#         plt.title('threshold={} , acc={:.3f} , auc={:.3f}'.format(thresh,acc_score,roc_auc_score),fontsize=20)
#         plt.tight_layout()
#         plt.show()
if __name__ == "__main__":
    InputFeature = arcpy.GetParameterAsText(0)
    InputField = arcpy.GetParameterAsText(1)

    obj = basicfunction( InputField,InputFeature)
    data_dic = obj.getdata()
    true_label = data_dic['JTP']
    pred_label = data_dic['BNP']
    C2 = confusion_matrix(true_label, pred_label, labels=[1,2])
    acc_score = accuracy_score(true_label, pred_label)
    printRoc(true_label,pred_label,group='Group 1')
    arcpy.AddMessage('Confusion matrix：'+str(C2))
    arcpy.AddMessage('Accuracy: '+str(acc_score))

