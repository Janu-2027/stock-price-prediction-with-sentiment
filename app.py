import streamlit as st
import plotly.graph_objects as go

# Fullscreen wide layout
st.set_page_config(page_title="Stock Price Prediction", layout="wide")

# Custom CSS with darker background overlay
st.markdown("""
<style>
body {
    margin:0;
    font-family: Arial, sans-serif;
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                url("https://img.freepik.com/free-vector/gradient-stock-market-concept_23-2149166910.jpg?semt=ais_hybrid&w=740&q=80") 
                no-repeat center center fixed;
    background-size: cover;
    color: white;
}
.overlay {
    background: rgba(0,0,0,0.2);
    padding: 30px;
    border-radius: 12px;
}
.card {
    background: rgba(255,255,255,0.15);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}
h1 {
    text-align: center;
    margin-bottom: 30px;
}
select {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border-radius: 8px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="overlay"><h1>Stock Price Prediction (Using Sentiment Analysis)</h1></div>', unsafe_allow_html=True)

# Stock data
stock_data = {
    "Reliance": {"open":1505,"close":1519,"high":1530,"low":1490,"weekHigh":2630,"weekLow":2150,
                 "marketCap":"₹15.7 Lakh Crore","sentimentScore":0.74,"sentimentType":"Positive",
                 "sentimentSummary":"Strong investor confidence due to retail and Jio performance",
                 "actual":[1200,1400,1600,1550,1519],"predicted":[1180,1450,1580,1540,1530]},
    "TCS": {"open":3530,"close":3555,"high":3600,"low":3500,"weekHigh":3850,"weekLow":3150,
            "marketCap":"₹13.3 Lakh Crore","sentimentScore":0.42,"sentimentType":"Neutral",
            "sentimentSummary":"Stable demand but global recession fears",
            "actual":[3200,3300,3400,3500,3555],"predicted":[3250,3350,3450,3480,3520]},
    "Infosys": {"open":1480,"close":1499,"high":1520,"low":1470,"weekHigh":1650,"weekLow":1350,
                "marketCap":"₹6.2 Lakh Crore","sentimentScore":0.25,"sentimentType":"Slightly Positive",
                "sentimentSummary":"Moderate growth in cloud services",
                "actual":[1300,1400,1450,1470,1499],"predicted":[1280,1420,1460,1480,1510]},
    "HDFC": {"open":1620,"close":1645,"high":1660,"low":1600,"weekHigh":1800,"weekLow":1505,
             "marketCap":"₹12.4 Lakh Crore","sentimentScore":0.61,"sentimentType":"Positive",
             "sentimentSummary":"Strong banking results and credit growth",
             "actual":[1500,1550,1580,1600,1645],"predicted":[1520,1570,1600,1610,1655]},
    "SBI": {"open":590,"close":602,"high":610,"low":585,"weekHigh":640,"weekLow":520,
            "marketCap":"₹5.8 Lakh Crore","sentimentScore":0.48,"sentimentType":"Neutral",
            "sentimentSummary":"Stable loan growth but NPA concerns",
            "actual":[520,540,560,580,602],"predicted":[525,550,565,590,610]}
}

# Dropdown
stock_choice = st.selectbox("", ["-- Select Indian Stock --"] + list(stock_data.keys()))

if stock_choice == "-- Select Indian Stock --":
    st.markdown('<div class="overlay"><h3>Please select a stock to view predictions.</h3></div>', unsafe_allow_html=True)
else:
    stock = stock_data[stock_choice]

    # Two columns for text cards
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>Stock Information</h3>
            <p>Opening Price: ₹{stock['open']}</p>
            <p>Closing Price: ₹{stock['close']}</p>
            <p>Day High: ₹{stock['high']}</p>
            <p>Day Low: ₹{stock['low']}</p>
            <p>52 Week High: ₹{stock['weekHigh']}</p>
            <p>52 Week Low: ₹{stock['weekLow']}</p>
            <p>Market Cap: {stock['marketCap']}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <h3>Sentiment Analysis</h3>
            <p>Sentiment Score: {stock['sentimentScore']}</p>
            <p>Sentiment Type: {stock['sentimentType']}</p>
            <p>{stock['sentimentSummary']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Generic date labels
    dates = [f"Day {i+1}" for i in range(5)]

    # Chart toggles
    show_actual = st.checkbox("Show Actual Price", value=True)
    show_predicted = st.checkbox("Show Predicted Price", value=True)

    # Chart
    fig = go.Figure()
    if show_actual:
        fig.add_trace(go.Scatter(x=dates, y=stock["actual"], mode='lines+markers',
                                 name='Actual Price', line=dict(color='cyan', width=4)))
    if show_predicted:
        fig.add_trace(go.Scatter(x=dates, y=stock["predicted"], mode='lines+markers',
                                 name='Predicted Price', line=dict(color='yellow', width=4)))
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                      paper_bgcolor='rgba(0,0,0,0)',
                      font_color='white',
                      margin=dict(t=30, b=0),
                      legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    st.plotly_chart(fig, use_container_width=True)

    # Footer disclaimer
    st.markdown("<p style='text-align:center; color:lightgray;'>Note: Data shown is for illustrative purposes only.</p>", unsafe_allow_html=True)