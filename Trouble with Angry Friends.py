def friends_in_trouble(j_angry, s_angry):
    if(j_angry==True and s_angry==True):
        print("You are in trouble")
        return True
    else:
        print("You are not in trouble")
        return False
        
friends_in_trouble(True,True)
friends_in_trouble(False,True)

