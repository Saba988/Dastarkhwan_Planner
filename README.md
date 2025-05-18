
# 🍛 DastarkhwanPlanner

**DastarkhwanPlanner** is a mission-driven web app that connects **Donors**, **Volunteers**, and **NGOs** to reduce food waste and provide meals to those in need — with dignity and transparency.

---

## 🚀 Overview

This platform facilitates food donations by enabling:
- **Donors** to share surplus food and optionally donate money.
- **Volunteers** to view and pick up pending food donations.
- **NGOs** to monitor and manage donation activities.

Built with [Streamlit](https://dastarkhwanplanner-sj.streamlit.app/), it provides a simple and elegant UI for real-time collaboration.The app is designed using Python OOP principles, organizing the core functionality — users, donations, and payments — into clear and maintainable classes.

---

## 🧰 Tech Stack

- **Frontend/UI**: Streamlit
- **Backend**: Python(with OOP design)
- **Database**: JSON-based local storage
- **Authentication**: Role-based user system
- **Payment**: Simulated monetary donations

---

## 👥 User Roles

### 👤 Donor
- Register/login using email.
- Submit food donation details (items, quantity, expiry, location).
- Optionally donate money to NGOs.

### 🤝 Volunteer
- View all **pending** food donations.
- Help pick up and deliver food.

### 🏢 NGO
- Access all donation data.
- Monitor donor activity and food flow.

---

## 📁 Project Structure

```
📦 DastarkhwanPlanner/
├── app.py              # Main Streamlit application
├── auth.py             # Login & Registration logic
├── database.py         # Data storage and operations
├── donation.py         # Donation object (class)
├── user.py             # Donor, Volunteer, NGO classes
├── payment.py          # Simulated payment processor
└── data/db.json        # JSON database
```

---

## 🔐 Authentication

- Managed via `auth.py`
- Users are registered and logged in using their email and a selected role.
- Simple role-based session state using Streamlit.

---

## 💾 Database

- JSON file (`data/db.json`) is used for persistent storage.
- Automatically created if it doesn’t exist.

**Schema:**
```json
{
  "users": [{"username": "test@example.com", "role": "Donor"}],
  "donations": [
    {
      "donor": "test@example.com",
      "food_items": "Rice, Curry",
      "quantity": 5,
      "expiry_time": "15:00:00",
      "location": "Downtown",
      "status": "Pending"
    }
  ]
}
```

---

## 💳 Payment Simulation

- Function: `process_donation_payment(username, amount)`
- Called when Donor submits food and a monetary donation.
- Simulated only — no real payment integration.

---

## 🧪 How to Run

1. **Clone the repo**:
```bash
git clone https://github.com/Saba988/Dastarkhwan_Planner.git
cd DastarkhwanPlanner
```

2. **Install requirements**:
```bash
pip install streamlit
```

3. **Start the app**:
```bash
streamlit run app.py
```

4. **Register users and start donating!**

---

## 🌱 Future Improvements

- Real payment gateway integration
- Volunteer route optimization with maps
- Email/password authentication
- Notifications for expiring food
- Admin analytics dashboard

---

## 🤝 Contributing

1. Fork this repo
2. Create a branch: `git checkout -b feature-name`
3. Make your changes
4. Push: `git push origin feature-name`
5. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## ✉️ Contact

For questions, reach out at: [dastarkhwan@example.com](mailto:dastarkhwan@example.com)

---

Made with ❤️ by Saba Junaid for a hunger-free world.
