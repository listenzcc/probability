# %%
import numpy as np
import matplotlib.pyplot as plt


def lognormal_pdf(x, mean, median):
    '''
    Compute the PDF of a log-normal distribution given the mean and median.

    $$mean = \exp(\mu + \sigma^2/2)$$

    $$median = \exp(\mu)$$

    $$pdf = \frac{1}{\sigma * x * \sqrt(2*\pi)} * exp(-\frac{(log(x) - mu)^2} { 2 \sigma^2}$$

    :param x: The x values to compute the PDF for.
    :param mean: The mean of the log-normal distribution.
    :param median: The median of the log-normal distribution.
    '''
    mu = np.log(median)
    mu_s2_2 = np.log(mean)
    s = np.sqrt((mu_s2_2 - mu) * 2)
    return 1/s/np.sqrt(2*np.pi)/x * np.exp(-((np.log(x) - mu) ** 2) / 2 / s ** 2)


def compute_cdf(pdf, x):
    """Compute the CDF from the PDF."""
    return np.cumsum(pdf) * np.diff(np.insert(x, 0, 0))


# Example usage
if __name__ == "__main__":
    # Log-Normal distribution for USA with mean 120 and median 19.2
    median1 = 19.2
    mean1 = 120
    x = np.linspace(0.01, 100, 1000)
    pdf_values1 = lognormal_pdf(x, mean1, median1)
    cdf_values1 = compute_cdf(pdf_values1, x)

    # Log-Normal distribution for China with mean 289 and median 141
    exchange_rate = 1 / 6.6
    median2 = 141 * exchange_rate
    mean2 = 289 * exchange_rate
    pdf_values2 = lognormal_pdf(x, mean2, median2)
    cdf_values2 = compute_cdf(pdf_values2, x)

    fig, ax1 = plt.subplots()

    # Plot the Log-Normal distribution for USA
    line1, = ax1.plot(x, pdf_values1, label=f'Log-Normal PDF USA (mean={
                      mean1:.2f}, median={median1:.2f})', color='b')
    ax1.set_xlabel('x')
    ax1.set_ylabel('Probability Density', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    # Create a second y-axis for the second distribution
    ax2 = ax1.twinx()
    line2, = ax2.plot(x, pdf_values2, label=f'Log-Normal PDF China (mean={
                      mean2:.2f}, median={median2:.2f})', color='r')
    ax2.set_ylabel('Probability Density', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    fig.tight_layout()
    plt.title('Log-Normal Distributions for USA and China')
    plt.grid(True)
    fig.legend(handles=[line1, line2], loc='lower center',
               bbox_to_anchor=(0.5, -0.05), ncol=1)
    plt.savefig('pdf_comparison.png', bbox_inches='tight')
    plt.show()

    # Plot the CDFs
    plt.plot(x, cdf_values1,
             label=f'Log-Normal CDF USA (median={median1:.2f})', color='gray')
    plt.plot(x, cdf_values2, label=f'Log-Normal CDF China (median={
             median2:.2f})', color='gray', linestyle='dashed')
    plt.axvline(median1, color='b', linestyle='dotted', linewidth=1)
    plt.axvline(median2, color='r', linestyle='dotted', linewidth=1)
    plt.xlabel('x')
    plt.ylabel('Cumulative Probability')
    plt.title('Cumulative Distribution Functions for USA and China')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.savefig('cdf_comparison.png', bbox_inches='tight')
    plt.show()

# %%
