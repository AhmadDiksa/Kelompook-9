#Fungsi Program agar robot bisa berbelok  ke kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#Fungsi Program agar robot bisa melarikan diri
def keluar():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

#Memanggil fungsi keluar 
keluar()
