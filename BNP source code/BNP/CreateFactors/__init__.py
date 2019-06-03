#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Author: Fenghao Tian
##Date: October 20,2018

from bayesian.bbn import *
class BN_CreateFactors:
    def __init__(self,dic):
        self.dic = dic
    def addNodes(self):
        def fG(G):
            '''Gradient'''
            dicG = self.dic['G']
            if G == 1:
                return dicG['G(1)']
            elif G == 2:
                return dicG['G(2)']
            elif G == 3:
                return dicG['G(3)']
            elif G == 4:
                return dicG['G(4)']

        def fDW(DW):
            '''Distance to a water body'''
            dicDW = self.dic['DW']
            if DW == 1:
                return dicDW['DW(1)']
            elif DW == 2:
                return dicDW['DW(2)']
            elif DW == 3:
                return dicDW['DW(3)']
            elif DW == 4:
                return dicDW['DW(4)']

        def fA(A):
            '''Altitude'''
            dicA = self.dic['A']
            if A == 1:
                return dicA['A(1)']
            elif A == 2:
                return dicA['A(2)']
            elif A == 3:
                return dicA['A(3)']
            elif A == 4:
                return dicA['A(4)']

        def fR(R):
            '''Relief amolitude'''
            dicR = self.dic['R']
            if R == 1:
                return dicR['R(1)']
            elif R == 2:
                return dicR['R(2)']
            elif R == 3:
                return dicR['R(3)']
            elif R == 4:
                return dicR['R(4)']

        def fIW(IW):
            '''Importance of water conservation'''
            dicIW = self.dic['IW']
            if IW == 1:
                return dicIW['IW(1)']
            elif IW == 2:
                return dicIW['IW(2)']
            elif IW == 3:
                return dicIW['IW(3)']
            elif IW == 4:
                return dicIW['IW(4)']

        def fDNR(DNR):
            '''Distance to ecological forest'''
            dicDNR = self.dic['DNR']
            if DNR == 1:
                return dicDNR['DNR(1)']
            elif DNR == 2:
                return dicDNR['DNR(2)']
            elif DNR == 3:
                return dicDNR['DNR(3)']
            elif DNR == 4:
                return dicDNR['DNR(4)']

        def fDRW(DRW):
            '''Distance to railway'''
            dicDRW = self.dic['DRW']
            if DRW == 1:
                return dicDRW['DRW(1)']
            elif DRW == 2:
                return dicDRW['DRW(2)']
            elif DRW == 3:
                return dicDRW['DRW(3)']
            elif DRW == 4:
                return dicDRW['DRW(4)']

        def fDT(DT):
            '''Distance to township'''
            dicDT = self.dic['DT']
            if DT == 1:
                return dicDT['DT(1)']
            elif DT == 2:
                return dicDT['DT(2)']
            elif DT == 3:
                return dicDT['DT(3)']
            elif DT == 4:
                return dicDT['DT(4)']

        def fDRD(DRD):
            '''Distance to road'''
            dicDRD = self.dic['DRD']
            if DRD == 1:
                return dicDRD['DRD(1)']
            elif DRD == 2:
                return dicDRD['DRD(2)']
            elif DRD == 3:
                return dicDRD['DRD(3)']
            elif DRD == 4:
                return dicDRD['DRD(4)']

        def fFO(G, DW, FO):
            '''Farmland occupancy'''
            table = self.dic['FO']['FO']
            key = ''
            if FO == 1:
                key = key + 'FO(1)'
            elif FO == 2:
                key = key + 'FO(2)'
            if DW == 1:
                key = key + 'DW(1)'
            elif DW == 2:
                key = key + 'DW(2)'
            elif DW == 3:
                key = key + 'DW(3)'
            elif DW == 4:
                key = key + 'DW(4)'
            if G == 1:
                key = key + 'G(1)'
            elif G == 2:
                key = key + 'G(2)'
            elif G == 3:
                key = key + 'G(3)'
            elif G == 4:
                key = key + 'G(4)'
            return table[key]

        def fES(DW, A, R, ES):
            '''Eco-environmental sensitivity'''
            table = self.dic['ES']['ES']
            key = ''
            if ES == 1:
                key = key + 'ES(1)'
            elif ES == 2:
                key = key + 'ES(2)'
            elif ES == 3:
                key = key + 'ES(3)'
            elif ES == 4:
                key = key + 'ES(4)'
            if A == 1:
                key = key + 'A(1)'
            elif A == 2:
                key = key + 'A(2)'
            elif A == 3:
                key = key + 'A(3)'
            elif A == 4:
                key = key + 'A(4)'
            if DW == 1:
                key = key + 'DW(1)'
            elif DW == 2:
                key = key + 'DW(2)'
            elif DW == 3:
                key = key + 'DW(3)'
            elif DW == 4:
                key = key + 'DW(4)'
            if R == 1:
                key = key + 'R(1)'
            elif R == 2:
                key = key + 'R(2)'
            elif R == 3:
                key = key + 'R(3)'
            elif R == 4:
                key = key + 'R(4)'

            return table[key]

        def fIE(IW, DNR, IE):
            '''Importance of ecosystem services'''
            table = self.dic['IE']['IE']
            key = ''
            if IE == 1:
                key = key + 'IE(1)'
            elif IE == 2:
                key = key + 'IE(2)'
            elif IE == 3:
                key = key + 'IE(3)'
            elif IE == 4:
                key = key + 'IE(4)'
            if DNR == 1:
                key = key + 'DNR(1)'
            elif DNR == 2:
                key = key + 'DNR(2)'
            elif DNR == 3:
                key = key + 'DNR(3)'
            elif DNR == 4:
                key = key + 'DNR(4)'
            if IW == 1:
                key = key + 'IW(1)'
            elif IW == 2:
                key = key + 'IW(2)'
            elif IW == 3:
                key = key + 'IW(3)'
            elif IW == 4:
                key = key + 'IW(4)'
            return table[key]

        def fUE(DRW, DT, DRD, UE):
            '''Urban encroachment'''
            table = self.dic['UE']['UE']
            key = ''
            if UE == 1:
                key = key + 'UE(1)'
            elif UE == 2:
                key = key + 'UE(2)'

            if DRD == 1:
                key = key + 'DRD(1)'
            elif DRD == 2:
                key = key + 'DRD(2)'
            elif DRD == 3:
                key = key + 'DRD(3)'
            elif DRD == 4:
                key = key + 'DRD(4)'
            if DRW == 1:
                key = key + 'DRW(1)'
            elif DRW == 2:
                key = key + 'DRW(2)'
            elif DRW == 3:
                key = key + 'DRW(3)'
            elif DRW == 4:
                key = key + 'DRW(4)'
            if DT == 1:
                key = key + 'DT(1)'
            elif DT == 2:
                key = key + 'DT(2)'
            elif DT == 3:
                key = key + 'DT(3)'
            elif DT == 4:
                key = key + 'DT(4)'

            return table[key]

        def fLOP(FO, UE, LOP):
            '''Ecological land potential'''
            table = self.dic['LOP']['LOP']
            key = ''
            if LOP == 1:
                key = key + 'LOP(1)'
            elif LOP == 2:
                key = key + 'LOP(2)'
            if FO == 1:
                key = key + 'FO(1)'
            elif FO == 2:
                key = key + 'FO(2)'
            if UE == 1:
                key = key + 'UE(1)'
            elif UE == 2:
                key = key + 'UE(2)'
            return table[key]

        def fELP(ES, IE, LOP, ELP):
            '''Land occupation  potential'''
            table = self.dic['ELP']['ELP']
            key = ''
            if ELP == 1:
                key = key + 'ELP(1)'
            elif ELP == 2:
                key = key + 'ELP(2)'
            if ES == 1:
                key = key + 'ES(1)'
            elif ES == 2:
                key = key + 'ES(2)'
            elif ES == 3:
                key = key + 'ES(3)'
            elif ES == 4:
                key = key + 'ES(4)'
            if IE == 1:
                key = key + 'IE(1)'
            elif IE == 2:
                key = key + 'IE(2)'
            elif IE == 3:
                key = key + 'IE(3)'
            elif IE == 4:
                key = key + 'IE(4)'
            if LOP == 1:
                key = key + 'LOP(1)'
            elif LOP == 2:
                key = key + 'LOP(2)'
            return table[key]

        g = build_bbn(fDRW, fDT, fDRD, fG, fDW, fUE, fFO, fLOP, fDW, fA, fR, fES, fIW, fDNR, fIE, fELP,
                      domains={'G': [1, 2, 3, 4],
                               'DW': [1, 2, 3, 4],
                               'A': [1, 2, 3, 4],
                               'R': [1, 2, 3, 4],
                               'IW': [1, 2, 3, 4],
                               'DNR': [1, 2, 3, 4],
                               'DRW': [1, 2, 3, 4],
                               'DT': [1, 2, 3, 4],
                               'DRD': [1, 2, 3, 4],
                               'FO': [1, 2],
                               'ES': [1, 2, 3, 4],
                               'IE': [1, 2, 3, 4],
                               'UE': [1, 2],
                               'LOP': [1, 2],
                               'ELP': [1, 2]})
        return g