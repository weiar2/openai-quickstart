import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Animation Chatbot Argument Parser')
        self.parser.add_argument('--enable_chat', type=bool, default=False, help='Enable or disable chat functionality')
        self.parser.add_argument('--temperature', type=float, default=0.5, help='Set the temperature for the language model. Of enable_chat is set to False, this argument will be ignored.')

    def parse_arguments(self):
        args = self.parser.parse_args()
        if not args.enable_chat:
            args.temperature = 0
        return args
