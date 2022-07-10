import json
import os

def load_students() -> list:
    with open("./data/students.json", 'r') as f:
        students = json.load(f)["students"]
    return students

def load_data() -> list:
    with open("./data/baofan.txt", 'r') as f:
        lines = f.readlines()
        # 删除前三行无用信息
        for i in range(3):
            lines.pop(0)
    return lines

def words_inp(in_str: str, words: dict) -> list:
    result = []
    for word in words.keys():
        inp = False
        for v in words[word]:
            if v in in_str:
                inp = True
                break
        if inp:
            result.append(word)
    return result

def save_no_report(no_report: list):
    report_result = {}
    if os.path.exists("./data/noreport.json"):
        with open("./data/noreport.json", 'r') as f:
            no_reports_last = json.load(f)
            for student in no_report:
                if student in no_reports_last.keys():
                    no_reports_last[student] += 1
                else:
                    no_reports_last[student] = 1
            report_result = no_reports_last
    else:
        for student in no_report:
            report_result[student] = 1
    with open("./data/noreport.json", "w") as f:
        json.dump(report_result, f, indent=4, ensure_ascii=False)
        
if __name__ == "__main__":
    students = load_students()
    datas = load_data()
    
    eat_food_studnet = {}
    morning_n = 0
    noon_n = 0
    night_n = 0
    words = {"早": ["早"], "午": ["中", "午"], "晚": ["晚"]}
    for line in datas:
        report_result = words_inp(line, words)
        if '早' in report_result:
            morning_n += 1
        if '午' in report_result:
            noon_n += 1
        if '晚' in report_result:
            night_n += 1
                
        for student_name in students:
            if student_name in line:
                # eat_food_studnet[student] = words_inp(line, words)
                eat_food_studnet[student_name] = report_result
    # print(json.dumps(eat_food_studnet, indent=4, ensure_ascii=False))
    print(eat_food_studnet)
    print(f"早 人数: {morning_n}")
    print(f"午 人数: {noon_n}")
    print(f"晚 人数: {night_n}")
    print(f"总人数: {len(datas)}")
    
    no_report = set(students) - set(eat_food_studnet.keys())
    no_report_breakfast = []
    for student in eat_food_studnet.keys():
        if '早' not in eat_food_studnet[student]:
            no_report_breakfast.append(student)
            
    print("没有报早饭的人数是: {}".format(len(no_report_breakfast)))
    print("没有报早饭的人是: {}".format(no_report_breakfast))
    save_no_report(no_report_breakfast)

