"""
    A Pushdown Automata which accepts the Context Free Grammar:
    S -> 0S0 | 1S1 | c
"""

stack = ["RED"]

state = "q1"

def top_element():
    global stack
    if len(stack) <= 0:
        return None
    return stack[-1]
    
def pop():
    global stack
    stack = stack[:-1]

def push(element):
    global stack
    stack.append(element)

def goto_q2():
    global state
    state = "q2"

def add_green_stay_q1():
    global state
    push("GREEN")
    state = "q1"

def add_blue_stay_q1():
    global state
    push("BLUE")
    state = "q1"

def remove_top_stay_q2():
    pop()
    global state
    state = "q2"

def remove_top():
    pop()

def do_nothing():
    pass

table = {
    # 1
    "BLUE": {
        "q1":{
            "1": add_blue_stay_q1,
            "0": add_green_stay_q1,
            "c": goto_q2
            },
        "q2": {
            "1": remove_top_stay_q2,
            "0": do_nothing,
            "c": do_nothing
        }
    },
    # 0
    "GREEN": {
        "q1": {
            "1": add_blue_stay_q1,
            "0": add_green_stay_q1,
            "c": goto_q2
            },
        "q2": {
            "1": do_nothing,
            "0": remove_top_stay_q2,
            "c": do_nothing
        }
    },
    "RED": {
        "q1": {
            "1": add_blue_stay_q1,
            "0": add_green_stay_q1,
            "c": remove_top
        },
        "q2": {
            "1": remove_top,
            "0": remove_top,
            "c": remove_top
        }
    }
}

def pda(input):
    global stack
    global state
    stack = ["RED"]
    state = "q1"
    for c in input:
        top = top_element()
        if top == None:
            print(input, "Not Accepted!")
            return 
        fun = table[top][state][c]
        fun()
    top = top_element()
    if top == "RED" and state == "q2":
        remove_top()
    if len(stack) == 0:
        print(input, "Accepted!")
    else:
        print(input, "Not Accepted!")

pda("01c10")
pda("01c01")
pda("0001c1000")
pda("1001c1001")
pda("1111c1111")
pda("0100c0010")
pda("0101c0010")
