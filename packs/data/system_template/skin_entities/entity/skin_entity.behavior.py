{
    "format_version": "1.20.50",
    "minecraft:entity": {
        "description": {
            "identifier": f"shapescape:skin_entity{variant}",
            "is_spawnable": variant == "",
            "is_summonable": true,
            "description": "",
            "category": "player_facing_utility",
            "locations": [],
            "spawn_egg_description": "",
            "spawn_egg_player_facing": true,
            "runtime_identifier": "minecraft:armor_stand",
            "animations": {
                "ac.ui_trigger": "controller.animation.shapescape.skin_entity_trigger"
            },
            "scripts": {
                "animate": [
                    "ac.ui_trigger",
                ]
            },
            "properties": {
                "shapescape:ui_trigger": {
                    "client_sync": false,
                    "type": "bool",
                    "default": false,
                },
            },
        },
        "component_groups": {
            f"shapescape:skin.{name}": {
                "minecraft:skin_id": {"value": index + 1},
                "minecraft:type_family": {"family": [f"shapescape:skin.{name}"]},
                **(
                    {
                        "minecraft:is_baby": {},
                    }
                    if is_steve(name)
                    else {}
                ),
                **(
                    {
                        "minecraft:transformation": {
                            "begin_transform_sound": "",
                            "drop_equipment": false,
                            "into": "shapescape:skin_entity_slim<shapescape:preserve_skin>",
                            "transformation_sound": "",
                            "preserve_equipment": true,
                        }
                    }
                    if variant == "" and not is_steve(name)
                    else {}
                ),
                **(
                    {
                        "minecraft:transformation": {
                            "begin_transform_sound": "",
                            "drop_equipment": false,
                            "into": "shapescape:skin_entity<shapescape:preserve_skin>",
                            "transformation_sound": "",
                            "preserve_equipment": true,
                        }
                    }
                    if variant == "_slim" and is_steve(name)
                    else {}
                ),
            }
            for index, name in enumerate(return_all_skins_list("skins"))
        }
        | {
            f"shapescape:pose.{name}": {
                "minecraft:mark_variant": {
                    "value": index + 1,
                }
            }
            for index, name in enumerate(return_all_animation_names())
        }
        | {
            "shapescape:pose_none": {
                "minecraft:mark_variant": {
                    "value": 0,
                },
            },
            "shapescape:default": {"minecraft:skin_id": {"value": 0}},
        },
        "components": {
            "minecraft:interact": {
                "interactions": [
                    {
                        "on_interact": {
                            "filters": {
                                "all_of": [
                                    {
                                        "test": "is_sneak_held",
                                        "subject": "other",
                                        "value": true,
                                    },
                                    {
                                        "test": "bool_property",
                                        "subject": "self",
                                        "domain": "shapescape:ui_trigger",
                                        "value": false,
                                    },
                                ]
                            },
                            "event": "shapescape:ui_trigger_true",
                        }
                    },
                    {
                        "on_interact": {
                            "filters": {
                                "all_of": [
                                    {
                                        "test": "is_sneak_held",
                                        "subject": "other",
                                        "value": true,
                                    },
                                    {
                                        "test": "bool_property",
                                        "subject": "self",
                                        "domain": "shapescape:ui_trigger",
                                        "value": true,
                                    },
                                ]
                            },
                            "event": "shapescape:ui_trigger_false",
                        }
                    },
                ]
            },
            "minecraft:nameable": {
                "allow_name_tag_renaming": true,
                "always_show": true,
            },
            "minecraft:physics": {"has_collision": true, "has_gravity": false},
            "minecraft:collision_box": {"width": 0.6, "height": 1.8},
            "minecraft:damage_sensor": {
                "triggers": [{"cause": "all", "deals_damage": false}]
            },
            "minecraft:rideable": {
                "controlling_seat": 0,
                "family_types": ["shapescape_shadow"],
                "pull_in_entities": true,
                "rider_can_interact": false,
                "seat_count": 1,
                "seats": [{"position": [0, 0, 0]}],
            },
            "minecraft:addrider": {"entity_type": "shapescape:shadow_entity"},
            "minecraft:equip_item": {
                "excluded_items": [{"item": "minecraft:banner:15"}]
            },
            "minecraft:sittable": {},
            "minecraft:movement.basic": {},
            "minecraft:navigation.walk": {},
            "minecraft:movement": {"value": 0.0, "max": 0.0},
        },
        "events": {
            f"shapescape:skin.{name}": {
                "sequence": [
                    {
                        "remove": {
                            "component_groups": return_all_skins_list_with_shapescape(
                                "skins"
                            ),
                        },
                    },
                    {
                        "add": {
                            "component_groups": [f"shapescape:skin.{name}"],
                        },
                    },
                ]
            }
            for name in return_all_skins_list("skins")
        }
        | {
            f"shapescape:pose.{name}": {
                "sequence": [
                    {
                        "remove": {
                            "component_groups": [
                                f"shapescape:pose.{pose_name}"
                                for pose_name in return_all_animation_names()
                            ]
                        },
                    },
                    {
                        "add": {
                            "component_groups": [f"shapescape:pose.{name}"],
                        },
                    },
                ]
            }
            for name in return_all_animation_names()
        }
        | {
            "shapescape:default": {
                "sequence": [
                    {
                        "remove": {
                            "component_groups": return_all_skins_list_with_shapescape(
                                "skins"
                            ),
                        },
                    },
                    {
                        "add": {
                            "component_groups": [f"shapescape:default"],
                        },
                    },
                ]
            },
            "shapescape:preserve_skin": {
                "sequence": [
                    {
                        "filters": {
                            "test": "is_family",
                            "subject": "other",
                            "value": f"shapescape:skin.{name}",
                        },
                        "add": {"component_groups": [f"shapescape:skin.{name}"]},
                    }
                    for name in return_all_skins_list("skins")
                ]
                + [
                    {
                        "filters": {
                            "test": "is_mark_variant",
                            "subject": "other",
                            "value": 0,
                        },
                        "add": {"component_groups": []},
                    }
                ]
                + [
                    {
                        "filters": {
                            "test": "is_mark_variant",
                            "subject": "other",
                            "value": index + 1,
                        },
                        "add": {"component_groups": [f"shapescape:pose.{name}"]},
                    }
                    for index, name in enumerate(return_all_animation_names())
                ]
            },
            "shapescape:pose_none": {
                "sequence": [
                    {
                        "remove": {
                            "component_groups": [
                                f"shapescape:pose.{pose_name}"
                                for pose_name in return_all_animation_names()
                            ]
                        },
                    },
                    {
                        "add": {
                            "component_groups": ["shapescape:pose_none"],
                        },
                    },
                ]
            },
            "shapescape:ui_trigger_true": {
                "set_property": {"shapescape:ui_trigger": true}
            },
            "shapescape:ui_trigger_false": {
                "set_property": {"shapescape:ui_trigger": false}
            },
            "minecraft:entity_spawned": {
                "add": {
                    "component_groups": [
                        "shapescape:default",
                        "shapescape:pose_none",
                    ],
                }
            },
        },
    },
}
