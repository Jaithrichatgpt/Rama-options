import streamlit as st

st.title("📈 Options Income Calculator")

strategy = st.selectbox("Select Strategy", ["Cash-Secured Put", "Covered Call"])

strike = st.number_input("Strike Price", value=100.0)
premium = st.number_input("Premium Received", value=2.5)
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
