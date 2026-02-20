# from webscout import PhindSearch as brain


# ai = brain(
#     is_conversation=True,
#     max_tokens=800,
#     timeout=30,
#     intro='J.A.R.V.I.S',
#     filepath=r"C:\Users\chatu\Desktop\J.A.R.V.I.S\chat_hystory.txt",
#     update_file=True,
#     proxies={},
#     history_offset=10250,
#     act=None,
# )

# def Main_Brain(text):
#     r = ai.chat(text)
#     return r 

from webscout import LLMChat
from os import getcwd

def Main_Brain(text):
    chat_history_path = f"{getcwd()}\\chat_hystory.txt"
    ai = LLMChat(is_conversation=True, filepath=chat_history_path)

    res = ai.chat(text) # internel stream is not available for this Privider

    return res

