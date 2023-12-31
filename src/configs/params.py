X_SPACE_GUIDANCE_SCALE_DICT = {
    'stable-diffusion' : {
        1.0 : 0.5,
        0.9 : 0.5,
        0.8 : 1,
        0.7 : 1,
        0.6 : 2,
        0.5 : 2,
        0.4 : 2,
        0.3 : 2,
        0.2 : 2,
        0.1 : 2,
        0.0 : 0,
    },
    'uncond' : {
        1.0 : 0.5,
        0.8 : 1,
        0.6 : 4,
        0.4 : 16,
        0.2 : 16,
    }
}
X_SPACE_EDIT_STEP_SIZE_DICT = {
    'stable-diffusion' : {
        1.0 : 0.5,  # 1.0 : 4,
        0.9 : 0.5,  # 0.9 : 4,
        0.8 : 1,    # 0.8 : 8,
        0.7 : 1,    # 0.7 : 8,
        0.6 : 2,    # 0.6 : 16,
        0.5 : 2,    # 0.5 : 16,
        0.4 : 2,    # 0.4 : 32,
        0.3 : 2,    # 0.3 : 32,
        0.2 : 2,    # 0.2 : 32,
        0.1 : 2,    # 0.1 : 32,
        0.0 : 0,    # 0.0 : 0,
    },
    'uncond' : {
        1.0 : 0.5,  # 1.0 : 0.5,  # 1.0 : 8,
        0.8 : 1,    # 0.8 : 8,
        0.6 : 4,    # 0.6 : 16,
        0.4 : 16,   # 0.4 : 32,
        0.2 : 16,   # 0.2 : 32,
    }
}