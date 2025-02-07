# Number Classification API

## 🌟 Features
- **Checks if a number is prime, perfect, Armstrong, and odd/even.**
- **Calculates the sum of digits.**
- **Fetches a fun fact from the Numbers API.**
- **Handles invalid inputs and returns appropriate errors.**

---

## 🚀 API Usage
### 📍 **Base URL**

### 📍 Endpoint
<GET /api/classify-number?number=<integer>```

### ✅ Success Response (200)
GET /api/classify-number?number=371```

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

❌ Error Response (400 Bad Request)
GET /api/classify-number?number=abc```

{
    "number": "alphabet",
    "error": true
}

## 🔧 Setup Instructions
### 1️⃣ Clone the Repository
git clone https://github.com/yourusername/number-classifier-api.git
cd number-classifier-api```

### 2️⃣ Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate```

### 3️⃣ Install Dependencies
pip install -r requirements.txt```

### 4️⃣ Run Migrations
python manage.py migrate```

### 5️⃣ Start the Server
python manage.py runserver```

### 6️⃣ Test the API
Open in your browser:
python manage.py runserver```

## 📜 License
This project is open-source and available under the MIT License.

