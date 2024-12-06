from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.goto = defaultdict(dict)
        self.output = defaultdict(list)
        self.fail = {}

    def build_goto(self, patterns):
        new_state = 0
        for pattern in patterns:
            current_state = 0
            for symbol in pattern:
                if symbol not in self.goto[current_state]:
                    new_state += 1
                    self.goto[current_state][symbol] = new_state
                current_state = self.goto[current_state][symbol]
            self.output[current_state].append(pattern)

        for symbol in self.goto[0]:
            self.fail[self.goto[0][symbol]] = 0

    def build_fail(self):
        queue = deque()
        for symbol in self.goto[0]:
            state = self.goto[0][symbol]
            self.fail[state] = 0
            queue.append(state)

        while queue:
            r = queue.popleft()
            for symbol in self.goto[r]:
                s = self.goto[r][symbol]
                queue.append(s)
                state = self.fail[r]
                while state != 0 and symbol not in self.goto[state]:
                    state = self.fail[state]
                if symbol in self.goto[state]:
                    self.fail[s] = self.goto[state][symbol]
                else:
                    self.fail[s] = 0
                self.output[s] += self.output[self.fail[s]]

    def build(self, patterns):
        self.build_goto(patterns)
        self.build_fail()

    def search(self, text):
        current_state = 0
        results = []
        for i in range(len(text)):
            while current_state != 0 and text[i] not in self.goto[current_state]:
                current_state = self.fail[current_state]
            if text[i] in self.goto[current_state]:
                current_state = self.goto[current_state][text[i]]
            else:
                current_state = 0
            if self.output[current_state]:
                for pattern in self.output[current_state]:
                    results.append((i - len(pattern) + 1, pattern))
        return results




patterns = ['he', 'she', 'his', 'hers']
text = 'ahishers'

aho_corasick = AhoCorasick()
aho_corasick.build(patterns)
matches = aho_corasick.search(text)

for match in matches:
    print(f"Pattern '{match[1]}' found at position {match[0]}")
