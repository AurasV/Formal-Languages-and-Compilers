class DFA:
    def __init__(self):
        self.current_state = 'A'  # Starting state

    def transition(self, character):
        if self.current_state == 'A':
            if character == '0':
                self.current_state = 'B'
            elif character == '1':
                self.current_state = 'reject'
        elif self.current_state == 'B':
            if character == '0':
                self.current_state = 'C'
            elif character == '1':
                self.current_state = 'reject'
        elif self.current_state == 'C':
            if character == '1':
                self.current_state = 'E'
            elif character == '0':
                self.current_state = 'D'
        elif self.current_state == 'D':
            if character == '0':
                self.current_state = 'F'
            elif character == '1':
                self.current_state = 'reject'
        elif self.current_state == 'E':
            if character == '1':
                self.current_state = 'G'
            elif character == '0':
                self.current_state = 'reject'
        elif self.current_state == 'F':
            if character == '0':
                self.current_state = 'D'
            elif character == '1':
                self.current_state = 'E'
        elif self.current_state == 'G':
            if character == '1':
                self.current_state = 'G'
            elif character == '0':
                self.current_state = 'reject'

    def is_accepting(self):
        return self.current_state in {'E', 'G'}

    def process_input(self, input_string):
        self.current_state = 'A'
        for char in input_string:
            self.transition(char)
            if self.current_state == 'reject':
                return False
        return self.is_accepting()


dfa = DFA()
print("001 result:", dfa.process_input("001"))
print("00001 result:", dfa.process_input("00001"))
print("000 result:", dfa.process_input("000"))
print("01 result:", dfa.process_input("01"))
print("00010 result:", dfa.process_input("00010"))
