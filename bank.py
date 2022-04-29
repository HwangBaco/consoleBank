from account import Account

def create() : #계좌개설
    print("\n======계좌개설======\n")
    while(True):
        new_account = input("계좌번호 : ")
        if not new_account.isnumeric() :
            print("##계좌번호는 숫자를 입력해야 합니다##")
        else:
            break
    while(True):
        new_name = input("이름 : ")
        if new_name.isnumeric() :
                print("##이름은 글자를 입력해야 합니다##")
        else:
            break
    while(True):
        new_deposit = input("예금 : ")
        if not new_deposit.isnumeric() :
            print("##예금은 숫자를 입력해야 합니다##")
        else:
            break
    member_list.append(Account(new_account, new_name, int(new_deposit)))
    print("##계좌개설을 완료하였습니다##")
    print("====================")

def deposit() : #입금
    print("======입금하기======")
    while(True):
        dpst_account = input("입금하실 계좌번호를 입력해주세요 : ")
        if not dpst_account.isnumeric() :
            print("##계좌번호는 숫자를 입력해야 합니다##")
        else:
            break
    for i in member_list :
        if dpst_account == i.account_number :
            print("계좌이름 : {}".format(i.name))
            print("계좌잔고 : {}".format(i.balance))
            while(True):
                dpst_money = input("입금하실 금액을 입력해주세요 : ")
                if not dpst_money.isnumeric() :
                    print("##입금액은 숫자를 입력해야 합니다##")
                elif int(dpst_money) < 0:
                    print("##잘못된 입력입니다##")
                else:
                    break
            i.balance += int(dpst_money)
            print("\n##계좌잔고 : {}원##".format(i.balance))
            print("##입금이 완료되었습니다##")
            print("====================")
        else:
            print("##입력하신 계좌번호는 없는 계좌번호입니다##")

def withdraw() : #출금
    print("======출금하기======")
    while(True):
        wd_account = input("출금하실 계좌번호를 입력해주세요 : ")
        if not wd_account.isnumeric() :
            print("##계좌번호는 숫자를 입력해야 합니다##")
        else:
            break
    for i in member_list :
        if wd_account == i.account_number :
            print("계좌이름 : {}".format(i.name))
            print("계좌잔고 : {}".format(i.balance))
            while(True) :
                wd_money = input("출금하실 금액을 입력해주세요 : ")
                if not wd_money.isnumeric() :
                    print("##출금액은 숫자를 입력해야 합니다##")
                else:
                    if int(wd_money) > i.balance:
                        print("##잔액이 부족합니다##")
                    elif int(wd_money) < 0:
                        print("##잘못된 입력입니다##")
                    else:
                        break
            i.balance -= int(wd_money)
            print("\n##계좌잔고 : {}원##".format(i.balance))
            print("##출금이 완료되었습니다##")
            print("====================")
        else:
            print("##입력하신 계좌번호는 없는 계좌번호입니다##")

def check_all() : #전체조회
    print("======전체조회======")
    for i in member_list :
        print("계좌번호 : {0} / 이름 : {1} / 잔액 : {2}원".format(i.account_number, i.name, i.balance))
    print("====================")

def delete() : #계좌삭제
    print("======계좌삭제======")
    while(True):
        dlt_account = input("삭제하실 계좌번호를 입력해주세요 : ")
        if not dlt_account.isnumeric() :
            print("##계좌번호는 숫자를 입력해야 합니다##")
        else:
            break
    for i in member_list :
        if dlt_account == i.account_number :
            print("계좌이름 : {}".format(i.name))
            print("계좌잔고 : {}".format(i.balance))
            while(True):
                YesOrNo = input("정말 삭제하시겠습니까?(Y/N) ")
                if YesOrNo == "Y" or "y" or "yes" or "Yes" :
                    member_list.remove(i)
                    print("##계좌삭제가 완료되었습니다##")
                    break
                elif YesOrNo == "N" or "n" or "no" or "No" :
                    print("##앞으로도 잘 부탁드립니다##")
                    break
                else :
                    print("##잘못된 입력입니다##")
            print("====================")
        else:
            print("##입력하신 계좌번호는 없는 계좌번호입니다##")
        
def end() : #프로그램 종료
    print("##프로그램을 종료합니다##")


#메인 메소드

member_list = [] #회원 리스트
idx = 0
while(True):
    print("======Bank Menu=====")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. (선택기능)")
    print("6. 프로그램 종료")
    print("====================")
    select_service = input("입력 :")

    if select_service  == "1":
        create()
        idx += 1
    elif select_service == "2":
        deposit()
    elif select_service == "3":
        withdraw()
    elif select_service == "4":
        check_all()
    elif select_service == "5":
        delete()
    elif select_service == "6":
        end()
        break
    else :
        print("##잘못된 입력입니다##")