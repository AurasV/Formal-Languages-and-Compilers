class DFA:
    def __init__(self):
        self.current_state = 'S0'

    def transition(self, input_char):
        if self.current_state == 'S0':
            if input_char == '0':
                self.current_state = 'S1'
            elif input_char == '1':
                self.current_state = 'reject'
        elif self.current_state == 'S1':
            if input_char == '1':
                self.current_state = 'S2'
            elif input_char == '0':
                self.current_state = 'reject'
        elif self.current_state == 'S2':
            if input_char == '0':
                self.current_state = 'S3'
            elif input_char == '1':
                self.current_state = 'reject'
        elif self.current_state == 'S3':
            if input_char == '0':
                self.current_state = 'S4'
            elif input_char == '1':
                self.current_state = 'reject'
        elif self.current_state == 'S4':
            if input_char == '0':
                self.current_state = 'S3'
            elif input_char == '1':
                self.current_state = 'S5'
        elif self.current_state == 'S5':
            if input_char == '1':
                self.current_state = 'S6'
            elif input_char == '0':
                self.current_state = 'reject'
        elif self.current_state == 'S6':
            if input_char == '1':
                self.current_state = 'S5'
            elif input_char == '0':
                self.current_state = 'S7'
        elif self.current_state == 'S7':
            if input_char == '0':
                self.current_state = 'S7'
            elif input_char == '1':
                self.current_state = 'reject'

    def is_accepting(self):
        return self.current_state == 'S7'

    def process_input(self, input_str):
        for char in input_str:
            self.transition(char)
        return self.is_accepting()


dfa = DFA()
input_str = "0100001100"
result = dfa.process_input(input_str)
print(f"'{input_str}' result -> {result}")
