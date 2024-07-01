from transformers import pipeline, Conversation
import gradio as gr
chatbot = pipeline(model="facebook/blenderbot-400M-distill")

message_list = []
response_list = []

def DS_chatbot(message, history):
    conversation = chatbot(message)
    
    return conversation[0]['generated_text']

demo_chatbot = gr.ChatInterface(DS_chatbot, title="DS Chatbot", description="Enter text to start chatting.")

demo_chatbot.launch()
