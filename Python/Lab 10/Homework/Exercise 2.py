class DFA:
    def __init__(self):
        self.start_state = 'q0'
        self.current_state = self.start_state

    def transition(self, character):
        if self.current_state == 'q0':
            self.current_state = f'q1{character}'
        elif self.current_state.startswith('q1'):
            pass

    def accept(self, input_string):
        if not input_string:
            return False
        start_char = input_string[0]
        end_char = input_string[-1]
        return start_char == end_char

    def process(self, input_string):
        self.current_state = self.start_state
        for char in input_string:
            self.transition(char)
        return self.accept(input_string)


dfa = DFA()

test_words = ["appla", "banana", "racecar", "rotor", "hello"]
results = {word: dfa.process(word) for word in test_words}

for word, result in results.items():
    print(f"Word '{word}' is accepted by the DFA: {result}")
