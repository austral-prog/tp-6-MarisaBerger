def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements) >= 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements) <= 4 and len(list_to_remove_elements) != 0:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements) == 0:
        return list_to_remove_elements



def add_elements(list_to_add_elements):
    length = len(list_to_add_elements)
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements



def is_empty(list_to_check):
    if len(list_to_check) > 0:
        return False
    else:
        return True



def check_lists(list_to_compare1, list_to_compare2):
    return len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3 and list_to_compare1[2] == list_to_compare2[2]
    



def list_of_lists(list_of_lists_to_modify):
    
    if len(list_of_lists_to_modify[0]) >= 2 and len(list_of_lists_to_modify[1]) > 4 and len(list_of_lists_to_modify[2])>= 2:
        return [list_of_lists_to_modify[0][:2], list_of_lists_to_modify[1][1:4], list_of_lists_to_modify[2][-2:]]
    elif len(list_of_lists_to_modify[0]) <= 1 and len(list_of_lists_to_modify[1]) > 4 and len(list_of_lists_to_modify[2])>= 2:
        return [list_of_lists_to_modify[0], list_of_lists_to_modify[1][1:4], list_of_lists_to_modify[2][-2:]]
    elif len(list_of_lists_to_modify[0]) >= 2 and len(list_of_lists_to_modify[1]) <= 4 and len(list_of_lists_to_modify[2])>= 2:
        return [list_of_lists_to_modify[0][:2], list_of_lists_to_modify[1][1:], list_of_lists_to_modify[2][-2:]]
    elif len(list_of_lists_to_modify[0]) <= 1 and len(list_of_lists_to_modify[1]) <= 4 and len(list_of_lists_to_modify[2])>= 2:
        return [list_of_lists_to_modify[0], list_of_lists_to_modify[1][1:], list_of_lists_to_modify[2][-2:]]
    elif len(list_of_lists_to_modify[0]) >= 2 and len(list_of_lists_to_modify[1]) > 4 and len(list_of_lists_to_modify[2]) <= 1:
        return [list_of_lists_to_modify[0][:2], list_of_lists_to_modify[1][1:4], list_of_lists_to_modify[2]]
    elif len(list_of_lists_to_modify[0]) <= 1 and len(list_of_lists_to_modify[1]) > 4 and len(list_of_lists_to_modify[2]) <= 1:
        return [list_of_lists_to_modify[0], list_of_lists_to_modify[1][1:4], list_of_lists_to_modify[2]]
    elif len(list_of_lists_to_modify[0]) >= 2 and len(list_of_lists_to_modify[1]) <= 4 and len(list_of_lists_to_modify[2]) <= 1:
        return [list_of_lists_to_modify[0][:2], list_of_lists_to_modify[1][1:], list_of_lists_to_modify[2]]
    elif len(list_of_lists_to_modify[0]) <= 1 and len(list_of_lists_to_modify[1]) <= 4 and len(list_of_lists_to_modify[2]) <= 1:
        return [list_of_lists_to_modify[0], list_of_lists_to_modify[1][1:], list_of_lists_to_modify[2]]
