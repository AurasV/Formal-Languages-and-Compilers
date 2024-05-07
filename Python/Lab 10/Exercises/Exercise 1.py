class DFA:
    def __init__(self):
        self.states = ['A', 'B']
        self.start_state = 'A'
        self.accept_state = 'B'
        self.current_state = self.start_state

    def transition(self, character):
        if self.current_state == 'A' and character == '1':
            self.current_state = 'B'
        elif self.current_state == 'B' and character == '1':
            self.current_state = 'B'
        else:
            self.current_state = 'reject'

    def is_accepting(self):
        return self.current_state == self.accept_state

    def process_input(self, input_string):
        self.current_state = self.start_state
        for char in input_string:
            self.transition(char)
            if self.current_state == 'reject':
                return False
        return self.is_accepting()


dfa = DFA()
print("111 result:", dfa.process_input("111"))
print("11 result:", dfa.process_input("11"))
print("011 result:", dfa.process_input("011"))
print("110 result:", dfa.process_input("110"))
