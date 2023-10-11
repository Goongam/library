from datetime import datetime

# 현재 날짜 가져오기
current_date = datetime.now()

# 사용자로부터 생년월일 입력 받기
birth_year = int(input("태어난 년도를 입력하세요 (예: 1990): ")
birth_month = int(input("태어난 월을 입력하세요 (1-12): ")
birth_day = int(input("태어난 일을 입력하세요 (1-31): ")

# 태어난 날짜를 생성
birth_date = datetime(birth_year, birth_month, birth_day)

# 만나이 계산
age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

# 결과 출력
print("당신은 현재", age, "세 입니다.")
#ㅇㅇ
