#!/usr/bin/env python3

import numpy as np
import pandas as pd
import scipy.stats as stats
import researchpy as rp
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

#The code can be used to perform ANOVA and post-hoc analysis of data

Binding_results_dic = {
    "0BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9919000267982483,
        1.0,
        8.085294005199332,
        3.0259653054740308
    ],
    "1BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9912999868392944,
        1.0,
        6.323095334126456,
        2.494223961912464
    ],
    "2BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9905999898910522,
        1.0,
        6.835273336711348,
        3.1118895379132243
    ],
    "3BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9911999702453613,
        1.0,
        7.899855813883514,
        2.6618164316891284
    ],
    "4BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9904999732971191,
        1.0,
        8.138092100307553,
        3.3169798286698238
    ],
    "5BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.988099992275238,
        1.0,
        4.163466855896007,
        2.608252397758735
    ],
    "6BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9914000034332275,
        1.0,
        8.190411026361543,
        3.4504699885575523
    ],
    "7BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9905999898910522,
        1.0,
        6.5371675731143215,
        3.0435319638987757
    ],
    "8BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9900000095367432,
        1.0,
        6.716364879138789,
        2.360162407299159
    ],
    "9BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9921000003814697,
        1.0,
        6.693336068002297,
        2.9619501547747586
    ],
    "10BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9900000095367432,
        1.0,
        6.105138741450928,
        3.4260465506426176
    ],
    "11BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.991599977016449,
        1.0,
        6.726514144334121,
        2.853040515602057
    ],
    "12BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9914000034332275,
        1.0,
        5.761382112950186,
        3.3917656643924086
    ],
    "13BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.9908000230789185,
        1.0,
        6.064759881498516,
        3.229674035811643
    ],
    "14BindingCNN_L1-0.0_L2-0.0_drop-0.25": [
        1.0,
        0.991599977016449,
        1.0,
        6.116540251455865,
        2.9159748188457115
    ]
}

LeNet_results_dic = {
    "0LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9815000295639038,
        1.0,
        1.5298288563587805,
        0.6845824902257702
    ],
    "1LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        0.9921875,
        0.9794999957084656,
        1.0,
        1.6491628217724514,
        0.8283661608346343
    ],
    "2LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9793999791145325,
        1.0,
        1.4013114679209762,
        0.8307273028129357
    ],
    "3LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9819999933242798,
        1.0,
        1.6974695623795255,
        0.6929029309453155
    ],
    "4LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9829999804496765,
        0.99,
        1.331042126501039,
        0.7347084691871606
    ],
    "5LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9817000031471252,
        1.0,
        1.1699902071063213,
        0.6453074884356044
    ],
    "6LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9789999723434448,
        1.0,
        1.5709010629538727,
        0.8097465804533917
    ],
    "7LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.980400025844574,
        0.93,
        1.5679346455460308,
        0.8484765529386583
    ],
    "8LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        0.9921875,
        0.9793000221252441,
        1.0,
        1.7445505433301074,
        0.8910280011622878
    ],
    "9LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9670000076293945,
        1.0,
        1.0672275541727059,
        0.7628355801031418
    ],
    "10LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9750000238418579,
        1.0,
        1.1996800916906876,
        0.8167095596526135
    ],
    "11LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9799000024795532,
        1.0,
        1.6425727294068218,
        0.9058646249156294
    ],
    "12LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9786999821662903,
        1.0,
        1.500443394664355,
        0.8937419528474702
    ],
    "13LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        1.0,
        0.9779999852180481,
        1.0,
        1.44091805326493,
        0.7936718846247275
    ],
    "14LeNet_L1-0.00125_L2-0.0_drop-0.5": [
        0.9765625,
        0.9746999740600586,
        1.0,
        1.5386741485206625,
        0.8138504166926506
    ]
}

Madry_results_dic = {
    "0Madry": [
        0.98,
        1.4637769607780273,
        0.5031264154549423
    ],
    "1Madry": [
        0.97,
        1.4565787226310905,
        0.5584373053550178
    ],
    "2Madry": [
        0.98,
        1.4600651048593434,
        0.532813400791941
    ],
    "3Madry": [
        0.97,
        1.470665310082481,
        0.5586854573276383
    ],
    "4Madry": [
        0.97,
        1.464280210681411,
        0.5818730502207703
    ],
    "5Madry": [
        0.99,
        1.4659947567428961,
        0.5139115214241747
    ],
    "6Madry": [
        0.97,
        1.4640276726737458,
        0.5509551974609954
    ],
    "7Madry": [
        0.99,
        1.504659154797359,
        0.5217822175568011
    ],
    "8Madry": [
        0.97,
        1.4424689401953492,
        0.5468084372711818
    ],
    "9Madry": [
        1.0,
        1.4622067316765126,
        0.48646331087758976
    ],
    "10Madry": [
        0.99,
        1.4889504580718247,
        0.520459531569079
    ],
    "11Madry": [
        0.98,
        1.449143475191677,
        0.5437939631228192
    ],
    "12Madry": [
        0.97,
        1.4579039806673812,
        0.5316957268797073
    ],
    "13Madry": [
        1.0,
        1.4725424125373088,
        0.4837941454135138
    ],
    "14Madry": [
        1.0,
        1.5180973230377897,
        0.5044836912355408
    ]
}

combined_results_dic = {'Model':[],
    'Distance':[]}

for key in Binding_results_dic:
    combined_results_dic['Model'].append('BindingCNN')
    combined_results_dic['Distance'].append((Binding_results_dic[key])[3])
for key in LeNet_results_dic:
    combined_results_dic['Model'].append('LeNet')
    combined_results_dic['Distance'].append((LeNet_results_dic[key])[3])
for key in Madry_results_dic:
    combined_results_dic['Model'].append('Madry')
    combined_results_dic['Distance'].append((Madry_results_dic[key])[1])


#print(combined_results_dic)

results_df = pd.DataFrame(combined_results_dic, 
    columns = ['Model', 'Distance'])

#print(results_df)

print(rp.summary_cont(results_df['Distance'].groupby(results_df['Model'])))

print(stats.f_oneway(results_df['Distance'][results_df['Model']=='BindingCNN'], 
             results_df['Distance'][results_df['Model']=='LeNet'],
             results_df['Distance'][results_df['Model']=='Madry']))

results = ols('Distance ~ C(Model)', data=results_df).fit()
print(results.summary())

aov_table = sm.stats.anova_lm(results, typ=2)
print(aov_table)

mc = MultiComparison(results_df['Distance'], results_df['Model'])
mc_results = mc.tukeyhsd(0.001)
print(mc_results)
