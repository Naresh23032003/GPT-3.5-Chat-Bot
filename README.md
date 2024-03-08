# GPT 3.5 Chat-Bot
This project demonstrates a simple chat bot interface powered by OpenAI's GPT-3.5 model using Streamlit. Users can interact with the chat bot by typing their questions or messages, and the bot responds accordingly.

## How to Run

1. Install the required libraries by running:
`pip install -r requirements.txt`

2. Set up your OpenAI API key:
- Create a file named `.env` in the project root directory.
- Add your OpenAI API key to the `.env` file in the following format:
  ```
  OPENAI_API_KEY=your_openai_api_key_here
  ```

3. Run the Streamlit app:
`streamlit run app.py`

## Project Structure

- `app.py`: Contains the main code for the Streamlit application.
- `requirements.txt`: Lists the required Python libraries.
- `README.md`: Provides instructions for running the application and a brief overview of the project.

## Usage

- Users can type their questions or messages in the text input field.
- The chat bot, powered by GPT-3.5, generates responses based on user input.

## Memory Capability

The chat bot implemented in this project has memory capability, which means it can retain context from previous interactions within the same session. This allows for a more coherent conversation experience, as the bot can reference past messages when generating responses. The memory is maintained using the session state in the Streamlit application, ensuring that the conversation history remains accessible and relevant throughout the interaction.
