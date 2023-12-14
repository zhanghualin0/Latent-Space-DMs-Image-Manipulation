# my method : local pullback (w/ Jacobian subspace iteration)

for t in 0.6
    do
    for sample_idx in 8
        do
        python main_various_layer.py \
            --sh_file_name                          main_various_layer_various_local_basis_pullback_without_edit_prompt.sh   \
            --device                                cuda:0                                      \
            --sample_idx                            $sample_idx                                 \
            --model_name                            stabilityai/stable-diffusion-2-1-base       \
            --dataset_name                          CelebA_HQ                                    \
            --edit_prompt                           ""                                          \
            --x_space_guidance_scale                2                                           \
            --x_space_guidance_num_step             16                                          \
            --x_space_guidance_use_edit_prompt      True                                        \
            --edit_t                                $t                                          \
            --run_edit_local_encoder_pullback_zt    True                                        \
            --note                                  "without_prompt"
        done
    done
