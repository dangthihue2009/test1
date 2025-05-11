import streamlit as st
from PIL import Image

# --- Cài đặt trang ---
st.set_page_config(page_title="Giới thiệu cá nhân", page_icon="👤", layout="centered")


# --- Tiêu đề và thông tin cơ bản ---
st.title("👋 Xin chào, tôi là [Tên của bạn]")
st.subheader("🌟 Một chút về tôi")

st.write("""
Chào mừng bạn đến với trang giới thiệu cá nhân của tôi.  
Tôi là một người đam mê [lĩnh vực của bạn: lập trình, thiết kế, giáo dục...].  
Hiện tại, tôi đang làm việc tại [nơi làm việc hoặc vị trí hiện tại], và không ngừng học hỏi để phát triển bản thân mỗi ngày.
""")

# --- Kỹ năng ---
st.header("🛠️ Kỹ năng")
st.markdown("""
- 💻 Lập trình: Python, JavaScript, HTML/CSS
- 📊 Phân tích dữ liệu: Pandas, NumPy, Matplotlib
- 🤖 Machine Learning: Scikit-learn, TensorFlow
- 🌐 Ngôn ngữ: Tiếng Việt (bản ngữ), Tiếng Anh (tốt)
""")

# --- Dự án nổi bật ---
st.header("🚀 Dự án nổi bật")
st.markdown("""
- 🔍 **Hệ thống phân tích dữ liệu khách hàng** – Tự động phân loại nhóm khách hàng và đưa ra gợi ý chiến lược marketing.
- 🎯 **Ứng dụng quản lý công việc cá nhân** – Viết bằng Streamlit, giúp theo dõi và nhắc nhở các nhiệm vụ hàng ngày.
""")

# --- Liên hệ ---
st.header("📫 Liên hệ")
st.markdown("""
- 📧 Email: [youremail@example.com](mailto:youremail@example.com)
- 🔗 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- 🐙 GitHub: [github.com/yourusername](https://github.com/yourusername)
""")
