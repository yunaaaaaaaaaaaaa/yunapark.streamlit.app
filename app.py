import streamlit as st
import base64

st.title('Yuna site')

st.header("No Poverty")
story = """
This game is about sdg 1, which is no poverty. In this game, you have to give people money, food, or a house to the poor people, depending on their situation and their needs. 
You have to decide what people need and help them with it.
"""
st.write(story)


# Function to convert an image file to a base64 encoded string.
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

encoded_image_1 = get_base64_image("1.png")
encoded_image_2 = get_base64_image("2.png")
encoded_image_3 = get_base64_image("3.png")
encoded_image_4 = get_base64_image("4.png")
encoded_image_5 = get_base64_image("5.png")
encoded_image_6 = get_base64_image("6.png")
encoded_image_7 = get_base64_image("7.png")
encoded_image_8 = get_base64_image("ending.png")

# Create a list of base64-encoded images from 1.png to 7.png
images = [get_base64_image(f"{i}.png") for i in range(1, 8)]


html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {{
      position: relative;
      display: inline-block;
    }}
    .clickable-area {{
      position: absolute;
      cursor: pointer;
    }}
    #start-box {{
      top: 270px;
      left: 35px;
      width: 150px;
      height: 50px;
    }}
    .box1 {{
      top: 289px;
      left: 45px;
      width: 130px;
      height: 45px;
    }}
    .box2 {{
      top: 288px;
      left: 220px;
      width: 130px;
      height: 45px;
    }}
    .box3 {{
      top: 287px;
      left: 408px;
      width: 130px;
      height: 45px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <img id="game-image" src="data:image/jpeg;base64,{images[0]}" width="600" alt="Game Image">

    <!-- Start box for 1.png -->
    <div class="clickable-area" id="start-box" onclick="nextImage()"></div>

    <!-- Choice boxes for 2.png to 7.png -->
    <div class="clickable-area box1" id="choice1" onclick="nextImage()" style="display:none;"></div>
    <div class="clickable-area box2" id="choice2" onclick="nextImage()" style="display:none;"></div>
    <div class="clickable-area box3" id="choice3" onclick="nextImage()" style="display:none;"></div>
  </div>

  <script>
  const images = {images};
  const endingImage = "data:image/png;base64,{encoded_image_8}";
  let currentIndex = 0;
  let isEnding = false;

  function nextImage() {{
    if (isEnding) {{
      return;
    }}

    if (currentIndex < images.length - 1) {{
      currentIndex += 1;
      document.getElementById("game-image").src = "data:image/jpeg;base64," + images[currentIndex];

      if (currentIndex === 1) {{
        document.getElementById("start-box").style.display = "none";
      }}
      if (currentIndex >= 1 && currentIndex <= 6) {{
        document.getElementById("choice1").style.display = "block";
        document.getElementById("choice2").style.display = "block";
        document.getElementById("choice3").style.display = "block";
      }}
    }} else if (currentIndex === images.length - 1) {{
      document.getElementById("game-image").src = endingImage;
      isEnding = true;
      document.getElementById("choice1").style.display = "none";
      document.getElementById("choice2").style.display = "none";
      document.getElementById("choice3").style.display = "none";
    }}
  }}
</script>

</body>
</html>
"""

# Placeholder for message
msg_box = st.empty()

# Show the custom HTML in the app
st.components.v1.html(html_code, height=700)

# Capture message if clicked (this part uses query params just for simplicity)
import streamlit.components.v1 as components

# Note: JS-to-Python communication is limited unless you use a full Streamlit component.
# For now, we can simulate the effect using Streamlit messages if you later add them via session state or custom component.

# Render the custom HTML code within the Streamlit app.
st.components.v1.html(html_code, height=700)
