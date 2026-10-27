import streamlit as st
from datetime import datetime

# ------------------------------------------------------------
# Campus Bookstore - Book Order and Bill Calculator
# A beginner-level Python + Streamlit business application.
# ------------------------------------------------------------

st.set_page_config(
    page_title="Campus Bookstore | Order Calculator",
    page_icon="📚",
    layout="wide"
)

# Dictionary: each book title is linked to its sample selling price.
BOOKS = {
    "Introduction to Business": 450.00,
    "Principles of Management": 520.00,
    "Business Statistics": 480.00,
    "Python Programming for Beginners": 600.00,
    "Financial Accounting": 550.00,
    "Marketing Management": 575.00,
    "Business Law": 500.00,
    "Economics: An Introduction": 425.00,
}

# Simple page styling. All calculations are performed in Python below.
st.markdown("""
<style>
    .stApp { background-color: #f7f8fb; }
    .block-container { padding-top: 1.7rem; padding-bottom: 2rem; }
    h1, h2, h3 { color: #203354; }
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e1e6ef;
        border-radius: 12px;
        padding: 14px;
    }
    div.stButton > button {
        border-radius: 9px;
        font-weight: 600;
    }
    .book-note {
        background: #eef3fb;
        border-left: 4px solid #315a91;
        padding: 12px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Header area
st.title("📚 Campus Bookstore")
st.subheader("Book Order & Bill Calculator")
st.write(
    "Choose your books and order preferences to prepare an estimated bill. "
    "This demo uses sample book prices and is designed for a classroom project."
)

with st.sidebar:
    st.header("About this tool")
    st.write("A simple ordering calculator for a small bookstore.")
    st.write("It calculates the book subtotal, discount, optional gift wrapping, and final amount.")
    st.caption("No order is stored and no payment is collected.")

st.divider()

# Two-column layout keeps the input area readable.
input_col, info_col = st.columns([1.15, 0.85], gap="large")

with input_col:
    st.header("1. Build your order")

    # Input 1: choose a book from the available catalogue.
    selected_book = st.selectbox("Select a book", list(BOOKS.keys()))

    # Input 2: quantity is restricted to whole numbers from 1 to 20.
    quantity = st.number_input(
        "Number of copies",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

    # Input 3: customers choose standard or express delivery.
    delivery = st.radio(
        "Delivery option",
        ["Store pickup (Free)", "Standard delivery (₹60)", "Express delivery (₹120)"],
        index=0
    )

    # Input 4: optional gift wrapping.
    gift_wrap = st.checkbox("Add gift wrapping (+₹30 per order)")

    # Input 5: optional student discount, applied before delivery.
    student_discount = st.checkbox("Apply student discount (5%)")

    # Input 6: coupon selection determines an additional discount.
    coupon = st.selectbox(
        "Coupon code",
        ["No coupon", "READ10 (10% off books)", "WELCOME5 (5% off books)"]
    )

    # Input 7: optional customer name for the bill heading.
    customer_name = st.text_input("Customer name (optional)", max_chars=60)

with info_col:
    st.header("2. Book details")
    st.markdown("### " + selected_book)
    st.metric("Price per copy", f"₹{BOOKS[selected_book]:,.2f}")
    st.write(f"**Copies selected:** {quantity}")
    st.write("**Catalogue size:**", len(BOOKS), "sample titles")
    st.markdown(
        '<div class="book-note">Tip: select a quantity, delivery option and any eligible discount. '
        'The bill below updates automatically.</div>',
        unsafe_allow_html=True
    )
    st.caption("All titles and prices are illustrative examples for this project.")

# --------------------- Calculation section ---------------------

# Calculate the total price before discounts.
unit_price = BOOKS[selected_book]
book_subtotal = unit_price * quantity

# Determine coupon rate using if/elif/else conditional logic.
if coupon == "READ10 (10% off books)":
    coupon_rate = 0.10
elif coupon == "WELCOME5 (5% off books)":
    coupon_rate = 0.05
else:
    coupon_rate = 0.00

# Student discount is represented by a Boolean checkbox value.
student_rate = 0.05 if student_discount else 0.00

# Discounts apply to the book subtotal, and combined discount is capped at 15%.
combined_discount_rate = min(coupon_rate + student_rate, 0.15)
discount_amount = book_subtotal * combined_discount_rate
discounted_books_total = book_subtotal - discount_amount

# Delivery charge is selected by the user.
if delivery == "Standard delivery (₹60)":
    delivery_charge = 60.00
elif delivery == "Express delivery (₹120)":
    delivery_charge = 120.00
else:
    delivery_charge = 0.00

# Gift wrapping is a one-time order charge, not a per-book charge.
gift_wrap_charge = 30.00 if gift_wrap else 0.00

# This classroom example does not add GST because actual tax treatment depends
# on the product and seller. The displayed final amount is an estimate.
final_total = discounted_books_total + delivery_charge + gift_wrap_charge

# ------------------------ Bill display -------------------------

st.divider()
st.header("3. Order summary")

if customer_name.strip():
    st.write(f"Prepared for **{customer_name.strip()}**")
else:
    st.write("Customer name: **Not provided**")

# Display a simple itemised summary.
summary = [
    {"Description": selected_book, "Details": f"{quantity} × ₹{unit_price:,.2f}", "Amount": f"₹{book_subtotal:,.2f}"},
    {"Description": "Book discount", "Details": f"{combined_discount_rate:.0%}", "Amount": f"-₹{discount_amount:,.2f}"},
    {"Description": "Delivery", "Details": delivery, "Amount": f"₹{delivery_charge:,.2f}"},
    {"Description": "Gift wrapping", "Details": "Selected" if gift_wrap else "Not selected", "Amount": f"₹{gift_wrap_charge:,.2f}"},
]
st.table(summary)

metric1, metric2, metric3 = st.columns(3)
metric1.metric("Book subtotal", f"₹{book_subtotal:,.2f}")
metric2.metric("Total discount", f"₹{discount_amount:,.2f}")
metric3.metric("Amount payable", f"₹{final_total:,.2f}")

# Business message changes depending on the amount and discount.
if combined_discount_rate > 0:
    st.success(f"Discount applied: {combined_discount_rate:.0%} on the book subtotal.")
elif quantity >= 5:
    st.info("You have selected several copies. Ask the bookstore whether bulk-order pricing is available.")
else:
    st.info("No book discount has been applied. You can select an eligible discount above.")

# Validation and edge-case messaging. Widgets also restrict the quantity range.
if quantity == 20:
    st.warning("You selected the maximum quantity allowed in this demo. Please confirm that it is intentional.")

st.caption(
    "Educational prototype only. Prices, coupons and delivery fees are sample values. "
    "This app does not process payments, save customer information, or issue a tax invoice."
)
