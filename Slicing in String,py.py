def join_middle(bound_by, tag_name):
    return bound_by[:len(bound_by)//2] + tag_name + bound_by[len(bound_by)//2:]

print(join_middle("[[]]", "tag"))  
print(join_middle("<>", "body"))  
