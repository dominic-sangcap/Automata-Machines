#testing 
#inspired by https://stackoverflow.com/questions/35272592/how-are-finite-automata-implemented-in-code/35279645
#HOW THIS WORKS..........

#Choose segment from dfa_storage.py, place code under line 19. 
#code runner extension, highlight lines 8 - added code 
#press ctrl + alt + n. output = (if input is valid, and order of states processes)

def accepts(transitions,initial,accepting,s):
    state = initial
    state_sequence = []

    state_sequence.append(initial)
    for c in s:
        state = transitions[state][c]
        state_sequence.append(state)
    return state in accepting, state_sequence

#Put input here ----------------

# {w|w ends with (suffix of) 10}----------------------------------------
dfa = { 
    0: {'0': 0, '1': 1},
    1: {'0': 2, '1': 1},
    2: {'0': 0, '1': 1},
}

start_state = 0
accept_states = {2}
input_string1 = '00010'

# -----------------------------

#call function
print(accepts(dfa, start_state, accept_states, input_string1))

