# 🚕 Dynamic Ride Pricing API

This Django application calculates ride prices dynamically based on configurable parameters like distance, ride time, waiting time, day of the week, and time-based pricing multipliers.

---

## 📦 Features

- 🧮 Price calculation based on real-time input
- 🗓️ Different pricing per day of the week
- ⏱️ Waiting time charges after a free threshold
- ⌚ Time-of-day ride multipliers
- 📊 Admin interface for managing pricing rules
- 📚 Change logs for pricing updates
- 🧪 Test cases included

---

## ⚙️ Setup Instructions


1. Clone the Repository

```bash
git clone https://github.com/nd-09/pricing_app.git
cd pricing_app

2. Create a Virtual Environment

python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

If requirements.txt does not exist yet, you can generate it with:  pip freeze > requirements.txt


4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser
python manage.py createsuperuser

6. Run the Server
python manage.py runserver



Visit the admin panel at:
📍 http://127.0.0.1:8000/admin/




📡 API Endpoint
➕ POST /api/calculate-price/

Request Body:  {
  "day": "tue",
  "distance": 10.5,
  "ride_time": 75,
  "waiting_time": 10
}

Response Example: 
{
  "price": 322.5,
  "details": {
    "distance_cost": 125.0,
    "time_cost": 150.0,
    "waiting_cost": 47.5
  }
}



🧾 Admin Panel: How to Configure Pricing

Visit /admin/ and: 
1.  Add a PricingConfig with:

-> Base distance and price

-> Additional price per km

-> Waiting charge per 3 mins

-> JSON for time_multipliers, e.g.: [
  { "upto_min": 30, "factor": 1.0 },
  { "upto_min": 60, "factor": 1.5 },
  { "upto_min": 120, "factor": 2.0 }
]

2. Ensure the config is marked active and days are set as comma-separated values like: mon,tue,wed



🧪 Running Tests
python manage.py test pricing.tests.test_pricing -v 2
Test cases are located in:
📁 pricing/tests/test_pricing.py


🗂️ Project Structure
pricing_project/
├── pricing_app/             # Django project settings
├── pricing/                 # Core app with models, views, services
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   ├── urls.py
│   └── tests/
│       └── test_pricing.py
├── db.sqlite3
├── manage.py
└── README.md

👨‍💻 Author
Built by Navdeep Chovatiya(http://www.linkedin.com/in/navdeep-chovatiya-73349222a)
Feel free to reach out or contribute via issues or PRs!



























