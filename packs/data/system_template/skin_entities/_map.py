# fmt: off
[
    {
        "source": "skins/*.entity.png", 
        "target": AUTO_FLAT
    },
    {
        "source": "entity/skin_entity.bp_ac.json", 
        "target": AUTO_FLAT
    },
    {
        "source": "entity/skin_entity.entity.py", 
        "target": AUTO_FLAT
    },
    {
        "source": "entity/skin_entity_slim.entity.py", 
        "target": AUTO_FLAT
    },
    {
        "source": "entity/shadow_entity.behavior.json", 
        "target": AUTO_FLAT
    },
    {
        "source": "entity/shadow_entity.entity.json", 
        "target": AUTO_FLAT
    },
    *[  {
            "source": "entity/skin_entity.behavior.py", 
            "target": f"BP/entities/skin_entity{variant}.behavior.json",
            "scope": {
                "variant": variant,
            }
        } 
        for variant in variants
    ],
    {
        "source": "entity/item_texture.json",
        "target": "RP/textures/item_texture.json",
        "on_conflict": "merge",
    },
    {
        "source": "entity/skin_entity.item.png", 
        "target": AUTO_FLAT
    },
    {
        "source": "entity/geometry/*.geo.json", 
        "target": AUTO_FLAT
    },
    {
        "source": "animation/poses.animation.json", 
        "target": AUTO_FLAT
    },
    {
        "source": "entity/*.rc.py", 
        "target": AUTO_FLAT
    },
    {
        "source": "entity/default.entity.png", 
        "target": AUTO_FLAT
    },
    {
        "source": "entity/empty.entity.png", 
        "target": AUTO_FLAT
    },
    {
        "source": "main.js",
        "target": AUTO_FLAT,
        "on_conflict": "append_end"
    },
    replace_macros(
        map_py_item={
            "source": "subscripts/skin_entity_ui.js",
            "target": f"BP/scripts//subscripts/skin_entity_ui.js"
        },
        replacements={
            "[/*@skins_list*/]": return_all_skins_list("skins"),
            "[/*@animation_names*/]": return_all_animation_names(),
        }
    ),
    {
        "source": "ui/*.ui.png",
        "target": AUTO_FLAT    
    },
]
