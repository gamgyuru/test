print('\n ***********************')
print('  Wpm to Cpm & Cpm to Wpm')
print('     by gamgyuru')
print(' ***********************\n')
while True :
    print("* 모드를 선택해주세요")
    print("-------------------------")
    print("1. wpm -> 타수(cpm)")
    print("2. 타수(cpm) -> wpm\n")
    mod = input("선택 모드 : ")
    print("-------------------------")

    if mod == '1' :
        data = input("\nwpm을 입력하세요 : ")
        print("당신의 타수는 ", int(data)*5, "타 입니다.")

    elif mod == '2' :
        data = input("\n타수를 입력하세요 : ")
        print("당신의 wpm은 ", int(data)/5, "입니다.")

    else :
        print("올바르지 않은 값입니다.")

    exist = input("\n종료하시겠습니까? 종료하려면 q를 눌러주세요 : ")
    if exist == 'q' :
        break;
    else :
        print('\n\n\n')

