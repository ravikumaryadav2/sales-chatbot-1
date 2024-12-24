# Sales Chatbot

This project is a sales chatbot for an e-commerce platform that provides users with an interactive interface to browse products and make inquiries. The application is divided into two main parts: the backend and the frontend.

## Project Structure

```
sales-chatbot
├── backend
│   ├── app.py                # Entry point for the backend application
│   ├── inventory.py          # Manages mock inventory data
│   ├── routes
│   │   └── chat.py           # API endpoints for the chatbot
│   └── requirements.txt       # Python dependencies for the backend
├── frontend
│   ├── public
│   │   └── index.html        # Main HTML file for the frontend
│   ├── src
│   │   ├── App.js            # Main React component
│   │   ├── components
│   │   │   └── Chatbot.js    # Chatbot component for user interactions
│   │   └── styles
│   │       └── App.css       # CSS styles for the frontend
│   ├── package.json          # Configuration file for npm
│   └── webpack.config.js      # Webpack configuration for bundling
└── README.md                 # Documentation for the project
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the backend application:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the frontend application:
   ```
   npm start
   ```

## Usage

Once both the backend and frontend are running, open your web browser and navigate to `http://localhost:3000` to interact with the sales chatbot. You can ask questions about products, and the chatbot will provide relevant information based on the mock inventory.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.