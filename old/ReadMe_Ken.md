



python tracking.py --video_path=Street_1080p_30fps.mp4 --width=1280 \
--height=768 --frames_to_propagate=1000 --output_video_path=res_Street_1080p_30fps.mp4 --device=0 \
--yolo_every=1 --output_path=OUTPUT_CSV_PATH.csv

python tracking.py --video_path=Street_1080p_30fps.mp4 --width=1280 \
--height=1080 --frames_to_propagate=1000 --output_video_path=res_Street_1080p_30fps.mp4 --device=0 \
--yolo_every=1 --output_path=OUTPUT_CSV_PATH.csv



python tracking.py --video_path=Street_1080p_30fps.mp4 --width=1920 \
--height=1080 --frames_to_propagate=300 --output_video_path=res_Street_1080p_30fps.mp4 --device=0 \
--person_conf=0.7 --kpts_conf=0.4 --iou_thresh=0.5 --yolo_every=1 \ --output_path=OUTPUT_CSV_PATH.csv

python tracking.py --video_path=Street_1080p_30fps.mp4 --width=1920 \
--height=1080 --frames_to_propagate=1000 --output_video_path=res_Street_1080p_30fps.mp4 --device=0 \
--person_conf=0.9 --iou_thresh=0.9 --yolo_every=1 --output_path=OUTPUT_CSV_PATH.csv


Newper.mp4


python tracking.py --video_path=Newper.mp4 --width=1920 \
--height=1080 --frames_to_propagate=1000 --output_video_path=res.Newper.mp4 --device=0 \
--yolo_every=1 --output_path=OUTPUT_CSV_PATH.csv


python tracking.py --video_path=Newper.mp4 --width=1280 \
--height=768 --frames_to_propagate=1000 --output_video_path=res.Newper.mp4 --device=0 \
--yolo_every=1 --output_path=OUTPUT_CSV_PATH.csv

python tracking.py --video_path=Newper.mp4 --width=1280 \
--height=768 --frames_to_propagate=2341 --output_video_path=res.Newper.mp4 --device=0 \
--yolo_every=1 --output_path=OUTPUT_CSV_PATH.csv