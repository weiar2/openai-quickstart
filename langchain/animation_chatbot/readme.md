# Animation Search Chatbot

This project is an animation search chatbot built using Gradio and LangChain. The chatbot uses a vector store for retrieving relevant animations based on user queries.

## Requirements

- Python 3.10.14
- Gradio 4.39.0
- LangChain 0.2.11
- FAISS 1.8.0
- LangChain-OpenAI 0.1.7
- LangChain-Community 0.2.0

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/weiar2/openai-quickstart.git
    cd langchain/animation_chatbot
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Initialize the animation search bot and launch the Gradio interface:
    ```sh
    python animations_chatbot.py
    python animations_chatbot.py --enable_chat True # Enable chat mode
    ```

2. The Gradio interface will be available at `http://0.0.0.0:7860`. You can interact with the chatbot through this interface.

## Project Structure

- `animations_chatbot.py`: Main script to initialize and launch the chatbot.
- `requirements.txt`: List of dependencies required for the project.
- `utils.py`: Utility functions and classes (e.g., `ArgumentParser`).

## How It Works

1. **Initialization**:
    - The `initialize_animations_bot` function loads the FAISS vector store and sets up the LangChain RetrievalQA with a custom prompt template.

2. **Chat Function**:
    - The `animations_chat` function processes user messages, retrieves relevant animations, and returns the results.

3. **Gradio Interface**:
    - The `launch_gradio` function sets up and launches the Gradio interface for user interaction.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.