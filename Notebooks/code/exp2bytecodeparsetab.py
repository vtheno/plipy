
# exp2bytecodeparsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "NAME NUMBER EQ LE RVX TSX STRING PRINT INPUT STORE JUMPT JUMPF JUMP CALL RETURN PUSHV POPV PUSHF POPF STOP NOOP\n    prog : instr_list\n    \n    instr_list : labeled_instr instr_list\n              | empty\n    \n    labeled_instr : label_def instr\n    \n    label_def : NAME ':' \n              | empty\n    \n    instr : PRINT opt_string exp ';'\n          | INPUT opt_string storable ';'\n          | STORE storable exp ';'\n          | JUMPT exp label ';'\n          | JUMPF exp label ';'\n          | JUMP label ';'\n          | CALL label ';'\n          | RETURN ';'\n          | PUSHV exp ';'\n          | POPV opt_storable ';'\n          | PUSHF size ';'\n          | POPF size ';'\n          | STOP ';'\n          | NOOP ';'\n    \n    opt_string : STRING\n               | empty\n\n    opt_storable : storable\n                 | empty\n\n    size : exp\n    \n    label : NAME\n    \n    exp : '+' exp exp\n        | '-' exp exp\n        | '*' exp exp\n        | '/' exp exp\n        | EQ exp exp\n        | LE exp exp\n    \n    exp : '-' exp\n    \n    exp : '!' exp\n    \n    exp : '(' exp ')'\n    \n    exp : storable\n    \n    exp : NUMBER\n    \n    storable : var\n    \n    storable : RVX\n             | TSX opt_offset\n    \n    opt_offset : '[' offset ']'\n               | empty\n    \n    offset : exp\n    \n    var : NAME\n    \n    empty :\n    "
    
_lr_action_items = {'$end':([0,1,2,3,4,7,8,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,0,-1,-45,-3,-2,-4,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'PRINT':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,9,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'INPUT':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,10,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'STORE':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,11,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'JUMPT':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,12,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'JUMPF':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,13,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'JUMP':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,14,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'CALL':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,15,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'RETURN':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,16,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'PUSHV':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,17,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'POPV':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,18,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'PUSHF':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,19,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'POPF':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,20,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'STOP':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,21,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'NOOP':([0,3,4,5,8,23,48,56,57,74,75,76,77,78,79,80,81,82,85,93,],[-45,-45,-6,22,-4,-5,-14,-19,-20,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-11,]),'NAME':([0,3,8,9,10,11,12,13,14,15,17,18,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,56,57,61,62,63,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,82,85,86,87,88,89,90,91,92,93,94,],[6,6,-4,-45,-45,32,32,32,46,46,32,32,32,32,32,-21,-22,32,32,-38,-39,-45,-44,46,32,32,32,32,32,32,32,32,-36,-37,46,-14,-19,-20,-40,32,-42,32,32,32,32,32,32,-34,-12,-13,-15,-16,-17,-18,-7,-8,-9,-10,-27,-28,-29,-30,-31,-32,-35,-11,-41,]),':':([6,],[23,]),'STRING':([9,10,],[25,25,]),'+':([9,12,13,17,19,20,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,34,34,34,34,34,34,-21,-22,34,-38,-39,-45,-44,34,34,34,34,34,34,34,34,-36,-37,-40,34,-42,34,34,34,34,34,34,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'-':([9,12,13,17,19,20,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,35,35,35,35,35,35,-21,-22,35,-38,-39,-45,-44,35,35,35,35,35,35,35,35,-36,-37,-40,35,-42,35,35,35,35,35,35,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'*':([9,12,13,17,19,20,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,36,36,36,36,36,36,-21,-22,36,-38,-39,-45,-44,36,36,36,36,36,36,36,36,-36,-37,-40,36,-42,36,36,36,36,36,36,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'/':([9,12,13,17,19,20,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,37,37,37,37,37,37,-21,-22,37,-38,-39,-45,-44,37,37,37,37,37,37,37,37,-36,-37,-40,37,-42,37,37,37,37,37,37,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'EQ':([9,12,13,17,19,20,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,38,38,38,38,38,38,-21,-22,38,-38,-39,-45,-44,38,38,38,38,38,38,38,38,-36,-37,-40,38,-42,38,38,38,38,38,38,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'LE':([9,12,13,17,19,20,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,39,39,39,39,39,39,-21,-22,39,-38,-39,-45,-44,39,39,39,39,39,39,39,39,-36,-37,-40,39,-42,39,39,39,39,39,39,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'!':([9,12,13,17,19,20,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,40,40,40,40,40,40,-21,-22,40,-38,-39,-45,-44,40,40,40,40,40,40,40,40,-36,-37,-40,40,-42,40,40,40,40,40,40,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'(':([9,12,13,17,19,20,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,41,41,41,41,41,41,-21,-22,41,-38,-39,-45,-44,41,41,41,41,41,41,41,41,-36,-37,-40,41,-42,41,41,41,41,41,41,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'NUMBER':([9,12,13,17,19,20,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,43,43,43,43,43,43,-21,-22,43,-38,-39,-45,-44,43,43,43,43,43,43,43,43,-36,-37,-40,43,-42,43,43,43,43,43,43,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'RVX':([9,10,11,12,13,17,18,19,20,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,-45,30,30,30,30,30,30,30,30,-21,-22,30,30,-38,-39,-45,-44,30,30,30,30,30,30,30,30,-36,-37,-40,30,-42,30,30,30,30,30,30,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),'TSX':([9,10,11,12,13,17,18,19,20,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,61,62,63,65,66,67,68,69,70,71,86,87,88,89,90,91,92,94,],[-45,-45,31,31,31,31,31,31,31,31,-21,-22,31,31,-38,-39,-45,-44,31,31,31,31,31,31,31,31,-36,-37,-40,31,-42,31,31,31,31,31,31,-34,-27,-28,-29,-30,-31,-32,-35,-41,]),';':([16,18,21,22,29,30,31,32,42,43,45,46,47,49,50,51,52,53,54,55,58,59,60,61,63,64,66,71,73,86,87,88,89,90,91,92,94,],[48,-45,56,57,-38,-39,-45,-44,-36,-37,74,-26,75,76,77,-23,-24,78,-25,79,80,81,82,-40,-42,85,-33,-34,93,-27,-28,-29,-30,-31,-32,-35,-41,]),')':([29,30,31,32,42,43,61,63,66,71,72,86,87,88,89,90,91,92,94,],[-38,-39,-45,-44,-36,-37,-40,-42,-33,-34,92,-27,-28,-29,-30,-31,-32,-35,-41,]),']':([29,30,31,32,42,43,61,63,66,71,83,84,86,87,88,89,90,91,92,94,],[-38,-39,-45,-44,-36,-37,-40,-42,-33,-34,94,-43,-27,-28,-29,-30,-31,-32,-35,-41,]),'[':([31,],[62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'instr_list':([0,3,],[2,7,]),'labeled_instr':([0,3,],[3,3,]),'empty':([0,3,9,10,18,31,],[4,4,26,26,52,63,]),'label_def':([0,3,],[5,5,]),'instr':([5,],[8,]),'opt_string':([9,10,],[24,27,]),'storable':([11,12,13,17,18,19,20,24,27,28,34,35,36,37,38,39,40,41,62,65,66,67,68,69,70,],[28,42,42,42,51,42,42,42,59,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'var':([11,12,13,17,18,19,20,24,27,28,34,35,36,37,38,39,40,41,62,65,66,67,68,69,70,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'exp':([12,13,17,19,20,24,28,34,35,36,37,38,39,40,41,62,65,66,67,68,69,70,],[33,44,49,54,54,58,60,65,66,67,68,69,70,71,72,84,86,87,88,89,90,91,]),'label':([14,15,33,44,],[45,47,64,73,]),'opt_storable':([18,],[50,]),'size':([19,20,],[53,55,]),'opt_offset':([31,],[61,]),'offset':([62,],[83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> instr_list','prog',1,'p_prog','exp2bytecode_interp_gram.py',7),
  ('instr_list -> labeled_instr instr_list','instr_list',2,'p_instr_list','exp2bytecode_interp_gram.py',13),
  ('instr_list -> empty','instr_list',1,'p_instr_list','exp2bytecode_interp_gram.py',14),
  ('labeled_instr -> label_def instr','labeled_instr',2,'p_labeled_instr','exp2bytecode_interp_gram.py',20),
  ('label_def -> NAME :','label_def',2,'p_label_def','exp2bytecode_interp_gram.py',31),
  ('label_def -> empty','label_def',1,'p_label_def','exp2bytecode_interp_gram.py',32),
  ('instr -> PRINT opt_string exp ;','instr',4,'p_instr','exp2bytecode_interp_gram.py',38),
  ('instr -> INPUT opt_string storable ;','instr',4,'p_instr','exp2bytecode_interp_gram.py',39),
  ('instr -> STORE storable exp ;','instr',4,'p_instr','exp2bytecode_interp_gram.py',40),
  ('instr -> JUMPT exp label ;','instr',4,'p_instr','exp2bytecode_interp_gram.py',41),
  ('instr -> JUMPF exp label ;','instr',4,'p_instr','exp2bytecode_interp_gram.py',42),
  ('instr -> JUMP label ;','instr',3,'p_instr','exp2bytecode_interp_gram.py',43),
  ('instr -> CALL label ;','instr',3,'p_instr','exp2bytecode_interp_gram.py',44),
  ('instr -> RETURN ;','instr',2,'p_instr','exp2bytecode_interp_gram.py',45),
  ('instr -> PUSHV exp ;','instr',3,'p_instr','exp2bytecode_interp_gram.py',46),
  ('instr -> POPV opt_storable ;','instr',3,'p_instr','exp2bytecode_interp_gram.py',47),
  ('instr -> PUSHF size ;','instr',3,'p_instr','exp2bytecode_interp_gram.py',48),
  ('instr -> POPF size ;','instr',3,'p_instr','exp2bytecode_interp_gram.py',49),
  ('instr -> STOP ;','instr',2,'p_instr','exp2bytecode_interp_gram.py',50),
  ('instr -> NOOP ;','instr',2,'p_instr','exp2bytecode_interp_gram.py',51),
  ('opt_string -> STRING','opt_string',1,'p_opt_string_pp','exp2bytecode_interp_gram.py',87),
  ('opt_string -> empty','opt_string',1,'p_opt_string_pp','exp2bytecode_interp_gram.py',88),
  ('opt_storable -> storable','opt_storable',1,'p_opt_string_pp','exp2bytecode_interp_gram.py',90),
  ('opt_storable -> empty','opt_storable',1,'p_opt_string_pp','exp2bytecode_interp_gram.py',91),
  ('size -> exp','size',1,'p_opt_string_pp','exp2bytecode_interp_gram.py',93),
  ('label -> NAME','label',1,'p_label','exp2bytecode_interp_gram.py',99),
  ('exp -> + exp exp','exp',3,'p_bin_exp','exp2bytecode_interp_gram.py',105),
  ('exp -> - exp exp','exp',3,'p_bin_exp','exp2bytecode_interp_gram.py',106),
  ('exp -> * exp exp','exp',3,'p_bin_exp','exp2bytecode_interp_gram.py',107),
  ('exp -> / exp exp','exp',3,'p_bin_exp','exp2bytecode_interp_gram.py',108),
  ('exp -> EQ exp exp','exp',3,'p_bin_exp','exp2bytecode_interp_gram.py',109),
  ('exp -> LE exp exp','exp',3,'p_bin_exp','exp2bytecode_interp_gram.py',110),
  ('exp -> - exp','exp',2,'p_uminus_exp','exp2bytecode_interp_gram.py',116),
  ('exp -> ! exp','exp',2,'p_not_exp','exp2bytecode_interp_gram.py',122),
  ('exp -> ( exp )','exp',3,'p_paren_exp','exp2bytecode_interp_gram.py',128),
  ('exp -> storable','exp',1,'p_storable_exp','exp2bytecode_interp_gram.py',135),
  ('exp -> NUMBER','exp',1,'p_number_exp','exp2bytecode_interp_gram.py',141),
  ('storable -> var','storable',1,'p_var_storable','exp2bytecode_interp_gram.py',147),
  ('storable -> RVX','storable',1,'p_X_storable','exp2bytecode_interp_gram.py',153),
  ('storable -> TSX opt_offset','storable',2,'p_X_storable','exp2bytecode_interp_gram.py',154),
  ('opt_offset -> [ offset ]','opt_offset',3,'p_opt_offset','exp2bytecode_interp_gram.py',165),
  ('opt_offset -> empty','opt_offset',1,'p_opt_offset','exp2bytecode_interp_gram.py',166),
  ('offset -> exp','offset',1,'p_offset','exp2bytecode_interp_gram.py',175),
  ('var -> NAME','var',1,'p_var','exp2bytecode_interp_gram.py',181),
  ('empty -> <empty>','empty',0,'p_empty','exp2bytecode_interp_gram.py',187),
]
