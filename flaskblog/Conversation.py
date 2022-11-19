from nltk.chat.util import Chat,reflections

pairs =[
    ['(hi EcoClan|hello EcoClan)', ['Hey there what is your name?', 'Hi there what is your name? !']],
    [r'my name is (.*)', ['Hello ! %1']],
    ['(hi|hello|hey|holla|hola)', ['Hey there!', 'Hi there !', 'Hey !']],
    ['(.*) your name ?', ['My name is Eco clan Bot']],
    ['(.*) do you do ?', ['I am here to help you understand more about sustainable life style.']],
    ['(.*) created you ?', ['The Eco Clan Team created me.']],
    ['who|what are you ?', ['I am the Eco Clan Bot.']],
    ['how are you ?', ['I am doing great, how are you?']],
    ['I am fine|I am good|fine|good', ['Good to know!']],
    ['thanks', ['Your Welcome']],
    ['Ok|oh', ['yep']],
    ['(Are you a robot?)', ['Yes, I am a digital assistant named Eco Clan Bot.']],
    ['((.*) sustain?)', [' Sustainable living is based on four main pillars namely minimizing waste, limiting the use of Earth’s natural resources, the wise use of the environment, and ensuring quality working/living environments.']],
    ['(bye)', ['Bye!']],
]

def start_chat(user_input):
    chat=Chat(pairs,reflections)
    response=chat.converse(user_input)
    return response
