
# ZeuxAI - openAI but it's actually open!
<p align="right">
  <img align="right" height="140" src="https://github.com/user-attachments/assets/6568e108-057d-49e5-873c-920f995bb4eb" alt="zeuxAI Logo" style="float: right; border-radius: 10px;"/>
</p>



ZeuxAI is a powerful and flexible AI chatbot that allows you to fine-tune its behavior and responses. Whether you need a fully static assistant, a dynamic conversational AI, or something in between, ZeuxAI gives you full control over its temperature settings and even lets you train your own LLMs!

## Features
- **Static Mode**: Provides deterministic responses with no randomness. (coming soon)
- **Half-Static Mode**: Maintains a balance between consistency and creativity. (coming soon)
- **Non-Static Mode**: Offers highly dynamic and creative responses. (coming soon)
- **Train Your Own AI**: ZeuxAI supports fine-tuning and training your own large language models (LLMs)!
- **Customizable Personality**: Modify ZeuxAI's tone, style, and response behavior.
- **Self-Learning Capabilities**: Train ZeuxAI with your own data for better domain-specific accuracy.

## AI Temperature Explained
ZeuxAI operates based on the **temperature** parameter, which controls the randomness of responses:
- **Static (temperature = 0.0)**: The AI always provides the same answer to a given prompt.
- **Half-Static (temperature = 0.3 - 0.5)**: A mix of structured responses with slight variations.
- **Non-Static (temperature = 0.7 - 1.0)**: More randomness and creativity, ideal for storytelling and brainstorming.

## How to Train Your Own LLM
Want to create your own AI model? ZeuxAI makes it possible!
1. Gather and preprocess your dataset.
2. Use ZeuxAI’s fine-tuning tools to train a new model.
3. Deploy your trained model and integrate it with ZeuxAI.
4. Adjust temperature settings to optimize responses.

## Installation
```
git clone https://github.com/yourusername/zeuxAI
cd zeuxAI
python main.py
```
## Usage

Run ZeuxAI in interactive mode:

python main.py

Adjust temperature settings:

zeuxai.set_temperature(0.5)  # Half-static mode (coming soon)

## Contribute

We welcome contributions! Feel free to fork the repo, create pull requests, or suggest improvements.

## License

ZeuxAI is open-source and available under the MIT License.
