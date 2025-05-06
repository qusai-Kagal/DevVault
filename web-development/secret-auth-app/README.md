# 🔐 Secret Auth App

## 🌟 Overview
A secure authentication system built with Node.js, Express, and PostgreSQL, part of the DevVault web development collection. This application demonstrates secure user authentication, password encryption, and session management.

## ✨ Features
- 🔒 Secure local authentication with Passport.js
- 🛡️ Password hashing using bcrypt
- 👤 User registration and login system
- 🔄 Session persistence
- 🔐 Protected routes for authenticated users
- 📊 PostgreSQL data storage

## 🚀 Getting Started

### Prerequisites
- Node.js (v14+)
- PostgreSQL
- npm

### 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/qusai-Kagal/DevVault.git
cd DevVault/web-development/secret-auth-app
```

2. Install dependencies:
```bash
npm install
```

3. Set up your PostgreSQL database:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL
);
```

4. Create a `.env` file in the root directory:
```
# PostgreSQL Configuration
PG_USER=your_postgres_username
PG_HOST=localhost
PG_DATABASE=your_database_name
PG_PASSWORD=your_postgres_password
PG_PORT=5432

# Session Secret
SESSION_SECRET=your_session_secret
```

## 🏃‍♂️ Running the Application

```bash
# Start the server
node index.js
```

The application will be available at `http://localhost:3000`

## 📁 Project Structure

```
secret-auth-app/
├── index.js           # Main server file
├── package.json       # Dependencies
├── public/            # Static assets
│   └── css/
│       └── styles.css # Custom styling
└── views/             # EJS templates
    ├── home.ejs       # Landing page
    ├── login.ejs      # Login form
    ├── register.ejs   # Registration form
    ├── secrets.ejs    # Protected content
    └── partials/      # Reusable components
        ├── header.ejs # Page header
        └── footer.ejs # Page footer
```

## 💻 Tech Stack
- 🖥️ **Node.js** - JavaScript runtime
- 🛣️ **Express** - Web framework
- 🎨 **EJS** - Templating engine
- 🗄️ **PostgreSQL** - Database
- 🔐 **Passport.js** - Authentication middleware
- 🔄 **Express-session** - Session management
- 🔒 **Bcrypt** - Password hashing

## 🔒 Security Implementation
- Passwords are hashed using bcrypt with 10 salt rounds
- Session-based authentication with secure cookies
- Protected routes requiring authentication
- Environment variables for sensitive configuration

## 📝 Learning Outcomes
- Implementing secure authentication in Node.js applications
- Working with PostgreSQL databases in JavaScript
- Session management and protected routes
- Password security best practices

## 🤝 Contributing
This project is part of the DevVault collection. Contributions are welcome to improve the application or add new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👨‍💻 Author
Qusai Kagal - [GitHub Profile](https://github.com/qusai-Kagal)

---

⭐️ **Star this repo if you find it useful!** ⭐️
