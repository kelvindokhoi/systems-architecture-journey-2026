list1 = [1,3,5,7,9, 20, 21, 23, 24]
list2 = list(chr(n)for n in range(ord("b"),ord("f")+1))
list3 = [*range(1,9+1), 15, 18, 19, 24,25,26]
list4 = [*range(1,12,2)]

def Subsect_from_list(listn):
    for n in listn:
        print(f"\\subsection{{Question {n}:}}")

def Section_from_list(listn):
    for n in listn:
        print(f"\\section")

def Read_and_format(function):
    n = int(input("Number of lines: "))
    function([input() for _ in range(n)])
Subsect_from_list(list2)

# for n in list2:
#     print(f"\\subsection{{{n})}}")
#     print("Two strings that are members:")
#     print("\\begin{itemize}")
#     print("\t\\item ")
#     print("\t\\item ")
#     print("\\end{itemize}")
#     print("Two strings that are NOT members:")
#     print("\\begin{itemize}")
#     print("\t\\item ")
#     print("\t\\item ")
#     print("\\end{itemize}")