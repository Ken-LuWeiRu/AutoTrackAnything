# -*- coding: utf-8 -*-

DEVICE = '0' # For GPU set device num which you want to use (or set 'cpu', but it's too slow)
# DEVICE = 'cpu'

# Our confidence for every person (bbox)
PERSON_CONF = 0.2

KEYPOINTS = ["nose", "left_eye", "right_eye", "left_ear", "right_ear", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow", "left_wrist", "right_wrist", "left_hip", "right_hip", "left_knee", "right_knee", "left_ankle", "right_ankle"]

# Our confidence for used keypoints
KPTS_CONF = 0.6

IOU_THRESHOLD = 0.2

# It's xMem original config, you can try to change this values for your task (check xMem article)
XMEM_CONFIG = {
    'top_k': 30,
    'mem_every': 5,
    'deep_update_every': -1,
    'enable_long_term': True,
    'enable_long_term_count_usage': True,
    'num_prototypes': 256,
    'min_mid_term_frames': 28,
    'max_mid_term_frames': 60,
    'max_long_term_elements': 10000,
}

# Max possible count of persons in video (if you has error, set bigger number)
MAX_OBJECT_CNT = 21

# Check new persons in frame every N frames
YOLO_EVERY = 5

# # Resize processed video. For better results you can increase resolution
INFERENCE_SIZE = (960, 500)

#     parser.add_argument('--images', help='Folders containing input images.', default=None)
#     parser.add_argument('--video', help='Video file readable by OpenCV.', default=None)
#     parser.add_argument('--workspace', help='directory for storing buffered images (if needed) and output masks', default=None)

#     parser.add_argument('--buffer_size', help='Correlate with CPU memory consumption', type=int, default=100)
    
#     parser.add_argument('--num_objects', type=int, default=1)

#     # Long-memory options
#     # Defaults. Some can be changed in the GUI.
#     parser.add_argument('--max_mid_term_frames', help='T_max in paper, decrease to save memory', type=int, default=10)
#     parser.add_argument('--min_mid_term_frames', help='T_min in paper, decrease to save memory', type=int, default=5)
#     parser.add_argument('--max_long_term_elements', help='LT_max in paper, increase if objects disappear for a long time', 
#                                                     type=int, default=10000)
#     parser.add_argument('--num_prototypes', help='P in paper', type=int, default=128) 

#     parser.add_argument('--top_k', type=int, default=30)
#     parser.add_argument('--mem_every', type=int, default=10)
#     parser.add_argument('--deep_update_every', help='Leave -1 normally to synchronize with mem_every', type=int, default=-1)
#     parser.add_argument('--no_amp', help='Turn off AMP', action='store_true')
#     parser.add_argument('--size', default=480, type=int, 
#             help='Resize the shorter side to this size. -1 to use original resolution. ')
#     args = parser.parse_args()







# # It's xMem original config, you can try to change this values for your task (check xMem article)
# XMEM_CONFIG = {
#     'top_k': 30,
#     'mem_every': 5,
#     'deep_update_every': -1,
#     'enable_long_term': True,
#     'enable_long_term_count_usage': True,
#     'num_prototypes': 256,
#     'min_mid_term_frames': 7,
#     'max_mid_term_frames': 20,
#     'max_long_term_elements': 10000,
# }
