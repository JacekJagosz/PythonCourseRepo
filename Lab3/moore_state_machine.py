class State:
    def __init__(self, name, output):
        self.name = name
        self.output = output
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state

    def get_next_state(self, input_symbol):
        return self.transitions.get(input_symbol)

    def get_output(self):
        return self.output


class MooreMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, output):
        state = State(name, output)
        self.states[name] = state
        if self.current_state is None:
            self.current_state = state
        return state

    def set_start_state(self, name):
        self.current_state = self.states[name]

    def transition(self, input_symbol):
        if self.current_state:
            next_state = self.current_state.get_next_state(input_symbol)
            if next_state:
                self.current_state = next_state

    def get_output(self):
        if self.current_state:
            return self.current_state.get_output()
        return None


# Create the Moore Machine
moore_machine = MooreMachine()

# Add states
state_A = moore_machine.add_state("A", "Output_A")
state_B = moore_machine.add_state("B", "Output_B")
state_C = moore_machine.add_state("C", "Output_C")

# Define transitions
state_A.add_transition("0", state_B)
state_A.add_transition("1", state_C)
state_B.add_transition("0", state_A)
state_B.add_transition("1", state_C)
state_C.add_transition("0", state_A)
state_C.add_transition("1", state_B)

# Set start state
moore_machine.set_start_state("A")

# Process inputs
inputs = "010101"
for input_symbol in inputs:
    moore_machine.transition(input_symbol)
    output = moore_machine.get_output()
    print(f"Input: {input_symbol}, Output: {output}")
