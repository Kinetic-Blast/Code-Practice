def Green_Bottles(num):
    if num != 1:
        print (f"""
            {num} green bottles hanging on the wall,
            {num} green bottles hanging on the wall,
            And if one green bottle should accidentally fall,
            There'll be {num -1} green bottles hanging on the wall.""")
        Green_Bottles(num-1)
    else:
        print("""
            One green bottle hanging on the wall,
            One green bottle hanging on the wall,
            And if one green bottle should accidentally fall,
            There'll be no green bottles hanging on the wall.""")

Green_Bottles(100)