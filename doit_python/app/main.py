import os
from pathlib import Path
from enum import Enum
from dotenv import load_dotenv


from utils.excel import Excel
from utils.mail import Mail


class UserInput(Enum):
    EXIT = 0
    MAIL = 1
    EXCEL = 2


def get_user_input():
    # type: () -> UserInput
    user_input_str = input("원하는 작업을 선택하세요. \n[1] 테스트 이메일 발송 \n[2] 엑셀파일 수정 \n[0] 종료\n:")
    try:
        user_input = UserInput(int(user_input_str))
    except ValueError as e:
        print(f"잘못된 값을 입력했습니다 : {e}")
        return None
    print(f"{user_input_str}번 작업을 선택하셨습니다.")
    return user_input


def mail_helper():
    # 보안을 위해 환경변수로 설정
    account = os.environ.get("MAIL_ACCOUNT")
    password = os.environ.get("MAIL_PASSWORD")
    if not account or not password:
        return
    with Mail(account, password) as mail:
        mail.send(subject="테스트 메일입니다.", content="테스트 메일입니다.", to_email="jinaia87@gmail.com")


def excel_helper():
    BASE_DIR = Path(__file__).resolve().parent
    excel_dir = os.path.join(BASE_DIR, "excel")
    excel = Excel(excel_dir)
    excel.write()


def main():
    # .env 파일 로드
    load_dotenv()
    user_input = get_user_input()

    if user_input == UserInput.MAIL:
        mail_helper()
    elif user_input == UserInput.EXCEL:
        excel_helper()
    else:
        return


# 실행지점 (entry-point 임을 표현)
if __name__ == "__main__":
    main()
