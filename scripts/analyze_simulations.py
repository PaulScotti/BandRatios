""" This script calculates ratios and plots from simulated power spectral data where a parameter vary."""
import sys
sys.path.append('../bratios')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_context('poster')

from fooof import FOOOF, FOOOFGroup

from ratios import *
from analysis import *
from settings import *
from plot import *

def main():

    # Load data
    cf_low = np.load("../dat/single_param_sims/cf_data_low.npy")
    cf_high = np.load("../dat/single_param_sims/cf_data_high.npy")
    pw_low = np.load("../dat/single_param_sims/pw_data_low.npy")
    pw_high = np.load("../dat/single_param_sims/pw_data_high.npy")
    bw_low = np.load("../dat/single_param_sims/bw_data_low.npy")
    bw_high = np.load("../dat/single_param_sims/bw_data_high.npy")
    f_data = np.load("../dat/single_param_sims/exp_data.npy")
    offset = np.load("../dat/single_param_sims/offset_data.npy")
    exp = np.load("../dat/single_param_sims/exp_data.npy")
    a_shift = np.load('../dat/single_param_sims/shifting_alpha.npy')
    
    cf_low_df = prep_single_sims(cf_low, "CF")
    cf_high_df = prep_single_sims(cf_high, "CF")
    pw_low_df = prep_single_sims(pw_low, "PW")
    pw_high_df = prep_single_sims(pw_high, "PW")
    bw_low_df = prep_single_sims(bw_low, "BW")
    bw_high_df = prep_single_sims(bw_high, "BW")
    f_df = prep_single_sims(f_data, "EXP", periodic_param=0)
    offset_df = prep_single_sims(offset, "OFF", periodic_param=0)
    exp_df = prep_single_sims(exp, "EXP", periodic_param=0)
    a_shift_df = prep_single_sims(a_shift, "Alpha CF")
    
    print(exp_df)
    print(exp_df.iloc[:,3])

    for ratio in ["TBR", "TAR", "ABR"]:

        fig = plt.figure(figsize=(20,18))
        #low cf
        ax = fig.add_subplot(331)
        ax.set_xlabel("CF")
        ax.set_ylabel(ratio)
        ax.plot(cf_low_df.iloc[:,3], cf_low_df[ratio])

        #low pw
        ax = fig.add_subplot(332)
        ax.set_xlabel("PW")
        ax.set_ylabel(ratio)
        ax.plot(pw_low_df.iloc[:,3], pw_low_df[ratio])
        if max(pw_low_df[ratio]) - min(pw_low_df[ratio]) < .5:

            maxx = np.max(pw_low_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])

        #low bw
        ax = fig.add_subplot(333)
        ax.set_xlabel("BW")
        ax.set_ylabel(ratio)
        ax.plot(bw_low_df.iloc[:,3], bw_low_df[ratio])

        if max(bw_low_df[ratio]) - min(bw_low_df[ratio]) < .3:

            maxx = np.max(bw_low_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])

        #high cf
        ax = fig.add_subplot(334)
        ax.set_xlabel("CF")
        ax.set_ylabel(ratio)
        ax.plot(cf_high_df.iloc[:,3], cf_high_df[ratio])

        #high pw
        ax = fig.add_subplot(335)
        ax.set_xlabel("PW")
        ax.set_ylabel(ratio)
        ax.plot(pw_high_df.iloc[:,3], pw_high_df[ratio])
        if max(pw_high_df[ratio]) - min(pw_high_df[ratio]) < .3:

            maxx = np.max(pw_high_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])

        #high bw
        ax = fig.add_subplot(336)
        ax.set_xlabel("BW")
        ax.set_ylabel(ratio)
        ax.plot(bw_high_df.iloc[:,3], bw_high_df[ratio])

        if max(bw_high_df[ratio]) - min(bw_high_df[ratio]) < .3:

            maxx = np.max(bw_high_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])

        
        plt.tight_layout()
        plt.savefig("../figures/SingleParamSims/periodic_" + ratio+".pdf")
        plt.clf()
        ################################################

        fig = plt.figure(figsize=(8,12))

        #offset
        ax = fig.add_subplot(211)
        ax.set_xlabel("Off")
        ax.set_ylabel(ratio)
        ax.plot(offset_df.iloc[:,3], offset_df[ratio])

        #exponent
        ax = fig.add_subplot(212)
        ax.set_xlabel("Exp")
        ax.set_ylabel(ratio)
        ax.plot(exp_df.iloc[:,3], exp_df[ratio])
        plt.tight_layout()
        plt.savefig("../figures/SingleParamSims/aperiodic_" + ratio+".pdf")

    # Plot
    # plot_single_param_sims(cf_low_df, filename="cf_low")
    # plot_single_param_sims(cf_high_df, filename="cf_high")
    # plot_single_param_sims(pw_low_df, filename="pw_low")
    # plot_single_param_sims(pw_high_df, filename="pw_high")
    # plot_single_param_sims(bw_low_df, filename="bw_low")
    # plot_single_param_sims(bw_high_df, filename="bw_high")
    # plot_single_param_sims(exp_df, filename="exp")
    # plot_single_param_sims(offset_df, filename="offset")
    # plot_single_param_sims(f_df, filename="1f")
    # plot_single_param_sims(a_shift_df, filename="shifting_alpha")
    
if __name__ == "__main__":
    main()
    