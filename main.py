
# import numpy as np
# import pandas as pd
# from PIL import Image
import streamlit as st
import time

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(i + 1)
    bar.progress(i + 1)
    time.sleep(0.01)

st.write('Streamlit 超入門')

"""
# Streamlit 超入門
```
$ pip install streamlit
$ streamlit run main.py
```
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns = [ 'lat', 'lon']
# )

# st.dataframe(df.style.highlight_max(axis=0), width=1100) # 動的な表示
# st.table(df.style.highlight_max(axis=0)) # 静的な表示

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df, size=10, color='#0000ff')

# if st.checkbox('Show Image'):
#     sampleImg = Image.open('./img/sample.jpg')
#     st.image(sampleImg, caption='Streamlit', use_column_width=True)

text = st.text_input('趣味を教えてください')
'趣味: ', text

option = st.selectbox(
    '好きな数字を教えてください',
    list(range(1, 11))
)
'好きな数字: ', option

condition = st.slider('今の調子は？', 0, 100, 50)
'コンディション: ', condition

left_column, right_column = st.columns(2)
button = left_column.button('テキスト表示')
if button:
    right_column.write('右カラム')

ex1 = st.expander('expander1')
ex1.write('expander1の内容')
ex2 = st.expander('expander2')
ex2.write('expander2の内容')