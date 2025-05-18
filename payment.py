import streamlit as st
import uuid

def process_donation_payment(donor, amount, method="PayFast"):
    if amount <= 0:
        return "No payment made."

    if method == "PayFast":
        invoice_ref = uuid.uuid4().hex[:8]
        payfast_url = f"https://sandbox.payfast.pk/invoice?ref={invoice_ref}&amount={amount}&user={donor}"
        st.markdown(f"[Pay Now via PayFast]({payfast_url})", unsafe_allow_html=True)
        transaction_id = st.text_input("Enter PayFast Transaction ID after payment")
        if st.button("Confirm PayFast Payment"):
            st.success(f"✅ Rs. {amount} received. Transaction ID: {transaction_id}")
            return f"Payment confirmed with PayFast ID: {transaction_id}"
        return "Awaiting PayFast confirmation..."

    elif method == "JazzCash (Simulated)":
        fake_url = f"https://jazzcash.fakegateway.com/pay?user={donor}&amount={amount}&ref={uuid.uuid4().hex[:8]}"
        st.markdown(f"[Click to Pay with JazzCash]({fake_url})", unsafe_allow_html=True)
        transaction_id = st.text_input("Enter JazzCash Transaction ID after payment")
        if st.button("Confirm JazzCash Payment"):
            st.success(f"✅ Rs. {amount} received from {donor}. Transaction ID: {transaction_id}")
            return f"Payment confirmed with JazzCash ID: {transaction_id}"
        return "Awaiting JazzCash payment confirmation..."

    return "Unsupported payment method."
