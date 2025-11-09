def create_password(num):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num
    c3 = num -5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num_entero}"
    print("Your new password is:", contrasena)
create_password(10)