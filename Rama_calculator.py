import streamlit as st

st.title("📈 Options Income Calculator")

strategy = st.selectbox("Select Strategy", ["Cash-Secured Put", "Covered Call"])

strike = st.number_input("Strike Price", value=100.0)
premium = st.number_input("Premium Received (Sold Option)", value=2.5)
option_buyback_price = st.number_input("Price of Option Purchased (if closed)", value=0.0)
current_option_price = st.number_input("Current Option Price (Market)", value=2.5)
stock_price = st.number_input("Stock Price at Expiry", value=98.0)
fees = st.number_input("Fees ($)", value=0.0)

if strategy == "Covered Call":
    cost_basis = st.number_input("Stock Purchase Price (Cost Basis)", value=95.0)

if st.button("Calculate"):
    if strategy == "Cash-Secured Put":
        assigned = stock_price < strike
        breakeven = strike - premium
        if assigned:
            profit = (stock_price - breakeven) * 100 - fees
        else:
            profit = premium * 100 - fees
        st.success(f"📊 Status: {'Assigned' if assigned else 'Expired Worthless'}")
        st.info(f"💰 Net Profit: ${profit:.2f}")
        st.warning(f"⚖️ Break-even Price: ${breakeven:.2f}")

    else:  # Covered Call
        called_away = stock_price > strike
        breakeven = cost_basis - premium
        if called_away:
            profit = ((strike - cost_basis) + premium) * 100 - fees
        else:
            profit = ((stock_price - cost_basis) + premium) * 100 - fees
        st.success(f"📊 Status: {'Called Away' if called_away else 'Not Called Away'}")
        st.info(f"💰 Net Profit: ${profit:.2f}")
        st.warning(f"⚖️ Break-even Price: ${breakeven:.2f}")

    # 🧾 Option Trade P/L (if closed or marked to market)
    if option_buyback_price > 0:
        option_trade_pl = (premium - option_buyback_price) * 100 - fees
        st.subheader("📉 Option Closed")
        st.write(f"Premium Received: ${premium:.2f}")
        st.write(f"Buyback Price: ${option_buyback_price:.2f}")
        st.info(f"🧮 Realized P/L on Option: ${option_trade_pl:.2f}")
    else:
        unrealized_pl = (premium - current_option_price) * 100 - fees
        st.subheader("📊 Option (Mark-to-Market)")
        st.write(f"Current Option Price: ${current_option_price:.2f}")
        st.info(f"📉 Unrealized P/L: ${unrealized_pl:.2f}")
