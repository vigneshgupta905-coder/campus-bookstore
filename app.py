import streamlit as st
from pathlib import Path

st.set_page_config(page_title="The Scholar’s Shelf", page_icon="📚", layout="wide", initial_sidebar_state="expanded")

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

# Image files uploaded to the GitHub repository under assets/
ASSET_DIR = Path(__file__).parent / "assets"
BRAND_DIR = ASSET_DIR / "branding"
LOGO_IMAGE = BRAND_DIR / "scholars_shelf_logo.png"
BANNER_IMAGE = BRAND_DIR / "brand_banner.jpg"
FLOATING_IMAGE = BRAND_DIR / "floating_books.png"
HERO_IMAGE = ASSET_DIR / "hero" / "homepage.jpg"
CATEGORY_IMAGES = {
    "Business": ASSET_DIR / "categories" / "business.jpg",
    "Finance & Analytics": ASSET_DIR / "categories" / "finance.jpg",
    "Technology": ASSET_DIR / "categories" / "tech.jpg",
    "Law & Economics": ASSET_DIR / "categories" / "law.jpg",
}
BOOK_IMAGES = {
    "Introduction to Business": ASSET_DIR / "books" / "introduction_to_business.jpg",
    "Principles of Management": ASSET_DIR / "books" / "principles_of_management.jpg",
    "Business Statistics": ASSET_DIR / "books" / "business_statistics.jpg",
    "Python Programming for Beginners": ASSET_DIR / "books" / "python_programming_for_beginners.jpg",
    "Financial Accounting": ASSET_DIR / "books" / "financial_accounting.jpg",
    "Marketing Management": ASSET_DIR / "books" / "marketing_management.jpg",
    "Business Law": ASSET_DIR / "books" / "business_law.jpg",
    "Economics: An Introduction": ASSET_DIR / "books" / "economics_an_introduction.jpg",
}

def show_image_if_available(path, **kwargs):
    if path.is_file():
        st.image(str(path), **kwargs)

# Store cart and wishlist while navigating between pages.
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# Cream, plum and forest-green theme.
st.markdown("""
<style>
:root { --plum:#5b1d3b; --green:#145b4f; --cream:#fff8f2; --blush:#f5e9ef; --gold:#c89a52; }
.stApp { background: radial-gradient(ellipse at 90% 8%, rgba(200,154,82,.10), transparent 30%), linear-gradient(180deg,#fffaf5 0%,#fff8f2 48%,#fbf0e8 100%); color: #30272a; }
[data-testid="stHeader"] { background: rgba(255,248,242,.86); }
h1, h2, h3 { color: var(--plum); font-family: Georgia, 'Times New Roman', serif; }
p, label, .stMarkdown { color: #3d3336; }
[data-testid="stSidebar"] { background: linear-gradient(180deg,#f6eaf0 0%,#fdf5f0 100%); border-right:1px solid #ead7e1; }
[data-testid="stSidebar"] [data-testid="stImage"] img { object-fit:contain; }
div[data-testid="stMetric"] { background: rgba(255,255,255,.84); border: 1px solid #ead7e1; border-radius: 16px; padding: 14px; box-shadow:0 5px 18px rgba(91,29,59,.04); }
div.stButton > button { border-radius: 12px; border: 1px solid #754263; transition:all .18s ease; }
div.stButton > button:hover { background:#5b1d3b; color:#fff8f2; border-color:#5b1d3b; transform:translateY(-1px); }
.book-card { background: rgba(255,255,255,.86); border: 1px solid #ead7e1; border-radius: 18px; padding: 16px; margin-bottom: 8px; box-shadow:0 8px 24px rgba(91,29,59,.045); }
.book-placeholder { background: linear-gradient(145deg,#5b1d3b,#a97891); color: white; border-radius: 12px; padding: 18px 8px; text-align: center; min-height: 90px; }
.eyebrow { color: #145b4f; letter-spacing: 2px; font-size: 12px; font-weight: 800; }
.brand-masthead { border-radius:0 0 24px 24px; overflow:hidden; margin: -1rem -1rem 1.5rem -1rem; box-shadow:0 8px 24px rgba(91,29,59,.08); border-bottom:1px solid #ead7e1; }
.brand-masthead img { display:block; width:100%; max-height:150px; object-fit:cover; object-position:center 45%; }
.page-intro { background:linear-gradient(115deg,rgba(255,255,255,.78),rgba(255,244,235,.64)); border:1px solid rgba(234,215,225,.85); border-radius:22px; padding:22px 26px; margin:8px 0 22px; }
.floating-brand { position:fixed; right:22px; bottom:18px; z-index:999; width:116px; opacity:.96; pointer-events:none; filter:drop-shadow(0 8px 12px rgba(58,32,43,.18)); animation:floatShelf 5s ease-in-out infinite; }
@keyframes floatShelf { 0%,100% { transform:translateY(0) rotate(0deg); } 50% { transform:translateY(-8px) rotate(-1deg); } }
@media (max-width: 700px) { .floating-brand { width:70px; right:8px; bottom:8px; opacity:.75; } .brand-masthead img { max-height:95px; } }
</style>
""", unsafe_allow_html=True)

# Consistent branded masthead and floating illustration across every page.
if BANNER_IMAGE.is_file():
    import base64
    banner_b64 = base64.b64encode(BANNER_IMAGE.read_bytes()).decode("utf-8")
    st.markdown(f'<div class="brand-masthead"><img src="data:image/jpeg;base64,{banner_b64}" alt="The Scholar’s Shelf — Books, Ideas, Brighter Tomorrows"></div>', unsafe_allow_html=True)
if FLOATING_IMAGE.is_file():
    import base64
    floating_b64 = base64.b64encode(FLOATING_IMAGE.read_bytes()).decode("utf-8")
    st.markdown(f'<img class="floating-brand" src="data:image/png;base64,{floating_b64}" alt="Books, learn, grow" />', unsafe_allow_html=True)

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
    st.markdown('<div class="book-card">', unsafe_allow_html=True)
    image_path = BOOK_IMAGES.get(name)
    if image_path and image_path.is_file():
        st.image(str(image_path), use_container_width=True)
    else:
        st.markdown(
            f'<div class="book-placeholder"><div style="font-size:26px">📚</div><b>{name}</b></div>',
            unsafe_allow_html=True,
        )
    st.markdown(f"<p class='eyebrow'>{book['category'].upper()}</p>", unsafe_allow_html=True)
    st.subheader(name)
    st.write(book["description"])
    st.markdown(f"**{money(book['price'])}**")
    st.markdown("</div>", unsafe_allow_html=True)
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

if LOGO_IMAGE.is_file():
    st.sidebar.image(str(LOGO_IMAGE), use_container_width=True)
st.sidebar.markdown("## THE SCHOLAR’S SHELF")
st.sidebar.caption("Books • Ideas • Brighter Tomorrows")
st.sidebar.markdown("Your campus. Your books. Your next chapter.")
page = st.sidebar.radio("Navigate", ["Home", "Browse Books", "Shopping Cart", "Offers & Student Zone", "Checkout", "Wishlist", "About Us"])
st.sidebar.metric("Books in cart", sum(st.session_state.cart.values()))
st.sidebar.caption("Demo store • No real payments")

if page == "Home":
    st.markdown('<div class="page-intro"><p class="eyebrow">A BOOKSTORE FOR CURIOUS MINDS</p><h1 style="margin-bottom:.25rem">Your next chapter starts here. ✦</h1><p style="font-size:1.08rem;margin-bottom:0">Discover useful reads for class, career and everything you’re curious about.</p></div>', unsafe_allow_html=True)
    if HERO_IMAGE.is_file():
        st.image(str(HERO_IMAGE), use_container_width=True)
    a, b = st.columns([1.3, 1])
    with a:
        st.subheader("Learn something new. Find your next favourite.")
        st.write("From business and finance to technology and law, explore a student-friendly catalogue.")
        st.caption("THOUGHTFUL PICKS · CLEAR PRICES · SIMPLE CHECKOUT")
    with b:
        st.markdown('<div class="book-card"><div class="book-placeholder" style="padding:35px 8px"><div style="font-size:40px">✦ 📚 ✦</div><h3 style="color:white">READ. LEARN. GROW.</h3><p>Your student bookshelf</p></div></div>', unsafe_allow_html=True)
    st.divider()
    st.subheader("Shop by category")
    category_cols = st.columns(4)
    for col, (icon, category) in zip(category_cols, [("◈","Business"),("▤","Finance & Analytics"),("⌘","Technology"),("§","Law & Economics")]):
        with col:
            category_image = CATEGORY_IMAGES.get(category)
            if category_image and category_image.is_file():
                st.image(str(category_image), use_container_width=True)
            else:
                st.markdown(f'<div class="book-card" style="text-align:center"><h2>{icon}</h2><b>{category}</b></div>', unsafe_allow_html=True)
            st.markdown(f"**{category}**")
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
            receipt = ["THE SCHOLAR’S SHELF", "DEMO RECEIPT", f"Customer: {customer_name or 'Not provided'}", ""]
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
    st.markdown('<p class="eyebrow">OUR STORY</p>', unsafe_allow_html=True)
    st.title("About The Scholar’s Shelf")
    st.markdown("### Books for curious minds, brighter tomorrows.")
    about_left, about_right = st.columns([1.05, 1])
    with about_left:
        st.write("The Scholar’s Shelf is a student-focused bookstore concept built to make learning simple, accessible and inspiring. We bring together a curated collection across business, finance, technology, law and economics — chosen for students and future professionals.")
        st.write("Whether you’re starting your first semester, exploring new interests or building skills for your career, we’re here to support your journey with useful reads, clear prices and a smooth, welcoming experience.")
        st.markdown("**Books • Ideas • Brighter Tomorrows**")
    with about_right:
        if HERO_IMAGE.is_file():
            st.image(str(HERO_IMAGE), use_container_width=True)
    st.divider()
    f1, f2, f3, f4 = st.columns(4)
    f1.metric("8+", "Curated titles")
    f2.metric("4", "Core categories")
    f3.metric("Student-first", "Approach")
    f4.metric("Our promise", "To you")
    st.info("This is a demonstration website. Prices are illustrative; no real payments, deliveries or saved orders are processed.")
    st.caption("Built with Python and Streamlit as a learning project.")

st.sidebar.divider()
st.sidebar.caption("Made for learning • The Scholar’s Shelf")
