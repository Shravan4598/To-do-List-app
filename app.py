import streamlit as st

# Set page config
st.set_page_config(page_title="To-Do List", page_icon="📝")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# App Title
st.title("📝 To-Do List App")

# Input for new task
task_input = st.text_input("Enter a new task:")

# Add task button
if st.button("Add Task"):
    if task_input.strip() != "":
        st.session_state.tasks.append(task_input.strip())
        st.success(f"✅ Task '{task_input}' added!")
    else:
        st.warning("⚠️ Please enter a valid task.")

st.markdown("## ✅ Your Tasks:")

# Display tasks with delete buttons
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            st.write(f"- {task}")
        with col2:
            if st.button("❌", key=f"del_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()  # Updated for latest Streamlit
else:
    st.info("No tasks yet. Add some above!")

# Clear all button
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.success("🗑️ All tasks cleared!")
