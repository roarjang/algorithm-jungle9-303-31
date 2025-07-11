import os

TEMPLATE = '''# 문제: https://www.acmicpc.net/problem/{problem_id}
# 날짜:
# 난이도:
# 문제유형:

# 문제 설명


# 핵심 아이디어


# 입력


# 출력


# 시간복잡도


# 공간복잡도


from sys import stdin
stdin = open('input.txt', 'r')

input = lambda: stdin.readline().strip()

'''

def create_problem_folder(week_folder, problem_id, title):
    safe_title = title.strip().replace(" ", "_")
    folder_name = f"{problem_id}_{safe_title}"
    full_path = os.path.join(week_folder, folder_name)
    os.makedirs(full_path, exist_ok=True)

    # solution.py 생성
    solution_path = os.path.join(full_path, "solution.py")
    with open(solution_path, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(problem_id=problem_id))

    # input.txt 생성
    input_path = os.path.join(full_path, "input.txt")
    open(input_path, "w").close()

    print(f"✅ 생성 완료: {full_path}/solution.py, input.txt")

if __name__ == "__main__":
    week_folder = input("주차 폴더명을 입력하세요 (예: Week01): ").strip()
    problem_id = input("문제 번호를 입력하세요 (예: 1000): ").strip()
    title = input("문제 제목을 입력하세요 (예: A plus B): ").strip()

    if not os.path.isdir(week_folder):
        print(f"❌ '{week_folder}' 폴더가 존재하지 않습니다. 먼저 만들어 주세요!")
    else:
        create_problem_folder(week_folder, problem_id, title)