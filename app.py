import streamlit as st
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="The Scholar’s Shelf", page_icon="📚", layout="wide", initial_sidebar_state="expanded")

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
    'Introduction to Business': ASSET_DIR / "books" / "introduction_to_business.jpg",
    'Principles of Management': ASSET_DIR / "books" / "principles_of_management.jpg",
    'Business Statistics': ASSET_DIR / "books" / "business_statistics.jpg",
    'Python Programming for Beginners': ASSET_DIR / 'book_covers' / 'python_programming_for_beginners.jpg',
    'Financial Accounting': ASSET_DIR / "books" / "financial_accounting.jpg",
    'Marketing Management': ASSET_DIR / 'book_covers' / 'marketing_management.jpg',
    'Business Law': ASSET_DIR / 'book_covers' / 'business_law.jpg',
    'Economics: An Introduction': ASSET_DIR / 'book_covers' / 'economics_an_introduction.jpg',
    'The Psychology of Money': ASSET_DIR / "book_covers" / "the_psychology_of_money.jpg",
    'Atomic Habits': ASSET_DIR / "book_covers" / "atomic_habits.jpg",
    'Deep Work': ASSET_DIR / "book_covers" / "deep_work.jpg",
    'Ikigai': ASSET_DIR / "book_covers" / "ikigai.jpg",
    'The Alchemist': ASSET_DIR / "book_covers" / "the_alchemist.jpg",
    'Pride and Prejudice': ASSET_DIR / "book_covers" / "pride_and_prejudice.jpg",
    '1984': ASSET_DIR / "book_covers" / "1984.jpg",
    'Animal Farm': ASSET_DIR / "book_covers" / "animal_farm.jpg",
    'To Kill a Mockingbird': ASSET_DIR / "book_covers" / "to_kill_a_mockingbird.jpg",
    'The Great Gatsby': ASSET_DIR / "book_covers" / "the_great_gatsby.jpg",
    'The Kite Runner': ASSET_DIR / "book_covers" / "the_kite_runner.jpg",
    'A Thousand Splendid Suns': ASSET_DIR / "book_covers" / "a_thousand_splendid_suns.jpg",
    'The White Tiger': ASSET_DIR / 'book_covers' / 'the_white_tiger.jpg',
    'The God of Small Things': ASSET_DIR / "book_covers" / "the_god_of_small_things.jpg",
    'Train to Pakistan': ASSET_DIR / "book_covers" / "train_to_pakistan.jpg",
    'The Guide': ASSET_DIR / 'book_covers' / 'the_guide.jpg',
    'Malgudi Days': ASSET_DIR / "book_covers" / "malgudi_days.jpg",
    'The Palace of Illusions': ASSET_DIR / "book_covers" / "the_palace_of_illusions.jpg",
    'The Immortals of Meluha': ASSET_DIR / 'book_covers' / 'the_immortals_of_meluha.jpg',
    'The Namesake': ASSET_DIR / "book_covers" / "the_namesake.jpg",
    'Interpreter of Maladies': ASSET_DIR / "book_covers" / "interpreter_of_maladies.jpg",
    'Midnight’s Children': ASSET_DIR / 'book_covers' / 'midnights_children.jpg',
    'The Discovery of India': ASSET_DIR / "book_covers" / "the_discovery_of_india.jpg",
    'India After Gandhi': ASSET_DIR / "book_covers" / "india_after_gandhi.jpg",
    'Wings of Fire': ASSET_DIR / 'book_covers' / 'wings_of_fire.jpg',
    'Steve Jobs': ASSET_DIR / "book_covers" / "steve_jobs.jpg",
    'Educated': ASSET_DIR / "book_covers" / "educated.jpg",
    'Sapiens': ASSET_DIR / "book_covers" / "sapiens.jpg",
    'Factfulness': ASSET_DIR / "book_covers" / "factfulness.jpg",
    'Thinking, Fast and Slow': ASSET_DIR / 'book_covers' / 'thinking_fast_and_slow.jpg',
    'Man’s Search for Meaning': ASSET_DIR / "book_covers" / "mans_search_for_meaning.jpg",
    'The Art of Thinking Clearly': ASSET_DIR / "book_covers" / "the_art_of_thinking_clearly.jpg",
    'Start with Why': ASSET_DIR / "book_covers" / "start_with_why.jpg",
    'Good to Great': ASSET_DIR / 'book_covers' / 'good_to_great.jpg',
    'The Lean Startup': ASSET_DIR / "book_covers" / "the_lean_startup.jpg",
    'Zero to One': ASSET_DIR / 'book_covers' / 'zero_to_one.jpg',
    'Rework': ASSET_DIR / 'book_covers' / 'rework.jpg',
    'The Intelligent Investor': ASSET_DIR / "book_covers" / "the_intelligent_investor.jpg",
    'Rich Dad Poor Dad': ASSET_DIR / "book_covers" / "rich_dad_poor_dad.jpg",
    'The Little Book of Common Sense Investing': ASSET_DIR / "book_covers" / "the_little_book_of_common_sense_investing.jpg",
    'A Random Walk Down Wall Street': ASSET_DIR / 'book_covers' / 'a_random_walk_down_wall_street.jpg',
    'The Design of Everyday Things': ASSET_DIR / 'book_covers' / 'the_design_of_everyday_things.jpg',
    'The Creative Act: A Way of Being': ASSET_DIR / 'book_covers' / 'the_creative_act_a_way_of_being.jpg',
    'Show Your Work!': ASSET_DIR / "book_covers" / "show_your_work.jpg",
    'Steal Like an Artist': ASSET_DIR / "book_covers" / "steal_like_an_artist.jpg",
    'The Hobbit': ASSET_DIR / "book_covers" / "the_hobbit.jpg",
    'Harry Potter and the Philosopher’s Stone': ASSET_DIR / "book_covers" / "harry_potter_and_the_philosophers_stone.jpg",
    'The Hunger Games': ASSET_DIR / "book_covers" / "the_hunger_games.jpg",
    'The Fault in Our Stars': ASSET_DIR / "book_covers" / "the_fault_in_our_stars.jpg",
    'The Book Thief': ASSET_DIR / "book_covers" / "the_book_thief.jpg",
    'The Midnight Library': ASSET_DIR / "book_covers" / "the_midnight_library.jpg",
    'Before the Coffee Gets Cold': ASSET_DIR / "book_covers" / "before_the_coffee_gets_cold.jpg",
}

# Catalogue entries use illustrative prices and curated tags; this demo has no sales analytics.
RAW_BOOKS = [
("Introduction to Business","OpenStax","Business",450,"A starting point for understanding how businesses work."),
("Principles of Management","Stephen P. Robbins and Mary Coulter","Business",520,"Explore planning, leadership and organising teams."),
("Business Statistics","J. K. Sharma","Finance & Analytics",480,"Build confidence with data and business decisions."),
("Python Programming for Beginners","John M. Zelle","Technology",600,"Learn programming fundamentals step by step."),
("Financial Accounting","S. N. Maheshwari","Finance & Analytics",550,"Understand accounts, statements and core concepts."),
("Marketing Management","Philip Kotler and Kevin Lane Keller","Business",575,"Discover customers, branding and marketing strategy."),
("Business Law","P. C. Tulsian","Law & Economics",500,"An introduction to legal ideas in business."),
("Economics: An Introduction","N. Gregory Mankiw","Law & Economics",425,"Explore markets, choices and economic thinking."),
("The Psychology of Money","Morgan Housel","Finance & Analytics",399,"Timeless lessons about wealth, behaviour and decisions."),
("Atomic Habits","James Clear","Self-Development",499,"Build better habits through small, repeatable changes."),
("Deep Work","Cal Newport","Self-Development",449,"Learn to focus in a distracted world."),
("Ikigai","Héctor García and Francesc Miralles","Self-Development",299,"Explore purpose, routines and a meaningful life."),
("The Alchemist","Paulo Coelho","Fiction",299,"A young shepherd follows a dream across the desert."),
("Pride and Prejudice","Jane Austen","Classics",250,"A classic novel about love, manners and first impressions."),
("1984","George Orwell","Dystopian Fiction",299,"A powerful story about surveillance and control."),
("Animal Farm","George Orwell","Classics",199,"A political fable about power and revolution."),
("To Kill a Mockingbird","Harper Lee","Classics",350,"A story of justice, empathy and growing up."),
("The Great Gatsby","F. Scott Fitzgerald","Classics",275,"A portrait of ambition and the American dream."),
("The Kite Runner","Khaled Hosseini","Fiction",399,"Friendship, memory and redemption across decades."),
("A Thousand Splendid Suns","Khaled Hosseini","Fiction",399,"Two women’s lives intertwine amid Afghanistan’s history."),
("The White Tiger","Aravind Adiga","Indian Writing",350,"A sharp, darkly comic look at class and ambition."),
("The God of Small Things","Arundhati Roy","Indian Writing",399,"A richly layered novel set in Kerala."),
("Train to Pakistan","Khushwant Singh","Indian Writing",299,"A village faces the human cost of Partition."),
("The Guide","R. K. Narayan","Indian Writing",250,"A charming and complex tale set in Malgudi."),
("Malgudi Days","R. K. Narayan","Indian Writing",299,"Short stories about everyday life in Malgudi."),
("The Palace of Illusions","Chitra Banerjee Divakaruni","Mythology",399,"The Mahabharata retold through Draupadi’s perspective."),
("The Immortals of Meluha","Amish Tripathi","Mythology",399,"A modern mythological adventure inspired by Shiva."),
("The Namesake","Jhumpa Lahiri","Indian Writing",350,"A family navigates identity between cultures."),
("Interpreter of Maladies","Jhumpa Lahiri","Short Stories",299,"Stories of connection, migration and belonging."),
("Midnight’s Children","Salman Rushdie","Indian Writing",499,"A magical, expansive novel tied to India’s history."),
("The Discovery of India","Jawaharlal Nehru","History",499,"A reflective journey through India’s civilisation and history."),
("India After Gandhi","Ramachandra Guha","History",699,"A detailed account of modern India after independence."),
("Wings of Fire","A. P. J. Abdul Kalam and Arun Tiwari","Biography",350,"The life and lessons of India’s former president and scientist."),
("Steve Jobs","Walter Isaacson","Biography",599,"A biography of the co-founder of Apple."),
("Educated","Tara Westover","Memoir",499,"A memoir about education, family and self-invention."),
("Sapiens","Yuval Noah Harari","History",599,"A broad history of humankind."),
("Factfulness","Hans Rosling","Nonfiction",449,"A data-minded way to understand the world."),
("Thinking, Fast and Slow","Daniel Kahneman","Psychology",599,"How two modes of thought shape our choices."),
("Man’s Search for Meaning","Viktor E. Frankl","Psychology",299,"A psychiatrist reflects on meaning and resilience."),
("The Art of Thinking Clearly","Rolf Dobelli","Psychology",399,"Common thinking errors and how to spot them."),
("Start with Why","Simon Sinek","Business",399,"How purpose can guide leadership and organisations."),
("Good to Great","Jim Collins","Business",499,"Research-based ideas about sustained business performance."),
("The Lean Startup","Eric Ries","Entrepreneurship",499,"Test ideas, learn quickly and build iteratively."),
("Zero to One","Peter Thiel with Blake Masters","Entrepreneurship",399,"A contrarian view of innovation and startups."),
("Rework","Jason Fried and David Heinemeier Hansson","Entrepreneurship",350,"Practical challenges to conventional business thinking."),
("The Intelligent Investor","Benjamin Graham","Finance & Analytics",599,"A classic introduction to value investing principles."),
("Rich Dad Poor Dad","Robert T. Kiyosaki","Finance & Analytics",399,"A popular introduction to personal finance mindsets."),
("The Little Book of Common Sense Investing","John C. Bogle","Finance & Analytics",399,"An accessible case for low-cost index investing."),
("A Random Walk Down Wall Street","Burton G. Malkiel","Finance & Analytics",599,"An overview of investing, markets and strategy."),
("The Design of Everyday Things","Don Norman","Design",499,"Understand how design shapes everyday experiences."),
("The Creative Act: A Way of Being","Rick Rubin","Creativity",599,"Reflections on creativity and the creative process."),
("Show Your Work!","Austin Kleon","Creativity",299,"Ways to share creative work and find an audience."),
("Steal Like an Artist","Austin Kleon","Creativity",299,"A compact guide to creative inspiration."),
("The Hobbit","J. R. R. Tolkien","Fantasy",399,"A hobbit joins an unexpected quest for treasure."),
("Harry Potter and the Philosopher’s Stone","J. K. Rowling","Fantasy",450,"A young wizard discovers a new world."),
("The Hunger Games","Suzanne Collins","Dystopian Fiction",399,"A teenager enters a televised fight for survival."),
("The Fault in Our Stars","John Green","Young Adult",350,"Two teenagers find connection while facing illness."),
("The Book Thief","Markus Zusak","Historical Fiction",399,"A young girl finds solace in books during wartime."),
("The Midnight Library","Matt Haig","Fiction",399,"A woman explores lives she might have lived."),
("Before the Coffee Gets Cold","Toshikazu Kawaguchi","Fiction",399,"Stories unfold in a café where visitors can travel through time."),
]

books = {
    title: {
        "author": author, "category": category, "price": price, "description": description,
        "genre": category, "popular": index <= 20, "formats": ["Paperback"],
        "purchase_available": True, "borrow_available": category in {"Business", "Finance & Analytics", "Technology", "Law & Economics", "Classics", "Indian Writing"},
        "rental_available": True,
    }
    for index, (title, author, category, price, description) in enumerate(RAW_BOOKS, start=1)
}

AUTHOR_IMAGES = {
    'A. P. J. Abdul Kalam and Arun Tiwari': ASSET_DIR / 'authors' / 'a_p_j_abdul_kalam_and_arun_tiwari.jpg',
    'Amish Tripathi': ASSET_DIR / 'authors' / 'amish_tripathi.jpg',
    'Aravind Adiga': ASSET_DIR / 'authors' / 'aravind_adiga.jpg',
    'Arundhati Roy': ASSET_DIR / 'authors' / 'arundhati_roy.jpg',
    'Austin Kleon': ASSET_DIR / 'authors' / 'austin_kleon.jpg',
    'Benjamin Graham': ASSET_DIR / 'authors' / 'benjamin_graham.jpg',
    'Burton G. Malkiel': ASSET_DIR / 'authors' / 'burton_g_malkiel.jpg',
    'Cal Newport': ASSET_DIR / 'authors' / 'cal_newport.jpg',
    'Chitra Banerjee Divakaruni': ASSET_DIR / 'authors' / 'chitra_banerjee_divakaruni.jpg',
    'Daniel Kahneman': ASSET_DIR / 'authors' / 'daniel_kahneman.jpg',
    'Don Norman': ASSET_DIR / 'authors' / 'don_norman.jpg',
    'Eric Ries': ASSET_DIR / 'authors' / 'eric_ries.jpg',
    'F. Scott Fitzgerald': ASSET_DIR / 'authors' / 'f_scott_fitzgerald.jpg',
    'George Orwell': ASSET_DIR / 'authors' / 'george_orwell.jpg',
    'Hans Rosling': ASSET_DIR / 'authors' / 'hans_rosling.jpg',
    'Harper Lee': ASSET_DIR / 'authors' / 'harper_lee.jpg',
    'Héctor García and Francesc Miralles': ASSET_DIR / 'authors' / 'hector_garcia_and_francesc_miralles.jpg',
    'J. K. Rowling': ASSET_DIR / 'authors' / 'j_k_rowling.jpg',
    'J. K. Sharma': ASSET_DIR / 'authors' / 'j_k_sharma.jpg',
    'J. R. R. Tolkien': ASSET_DIR / 'authors' / 'j_r_r_tolkien.jpg',
    'James Clear': ASSET_DIR / 'authors' / 'james_clear.jpg',
    'Jane Austen': ASSET_DIR / 'authors' / 'jane_austen.jpg',
    'Jason Fried and David Heinemeier Hansson': ASSET_DIR / 'authors' / 'jason_fried_and_david_heinemeier_hansson.jpg',
    'Jawaharlal Nehru': ASSET_DIR / 'authors' / 'jawaharlal_nehru.jpg',
    'Jhumpa Lahiri': ASSET_DIR / 'authors' / 'jhumpa_lahiri.jpg',
    'Jim Collins': ASSET_DIR / 'authors' / 'jim_collins.jpg',
    'John C. Bogle': ASSET_DIR / 'authors' / 'john_c_bogle.jpg',
    'John Green': ASSET_DIR / 'authors' / 'john_green.jpg',
    'John M. Zelle': ASSET_DIR / 'authors' / 'john_m_zelle.jpg',
    'Khaled Hosseini': ASSET_DIR / 'authors' / 'khaled_hosseini.jpg',
    'Khushwant Singh': ASSET_DIR / 'authors' / 'khushwant_singh.jpg',
    'Markus Zusak': ASSET_DIR / 'authors' / 'markus_zusak.jpg',
    'Matt Haig': ASSET_DIR / 'authors' / 'matt_haig.jpg',
    'Morgan Housel': ASSET_DIR / 'authors' / 'morgan_housel.jpg',
    'N. Gregory Mankiw': ASSET_DIR / 'authors' / 'n_gregory_mankiw.jpg',
    'OpenStax': ASSET_DIR / 'authors' / 'openstax.jpg',
    'P. C. Tulsian': ASSET_DIR / 'authors' / 'p_c_tulsian.jpg',
    'Paulo Coelho': ASSET_DIR / 'authors' / 'paulo_coelho.jpg',
    'Peter Thiel with Blake Masters': ASSET_DIR / 'authors' / 'peter_thiel_with_blake_masters.jpg',
    'Philip Kotler and Kevin Lane Keller': ASSET_DIR / 'authors' / 'philip_kotler_and_kevin_lane_keller.jpg',
    'R. K. Narayan': ASSET_DIR / 'authors' / 'r_k_narayan.jpg',
    'Ramachandra Guha': ASSET_DIR / 'authors' / 'ramachandra_guha.jpg',
    'Rick Rubin': ASSET_DIR / 'authors' / 'rick_rubin.jpg',
    'Robert T. Kiyosaki': ASSET_DIR / 'authors' / 'robert_t_kiyosaki.jpg',
    'Rolf Dobelli': ASSET_DIR / 'authors' / 'rolf_dobelli.jpg',
    'S. N. Maheshwari': ASSET_DIR / 'authors' / 's_n_maheshwari.jpg',
    'Salman Rushdie': ASSET_DIR / 'authors' / 'salman_rushdie.jpg',
    'Simon Sinek': ASSET_DIR / 'authors' / 'simon_sinek.jpg',
    'Stephen P. Robbins and Mary Coulter': ASSET_DIR / 'authors' / 'stephen_p_robbins_and_mary_coulter.jpg',
    'Suzanne Collins': ASSET_DIR / 'authors' / 'suzanne_collins.jpg',
    'Tara Westover': ASSET_DIR / 'authors' / 'tara_westover.jpg',
    'Toshikazu Kawaguchi': ASSET_DIR / 'authors' / 'toshikazu_kawaguchi.jpg',
    'Viktor E. Frankl': ASSET_DIR / 'authors' / 'viktor_e_frankl.jpg',
    'Walter Isaacson': ASSET_DIR / 'authors' / 'walter_isaacson.jpg',
    'Yuval Noah Harari': ASSET_DIR / 'authors' / 'yuval_noah_harari.jpg',
}

# Curated demo listings only; these are not real student posts or confirmed inventory.
EXCHANGE_LISTINGS = [
    {"title":"Business Statistics","condition":"Good","price":220,"seller":"Demo student A","note":"A few pencil notes in the margins."},
    {"title":"Marketing Management","condition":"Very good","price":300,"seller":"Demo student B","note":"Clean copy, minimal wear."},
    {"title":"The Psychology of Money","condition":"Like new","price":250,"seller":"Demo student C","note":"Paperback in excellent condition."},
    {"title":"Principles of Management","condition":"Good","price":280,"seller":"Demo student D","note":"Older edition; check course requirements."},
]

if "cart" not in st.session_state: st.session_state.cart = {}
if "rental_cart" not in st.session_state: st.session_state.rental_cart = {}
if "borrow_requests" not in st.session_state: st.session_state.borrow_requests = []
if "wishlist" not in st.session_state: st.session_state.wishlist = []
if "exchange_interest" not in st.session_state: st.session_state.exchange_interest = []
if "bundle" not in st.session_state: st.session_state.bundle = []

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

def show_branding():
    if BANNER_IMAGE.is_file():
        import base64
        encoded = base64.b64encode(BANNER_IMAGE.read_bytes()).decode("utf-8")
        st.markdown(f'<div class="brand-masthead"><img src="data:image/jpeg;base64,{encoded}" alt="The Scholar’s Shelf banner"></div>', unsafe_allow_html=True)
    if FLOATING_IMAGE.is_file():
        import base64
        encoded = base64.b64encode(FLOATING_IMAGE.read_bytes()).decode("utf-8")
        st.markdown(f'<img class="floating-brand" src="data:image/png;base64,{encoded}" alt="Floating books illustration" />', unsafe_allow_html=True)

def money(amount):
    return f"₹{amount:,.2f}"

def calculate_bill(subtotal, coupon, student_discount, delivery, gift_wrap):
    if coupon == "READ10": coupon_rate = 10
    elif coupon == "WELCOME5": coupon_rate = 5
    else: coupon_rate = 0
    student_rate = 5 if student_discount else 0
    discount_rate = min(coupon_rate + student_rate, 15)
    discount_amount = subtotal * discount_rate / 100
    if delivery == "Standard delivery (+₹60)": delivery_charge = 60
    elif delivery == "Express delivery (+₹120)": delivery_charge = 120
    else: delivery_charge = 0
    gift_charge = 30 if gift_wrap else 0
    final_amount = subtotal - discount_amount + delivery_charge + gift_charge
    return discount_rate, discount_amount, delivery_charge, gift_charge, final_amount

def add_book(name):
    if name in books:
        st.session_state.cart[name] = st.session_state.cart.get(name, 0) + 1
def book_card(name, show_author=True):
    book = books[name]
    st.markdown('<div class="book-card">', unsafe_allow_html=True)
    image_path = BOOK_IMAGES.get(name)
    if image_path and image_path.is_file():
        st.image(str(image_path), use_container_width=True)
    else:
        st.markdown(f'<div class="book-placeholder"><div style="font-size:26px">📚</div><b>{name}</b></div>', unsafe_allow_html=True)
    st.markdown(f"<p class='eyebrow'>{book['category'].upper()}</p>", unsafe_allow_html=True)
    st.subheader(name)
    if show_author: st.caption(f"By {book['author']}")
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
            if name in st.session_state.wishlist: st.session_state.wishlist.remove(name)
            else: st.session_state.wishlist.append(name)
            st.rerun()

def render_book_grid(names, columns=3):
    for start in range(0, len(names), columns):
        cols = st.columns(columns)
        for col, name in zip(cols, names[start:start + columns]):
            with col: book_card(name)

def author_books(author):
    return [title for title, item in books.items() if item["author"] == author]

show_branding()
if LOGO_IMAGE.is_file(): st.sidebar.image(str(LOGO_IMAGE), use_container_width=True)
st.sidebar.markdown("## THE SCHOLAR’S SHELF")
st.sidebar.caption("Books • Ideas • Brighter Tomorrows")
st.sidebar.markdown("Your campus. Your books. Your next chapter.")
page_order = [
    "Home",
    "Browse Books",
    "Popular Reads",
    "Authors",
    "Semester Bundle Builder",
    "Library Mode",
    "Campus Book Exchange",
    "Shopping Cart",
    "Offers & Student Zone",
    "Checkout",
    "Wishlist",
    "About Us",
]

if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = "Home"

page = st.sidebar.radio(
    "Navigate",
    page_order,
    key="nav_choice",
)
st.sidebar.metric("Books in catalogue", len(books))
st.sidebar.metric("Items in cart", sum(st.session_state.cart.values()) + sum(st.session_state.rental_cart.values()))
st.sidebar.caption("Demo store • No real payments or confirmed lending")

if page == "Home":
    st.markdown('<div class="page-intro"><p class="eyebrow">A BOOKSTORE FOR CURIOUS MINDS</p><h1 style="margin-bottom:.25rem">Your next chapter starts here. ✦</h1><p style="font-size:1.08rem;margin-bottom:0">Discover useful reads for class, career and everything you’re curious about.</p></div>', unsafe_allow_html=True)
    if HERO_IMAGE.is_file(): st.image(str(HERO_IMAGE), use_container_width=True)
    a, b = st.columns([1.3, 1])
    with a:
        st.subheader("Learn something new. Find your next favourite.")
        st.write("Explore 60 titles spanning coursework, novels, Indian writing, classics, finance, technology, biographies and more.")
        st.caption("THOUGHTFUL PICKS · CLEAR PRICES · STUDENT-FRIENDLY FEATURES")
    with b:
        st.markdown('<div class="book-card"><div class="book-placeholder" style="padding:35px 8px"><div style="font-size:40px">✦ 📚 ✦</div><h3 style="color:white">READ. LEARN. GROW.</h3><p>Your student bookshelf</p></div></div>', unsafe_allow_html=True)
    st.divider()
    st.subheader("Explore popular reads")
    st.caption("Curated picks for this demo — not ranked using real sales data.")
    render_book_grid([title for title, item in books.items() if item["popular"]][:3])
    st.subheader("Explore by genre")
    genres = sorted(set(item["category"] for item in books.values()))
    st.write(" · ".join(genres))
    st.info("Build a semester bundle, compare buying and borrowing information, or explore demo campus exchange listings from the sidebar.")

elif page == "Browse Books":
    st.title("Browse the bookshelf")
    st.write("Search 60 titles, filter by genre or author, and sort the results.")
    search = st.text_input("Search books, authors or topics", placeholder="Try Python, Jhumpa Lahiri, finance...")
    categories = ["All genres"] + sorted(set(item["category"] for item in books.values()))
    category = st.selectbox("Genre", categories)
    authors = ["All authors"] + sorted(set(item["author"] for item in books.values()))
    author_filter = st.selectbox("Author", authors)
    sorting = st.selectbox("Sort by", ["Featured", "Price: low to high", "Price: high to low", "Title: A to Z"])
    matches = [name for name, item in books.items()
               if search.lower() in (name + " " + item["author"] + " " + item["description"] + " " + item["category"]).lower()
               and (category == "All genres" or item["category"] == category)
               and (author_filter == "All authors" or item["author"] == author_filter)]
    if sorting == "Price: low to high": matches.sort(key=lambda name: books[name]["price"])
    elif sorting == "Price: high to low": matches.sort(key=lambda name: books[name]["price"], reverse=True)
    elif sorting == "Title: A to Z": matches.sort()
    st.caption(f"{len(matches)} book(s) found")
    if not matches: st.warning("No books match those filters. Try another search.")
    else: render_book_grid(matches)

elif page == "Popular Reads":
    st.title("Popular Reads & Curated Picks")
    st.write("A hand-picked mix of student favourites, contemporary reads and classics.")
    st.warning("These are editorial demo picks, not actual bestseller rankings or sales statistics.")
    selected = [title for title, item in books.items() if item["popular"]]
    render_book_grid(selected)

elif page == "Authors":
    st.title("Author Directory")
    st.write("Explore Indian and international writers represented in the catalogue.")
    author_list = sorted(set(item["author"] for item in books.values()))
    chosen_author = st.selectbox("Choose an author to view their profile", author_list)
    titles = author_books(chosen_author)
    photo_path = AUTHOR_IMAGES.get(chosen_author)
    profile_left, profile_right = st.columns([1, 3], gap="large")
    with profile_left:
        if photo_path and photo_path.is_file():
            st.image(str(photo_path), caption=chosen_author, use_container_width=True)
        else:
            st.markdown(
                '<div class="book-placeholder" style="padding:28px 8px">'
                '<div style="font-size:34px">👤</div><b>Portrait unavailable</b></div>',
                unsafe_allow_html=True,
            )
    with profile_right:
        st.markdown(f"### {chosen_author}")
        st.write(f"{len(titles)} title(s) currently listed in this demo catalogue.")
        if chosen_author in {"R. K. Narayan", "Arundhati Roy", "Jhumpa Lahiri", "Amish Tripathi", "Chitra Banerjee Divakaruni", "Khushwant Singh", "Aravind Adiga", "Salman Rushdie", "A. P. J. Abdul Kalam and Arun Tiwari"}:
            st.caption("Indian author / India-focused writing")
        else:
            st.caption("International author or co-author")
    st.subheader("Books in the catalogue")
    render_book_grid(titles, columns=3)

elif page == "Semester Bundle Builder":
    st.title("Semester Bundle Builder")
    st.write("Choose books for your course bundle and see an estimated total. This is a planning tool; it does not verify your official syllabus.")
    bundle_genres = st.multiselect("Filter books by subject", sorted(set(item["category"] for item in books.values())), default=["Business", "Finance & Analytics"])
    eligible = [title for title, item in books.items() if not bundle_genres or item["category"] in bundle_genres]
    selected_bundle = st.multiselect("Select books for your bundle", eligible, default=[t for t in ["Introduction to Business", "Business Statistics", "Financial Accounting"] if t in eligible])
    bundle_subtotal = sum(books[title]["price"] for title in selected_bundle)
    bundle_discount = 10 if len(selected_bundle) >= 3 else 0
    savings = bundle_subtotal * bundle_discount / 100
    total = bundle_subtotal - savings
    c1, c2, c3 = st.columns(3)
    c1.metric("Selected books", len(selected_bundle))
    c2.metric("Bundle subtotal", money(bundle_subtotal))
    c3.metric("Estimated total", money(total))
    if bundle_discount: st.success("A demo 10% bundle discount is applied for selecting 3 or more books.")
    else: st.caption("Select at least 3 books to unlock the demo bundle discount.")
    if selected_bundle:
        st.subheader("Your bundle")
        for title in selected_bundle: st.write(f"• {title} — {money(books[title]['price'])}")
    if st.button("Add selected bundle to cart", type="primary", disabled=not selected_bundle):
        for title in selected_bundle: add_book(title)
        st.success(f"Added {len(selected_bundle)} selected title(s) to your cart. The bundle discount is an estimate and is not automatically applied at checkout.")

elif page == "Library Mode":
    st.title("Library Mode: Buy, Borrow or Rent")
    st.write("Choose an option for each book. Rentals and borrowing requests are demo features; real inventory and due dates are not connected.")
    mode = st.radio("Show options for", ["All options", "Buying", "Borrowing information", "Rental information"], horizontal=True)
    query = st.text_input("Find a title", placeholder="Search by title or author")
    for title, item in books.items():
        if query.lower() not in (title + " " + item["author"]).lower():
            continue
        rental_price = max(1, round(item["price"] * 0.22))
        if mode == "Buying":
            st.write(f"**{title}** — Buy: {money(item['price'])}")
        elif mode == "Borrowing information":
            st.write(f"**{title}** — " + ("Borrowing may be available in a participating campus library; this demo can record a request but cannot confirm availability." if item["borrow_available"] else "Borrowing is not listed for this title. Check your campus library catalogue."))
        elif mode == "Rental information":
            st.write(f"**{title}** — Demo rental price: {money(rental_price)} for a short rental period.")
        else:
            st.markdown(f"**{title}** · By {item['author']}")
            st.write(f"Buy: {money(item['price'])} · Rent (demo): {money(rental_price)}")
            st.caption("Borrowing requests are saved for this session only and are not sent to a real library.")
        action = st.selectbox(f"Choose an option for {title}", ["Buy", "Rent", "Borrow"], key=f"action_{title}")
        if st.button(f"Confirm {action} — {title}", key=f"confirm_{title}"):
            if action == "Buy":
                add_book(title)
                st.success(f"{title} added to your purchase cart.")
            elif action == "Rent":
                st.session_state.rental_cart[title] = st.session_state.rental_cart.get(title, 0) + 1
                st.success(f"{title} added to your rental cart at {money(rental_price)} per copy.")
            else:
                if not item["borrow_available"]:
                    st.warning("Borrowing is not listed for this title. Please check your campus library catalogue.")
                else:
                    request = {"title": title, "author": item["author"], "requested_at": datetime.now().strftime("%d %b %Y, %I:%M %p")}
                    if not any(r["title"] == title for r in st.session_state.borrow_requests):
                        st.session_state.borrow_requests.append(request)
                    st.success(f"Demo borrowing request recorded for {title}. No payment was taken.")
        st.divider()

    if st.session_state.borrow_requests:
        st.subheader("Your demo borrowing requests")
        for request in st.session_state.borrow_requests:
            st.write(f"📚 **{request['title']}** — request recorded {request['requested_at']}")
        st.caption("These requests are stored only for this running session; they are not sent to a real library.")

elif page == "Campus Book Exchange":
    st.title("Campus Book Exchange")
    st.write("A concept for students to discover second-hand books. The listings below are sample demo listings, not real offers from students.")
    st.info("No student accounts, messaging, payments or live listing database are connected.")
    for i, listing in enumerate(EXCHANGE_LISTINGS):
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(listing["title"])
                st.caption(f"{listing['condition']} condition · Listed by {listing['seller']}")
                st.write(listing["note"])
            with col2:
                st.metric("Demo price", money(listing["price"]))
                if st.button("Register interest", key=f"exchange_{i}"):
                    interest = listing["title"]
                    if interest not in st.session_state.exchange_interest: st.session_state.exchange_interest.append(interest)
                    st.success("Interest noted for this session only.")
    st.subheader("Your demo interests")
    if st.session_state.exchange_interest: st.write(", ".join(st.session_state.exchange_interest))
    else: st.caption("You have not registered interest in a sample listing this session.")

elif page == "Shopping Cart":
    st.title("Your shopping cart")
    if not (st.session_state.cart or st.session_state.rental_cart):
        st.info("Your cart is empty. Browse books or open Library Mode to buy or rent a title.")
    else:
        subtotal = 0
        if st.session_state.cart:
            st.subheader("Books to buy")
            for name in list(st.session_state.cart.keys()):
                if name not in books:
                    del st.session_state.cart[name]
                    continue
                price = books[name]["price"]
                c1, c2, c3 = st.columns([4, 2, 1])
                with c1:
                    st.write(f"**{name}**")
                    st.caption(f"Purchase · {money(price)} each")
                with c2:
                    qty = st.number_input("Quantity", min_value=1, max_value=20, value=int(st.session_state.cart[name]), step=1, key="qty_" + name)
                    st.session_state.cart[name] = qty
                with c3:
                    if st.button("Remove", key="remove_" + name):
                        del st.session_state.cart[name]
                        st.rerun()
                subtotal += price * st.session_state.cart[name]
                st.divider()
        if st.session_state.rental_cart:
            st.subheader("Books to rent")
            for name in list(st.session_state.rental_cart.keys()):
                if name not in books:
                    del st.session_state.rental_cart[name]
                    continue
                price = max(1, round(books[name]["price"] * 0.22))
                c1, c2, c3 = st.columns([4, 2, 1])
                with c1:
                    st.write(f"**{name}**")
                    st.caption(f"Demo rental · {money(price)} per copy")
                with c2:
                    qty = st.number_input("Rental quantity", min_value=1, max_value=20, value=int(st.session_state.rental_cart[name]), step=1, key="rent_qty_" + name)
                    st.session_state.rental_cart[name] = qty
                with c3:
                    if st.button("Remove rental", key="remove_rent_" + name):
                        del st.session_state.rental_cart[name]
                        st.rerun()
                subtotal += price * st.session_state.rental_cart[name]
                st.divider()
        st.metric("Cart subtotal (buying + rentals)", money(subtotal))
        if st.session_state.borrow_requests:
            st.caption(f"{len(st.session_state.borrow_requests)} demo borrowing request(s) recorded. Borrowing requests are not charged.")
        if st.button("Clear cart"):
            st.session_state.cart = {}
            st.session_state.rental_cart = {}
            st.rerun()

elif page == "Offers & Student Zone":
    st.title("Offers & Student Zone")
    st.write("Student-friendly savings for your next study session.")
    c1, c2 = st.columns(2)
    with c1: st.markdown('<div class="book-card"><p class="eyebrow">STUDENT PERK</p><h2>Extra 5% off</h2><p>Apply the student discount at checkout.</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="book-card"><p class="eyebrow">BOOK LOVER OFFER</p><h2>READ10</h2><p>Use READ10 for 10% off the book subtotal.</p></div>', unsafe_allow_html=True)
    st.subheader("Available coupon codes")
    st.code("READ10  —  10% off books\nWELCOME5  —  5% off books")
    st.caption("Coupon and student discounts combine up to 15% in this demo.")

elif page == "Checkout":
    from io import BytesIO
    from datetime import datetime
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

    st.title("Checkout")
    if not (st.session_state.cart or st.session_state.rental_cart):
        st.info("Your cart is empty. Add books to buy or rent before checking out. Borrowing requests do not have a charge.")
    else:
        purchase_subtotal = sum(books[name]["price"] * quantity for name, quantity in st.session_state.cart.items() if name in books)
        rental_subtotal = sum(max(1, round(books[name]["price"] * 0.22)) * quantity for name, quantity in st.session_state.rental_cart.items() if name in books)
        subtotal = purchase_subtotal + rental_subtotal
        st.subheader("Order summary")
        for name, quantity in st.session_state.cart.items():
            if name in books:
                st.write(f"**Buy:** {name} × {quantity} — {money(books[name]['price'] * quantity)}")
        for name, quantity in st.session_state.rental_cart.items():
            if name in books:
                rental_price = max(1, round(books[name]["price"] * 0.22))
                st.write(f"**Rent (demo):** {name} × {quantity} — {money(rental_price * quantity)}")
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

        if st.button("Create PDF invoice", type="primary"):
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=42)
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name="InvoiceBrand", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=colors.HexColor("#5b1d3b"), alignment=TA_CENTER, spaceAfter=5))
            styles.add(ParagraphStyle(name="InvoiceSub", parent=styles["Normal"], fontSize=9, textColor=colors.HexColor("#6b6065"), alignment=TA_CENTER, spaceAfter=16))
            styles.add(ParagraphStyle(name="SmallNote", parent=styles["Normal"], fontSize=8, textColor=colors.HexColor("#6b6065"), leading=11))
            story = [
                Paragraph("THE SCHOLAR’S SHELF", styles["InvoiceBrand"]),
                Paragraph("BOOKS • IDEAS • BRIGHTER TOMORROWS", styles["InvoiceSub"]),
                Paragraph("DEMO INVOICE", styles["Heading1"]),
                Spacer(1, 5),
                Paragraph(f"<b>Invoice reference:</b> SS-{datetime.now().strftime('%Y%m%d-%H%M%S')}", styles["Normal"]),
                Paragraph(f"<b>Date:</b> {datetime.now().strftime('%d %B %Y, %I:%M %p')}", styles["Normal"]),
                Paragraph(f"<b>Customer:</b> {(customer_name.strip() or 'Not provided').replace('&', '&amp;')}", styles["Normal"]),
                Spacer(1, 18),
            ]
            rows = [["Book title", "Qty", "Unit price", "Line total"]]
            for name, quantity in st.session_state.cart.items():
                if name in books:
                    unit_price = books[name]["price"]
                    rows.append([Paragraph(("Buy: " + name).replace("&", "&amp;"), styles["Normal"]), str(quantity), money(unit_price), money(unit_price * quantity)])
            for name, quantity in st.session_state.rental_cart.items():
                if name in books:
                    unit_price = max(1, round(books[name]["price"] * 0.22))
                    rows.append([Paragraph(("Rent (demo): " + name).replace("&", "&amp;"), styles["Normal"]), str(quantity), money(unit_price), money(unit_price * quantity)])
            table = Table(rows, colWidths=[245, 42, 85, 95], repeatRows=1)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#5b1d3b")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#e4d6de")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#fff8f2")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]))
            story.extend([table, Spacer(1, 18)])
            totals = [["Subtotal", money(subtotal)], [f"Discount ({rate}%)", "-" + money(discount)], ["Delivery", money(delivery_charge)], ["Gift wrapping", money(gift_charge)], ["ESTIMATED TOTAL", money(total)]]
            totals_table = Table(totals, colWidths=[360, 107], hAlign="RIGHT")
            totals_table.setStyle(TableStyle([
                ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                ("FONTNAME", (0, 0), (-1, -2), "Helvetica"),
                ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("TEXTCOLOR", (0, -1), (-1, -1), colors.HexColor("#5b1d3b")),
                ("LINEABOVE", (0, -1), (-1, -1), 1, colors.HexColor("#5b1d3b")),
                ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]))
            story.extend([totals_table, Spacer(1, 22), Paragraph("<b>Demo only:</b> This invoice is generated for demonstration purposes. No payment has been taken, and this is not a GST tax invoice or proof of payment.", styles["SmallNote"]), Spacer(1, 5), Paragraph("Thank you for visiting The Scholar’s Shelf!", styles["SmallNote"])])
            doc.build(story)
            st.success("Your PDF demo invoice is ready. No payment has been taken.")
            st.download_button("Download PDF invoice", data=buffer.getvalue(), file_name="scholars_shelf_demo_invoice.pdf", mime="application/pdf", type="primary")

elif page == "Wishlist":
    st.title("Your wishlist")
    if not st.session_state.wishlist: st.info("Your wishlist is empty. Save books from Browse Books.")
    for name in list(st.session_state.wishlist):
        if name not in books: continue
        c1, c2, c3 = st.columns([4, 1, 1])
        with c1: st.write(f"**{name}** — {money(books[name]['price'])}"); st.caption(books[name]["author"])
        with c2:
            if st.button("Add to cart", key="wishlist_add_" + name):
                add_book(name); st.toast(f"Added {name} to cart")
        with c3:
            if st.button("Remove", key="wishlist_remove_" + name):
                st.session_state.wishlist.remove(name); st.rerun()

elif page == "About Us":
    st.markdown('<p class="eyebrow">OUR STORY</p>', unsafe_allow_html=True)
    st.title("About The Scholar’s Shelf")
    st.markdown("### Books for curious minds, brighter tomorrows.")
    about_left, about_right = st.columns([1.05, 1])
    with about_left:
        st.write("The Scholar’s Shelf is a student-focused bookstore concept built to make learning simple, accessible and inspiring. It brings together coursework essentials, novels, Indian writing, classics, biographies, finance, technology and more.")
        st.write("The catalogue, prices, popular picks, exchange listings and library estimates are illustrative educational demo data.")
        st.markdown("**Books • Ideas • Brighter Tomorrows**")
    with about_right:
        if HERO_IMAGE.is_file(): st.image(str(HERO_IMAGE), use_container_width=True)
    st.divider()
    f1, f2, f3, f4 = st.columns(4)
    f1.metric("60", "Catalogue titles"); f2.metric("12+", "Genres"); f3.metric("Student-first", "Approach"); f4.metric("Demo", "Store status")
    st.info("No real payments, deliveries, library reservations or exchange transactions are processed. Cart and wishlist data are session-based.")
    st.caption("Built with Python and Streamlit as a learning project.")

st.sidebar.divider()
st.sidebar.caption("Made for learning • The Scholar’s Shelf")

# Page navigation
st.divider()

current_index = page_order.index(page)
previous_col, page_col, next_col = st.columns([1, 2, 1])

with previous_col:
    if current_index > 0:
        st.button(
            "← Previous",
            use_container_width=True,
            on_click=lambda: st.session_state.update(
                nav_choice=page_order[current_index - 1]
            ),
        )

with page_col:
    st.markdown(
        f"<div style='text-align:center;padding-top:8px'>"
        f"Page {current_index + 1} of {len(page_order)}"
        f"</div>",
        unsafe_allow_html=True,
    )

with next_col:
    if current_index < len(page_order) - 1:
        st.button(
            "Next →",
            use_container_width=True,
            on_click=lambda: st.session_state.update(
                nav_choice=page_order[current_index + 1]
            ),
        )

