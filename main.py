# from PIL import Image
# from turtle import width
# from click import option
# from nbformat import write
# from soupsieve import select
import streamlit as st
# import numpy as np
# import pandas as pd
import time

st.title("Streamlit 超入門")
# st.title("あcola、シラユキ、つむすと")

# st.write("DataFrame")
# df = pd.DataFrame({
#     "1列目": [1, 2, 3, 4],
#     "2列目": [10, 20, 30, 40]
# })
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

# df_2 = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=["a", "b", "c"]
# )
# st.dataframe(df_2)
# st.line_chart(df_2)
# st.area_chart(df_2)
# st.bar_chart(df_2)

# df_3 = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )
# st.dataframe(df_3)
# st.line_chart(df_3)
# st.map(df_3)

# st.write("Display Image")
# if st.checkbox("Show Image"):
#     img = Image.open("cats.jpg")
#     st.image(img, caption="Ten and Rokuta", use_column_width=True)

# option = st.selectbox(
#     "あなたが好きな数字を教えてください。",
#     list(range(1, 11))
# )
# st.write(f"あなたの好きな数字は、{option}です。")

# st.sidebar.write("Interactive Widgets")
# text = st.sidebar.text_input("あなたの趣味を教えて下さい。")
# condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50, 10)
# st.write(f"あなたの趣味：{text}")
# st.write(f"コンディション：{condition}")

# left_column, right_column = st.columns(2)
# button = left_column.button("右カラムに文字を表示")
# if button:
#     right_column.write("ここは右カラム")

# expander_1 = st.expander("問い合わせ1")
# expander_1.write("問い合わせ内容を書く")
# expander_2 = st.expander("問い合わせ2")
# expander_2.write("問い合わせ内容を書く")
# expander_3 = st.expander("問い合わせ3")
# expander_3.write("問い合わせ内容を書く")

st.write("プログレスバーの表示")
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)
else:
    st.write("Done!!!!!")

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """