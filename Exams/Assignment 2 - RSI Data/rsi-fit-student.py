import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt


"""
Preamble: Load data from source CSV file
"""

# path to the csv file
path_to_datafile = "C:/Users/jcuzz_zici3uw/Desktop/School/PROGRAMMING/ENGR315-sp2026-student/data/drop-jump/all_participant_data_rsi.csv"

# function that reads the csv and returns the columns as arrays
def parse_file(path_to_file): 
    file = pd.read_csv(path_to_file)    # reads the csv
    trial = file['trial'].tolist()  # trial column
    force_plate_rsi = file['force_plate_rsi'].values    # force plate rsi column
    accelerometer_rsi = file['accelerometer_rsi'].values    # accelerometer rsi column
    percent_error = file['percent_error'].values    # percent error column
    return trial, force_plate_rsi, accelerometer_rsi, percent_error

# runs the function and stores the results
trial, force_plate_rsi, accelerometer_rsi, percent_error = parse_file(path_to_datafile)

# mean and std for force plate and accelerometer
mu_fp_rsi = np.mean(force_plate_rsi)
std_fp_rsi = np.std(force_plate_rsi)
mu_acc_rsi = np.mean(accelerometer_rsi)
std_acc_rsi = np.std(accelerometer_rsi)

# x and y values for the force plate bell curve
x_fp_rsi = np.linspace(mu_fp_rsi-5*std_fp_rsi, mu_fp_rsi+5*std_fp_rsi, 100) # 100 points spread across the linear range
y_fp_rsi = norm.pdf(x_fp_rsi, mu_fp_rsi, std_fp_rsi)    # probability density at each point

# plots the force plate curve
plt.plot(x_fp_rsi, y_fp_rsi, label=f'mu ={mu_fp_rsi:.3f}, sigma ={std_fp_rsi:.4f}')
plt.title('Normal Distribution, Force Plate')
plt.xlabel('Standard Deviation')
plt.ylabel('Probability Density')
plt.legend(loc='lower center')
plt.savefig("forceplate.png")
plt.show()


# same thing for accelerometer
x_acc_rsi = np.linspace(mu_acc_rsi-5*std_acc_rsi, mu_acc_rsi+5*std_acc_rsi, 100)    # 100 points spread across a linear range
y_acc_rsi = norm.pdf(x_acc_rsi, mu_acc_rsi, std_acc_rsi)    # probability density at each point

# plots the accelerometer curve
plt.plot(x_acc_rsi, y_acc_rsi, label=f'mu ={mu_acc_rsi:.3f}, sigma ={std_acc_rsi:.4f}')
plt.title('Normal Distribution, Accelerometer')
plt.xlabel('Standard Deviation')
plt.ylabel('Probability Density')
plt.legend(loc='lower center')
plt.savefig("accelerometer.png")
plt.show()

# plots both curves on the same graph
plt.plot(x_fp_rsi, y_fp_rsi, label=f'Force Plate (mu ={mu_fp_rsi:.3f}, sigma ={std_fp_rsi:.4f})')
plt.plot(x_acc_rsi, y_acc_rsi, label=f'Accelerometer (mu ={mu_acc_rsi:.3f}, sigma ={std_acc_rsi:.4f})')
plt.legend(loc='lower center')
plt.title('Normal Distribution, Overlaid')
plt.xlabel('Standard Deviation')
plt.ylabel('Probability Density')
plt.savefig("overlay.png")
plt.show()


"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')
print(f"\nForce Plate || mu - {mu_fp_rsi:.4f} || std - {std_fp_rsi:.4f}")
print(f"\nAccelerometer || mu - {mu_acc_rsi:.4f} || std - {std_acc_rsi:.4f}")

"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""

# force plate bins from 0 to 2
fp_bins = np.linspace(0,2,9)
fp_bins = np.r_[-np.inf, fp_bins[1:8], np.inf] #infinity on both ends so nothing gets left out
hist_fp = np.histogram(force_plate_rsi, bins=fp_bins)   # count how many data points fall in each bin

# expected counts based on the normal distribution we found
expected_prob_fp = np.diff(norm.cdf(fp_bins, loc=mu_fp_rsi, scale=std_fp_rsi))  # probability per bin
expected_counts_fp = expected_prob_fp * len(force_plate_rsi)    # scale to actual counts

# run the chi square test
(chi_stat_fp, p_value_fp) = chisquare(f_obs=hist_fp[0], f_exp=expected_counts_fp, ddof=2)
fit_fp = "good" if p_value_fp > 0.05 else "poor"    # p > 0.05 means it fits

# same thing for accelerometer
acc_bins = np.linspace(0,2,9)
acc_bins = np.r_[-np.inf, acc_bins[1:8], np.inf]    # infinity on both ends again
hist_acc = np.histogram(accelerometer_rsi, bins=acc_bins)   # count data points per bin

expected_prob_acc = np.diff(norm.cdf(acc_bins, loc=mu_acc_rsi, scale=std_acc_rsi))  # probability per bin
expected_counts_acc = expected_prob_acc * len(accelerometer_rsi)    # scale to actual counts

(chi_stat_acc, p_value_acc) = chisquare(f_obs=hist_acc[0], f_exp=expected_counts_acc, ddof=2)
fit_acc = "good" if p_value_acc > 0.05 else "poor"  # p > 0.05 means it fits

print('\n-----Question 2-----')
print(f"\nAccelerometer || p_value - {p_value_acc:.3f} || chi2 stat - {chi_stat_acc:.5f} || Fit Check - {fit_acc}")
print(f"\nForce Plate || p_value - {p_value_fp:.3f} || chi2 stat - {chi_stat_fp:.5f} || Fit Check - {fit_fp}")

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""

# t-test comparing force plate and accelerometer means
t_test, p_ttest = ttest_ind(force_plate_rsi, accelerometer_rsi)
alpha = 0.05    # significance threshold
t_results = "equal" if p_ttest > alpha else "unequal"   # p > 0.05 means the means are equal

print('\n-----Question 3-----')
print(f"\nThe p-value for this t-test is {p_ttest:.5f} and the values are therefore {t_results}\n")