import streamlit as st
import io

def process_text(content):
    # 대체할 문자 리스트
    replace_chars = ['，', '、', '？', '：', '；', '。', '「', '」', '《', '》']
    
    # 대체할 문자 딕셔너리
    replace_dict = {'教': '敎', '為': '爲', '即': '卽'}
    
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

if st.button('텍스트 처리') and 'content' in locals() and content.strip():
    processed_content = process_text(content)
    
    st.subheader("처리된 텍스트:")
    st.text_area("처리된 텍스트 (아래 '복사하기' 버튼을 사용하세요):", processed_content, height=200, key='processed_text')
    
    col1, col2 = st.columns(2)
    
    # 처리된 텍스트를 다운로드할 수 있게 합니다
    with col1:
        output = io.BytesIO()
        output.write(processed_content.encode('utf-8'))
        st.download_button(
            label="텍스트 파일로 다운로드",
            data=output.getvalue(),
            file_name="processed_text.txt",
            mime="text/plain"
        )
    
    # 클립보드에 복사 버튼 (Streamlit 방식)
    with col2:
        if st.button('복사하기'):
            st.code(processed_content)  # 이렇게 하면 'Copy to clipboard' 버튼이 자동으로 생성됩니다
            st.success('위의 코드 블록에서 "Copy to clipboard" 버튼을 클릭하여 텍스트를 복사하세요.')

else:
    st.info("텍스트를 입력하거나 파일을 업로드한 후 '텍스트 처리' 버튼을 클릭하세요.")