import streamlit as st
import json
from PIL import Image, ImageDraw
from io import BytesIO
from ultralytics import YOLO
import base64 
st.set_page_config("Computer Vision",layout="wide")
# background_image_url ="static/images/pipe_bg.png" # Replace with your image URL"
# def add_bg_from_local(image_file):
     
#     with open(image_file, "rb") as image_file:
    
#         encoded_string = base64.b64encode(image_file.read())
    
#     st.markdown(
#     f"""
#     <style>
    
#     stApp {{
    
#     background-image: url(data:image/{"png"}; base64, {encoded_string.decode()});
    
#     background-size: cover; background-repeat:
    
#     no-repeat; background-position: center center;}}
    
#     .block-container {{
    
#     padding-top: 1rem;
    
#     padding-bottom: @rem;
    
#     padding-left: 1rem;
    
#     padding-right: 5rem;
    
#     }}
    
#     </style>
#     """,
    
#     unsafe_allow_html=True)
 
# st.image((background_image_url))
# add_bg_from_local(background_image_url)


def detect_objects(image, confidence_threshold=0.3):
    model = YOLO('pipecount.pt')
    results = model.predict(image, conf=confidence_threshold)
    result = results[0]
    serialized_result = json.loads(result.tojson())
    pipe_count = len(serialized_result)
    # image_np = np.array(image)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]
            top_left = (int(b[0]),int(b[1]))
            bottom_right = (int(b[2]),int(b[3]))
            img1 = ImageDraw.Draw(image)  
            img1.rectangle((top_left,bottom_right), outline ="red",width=2) 
            # center_coordinates = (int((int(b[0]) + int(b[2])) / 2), int((int(b[1]) + int(b[3])) / 2))
            # image_np = cv2.circle(image_np, center_coordinates, 5, (255, 0, 0), 5)
    return pipe_count,image
    

def main():


    title=r"$\textsf {Pipe Count Identification}$"
    col1,col2=st.columns([8,2])
    col2.image("static/images/sogeti_logo.png", width=200)
    col1.title(title)#("Pipe Counting",)

    st.markdown("----")
   
    
    st.write("Upload an image to count pipes")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    # pipe_count = 0
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        col1, col2 = st.columns(2)
        
       
        with col1:
            st.image(image, caption='Uploaded Image', use_column_width=True, width=20)
            count_pipe = st.button("Count Pipes")
        with col2:
            if count_pipe:
                
                with st.spinner('Detecting...'):
                    pipe_count,image_np = detect_objects(image)
                    st.image(image_np, caption='Detected pipes', use_column_width=True, width=20)
                    st.markdown(f"<h5 style='text-align: center; color: #0070ad;'>Pipe count : {pipe_count} </h3>", unsafe_allow_html=True)     
                    # st.subheader("Pipe Count: "+ str(pipe_count))
                    
                    # st.write("Pipe_count", pipe_count)
              

if __name__ == "__main__":
    main()
