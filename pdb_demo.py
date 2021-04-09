my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

# import pdb; pdb.set_trace()

# 3.7 onwards
# can be controlled by $PYTHONBREAKPOINT
#   $PYTHONBREAKPOINT=   : enabled (default)
#   $PYTHONBREAKPOINT=0  : disabled PDB
#   $PYTHONBREAKPOINT=pudb.set_trace   : enable 3rd party's debugger (ex: pudb)
breakpoint()

del my_list[3]  # [5, 2, 1, "abcdefg", 3, False, 4]
del my_list[3]  # [5, 2, 1, 3, False, 4]
del my_list[4]  # [5, 2, 1, 3 4]
print(my_list)

"""
python -m pdb hoge.py

(Pdb) (help / ?)
"""
