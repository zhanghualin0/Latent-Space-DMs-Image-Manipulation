# 
for t in 0.6
    do
    for sample_idx in 2
        do
        python main_various_layer.py \
            --sh_file_name                          main_various_layer_afhq_local_encoder_pullback.sh    \
            --sample_idx                            $sample_idx                                 \
            --device                                cuda:0                                      \
            --dtype                                 fp32                                        \
            --seed                                  0                                           \
            --model_name                            AFHQ_P2                                \
            --dataset_name                          AFHQ                                   \
            --for_steps                             100                                         \
            --inv_steps                             100                                         \
            --use_yh_custom_scheduler               True                                        \
            --x_space_guidance_edit_step            1                                           \
            --x_space_guidance_scale                1.5                                         \
            --x_space_guidance_num_step             24                                          \
            --edit_t                                $t                                          \
            --performance_boosting_t                0.2                                         \
            --run_edit_local_encoder_pullback_zt    True                                        \
            --note                                  "Uncond"
        done
    done