[
    *[
        {
            "source": "template_screen.block.json",
            "target": f"BP/blocks/{color}_screen.block.json",
            "scope": {"color": color},
            "json_template": True,
        }
        for color in colors
    ],
    {"source": "screens.mcfunction", "target": AUTO_FLAT},
    {"source": "textures/*.block.png", "target": AUTO_FLAT},
    {
        "source": "terrain_texture.json",
        "target": "RP/textures/terrain_texture.json",
        "on_conflict": "merge",
        "json_template": True,
    },
]
