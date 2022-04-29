# from likelion import account

print("======Bank Menu=====")
print("1. 계좌개설")
print("2. 입금하기")
print("3. 출금하기")
print("4. 전체조회")
print("5. 계좌이체")
print("6. 프로그램 종료")
print("====================")
select_service = input("입력 :")

if select_service  == "1":
    print("\n======계좌개설======\n")
    new_account = input("계좌번호 : ")
    new_name = input("이름 : ")
    new_deposit = input("예금 : ")
    customer = Account(new_account, new_name, new_deposit)
    print("##계좌개설을 완료하였습니다##")
    print("====================")
    print(customer)