# TVT-News-Summary

## Overview
This project uses the OpenAI API to generate [Sparse Priming Representations (SPR)](https://www.youtube.com/watch?v=YjdmYCd6y0M) from YouTube video transcripts. The summary are generated by a Python script that communicates with the OpenAI API and Yooutube API.

## Prerequisites
- Python 3.8 or higher
- OpenAI API key 
- YouTube API key

## Server Setup
1. Navigate to the `server` directory.
2. Create a virtual environment by running `python -m venv venv`.
3. Activate the virtual environment by running `source venv/bin/activate` on Linux or `venv\Scripts\activate` on Windows.
4. Install the required Python packages by running `pip install -r requirements.txt`.
5. Set up your environment variables in a `.env` file in the `server` directory. You will need to include your OpenAI API key and YouTube API key.
6. Create a database by running `python create_db.py`.
7. Run `uvicorn main:app --reload` to start the server.

## Usage
1. Run `uvicorn main:app --reload` to start the server.
2. The server will automatically download YouTube video transcripts and generate Summary using the OpenAI API.
3. The generated Summary will be saved in the `server/core/transcripts` directory.

## Client Setup
1. Navigate to the `client` directory.
2. Install the required Node.js packages by running `npm install`.
3. Set up your environment variables in a `.env.local` file in the `client` directory.
4. Run `npm run build` to build the client application.
5. Run `npm start` to start the client application.

# Some additional informations
- The project work with a credentials.json file that you can get from the Google Cloud Console for the YouTube service. Example in ```server/core/credentials.json```.
- Another way will be to download the audio and extract the transcript using the Google Speech-to-Text API, but sometimes audio files can contains noise and the transcript can be wrong. So i prefere wait and trust the YouTube API with that.
- Create a issue if you have any problem with the project.

