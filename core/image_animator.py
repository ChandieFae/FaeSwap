# core/image_animator.py
import imageio
from skimage.io import imread
from demo import load_checkpoints, make_animation

def animate_image(template_image_path, motion_video_path, output_path):
    source_image = imread(template_image_path)
    driving_video = imageio.mimread(motion_video_path)

    generator, kp_detector = load_checkpoints(
        config_path='config/vox-256.yaml',
        checkpoint_path='models/fomm_model.pth'
    )

    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)
    imageio.mimsave(output_path, predictions, fps=25)

    return output_path
