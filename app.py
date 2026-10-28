import streamlit as st

st.set_page_config(page_title="The Campus Bookstore", page_icon="📚", layout="wide")

# Sample catalogue. Real book-cover images can be added later.
books = {
    "Introduction to Business": {"price": 450, "category": "Business", "description": "A starting point for understanding how businesses work."},
    "Principles of Management": {"price": 520, "category": "Business", "description": "Explore planning, leadership and organising teams."},
    "Business Statistics": {"price": 480, "category": "Finance & Analytics", "description": "Build confidence with data and business decisions."},
    "Python Programming for Beginners": {"price": 600, "category": "Technology", "description": "Learn the basics of Python step by step."},
    "Financial Accounting": {"price": 550, "category": "Finance & Analytics", "description": "Understand accounts, statements and core concepts."},
    "Marketing Management": {"price": 575, "category": "Business", "description": "Discover customers, branding and marketing strategy."},
    "Business Law": {"price": 500, "category": "Law & Economics", "description": "An introduction to legal ideas in business."},
    "Economics: An Introduction": {"price": 425, "category": "Law & Economics", "description": "Explore markets, choices and economic thinking."}
}

# Store cart and wishlist while navigating between pages.
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# Cream, plum and forest-green theme. Image placeholders are intentional for now.
st.markdown("""
<style>
.stApp { background: #fff8f2; color: #2d2928; }
h1, h2, h3 { color: #754263; }
[data-testid="stSidebar"] { background: #f5e9ef; }
div[data-testid="stMetric"] { background: white; border: 1px solid #ead7e1; border-radius: 14px; padding: 12px; }
div.stButton > button { border-radius: 10px; border: 1px solid #754263; }
.book-card { background: white; border: 1px solid #ead7e1; border-radius: 16px; padding: 16px; margin-bottom: 8px; }
.book-placeholder { background: linear-gradient(145deg,#754263,#a97891); color: white; border-radius: 10px; padding: 18px 8px; text-align: center; min-height: 90px; }
.eyebrow { color: #145b4f; letter-spacing: 2px; font-size: 12px; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

def money(amount):
    return f"₹{amount:,.2f}"

def calculate_bill(subtotal, coupon, student_discount, delivery, gift_wrap):
    # Choose the coupon percentage.
    if coupon == "READ10":
        coupon_rate = 10
    elif coupon == "WELCOME5":
        coupon_rate = 5
    else:
        coupon_rate = 0

    # Add the optional student discount and cap the total at 15%.
    if student_discount:
        student_rate = 5
    else:
        student_rate = 0
    discount_rate = min(coupon_rate + student_rate, 15)
    discount_amount = subtotal * discount_rate / 100

    # Work out the selected delivery charge.
    if delivery == "Standard delivery (+₹60)":
        delivery_charge = 60
    elif delivery == "Express delivery (+₹120)":
        delivery_charge = 120
    else:
        delivery_charge = 0

    # Gift wrapping is an optional flat charge.
    if gift_wrap:
        gift_charge = 30
    else:
        gift_charge = 0

    final_amount = subtotal - discount_amount + delivery_charge + gift_charge
    return discount_rate, discount_amount, delivery_charge, gift_charge, final_amount

def add_book(name):
    if name in st.session_state.cart:
        st.session_state.cart[name] += 1
    else:
        st.session_state.cart[name] = 1

def book_card(name):
    book = books[name]
    st.markdown(f"""
    <div class="book-card">
      <div class="book-placeholder"><div style="font-size:26px">📚</div><b>{name}</b><br><small>BOOK COVER PLACEHOLDER</small></div>
      <p class="eyebrow">{book['category'].upper()}</p>
      <h3>{name}</h3>
      <p>{book['description']}</p>
      <b>{money(book['price'])}</b>
    </div>
    """, unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:
        if st.button("＋ Add to cart", key="add_" + name, use_container_width=True):
            add_book(name)
            st.toast(f"Added {name} to your cart")
    with right:
        label = "♥ Saved" if name in st.session_state.wishlist else "♡ Wishlist"
        if st.button(label, key="wish_" + name, use_container_width=True):
            if name in st.session_state.wishlist:
                st.session_state.wishlist.remove(name)
            else:
                st.session_state.wishlist.append(name)
            st.rerun()

st.sidebar.markdown("## 📚 THE CAMPUS BOOKSTORE")
st.sidebar.caption("Your campus. Your books. Your next chapter.")
page = st.sidebar.radio("Navigate", ["Home", "Browse Books", "Shopping Cart", "Offers & Student Zone", "Checkout", "Wishlist", "About Us"])
st.sidebar.metric("Books in cart", sum(st.session_state.cart.values()))
st.sidebar.caption("Demo store • No real payments")

if page == "Home":
    st.markdown('<p class="eyebrow">A BOOKSTORE FOR CURIOUS MINDS</p>', unsafe_allow_html=True)
    st.title("Your next chapter starts here.")
    st.write("Discover useful reads for class, career and everything you're curious about.")
    a, b = st.columns([1.3, 1])
    with a:
        st.subheader("Learn something new. Find your next favourite.")
        st.write("From business and finance to technology and law, explore a student-friendly catalogue.")
        st.info("Book photography will be added in the next design pass.")
        st.caption("THOUGHTFUL PICKS · CLEAR PRICES · SIMPLE CHECKOUT")
    with b:
        st.markdown('<div class="book-card"><div class="book-placeholder" style="padding:45px 8px"><div style="font-size:40px">✦ 📚 ✦</div><h3 style="color:white">READ. LEARN. GROW.</h3><p>Your student bookshelf</p></div></div>', unsafe_allow_html=True)
    st.divider()
    st.subheader("Shop by category")
    category_cols = st.columns(4)
    for col, (icon, category) in zip(category_cols, [("◈","Business"),("▤","Finance & Analytics"),("⌘","Technology"),("§","Law & Economics")]):
        with col:
            st.markdown(f'<div class="book-card" style="text-align:center"><h2>{icon}</h2><b>{category}</b></div>', unsafe_allow_html=True)
    st.subheader("Featured reads")
    cols = st.columns(3)
    for col, name in zip(cols, list(books.keys())[:3]):
        with col:
            book_card(name)

elif page == "Browse Books":
    st.title("Browse the bookshelf")
    st.write("Search the catalogue, choose a category and sort by price or title.")
    search = st.text_input("Search books", placeholder="Try Python, business, accounting...")
    categories = ["All categories"] + sorted(set(item["category"] for item in books.values()))
    category = st.selectbox("Category", categories)
    sorting = st.selectbox("Sort by", ["Featured", "Price: low to high", "Price: high to low", "Title: A to Z"])
    matches = [name for name, item in books.items() if search.lower() in name.lower() and (category == "All categories" or item["category"] == category)]
    if sorting == "Price: low to high":
        matches.sort(key=lambda name: books[name]["price"])
    elif sorting == "Price: high to low":
        matches.sort(key=lambda name: books[name]["price"], reverse=True)
    elif sorting == "Title: A to Z":
        matches.sort()
    st.caption(f"{len(matches)} book(s) found")
    if not matches:
        st.warning("No books match those filters. Try another search.")
    for start in range(0, len(matches), 3):
        cols = st.columns(3)
        for col, name in zip(cols, matches[start:start+3]):
            with col:
                book_card(name)

elif page == "Shopping Cart":
    st.title("Your shopping cart")
    if not st.session_state.cart:
        st.info("Your cart is empty. Browse Books to add something to your shelf.")
    else:
        subtotal = 0
        for name in list(st.session_state.cart.keys()):
            price = books[name]["price"]
            c1, c2, c3 = st.columns([4, 2, 1])
            with c1:
                st.write(f"**{name}**")
                st.caption(f"{books[name]['category']} · {money(price)} each")
            with c2:
                qty = st.number_input("Quantity", min_value=1, max_value=20, value=st.session_state.cart[name], step=1, key="qty_" + name)
                st.session_state.cart[name] = qty
            with c3:
                if st.button("Remove", key="remove_" + name):
                    del st.session_state.cart[name]
                    st.rerun()
            subtotal += price * st.session_state.cart[name]
            st.divider()
        st.metric("Cart subtotal", money(subtotal))
        if st.button("Clear cart"):
            st.session_state.cart = {}
            st.rerun()

elif page == "Offers & Student Zone":
    st.title("Offers & Student Zone")
    st.write("Student-friendly savings for your next study session.")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="book-card"><p class="eyebrow">STUDENT PERK</p><h2>Extra 5% off</h2><p>Apply the student discount at checkout.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="book-card"><p class="eyebrow">BOOK LOVER OFFER</p><h2>READ10</h2><p>Use READ10 for 10% off the book subtotal.</p></div>', unsafe_allow_html=True)
    st.subheader("Available coupon codes")
    st.code("READ10  —  10% off books\nWELCOME5  —  5% off books")
    st.caption("Coupon and student discounts combine up to 15% in this demo.")

elif page == "Checkout":
    st.title("Checkout")
    if not st.session_state.cart:
        st.info("Your cart is empty. Add books before checking out.")
    else:
        subtotal = 0
        st.subheader("Order summary")
        for name, quantity in st.session_state.cart.items():
            line = books[name]["price"] * quantity
            subtotal += line
            st.write(f"{name} × {quantity} — {money(line)}")
        st.divider()
        delivery = st.radio("Delivery option", ["Store pickup (Free)", "Standard delivery (+₹60)", "Express delivery (+₹120)"])
        gift_wrap = st.checkbox("Gift wrapping (+₹30)")
        student_discount = st.checkbox("Apply student discount (5%)")
        coupon_choice = st.selectbox("Coupon code", ["No coupon", "READ10", "WELCOME5"])
        coupon = coupon_choice if coupon_choice in ["READ10", "WELCOME5"] else "No coupon"
        customer_name = st.text_input("Customer name (optional)")
        rate, discount, delivery_charge, gift_charge, total = calculate_bill(subtotal, coupon, student_discount, delivery, gift_wrap)
        x, y, z = st.columns(3)
        x.metric("Subtotal", money(subtotal))
        y.metric(f"Discount ({rate}%)", "-" + money(discount))
        z.metric("Estimated total", money(total))
        st.write(f"Delivery: {money(delivery_charge)} · Gift wrapping: {money(gift_charge)}")
        if st.button("Create demo receipt", type="primary"):
            receipt = ["THE CAMPUS BOOKSTORE", "DEMO RECEIPT", f"Customer: {customer_name or 'Not provided'}", ""]
            for name, quantity in st.session_state.cart.items():
                receipt.append(f"{name} x {quantity} — {money(books[name]['price'] * quantity)}")
            receipt += ["", f"Subtotal: {money(subtotal)}", f"Discount: -{money(discount)}", f"Delivery: {money(delivery_charge)}", f"Gift wrapping: {money(gift_charge)}", f"FINAL TOTAL: {money(total)}", "", "Demo only. No payment taken."]
            st.success("Demo receipt is ready. No payment has been taken.")
            st.download_button("Download receipt (.txt)", "\n".join(receipt), file_name="campus_bookstore_receipt.txt", mime="text/plain")

elif page == "Wishlist":
    st.title("Your wishlist")
    if not st.session_state.wishlist:
        st.info("Your wishlist is empty. Save books from Browse Books.")
    for name in list(st.session_state.wishlist):
        c1, c2, c3 = st.columns([4, 1, 1])
        with c1:
            st.write(f"**{name}** — {money(books[name]['price'])}")
        with c2:
            if st.button("Add to cart", key="wishlist_add_" + name):
                add_book(name)
                st.toast(f"Added {name} to cart")
        with c3:
            if st.button("Remove", key="wishlist_remove_" + name):
                st.session_state.wishlist.remove(name)
                st.rerun()

elif page == "About Us":
    st.title("A little about our bookstore")
    st.markdown("### Books for the curious, ambitious and always-learning.")
    st.write("The Campus Bookstore is a student project designed to make browsing a small learning-focused catalogue simple and welcoming.")
    st.write("Our sample collection includes business, finance, technology, law and economics titles.")
    st.info("This is a demonstration website. Prices are illustrative; no real payments, deliveries or saved orders are processed.")
    st.subheader("Project details")
    st.write("Built with Python and Streamlit.")
    st.write("Concepts used: dictionaries, lists, functions, loops, conditions, arithmetic and input widgets.")

st.sidebar.divider()
st.sidebar.caption("Made for learning • The Campus Bookstore")
