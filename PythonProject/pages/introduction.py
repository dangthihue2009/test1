import streamlit as st
from PIL import Image

st.set_page_config(page_title="Đất nước Việt Nam", layout="wide")

st.title("🇻🇳 Giới thiệu đất nước Việt Nam")

# --- Mô tả tổng quan ---
st.header("📍 Vị trí và tổng quan")
st.write("""
Việt Nam là một quốc gia nằm ở khu vực Đông Nam Á, phía đông bán đảo Đông Dương.  
Nước ta có đường bờ biển dài hơn 3.200 km, tiếp giáp với Trung Quốc, Lào, Campuchia và Biển Đông.
""")

# --- Thêm hình ảnh ---
image = Image.open("vietnam.jpg")  # Đặt một bức ảnh Việt Nam (nếu có)
st.image(image, caption="Cảnh đẹp Việt Nam", use_column_width=True)

# --- Văn hóa ---
st.header("🎎 Văn hóa và con người")
st.write("""
Việt Nam có nền văn hóa lâu đời với nhiều truyền thống đặc sắc như Tết Nguyên Đán, áo dài, múa rối nước và các làn điệu dân ca.  
Con người Việt Nam thân thiện, cần cù và hiếu khách.
""")

# --- Ẩm thực ---
st.header("🍜 Ẩm thực Việt Nam")
st.write("""
Ẩm thực Việt nổi tiếng với sự hài hòa giữa các vị chua, cay, mặn, ngọt. Một số món ăn tiêu biểu gồm:
- Phở
- Bánh mì
- Bún chả
- Gỏi cuốn
""")

# --- Địa danh nổi tiếng ---
st.header("🏞️ Các địa danh nổi bật")
st.write("""
- Hà Nội – Thủ đô nghìn năm văn hiến  
- TP. Hồ Chí Minh – Trung tâm kinh tế lớn nhất cả nước  
- Vịnh Hạ Long – Di sản thiên nhiên thế giới  
- Hội An – Phố cổ mang đậm dấu ấn lịch sử  
- Sapa – Nơi có khí hậu mát mẻ và văn hóa dân tộc độc đáo
""")

# --- Kết ---
st.write("🇻🇳 Việt Nam – Một đất nước tươi đẹp, đa dạng và đáng để khám phá!")
