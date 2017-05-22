from exp1bytecode_interp_gram import parser
from exp1bytecode_interp_state import state

def interp_program():
    'execute abstract bytecode machine'
    
    # We cannot use the list iterator here because we
    # need to be able to interpret jump instructions
    
    # start at the first instruction in program
    state.instr_ix = 0
    
    # keep interpreting until we run out of instructions
    # or we hit a 'stop'
    while True:
        if state.instr_ix == len(state.program):
            # no more instructions
            break
        else:
            # get instruction from program
            instr = state.program[state.instr_ix]
        
        # instruction format: (type, [arg1, arg2, ...])
        type = instr[0]
        
        # interpret instruction
        if type == 'print':
            # PRINT exp
            exp_tree = instr[1]
            val = eval_exp_tree(exp_tree)
            print("> {}".format(val))
            state.instr_ix += 1
        
        elif type == 'input':
            # INPUT NAME
            var_name = instr[1]
            val = input("Please enter a value: ")
            state.symbol_table[var_name] = int(val)
            state.instr_ix += 1
        
        elif type == 'store':
            # STORE type exp
            var_name = instr[1]
            val = eval_exp_tree(instr[2])
            state.symbol_table[var_name] = val
            state.instr_ix += 1
        
        elif type == 'jumpT':
            # JUMPT exp label
            val = eval_exp_tree(instr[1])
            if val:
                state.instr_ix = state.label_table.get(instr[2], None)
            else:
                state.instr_ix += 1

        elif type == 'jumpF':
            # JUMPF exp label
            val = eval_exp_tree(instr[1])
            if not val:
                state.instr_ix = state.label_table.get(instr[2], None)
            else:
                state.instr_ix += 1

        elif type == 'jump':
            # JUMP label
            state.instr_ix = state.label_table.get(instr[1], None)
        
        elif type == 'stop':
            # STOP
            break

        elif type == 'noop':
            # NOOP
            state.instr_ix += 1
        
        else:
            raise ValueError("Unexpected instruction type: {}".format(p[1]))


def eval_exp_tree(node):
    'walk expression tree and evaluate to an integer value'

    # tree nodes are tuples (TYPE, [arg1, arg2,...])
    
    type = node[0]
    
    if type == '+':
        # '+' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left + v_right
    
    elif type == '-':
        # '-' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left - v_right
    
    elif type == '*':
        # '*' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left * v_right
    
    elif type == '/':
        # '/' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left // v_right
    
    elif type == '=':
        # '=' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left == v_right
    
    elif type == '=<':
        # '=<' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left <= v_right
    
    elif type == 'UMINUS':
        # 'UMINUS' exp
        val = eval_exp_tree(node[1])
        return - val
    
    elif type == 'NAME':
        # 'NAME' var_name
        return state.symbol_table.get(node[1],0)

    elif type == 'NUMBER':
        # NUMBER val
        return node[1]

def exp1bytecode_interp(input_stream):
    'driver for our Exp1bytecode interpreter.'

    # initialize our abstract machine
    state.initialize()
    
    # build the IR
    parser.parse(input_stream)
    
    # interpret the IR
    interp_program()