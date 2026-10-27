import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="The Campus Bookstore", page_icon="📚", layout="wide")

# Store each book and its price in a dictionary
books = {
    "Introduction to Business": 450,
    "Principles of Management": 520,
    "Business Statistics": 480,
    "Python Programming for Beginners": 600,
    "Financial Accounting": 550,
    "Marketing Management": 575,
    "Business Law": 500,
    "Economics: An Introduction": 425
}

# Add a simple student-friendly design
st.markdown("""
<style>
.stApp { background-color: #fff8f2; }
h1, h2, h3 { color: #754263; }
div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #f0d7e5;
    border-radius: 12px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)
# Show the website heading
st.title("📚 The Campus Bookstore")
st.subheader("Find your next favourite book!")
st.write("Choose a book and order options to see your estimated bill.")

# Explain what the website does
with st.sidebar:
    st.header("About this website")
    st.write("This website calculates an estimated book order bill.")
    st.write("It is a student project and does not take payments or save orders.")

# Ask the customer for their choices
left, right = st.columns(2)

with left:
    st.header("1. Make your order")

    # Input 1: choose a book
    book_name = st.selectbox("Choose a book", list(books.keys()))

    # Input 2: choose the number of copies
    quantity = st.number_input("Number of copies", min_value=1, max_value=20, value=1, step=1)

    # Input 3: choose a delivery option
    delivery = st.radio(
        "Choose delivery",
        ["Store pickup (Free)", "Standard delivery (₹60)", "Express delivery (₹120)"]
    )

    # Input 4: choose gift wrapping if needed
    gift_wrap = st.checkbox("Add gift wrapping (+₹30)")

    # Input 5: choose the student discount student_discount = st.checkbox("Use student discount (5%)")
    student_discount = st.checkbox("Use student discount (5%)")

    # Input 6: choose a coupon
    coupon = st.selectbox(
        "Choose a coupon",
        ["No coupon", "READ10 (10% off books)", "WELCOME5 (5% off books)"]
    )

    # Input 7: name is optional
    customer_name = st.text_input("Your name (optional)")

with right:
    st.header("2. Book details")
    st.subheader(book_name)
    st.metric("Price for one book", f"₹{books[book_name]:,.2f}")
    st.write("Number of books in catalogue:", len(books))
    st.info("Change your choices to update the bill.")

# Use a function to calculate the bill
def calculate_bill(price, quantity, coupon, student_discount, delivery, gift_wrap):
    # Multiply price by quantity to get the book total
    book_total = price * quantity

    # Decide the coupon discount with if, elif and else
    if coupon == "READ10 (10% off books)":
        coupon_rate = 10
    elif coupon == "WELCOME5 (5% off books)":
        coupon_rate = 5
    else:
        coupon_rate = 0

    # Add the student discount if it was selected
    if student_discount:
        student_rate = 5
    else:
        student_rate = 0

    # Add the discount rates, but do not go over 15 percent
    discount_rate = coupon_rate + student_rate
    if discount_rate > 15:
        discount_rate = 15

    # Calculate how much money is taken off the book total
    discount_amount = book_total * discount_rate / 100
    after_discount = book_total - discount_amount

    # Decide the delivery charge
    if delivery == "Standard delivery (₹60)":
        delivery_charge = 60
    elif delivery == "Express delivery (₹120)":
        delivery_charge = 120
    else:
        delivery_charge = 0

    # Add the gift wrapping charge if selected
    if gift_wrap:
        gift_charge = 30
    else:
        gift_charge = 0

    # Return the values needed to show the bill
    final_amount = after_discount + delivery_charge + gift_charge
    return book_total, discount_rate, discount_amount, delivery_charge, gift_charge, final_amount

# Call the function with the customer's choices
price = books[book_name]
book_total, discount_rate, discount_amount, delivery_charge, gift_charge, final_amount = calculate_bill(
    price, quantity, coupon, student_discount, delivery, gift_wrap
)

# Show the bill heading
st.divider()
st.header("3. Your bill")

# Show the name only if the customer entered one
if customer_name.strip() != "":
    st.write("Prepared for:", customer_name.strip())
else:
    st.write("Customer name: Not provided")

# Use a loop to make the bill rows
bill_rows = [
    ["Book", book_name, f"₹{book_total:,.2f}"],
    ["Discount", f"{discount_rate}%", f"-₹{discount_amount:,.2f}"],
    ["Delivery", delivery, f"₹{delivery_charge:,.2f}"],
    ["Gift wrapping", "Yes" if gift_wrap else "No", f"₹{gift_charge:,.2f}"]
]

for row in bill_rows:
    st.write(row[0] + " — " + row[1] + ": " + row[2])

# Show the main totals in three columns
col1, col2, col3 = st.columns(3)
col1.metric("Book total", f"₹{book_total:,.2f}")
col2.metric("Discount", f"₹{discount_amount:,.2f}")
col3.metric("Final amount", f"₹{final_amount:,.2f}")

# Show a message based on the order
if discount_rate > 0:
    st.success("Discount applied: " + str(discount_rate) + "%")
elif quantity >= 5:
    st.info("You chose several copies. Ask about a bulk discount.")
else:
    st.info("No discount has been applied.")

# Warn the customer when the maximum quantity is selected
if quantity == 20:
    st.warning("You selected the maximum of 20 copies.")

st.caption("Sample prices only. No payments are taken and customer details are not saved.")
