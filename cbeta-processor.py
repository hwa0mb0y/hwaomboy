import streamlit as st
import io

def process_text(content):
    # 대체할 문자 리스트
    replace_chars = ['，', '、', '？', '：', '；', '。', '「', '」', '《', '》']
    
    # 대체할 문자 딕셔너리
    replace_dict = {'眾': '衆', '教': '敎', '為': '爲', '即': '卽'}
    
    # 리스트의 문자들을 공백으로 대체
    for char in replace_chars:
        content = content.replace(char, ' ')
    
    # 딕셔너리를 사용하여 문자 대체
    for old, new in replace_dict.items():
        content = content.replace(old, new)
    
    return content

st.title('CBETA 텍스트 처리')
st.text("이 앱은 CBETA 등의 텍스트를 입력받아서 표점 부호를 빈칸으로 바꾸고 중국/일본식 한자를 한국식 한자로 바꿉니다.")

input_option = st.radio(
    "입력 방식을 선택하세요:",
    ('텍스트 직접 입력', '파일 업로드')
)

if input_option == '텍스트 직접 입력':
    content = st.text_area("텍스트를 입력하세요:", height=200)
else:
    uploaded_file = st.file_uploader("텍스트 파일을 선택하세요", type=['txt'])
    if uploaded_file is not None:
        content = uploaded_file.getvalue().decode("utf-8")
        st.subheader("파일 내용:")
        st.text_area("", content, height=200)

if st.button('텍스트 처리') and 'content' in locals():
    processed_content = process_text(content)
    
    st.subheader("처리된 텍스트:")
    st.text_area("", processed_content, height=200)
    
    # 처리된 텍스트를 다운로드할 수 있게 합니다
    output = io.BytesIO()
    output.write(processed_content.encode('utf-8'))
    st.download_button(
        label="처리된 텍스트 다운로드",
        data=output.getvalue(),
        file_name="processed_text.txt",
        mime="text/plain"
    )
