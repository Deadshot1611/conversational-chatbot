# Conversational Chatbot

This project is a Conversational Chatbot built using the Facebook/BlenderBot-400M-distill model from Hugging Face and the Transformers library. The bot can engage in natural conversations, providing users with information and assistance.

## Features

- Natural language understanding and generation
- Engages in conversations on a variety of topics
- Provides informative and contextually relevant responses
- Accessible via a user-friendly web interface

## Technologies Used

- **Model:** Facebook/BlenderBot-400M-distill
- **Framework:** Transformers
- **API Integration:** FastAPI
- **User Interface:** Gradio
- **Deployment:** Hugging Face Spaces

## Setup and Installation

1. **Clone the repository:**

    \`\`\`bash
    git clone https://github.com/yourusername/conversational-chatbot.git
    cd conversational-chatbot
    \`\`\`

2. **Install the required packages:**

    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

3. **Run the FastAPI server:**

    \`\`\`bash
    uvicorn main:app --reload
    \`\`\`

4. **Access the Gradio interface:**

    The Gradio interface will be available at `[http://localhost:8000](https://deadshot2003-fastapi-gradio.hf.space/gradio/)`.

## Usage

- Open the Gradio interface in your web browser.
- Type your message in the input box and hit enter.
- The chatbot will respond with contextually relevant replies.

## Deployment

The bot is deployed on Hugging Face Spaces. You can access it [here]([https://huggingface.co/spaces/yourusername/conversational-chatbot](https://deadshot2003-fastapi-gradio.hf.space/gradio/)).

## Contributing

Feel free to open issues or submit pull requests if you would like to contribute to the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
