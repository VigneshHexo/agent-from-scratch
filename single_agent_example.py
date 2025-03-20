"""
Single Agent Example

This module demonstrates the implementation of a single agent system using the Agent and Swarm classes.
It creates a Weather Agent capable of providing weather information and sending emails.
The example runs an interactive loop where users can ask questions about the weather,
and the agent responds using its available functions.
"""

from dotenv import load_dotenv
_ = load_dotenv()

import json
from agent import pretty_print_messages, Agent, Swarm


def get_weather(location, time="now"):
    """
    Retrieve weather information for a specified location and time.
    
    Parameters:
        location (str): The location to get weather information for
        time (str, optional): The time for which to get the weather. Defaults to "now"
        
    Returns:
        str: JSON string containing location, temperature, and time information
    """
    return json.dumps({"location": location, "temperature": "65", "time": time})


def send_email(recipient, subject, body):
    """
    Simulate sending an email to a recipient with a subject and body.
    
    Parameters:
        recipient (str): Email address of the recipient
        subject (str): Subject line of the email
        body (str): Content of the email
        
    Returns:
        str: Confirmation message indicating the email was sent
    """
    return f"Sent! email to {recipient} with the subject: {subject} and body: {body}"


# Initialize a Weather Agent with specific instructions and functions
weather_agent = Agent(
    name="Weather Agent",
    instructions="You are a helpful agent for giving information on weather.",
    functions=[get_weather, send_email],
)

# Create a Swarm client to manage the agent interaction
client = Swarm()
print("Starting Single Agent - Weather Agent")
print('Ask me how is the weather today in Brussels?')

# Initialize conversation history
messages = []
agent = weather_agent

# Main interaction loop - continuously process user input and agent responses
while True:
    user_input = input("\033[90mUser\033[0m: ")
    messages.append({"role": "user", "content": user_input})

    # Run the agent with the current message history
    response = client.run(agent=agent, messages=messages)
    pretty_print_messages(response.messages)

    # Update conversation history and agent state
    messages.extend(response.messages)
    agent = response.agent