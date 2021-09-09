#contains the dfa transition data, start state. accept states, and input for a given machine

# {w|w starts with (prefix of) 10}----------------------------------------
dfa = { 
    0: {'0': 3, '1': 1},
    1: {'0': 2, '1': 3},
    2: {'0': 2, '1': 2},
    3: {'0': 3, '1': 3},
}

start_state = 0
accept_states = {2}
input_string1 = '101'

# {w|w contains odd # of 0's }--------------------------------
dfa = { 
    0: {'0': 1, '1': 0},
    1: {'0': 0, '1': 1},
}

start_state = 0
accept_states = {1}
input_string1 = '01'

# not 1, 10, 101*, 101*0, 101*001* ... 1(11)*----------------
dfa = { 
    0: {'0': 0, '1': 1},
    1: {'0': 2, '1': 0},
    2: {'0': 1, '1': 2}
}

start_state = 0
accept_states = {0}
input_string1 = '1'

# {w|w ends with (suffix of) 10}----------------------------------------
dfa = { 
    0: {'0': 0, '1': 1},
    1: {'0': 2, '1': 1},
    2: {'0': 0, '1': 1},
}

start_state = 0
accept_states = {2}
input_string1 = '00010'

