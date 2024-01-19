# Stock Strategy Performance Analysis

This Python script, Stock_Strategy_Performance_analysis.py, is designed for analyzing the historical stock data of a list of top stocks. It provides a comprehensive analysis of stock performance, implements a momentum trading strategy, and forecasts future stock prices using linear regression. Below is an explanation of the functionalities:

## Table of Contents

1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [Analysis](#analysis)
    - [Performance Metrics](#performance-metrics)
    - [Strategy vs. Benchmark](#strategy-vs-benchmark)
    - [Momentum Strategy](#momentum-strategy)
    - [Stock Price Forecasting](#stock-price-forecasting)
4. [Files](#files)
5. [License](#license)

## Introduction

This project leverages Python's pandas, NumPy, yfinance, scikit-learn, and plotly libraries to analyze historical stock data for a list of top stocks. The analysis includes calculating performance metrics, comparing the performance of the stocks with a benchmark index (Nifty 50), implementing a momentum trading strategy, and forecasting stock prices using linear regression.

## Dependencies

Make sure to install the required dependencies by running:

```bash
pip install pandas numpy yfinance matplotlib plotly scikit-learn statsmodels
```


## Analysis

### Performance Metrics

* Compound Annual Growth Rate (CAGR): Measures the annual growth rate of an investment.
* Volatility: Quantifies the degree of variation of a trading price series.
* Sharpe Ratio: Evaluates the performance of an investment in comparison to its risk.
* Daily Return: Calculates the percentage change in stock price on a daily basis.

### Strategy vs. Benchmark

* Compares the cumulative returns of a strategy (using daily returns) with a benchmark index (Nifty 50) to assess strategy performance.

### Momentum Strategy

* Implements a simple momentum trading strategy based on moving averages.
* Generates buy and sell signals and visualizes them on the stock price chart.

### Stock Price Forecasting

* Utilizes linear regression to forecast future stock prices.
* Plots historical prices alongside forecasted values, providing insights into potential trends.

## Files

- `Stock_Strategy_Performance_analysis.py`: The main Python script containing the analysis and forecasting code.
- `advanced_deployment.py` : The main Python Script containing the deploment code.
- `README.md`: The readme file providing an overview of the project and instructions.
- Other supporting files and directories.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
