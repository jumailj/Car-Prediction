0: 416x640 1 car, 37.8ms
Speed: 7.0ms preprocess, 37.8ms inference, 2.0ms postprocess per image at shape (1, 3, 416, 640)
[ultralytics.engine.results.Results object with attributes:

boxes: ultralytics.engine.results.Boxes object
keypoints: None
masks: None
names: {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
obb: None
orig_img: array([[[241, 247, 252],
        [241, 247, 252],
        [241, 247, 252],
        ...,
        [ 65,  66,  76],
        [ 67,  68,  78],
        [ 74,  75,  85]],

       [[243, 248, 251],
        [243, 248, 251],
        [243, 248, 251],
        ...,
        [ 70,  71,  81],
        [ 71,  72,  82],
        [ 77,  78,  88]],

       [[248, 249, 247],
        [248, 249, 247],
        [248, 249, 247],
        ...,
        [ 69,  70,  80],
        [ 69,  70,  80],
        [ 75,  76,  86]],

       ...,

       [[ 87,  82,  79],
        [ 87,  82,  79],
        [ 87,  82,  79],
        ...,
        [ 83,  78,  75],
        [ 83,  78,  75],
        [ 83,  78,  75]],

       [[ 87,  82,  79],
        [ 87,  82,  79],
        [ 87,  82,  79],
        ...,
        [ 83,  78,  75],
        [ 83,  78,  75],
        [ 83,  78,  75]],

       [[ 87,  82,  79],
        [ 87,  82,  79],
        [ 87,  82,  79],
        ...,
        [ 83,  78,  75],
        [ 83,  78,  75],
        [ 83,  78,  75]]], dtype=uint8)
orig_shape: (403, 620)
path: 'image0.jpg'
probs: None
save_dir: 'runs\\detect\\predict'
speed: {'preprocess': 7.004737854003906, 'inference': 37.828922271728516, 'postprocess': 1.9752979278564453}]
ultralytics.engine.results.Boxes object with attributes:

cls: tensor([2.], device='cuda:0')
conf: tensor([0.8721], device='cuda:0')
data: tensor([[110.1823,  62.0846, 555.8443, 360.8358,   0.8721,   2.0000]], device='cuda:0')
id: None
is_track: False
orig_shape: (403, 620)
shape: torch.Size([1, 6])
xywh: tensor([[333.0133, 211.4602, 445.6620, 298.7512]], device='cuda:0')
xywhn: tensor([[0.5371, 0.5247, 0.7188, 0.7413]], device='cuda:0')
xyxy: tensor([[110.1823,  62.0846, 555.8443, 360.8358]], device='cuda:0')
xyxyn: tensor([[0.1777, 0.1541, 0.8965, 0.8954]], device='cuda:0')
INFO:     127.0.0.1:62900 - "POST /predict/ HTTP/1.1" 200 OK