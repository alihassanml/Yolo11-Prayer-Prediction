from ultralytics import YOLO

# Load the model
model = YOLO('best.onnx')

# Run inference
results = model('namaz.jpg')

result = results[0]

# Show results
result.show()  # Display the results

# Save results
result.save('output.jpg')



    

# cap = cv2.VideoCapture(0)
# while True:
#     __,frame = cap.read()
    
#     result = model(frame)[0]
#     print(result)
#     cv2.imshow('image',frame)
    
#     if cv2.waitKey(1) ==27:
#         break
# cv2.destroyAllWindows()
# cap.release()