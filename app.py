import streamlit as st
from user import Donor, Volunteer, NGO
from donation import FoodDonation
from database import add_donation, get_all_donations, initialize_db
from auth import login_user, register_user
from payment import process_donation_payment

# ----------------- Page Config -----------------
st.set_page_config(page_title="DastarkhwanPlanner", layout="wide")

# ----------------- Database Initialization -----------------
initialize_db()

# ----------------- UI Components by Role -----------------
class DonorUI:
    def __init__(self, user_obj):
        self.user = user_obj

    def render(self):
        st.markdown("### 🍲 Donate Leftover Food")
        food_items = st.text_input("Food Items (e.g., Rice, Curry)")
        quantity = st.number_input("Quantity (e.g., plates)", min_value=1, step=1)
        expiry_time = st.time_input("Expiry Time")
        location = st.text_input("Pickup Location")
        amount = st.number_input("Optional Donation to NGO (Rs.)", min_value=0)

        if st.button("Donate Food"):
            donation = FoodDonation(self.user.username, food_items, quantity, str(expiry_time), location)
            add_donation(donation.to_dict())
            msg = process_donation_payment(self.user.username, amount)
            st.success(f"✅ Food Donation Recorded!\n💳 {msg}")


class VolunteerUI:
    def render(self):
        st.markdown("### 📦 Available Donations")
        donations = get_all_donations()
        found_pending = False
        for i, d in enumerate(donations):
            if d["status"] == "Pending":
                found_pending = True
                with st.expander(f"Donation #{i+1} from {d['donor']}"):
                    st.write(f"🍴 **Items:** {d['food_items']}")
                    st.write(f"📍 **Location:** {d['location']}")
                    st.write(f"🕓 **Expiry:** {d['expiry_time']}")
                    st.write(f"📦 **Quantity:** {d['quantity']}")
                    st.write(f"🚚 **Status:** {d['status']}")
        if not found_pending:
            st.info("No pending donations currently available.")


class NGOUI:
    def render(self):
        st.markdown("### 🧾 All Donations")
        donations = get_all_donations()
        if donations:
            for i, d in enumerate(donations):
                with st.expander(f"Donation #{i+1} by {d['donor']}"):
                    st.write(d)
        else:
            st.info("No donations found.")


# ----------------- Main App Controller -----------------
class DastarkhwanApp:
    def __init__(self):
        self.username = None
        self.role = None
        self.option = None
        self.user_obj = None

    def setup_ui(self):
        col1, col2 = st.columns([1, 6])
        with col1:
            st.image("Images/logo.png", width=100)
        with col2:
            st.markdown("""
                <h1 style='margin-bottom:0; color:#2E8B57;'>DastarkhwanPlanner</h1>
                <h4 style='margin-top:0; color:gray;'>🍛 Feed with Dignity – A Platform for Donors, Volunteers & NGOs</h4>
            """, unsafe_allow_html=True)
        st.markdown("---")

    def handle_sidebar(self):
        st.sidebar.header("🔐 Login/Register")
        self.username = st.sidebar.text_input("Enter Email")
        self.role = st.sidebar.selectbox("Select Role", ["Donor", "Volunteer", "NGO"])
        self.option = st.sidebar.radio("Login/Register", ["Login", "Register"])

        if 'is_logged_in' not in st.session_state:
            st.session_state['is_logged_in'] = False

        if self.username:
            if self.option == "Register":
                if register_user(self.username, self.role):
                    st.sidebar.success("✅ Registered successfully! Please login.")
                else:
                    st.sidebar.warning("⚠️ User already exists.")
            elif self.option == "Login":
                user_data = login_user(self.username)
                if user_data:
                    st.sidebar.success(f"✅ Logged in as {user_data['role']}")
                    st.session_state['is_logged_in'] = True
                    self.set_user_object(user_data['role'])
                else:
                    st.sidebar.error("❌ User not found. Please register first.")

    def set_user_object(self, role):
        if role == "Donor":
            self.user_obj = Donor(self.username)
        elif role == "Volunteer":
            self.user_obj = Volunteer(self.username)
        elif role == "NGO":
            self.user_obj = NGO(self.username)

    def show_intro(self):
         if not st.session_state['is_logged_in']:
             
            st.markdown("""
        <div style='margin-top:20px;'>
            <h3 style='color:#2E8B57; font-weight: 700;'>What is DastarkhwanPlanner?</h3>
            <p style='font-size:16px; line-height:1.8; color:#333;'>
                <strong>DastarkhwanPlanner</strong> is a mission-driven platform dedicated to alleviating food insecurity by seamlessly connecting those with surplus food to individuals and communities in need. Our initiative fosters collaboration among donors, volunteers, and NGOs to ensure that no edible food is wasted and no one goes hungry.
            </p>
            <p style='font-size:16px; line-height:1.8; color:#333;'>
                Leveraging intelligent logistics and community coordination, we facilitate the safe and timely collection and distribution of leftover meals from households, restaurants, caterers, and events. Our platform streamlines the donation process from initial entry to delivery confirmation, emphasizing full transparency and accountability.
            </p>
            <p style='font-size:16px; line-height:1.8; color:#333;'>
                Volunteers are essential in bridging the last mile. Through DastarkhwanPlanner, they receive notifications about nearby donations, are provided with efficient route guidance, and supported by NGOs that oversee and validate all transactions. This guarantees food reaches those in need while maintaining hygiene, safety, and dignity.
            </p>
            <p style='font-size:16px; line-height:1.8; color:#333;'>
                NGOs benefit from a centralized dashboard offering insights into community needs, donation flows, and volunteer engagement. This data-driven approach helps optimize their impact, reduce overlap, and serve communities more effectively.
            </p>
            <p style='font-size:16px; line-height:1.8; color:#333;'>
                Our mission transcends nourishment — we strive to cultivate a culture of empathy, shared responsibility, and sustainable giving. Every donation, regardless of size, contributes to a ripple effect of kindness and solidarity.
            </p>
            <p style='font-size:16px; line-height:1.8; color:#333;'>
                Currently operational in select regions, we are actively working towards nationwide expansion by partnering with local governments, food chains, and community organizations. With your support, we envision a future where food is wisely shared, not wasted.
            </p>
            <p style='font-size:16px; line-height:1.8; color:#333;'>
                Join us in transforming compassion into action. Whether one meal or many, together we nourish more than bodies — we nourish hope, dignity, and humanity.
            </p>
            <p style='font-size:16px; line-height:1.8; font-style: italic; color:#444; margin-top: 15px;'>
                #NourishWithDignity &nbsp;&nbsp;|&nbsp;&nbsp; #NoFoodWasted &nbsp;&nbsp;|&nbsp;&nbsp; #ServeHumanity
            </p>
            <p style='font-size:17px; font-family: monospace; color:#2E8B57; font-weight: 600; margin-top: 10px;'>
                <strong>#YourFoodTheirHope</strong> &nbsp;&nbsp;|&nbsp;&nbsp; <strong style="color:#2E8B57;">#ShareToCare</strong> &nbsp;&nbsp;|&nbsp;&nbsp; <strong style="color:#2E8B57;">#FeedTheFuture</strong> &nbsp;&nbsp;|&nbsp;&nbsp; <strong style="color:#2E8B57;">#TogetherWeNourish</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)
        

    def route_user(self):
        if self.user_obj:
            st.markdown(f"""
                <h2>👋 Welcome, <a href='mailto:{self.user_obj.username}'>{self.user_obj.username}</a></h2>
                <h3 style='color:#444;'>Role: {self.user_obj.role}</h3>
            """, unsafe_allow_html=True)

            if self.user_obj.role == "Donor":
                DonorUI(self.user_obj).render()
            elif self.user_obj.role == "Volunteer":
                VolunteerUI().render()
            elif self.user_obj.role == "NGO":
                NGOUI().render()
        else:
            self.show_intro()

    def run(self):
        self.setup_ui()
        self.handle_sidebar()
        self.route_user()
        self.render_footer()

    def render_footer(self):
        st.markdown("""
            <style>
                .footer {
                    background-color: #f9f9f9;
                    padding: 30px 20px;
                    border-top: 1px solid #e0e0e0;
                    text-align: center;
                    font-size: 15px;
                    color: #444;
                }
                .footer .links a {
                    margin: 0 10px;
                    color: #2e7d32;
                    text-decoration: none;
                    font-weight: 500;
                }
            </style>
            <footer>
                <div class="footer">
                    <div>Made with ❤️ by <strong>Saba Junaid</strong> — Feed with Dignity</div>
                    <div class="links" style="margin-top: 10px;">
                        <a href="#">Contact Us</a> |
                        <a href="#">Privacy Policy</a> |
                        <a href="#">Terms of Service</a> |
                        <a href="#">Donate</a>
                    </div>
                </div>
            </footer>
        """, unsafe_allow_html=True)


# ----------------- Run App -----------------
if __name__ == "__main__":
    app = DastarkhwanApp()
    app.run()
