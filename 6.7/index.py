# 6.7.1
num = 2

match num:
    case 1:
        print("весна")
    case 2:
        print("лето")  # -> 'лето'
    case 3:
        print("осень")
    case 4:
        print("зима")

# 6.7.2
num = 6

match num:
    case 3 | 4 | 5:
        print("весна")
    case 6 | 7 | 8:
        print("лето")  # -> 'лето'
    case 9 | 10 | 11:
        print("осень")
    case 12 | 1 | 2:
        print("зима")
