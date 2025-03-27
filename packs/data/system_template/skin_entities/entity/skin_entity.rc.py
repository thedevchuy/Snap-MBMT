{
    "format_version": "1.20.41",
    "render_controllers": {
        "controller.render.shapescape.skin_entity": {
            "geometry": "geometry.default",
            "materials": [
                {"*": "material.default"},
            ],
            "textures": ["array.textures[q.skin_id]"],
            "arrays": {
                "textures": {
                    "Array.textures": ["Texture.default"]
                    + return_all_skins_list_rc("skins")
                },
            },
        },
    },
}
