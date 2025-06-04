# JokeAPI-Express

A simple Express.js API for fetching, adding, updating, and deleting jokes. Supports filtering jokes by type and retrieving jokes by ID.

## 🚀 Features

✅ Fetch a random joke  
🔍 Retrieve jokes by ID or type  
➕ Add new jokes  
✏️ Update existing jokes (PUT & PATCH)  
❌ Delete specific or all jokes (with master key protection)

## 📦 Installation

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Setup
1. Clone the repository:
```bash
git clone <repository-url>
cd JokeAPI-Express
```

2. Install dependencies:
```bash
npm install
```

3. Start the server:
```bash
npm start
```

The server will start on `http://localhost:3000`

## 📚 API Documentation

### Get Random Joke
```http
GET /random
```

**Response:**
```json
{
  "id": 1,
  "jokeText": "Why don't scientists trust atoms? Because they make up everything.",
  "jokeType": "Science"
}
```

### Get Specific Joke
```http
GET /jokes/:id
```

**Example:**
```http
GET /jokes/1
```

### Filter Jokes by Type
```http
GET /filter?type=<jokeType>
```

**Available Types:** Science, Puns, Wordplay, Math, Food, Sports, Movies

**Example:**
```http
GET /filter?type=Science
```

### Add New Joke
```http
POST /jokes
```

**Request Body:**
```json
{
  "text": "Your joke here",
  "type": "Puns"
}
```

### Update Joke (Complete Replacement)
```http
PUT /jokes/:id
```

**Request Body:**
```json
{
  "text": "Updated joke text",
  "type": "Science"
}
```

### Update Joke (Partial Update)
```http
PATCH /jokes/:id
```

**Request Body:**
```json
{
  "text": "Updated joke text"
}
```

### Delete Specific Joke
```http
DELETE /jokes/:id
```

### Delete All Jokes
```http
DELETE /all?key=<masterKey>
```

**Note:** Requires master key for authorization.

## 🛠️ Technologies Used

- **Node.js** - Runtime environment
- **Express.js** - Web framework
- **body-parser** - Request parsing middleware

## 🔒 Security

- Master key protection for bulk deletion operations
- Input validation for joke creation and updates

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License.
