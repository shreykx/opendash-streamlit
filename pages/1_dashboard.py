from openbb import obb
import streamlit as st

name = st.text_input("What's your name?")
stocks = st.text_input("Type all symbols? Use ',' to separate.").split(",")

st.write(f"# Welcome {name}")
for stock in stocks:
    try:
        quote_data = obb.equity.price.quote(symbol=stock.strip(), provider="yfinance")
        if quote_data:
            st.write(f"# {stock}")

            k1 = quote_data.to_df()
            st.write(k1)
        else:
            st.write(f"{stock.strip()} - Not found")
    except Exception:
        st.write(f"{stock.strip()} - Not found")
