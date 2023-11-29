import streamlit as st

def main():
    st.title('Streamlit App with Embedded My Google Map')
    st.write('Stakes of Edmonton:')

    # Embedding Google Map using HTML iframe
    st.markdown("""
    <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1NLv7aSAUASYn9cieyeZuhIAmTDVX09U&ehbc=2E312F" width="640" height="480"></iframe>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

