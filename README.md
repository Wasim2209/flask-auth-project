# 🔐 Flask + MySQL User Authentication Project

Ye project Flask aur MySQL ka use karke ek basic user authentication system banata hai jisme:

✅ Register  
✅ Login  
✅ OTP verification  
✅ Password Update  
✅ Session logout  
✅ User dashboard  
✅ 404 Page  
✅ HTML templates  
✅ Static files (CSS, JS, Images)

---

## 🛠 Technologies

- Python (Flask)
- MySQL
- HTML, CSS, JavaScript
- Jinja2 Templates

---

## 📁 Folder Structure

/project-root
├── app.py
├── templates/ --> All HTML files
├── static/ --> css/, js/, image/, upload/

---

## 🧪 How to Run

1. Python install karo (agar pehle se nahi hai)
2. Virtual environment banao (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  (Windows)

pip install flask flask-mysqldb

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(200),
    otp VARCHAR(10),
    verified BOOLEAN DEFAULT FALSE
);

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'auth_db'

python app.py

| File             | Use                      |
| ---------------- | ------------------------ |
| `login.html`     | User login page          |
| `register.html`  | New user registration    |
| `otp.html`       | OTP verification         |
| `updateotp.html` | Update OTP               |
| `userpage.html`  | Logged-in user dashboard |
| `page404.html`   | Custom 404 error page    |

Created by: Wasim Ahmed
GitHub: Wasim2209
