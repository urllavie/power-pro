filepath = 'douga\�����p���t���v���싅�Q�O�P�W_20200524161426.mp4'

# ����t�@�C���ۑ��p�̐ݒ�
fps = int(v.get(cv2.CAP_PROP_FPS))                                # �����FPS���擾
w = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))                          # ����̉������擾
h = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # ����̏c�����擾
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # ����ۑ�����fourcc�ݒ�imp4�p�j
video = cv2.VideoWriter('video_out.mp4', fourcc, fps, (w, h), True)

