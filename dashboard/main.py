import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
from modules.fake_data import generate_fake_stock_data
from streamlit_elements import elements, dashboard, mui
from streamlit_lightweight_charts import renderLightweightCharts
import pandas as pd

def main():
    st.set_page_config(layout="wide")

    # Generate and format fake stock data
    fake_df_365 = generate_fake_stock_data(num_days=365)
    fake_df_365['time'] = fake_df_365['time'].dt.strftime('%Y-%m-%d')

    # Prepare chart configuration
    chart_data = [{
        "chart": {
            "height": 700,
            "width": 950,
        },
        "series": [
            {
                "type": 'Candlestick',
                "data": fake_df_365.to_dict('records'),
            },
        ],
    }]

    # Create three columns for horizontal alignment
    col1, col2 = st.columns([ 1, 1])


    with col2:
        with elements("multiple_children"):
            # Create a container with a border
            mui.Button(
                mui.icon.Pix,
                "SNTJ Stock Screener"
            )
        options = ["Apple Inc", "SalesForce", "Visa", "Tesla", "Airbnb"]
        options_technical_indicators = ["RSI", "MACD", "SMA", "EMA"]
        options_chart_types = ["Candlestick", "Line", "Bar", "Area"]
        # selection = st.pills("Companies", options, selection_mode="multi")
        # Custom CSS for resizing the selectbox
        st.markdown("""
            <style>
            div[data-baseweb="select"] {
                width: 200px !important;  /* Adjust as needed */
                /*move to the right of the row*/
                
            }
            </style>
        """, unsafe_allow_html=True)
        with st.container(border=True):
            col_companies, col_tech, col_chart, col_timestamp,  = st.columns(4)
            with col_companies:
                st.multiselect("Companies", options, key="companies")
            
            with col_tech:
                st.multiselect("Technical Indicators", options_technical_indicators, key="tech_ind")

            with col_chart:
                st.selectbox("Chart Types", options_chart_types, key="chart_type")
            


            st.subheader("Yearly Performance")
            renderLightweightCharts(chart_data, key="chart_component")
    with col1:
        df1 = pd.DataFrame({
            "Name": ["Apple", "Google", "Amazon"],
            "Price": [150, 2800, 3400]
        })

        df3 = pd.DataFrame({
            "Country": ["USA", "Germany", "Japan"],
            "GDP": [21.43, 3.86, 5.08]
        })

        df2 = pd.DataFrame({
            "Attribute": ["Company Name", "Industry", "Founded Year", "Headquarters",
                        "CEO", "Number of Employees", "Key Products/Services"],
            "Value": ["Apple Inc", "Technology", 1995, "Silicon Valley, CA",
                    "Steve Jobs", 1500, "Software Solutions, Cloud Services"]
        })

        def generate_fake_fundamental_data(num_rows=20):
            import random
            symbols = ['AAPL', 'TSLA', 'V', 'CRM', 'ABNB']
            years = list(range(2020, 2025))
            data = []
            for _ in range(num_rows):
                symbol = random.choice(symbols)
                year = random.choice(years)
                revenue = round(random.uniform(100, 5000), 2)
                profit = round(random.uniform(10, 500), 2)
                market_cap = round(random.uniform(50, 3000), 2)
                pe_ratio = round(random.uniform(15, 50), 1)
                dividend_yield = round(random.uniform(0, 5), 2)
                debt_to_equity = round(random.uniform(0, 2), 2)
                operating_cash_flow = round(random.uniform(50, 1000), 2)
                free_cash_flow = round(random.uniform(30, 800), 2)
                return_on_equity = round(random.uniform(5, 25), 2)
                gross_margin = round(random.uniform(20, 80), 2)
                data.append([symbol, year, revenue, profit, market_cap, pe_ratio,
                            dividend_yield, debt_to_equity, operating_cash_flow,
                            free_cash_flow, return_on_equity, gross_margin])
            return pd.DataFrame(data, columns=['Symbol', 'Year', 'Revenue', 'Profit', 'Market Cap',
                                                'P/E Ratio', 'Dividend Yield', 'Debt to Equity',
                                                'Operating Cash Flow', 'Free Cash Flow',
                                                'Return on Equity', 'Gross Margin'])
        
        df4 = pd.DataFrame({
            "Stock": ["AAPL", "GOOGL", "AMZN"],
            "Volume": [1000000, 1500000, 1200000],
            "Market Cap": [2.5, 1.8, 1.6],
            "P/E Ratio": [30, 25, 35],
        })

        # Create two columns
        col1, col2 = st.columns([1, 2])  # You can tweak the ratio

        # Left column: 3 dataframes

    with col1:
        with elements("top_performers_group_1"):  # Unique key
            mui.Typography(
                mui.icon.EmojiEvents,
                "Top Performers"  , 
                variant="h6" # Corrected typo
            )
        st.dataframe(df1, height=200, width=350, hide_index=True)

        with elements("top_performers_group_2"):  # Unique key
            mui.Typography(
                mui.icon.Info,
                "Company Profile" , 
                variant="h6"  # Corrected typo
            )
        st.dataframe(df2, height=300, width=350, hide_index=True)

        with elements("top_performers_group_3"):  # Unique key
            mui.Typography(
                mui.icon.ModelTraining,
                "ML Model Prediction"  , 
                variant="h6" # Corrected typo
            )
        st.dataframe(df3, height=200, width=350, hide_index=True)

    # Right column: 1 dataframe
    with col2:
        options = ["Apple Inc", "SalesForce", "Visa", "Tesla", "Airbnb"]
        selection = st.pills("Companies", options)

        with elements("top_performers_group_4"):  # Unique key
            mui.Typography(
                mui.icon.AccountBalance,
                "Fundamental Financial Data" , 
                variant="h6"
            )
        df_fundamental = generate_fake_fundamental_data(num_rows=20)
        st.dataframe(df_fundamental, height=830, width=800, hide_index=True)

# Footer
    st.markdown("<hr><center>© 2025 SNTJ Pro Stock Screener</center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
