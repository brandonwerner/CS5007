import
copy
def
main():
my_list
=  [1, 2, 3, 4,   5]
copied_list1
= deep_copy(my_list)
copied_list2
= copy.deepcopy(my_list)
#  make
some
changes
 to   show
that
 it   in   fact
was a  deep
copy
my_list[0]
=  777
copied_list1[0]
= 888
copied_list2[0]
= 999
print(my_list)
print(copied_list1)
print(copied_list2)
#  will
be   a  deep
copy
only
 if   the
elements
in the original
 list
are
IMMUTABLE
def
deep_copy(original_list):
copied_list
=  []
for
i in   range(len(original_list)):
copied_list.append(original_list[i])
return
copied_list
if   __name__
 ==   '__main__':
main()
