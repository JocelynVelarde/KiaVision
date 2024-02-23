import streamlit as st

st.title('Welcome to Kia Vision AI!')
st.divider()

st.write('Could you imagine your own personal mechanic, ready when you actually need it? '
		 'Kia Vision AI is here. Snap a pic, tell us about your problem, and you\'ll get an answer instantly. '
		 'The expertise you need, whenever you need it.')

st.subheader('Who we are')
st.write('Kia Vision is an app that let\'s customers interact with custom AI assistants that get trained on Kia\'s vehicle manuals. '
		 'The assistants are multi-modal, meaning anyone can interact with them using visual and textual cues.')

admin_col, user_col = st.columns(2)

with admin_col:
	st.subheader('Admin')
	st.write('As an admin, you can create, delete, train and evaluate AI assistants in a simple manner, so you can keep them with up-to-date information.')

with user_col:
	st.subheader('User')
	st.write('To get answers, just send a photo along with a little description of your problem, and let the power of computer vision and LLM\'s give you an instant answer.')

st.page_link("pages/get started.py", label="Click this button to Get Started", icon="🚀")