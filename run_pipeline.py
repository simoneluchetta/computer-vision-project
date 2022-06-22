'''
Assume the project runs on a linux machine

Directory structure as:
|____A-NeRF
|
|____SPIN
|
|____OpenPose
|
|____ffmpeg
|
|____run_pipeline.py
|
|____video.mp4

If OpenPose on Windows:
|____A-NeRF
|
|____SPIN
|
|____OpenPose
|
|____run_pipeline.py
|
|____temp
|
|____output_json_folder
'''


def main():
    import subprocess

    #######################################
    ########   DEFINE CONSTANTS   #########
    #######################################

    openpose_on_windows = True
    run_mixamo = True
    run_surreal = not(run_mixamo)
    frame_number = 10

    anerf_dir = 'A-NeRF/'
    spin_dir = 'SPIN/'

    anerf_venv = 'anerf/bin/activate'
    spin_venv = 'spin/bin/activate'

    openpose_exe_path = '/OpenPose/OpenPoseDemo'

    video_name = 'video.mp4'

    #######################################
    ########     RUN COMMANDS      ########
    #######################################
    
    if(not openpose_on_windows):
        make_tmp = 'mkdir temp'

        run_ffmpeg = 'ffmpeg -i {} -vsync 0 temp/temp%d.png'.format(
            video_name)

        run_openpose = '{} --image_dir /temp/ --write_json output_json_folder/'.format(
            openpose_exe_path)

    source_spin = '. {}'.format(spin_venv)
    cd_spin = 'cd {}'.format(spin_dir)
    run_spin = 'python demo.py --checkpoint=data/model_checkpoint.pt --img=../temp/ --openpose=../output_json_folder/ --result_folder=../{}NPZ_OUTS/'.format(
        anerf_dir)

    source_anerf = '. {}'.format(anerf_venv)
    cd_anerf = 'cd {}'.format(anerf_dir)

    if run_surreal:
        run_anerf = 'python run_render.py --nerf_args=logs/surreal_model/args.txt --ckptpath=logs/surreal_model/150000.tar --dataset=surreal \
                                        --entry=hard --render_type=retarget --render_res 512 512 --white_bkgd --runname=surreal_run --frame_number={}'.format(frame_number)

    if run_mixamo:
        run_anerf = 'python run_render.py --nerf_args=log_mixamo/mixamo_archer/args.txt --ckptpath=log_mixamo/mixamo_archer/archer_ft.tar --dataset=mixamo \
                                        --entry=archer --render_type=animate --render_res 512 512 --white_bkgd --runname=mixamo_run'

    if openpose_on_windows:
        cmd = source_spin + "; " + cd_spin + "; " + run_spin + "; cd .. ;" + \
            source_anerf + "; " + cd_anerf + "; " + run_anerf
    else:
        cmd = make_tmp + ";" + run_ffmpeg + ";" + run_openpose + ";" + source_spin + \
            ";" + run_spin + ";" + source_anerf + ";" + run_anerf

    p = subprocess.Popen(cmd, shell=True)


if __name__ == '__main__':
    main()
