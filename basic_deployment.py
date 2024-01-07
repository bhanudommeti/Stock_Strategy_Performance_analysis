import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

def calculate_metrics(returns):
    cumulative_returns = (1 + returns).cumprod()

    # CAGR calculation
    cagr = ((cumulative_returns.iloc[-1] / cumulative_returns.iloc[0]) ** (1 / len(cumulative_returns.index.year.unique())) - 1) * 100

    volatility = np.std(returns) * np.sqrt(252) * 100
    sharpe_ratio = (cagr / volatility) if volatility != 0 else np.nan
    
    # Adjusted drawdown calculation
    dd_start = cumulative_returns.div(cumulative_returns.cummax()) - 1
    
    # Check for at least two data points
    if len(dd_start) > 1:
        max_drawdown = dd_start.min() * 100
    else:
        max_drawdown = np.nan

    return cagr, volatility, sharpe_ratio, max_drawdown

def main():
    st.title("Stock Strategy Performance Analysis")

    # Dropdown for stock selection
    selected_stock = st.selectbox("Select Stock", ['RELIANCE.NS', 'HCLTECH.NS', 'TATAMOTORS.NS', 'M&M.NS', 'EICHERMOT.NS', 'JSWSTEEL.NS', 'BAJFINANCE.NS', 'APOLLOHOSP.NS', 'WIPRO.NS', 'ADANIENT.NS'])

    # Date inputs
    start_date = st.date_input("Start Date", pd.to_datetime("2019-01-01"))
    
    # Set the end_date to the current date
    end_date = datetime.today()

    # Initial Equity
    initial_equity = st.number_input("Initial Equity", min_value=1, max_value=1000000000, value=1000000)

    # Fetch stock data from Yahoo Finance
    stock_data = yf.download(selected_stock, start=start_date, end=end_date)['Adj Close']

    # Calculate daily returns
    daily_returns = stock_data.pct_change().dropna()

    # Plot stock prices
    st.subheader("Stock Prices")
    st.line_chart(stock_data)

    # Plot equity curves using Plotly
    st.subheader("Equity Curves")

    # Simulate benchmark strategy (holding Nifty)
    nifty_data = yf.download('^NSEI', start=start_date, end=end_date)['Adj Close']
    benchmark_returns = nifty_data.pct_change().dropna()
    benchmark_equity = (1 + benchmark_returns).cumprod() * initial_equity
    strategy_equity = (1 + daily_returns).cumprod() * initial_equity

    # Create Plotly figure
    fig = go.Figure()

    # Add equity curves
    fig.add_trace(go.Scatter(x=strategy_equity.index, y=strategy_equity, mode='lines', name='Sample Strategy'))
    fig.add_trace(go.Scatter(x=benchmark_equity.index, y=benchmark_equity, mode='lines', name='Benchmark (Nifty)'))

    # Add equity curves for all selected stocks
    for stock in ['RELIANCE.NS', 'HCLTECH.NS', 'TATAMOTORS.NS', 'M&M.NS', 'EICHERMOT.NS', 'JSWSTEEL.NS', 'BAJFINANCE.NS', 'APOLLOHOSP.NS', 'WIPRO.NS', 'ADANIENT.NS']:
        stock_data = yf.download(stock, start=start_date, end=end_date)['Adj Close']
        stock_returns = stock_data.pct_change().dropna()
        stock_equity = (1 + stock_returns).cumprod() * initial_equity
        fig.add_trace(go.Scatter(x=stock_equity.index, y=stock_equity, mode='lines', name=stock))

    # Update layout
    fig.update_layout(
        title="Daily returns of each stock are taken as a mean to form the Sample Strategy",
        xaxis_title="Years",
        yaxis_title="Equity",
    )

    # Display the plot
    st.plotly_chart(fig)

    # Calculate and display performance metrics for Sample Strategy
    st.subheader("Performance Metrics - Sample Strategy")
    strategy_cagr, strategy_volatility, strategy_sharpe, strategy_drawdown = calculate_metrics(daily_returns)
    st.write(f"CAGR (%): {strategy_cagr:.2f}")
    st.write(f"Volatility (%): {strategy_volatility:.2f}")
    st.write(f"Sharpe Ratio: {strategy_sharpe:.2f}")
    st.write(f"Max Drawdown (%): {strategy_drawdown:.2f}")

    # Calculate and display performance metrics for Benchmark (Nifty)
    st.subheader("Performance Metrics - Benchmark (Nifty)")
    benchmark_cagr, benchmark_volatility, benchmark_sharpe, benchmark_drawdown = calculate_metrics(benchmark_returns)
    st.write(f"CAGR (%): {benchmark_cagr:.2f}")
    st.write(f"Volatility (%): {benchmark_volatility:.2f}")
    st.write(f"Sharpe Ratio: {benchmark_sharpe:.2f}")
    st.write(f"Max Drawdown (%): {benchmark_drawdown:.2f}")

if __name__ == "__main__":
    main()