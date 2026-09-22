import streamlit as st

containers = {
    "1": ("500 mL Bottle", 10),
    "2": ("1 Liter Bottle", 15),
    "3": ("5 Liter Container", 40)
}

st.title("💧 Water Refilling Vendo")

st.subheader("Select Container")

choice = st.selectbox(
    "Container:",
    options=["1", "2", "3", "Exit"],
    format_func=lambda x: {
        "1": "1 - 500 mL Bottle (₱10)",
        "2": "2 - 1 Liter Bottle (₱15)",
        "3": "3 - 5 Liter Container (₱40)",
        "Exit": "Exit"
    }[x]
)

if choice == "Exit":
    st.success("Thank you for using the Water Refilling Vendo!")
    st.stop()

container, price = containers[choice]

st.write(f"**Container:** {container}")
st.write(f"**Price:** ₱{price}")

payment = st.number_input(
    "Enter payment (₱):",
    min_value=0,
    step=1
)

if st.button("Purchase"):
    if payment < price:
        st.error("Insufficient payment.")
    else:
        change = payment - price

        st.success("Transaction successful!")

        st.write(f"**Container:** {container}")
        st.write(f"**Price:** ₱{price}")
        st.write(f"**Change:** ₱{change}")

        remaining = change

        bills_20 = remaining // 20
        remaining %= 20

        bills_10 = remaining // 10
        remaining %= 10

        bills_5 = remaining // 5
        remaining %= 5

        bills_1 = remaining

        st.write(f"₱20: {bills_20}")
        st.write(f"₱10: {bills_10}")
        st.write(f"₱5: {bills_5}")
        st.write(f"₱1: {bills_1}")
