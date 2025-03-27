{
    "format_version": "1.10.0",
    "minecraft:client_entity": {
        "description": {
            "identifier": "shapescape:skin_entity_slim",
            "materials": {
                "default": "entity_alphatest",
            },
            "textures": {
                name: f"textures/shapescape/entity/{name}"
                for name in return_all_skins_list("skins")
            }
            | {"default": "textures/entity/default"},
            "geometry": {
                "default": "geometry.shapescape.alex",
            },
            "render_controllers": [
                "controller.render.shapescape.skin_entity",
            ],
            "spawn_egg": {"texture": "shapescape.skin_entity"},
            "enable_attachables": true,
            "animations": {
                name: "animation.shapescape.pose." + name
                for name in return_all_animation_names()
            },
            "scripts": {
                "scale": "0.9375",
                "animate": [
                    {name: f"q.mark_variant == {index + 1}"}
                    for index, name in enumerate(return_all_animation_names())
                ],
            },
        }
    },
}
