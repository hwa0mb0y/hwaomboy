import sys

def process_text(input_file, output_file):
    # 대체할 문자 리스트
    replace_chars = ['，', '、', '？', '：', '。', '「', '」', '《', '》']
    
    # 대체할 문자 딕셔너리
    replace_dict = {'教': '敎', '為': '爲', '即': '卽'}
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 리스트의 문자들을 공백으로 대체
        for char in replace_chars:
            content = content.replace(char, ' ')
        
        # 딕셔너리를 사용하여 문자 대체
        for old, new in replace_dict.items():
            content = content.replace(old, new)
        
        # 결과를 새 파일에 쓰기
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"처리가 완료되었습니다. 결과가 {output_file}에 저장되었습니다.")
    
    except FileNotFoundError:
        print(f"오류: {input_file} 파일을 찾을 수 없습니다.")
    except IOError:
        print("파일을 읽거나 쓰는 중 오류가 발생했습니다.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("사용법: python script.py <입력_파일> <출력_파일>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    process_text(input_file, output_file)
