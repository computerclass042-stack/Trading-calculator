import streamlit as st

# Page settings
st.set_page_config(page_title="Gold Trading Calculator", page_icon="📈", layout="centered")

# Title
st.title("📈 Gold Trading Calculator")
st.write("Only for gold lovers trading XAUUSD 😎")

# User Inputs
balance = st.number_input(
    "Enter your Balance",
    min_value=0.0,
    step=100.0,
    format="%.2f"
)

risk_percentage = st.number_input(
    "How many percent risk do you want to take?",
    min_value=0.0,
    max_value=100.0,
    step=0.1,
    format="%.2f"
)

current_price = st.number_input(
    "Enter Current Price / Entry Price",
    step=0.01,
    format="%.5f"
)

stoploss_price = st.number_input(
    "Enter Stop Loss Price",
    step=0.01,
    format="%.2f"
)

# Button
if st.button("Calculate"):

    try:
        # Risk Amount
        risk_amount = balance * risk_percentage / 100

        # Stop Loss in pips
        stoploss_in_pips = abs(current_price - stoploss_price) * 10

        # Avoid division by zero
        if stoploss_in_pips == 0:
            st.error("Current price and Stop Loss price cannot be the same.")

        else:
            # Lot Size Calculation
            lot_size = risk_amount / (stoploss_in_pips * 10)

            # Results
            st.success(f"Your Risk Amount is: ${risk_amount:.2f}")
            st.info(f"Your Stop Loss in Pips is: {stoploss_in_pips:.2f}")
            st.success(f"Your Lot Size is: {lot_size:.2f}")

    except Exception:
        st.error("Something went wrong. Please enter correct values.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
