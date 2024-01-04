# AI Art Critic

AI Art Critic is an innovative web-based platform that uses OpenAI's GPT model to analyze and critique artworks. It's aimed at artists, art students, and enthusiasts who seek insightful feedback on artworks, spanning various styles and periods.

## Features

- Artwork Analysis: Users upload images of artworks, and the AI provides an in-depth analysis considering composition, style, color usage, and historical context.
- Comparative Study: The AI compares the submitted artwork with historically significant pieces to offer a comparative study.
- Style Evolution Insights: For artists uploading multiple pieces, the AI analyzes and comments on the evolution of their style over time.
- Interactive Learning Modules: Educational content on art history, styles, and techniques, personalized based on user interests.
- Community Gallery and Discussions: A platform for users to share their art, receive critiques from peers, and engage in art-related discussions.

## Tech Stack

- Front-End: HTML, CSS, JavaScript (React.js or Vue.js).
- Back-End: Python Flask or Node.js with Express.
- Image Processing: Python libraries like OpenCV or PIL.
- Database: PostgreSQL or MongoDB.
- Hosting/Deployment: AWS, Google Cloud, or Heroku.

## Installation

1. Clone the repository
```
git clone https://github.com/yourusername/ai-art-critic.git
```
2. Install Python dependencies
```
pip install -r requirements.txt
```
3. Install JavaScript dependencies
```
npm install
```
4. Start the server
```
npm start
```

## Usage

- Visit the homepage at `localhost:5000/`.
- Upload an image for analysis at `localhost:5000/upload`.
- Compare two images at `localhost:5000/compare`.
- View a user's profile at `localhost:5000/user/<username>`.

## Testing

Run the test script with:
```
npm test
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[ISC](https://choosealicense.com/licenses/isc/)
