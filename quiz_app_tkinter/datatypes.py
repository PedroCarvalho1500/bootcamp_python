


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    
    else: can_drive = False

    return can_drive

if __name__ == '__main__':
    print(police_check(19))