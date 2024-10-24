from ultralytics import YOLO
import cv2
class_names = ['0', '1', '2', '3', 'Raising', 'Rasing', 'qiyam', 'ruku', 'sujud'] 

model = YOLO('best.onnx')

results = model('5.jpg')

result = results[0]
image = cv2.imread('5.jpg')

for box in result.boxes:
    class_id = int(box.cls.item())  # Convert tensor to int
    class_name = class_names[class_id]  # Map class ID to class name
    confidence = box.conf.item()  # Convert tensor to float
    
    # Get coordinates as a numpy array and convert to list
    coordinates = box.xyxy[0].cpu().numpy()  # Get the first (and only) box and convert to numpy
    x1, y1, x2, y2 = map(int, coordinates)  # Convert to integers

    # Draw bounding box
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Draw rectangle
    font_scale =2  # Increase this value for larger text
    cv2.putText(image, f"{class_name} {confidence:.2f}", 
                (x1, y1 - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                font_scale, (124, 252, 0), 
                2)   # Put text

# Save the output image
cv2.imwrite('output6.jpeg', image)
cv2.destroyAllWindows() 
