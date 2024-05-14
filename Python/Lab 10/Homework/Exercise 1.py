class DFA:
    def __init__(self):
        self.current_state = 'A'

    def transition(self, character):
        if self.current_state == 'A':
            if character == 'a':
                self.current_state = 'B'
            elif character == 'b':
                self.current_state = 'E'
        elif self.current_state == 'B':
            if character == 'a':
                self.current_state = 'D'
            elif character == 'b':
                self.current_state = 'C'
        elif self.current_state == 'C':
            if character == 'a':
                self.current_state = 'F'
            elif character == 'b':
                self.current_state = 'C'
        elif self.current_state == 'D':
            if character == 'a':
                self.current_state = 'D'
            elif character == 'b':
                self.current_state = 'D'
        elif self.current_state == 'E':
            if character == 'a':
                self.current_state = 'F'
            elif character == 'b':
                self.current_state = 'E'
        elif self.current_state == 'F':
            if character == 'a':
                self.current_state = 'F'
            elif character == 'b':
                self.current_state = 'C'

    def accept(self, input_string):
        starts_with_ab = input_string.startswith("ab")
        ends_with_ab = input_string.endswith("ab")
        return starts_with_ab or ends_with_ab

    def process(self, input_string):
        self.current_state = 'A'
        for char in input_string:
            self.transition(char)
        return self.accept(input_string)


dfa = DFA()

test_words = ["abababababbaa", "aabbabababaab", "babbbbababaabba", "aabbbbbbbbbbbbb"]
results = {word: dfa.process(word) for word in test_words}

for word, result in results.items():
    print(f"'{word}' accepted: {result}")
